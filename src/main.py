import os
import sys
from typing import Union
from ctypes import wintypes

from PySide6.QtCore import Qt, Slot, Signal, QByteArray, QObject, QEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PySide6.QtGui import QCloseEvent, QKeyEvent
from pynput import keyboard

from form.main_form import Ui_MainWindow
from class_dd import ClassDD
from record import (Recorder
                    , Runner
                    , RecordType
                    , KeyState
                    , MouseState
                    , MouseButton)
import hotkey


def key_press(w : QWidget):
    class filter_(QObject):
        sig = Signal(QKeyEvent)
        def eventFilter(self, obj : QObject, event : QEvent) -> bool:
            if event.type() == QEvent.KeyPress:
                event = QKeyEvent(event)
                self.sig.emit(event)
                return True

            return False

    f = filter_(w)
    w.installEventFilter(f)
    return f.sig


class MainWindow(QMainWindow, Ui_MainWindow):
    press_release_signal = Signal(tuple)
    click_signal = Signal(tuple)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.record_start_btn.clicked.connect(self.record_start_btn_clicked_handler)
        self.record_save_btn.clicked.connect(self.record_save_btn_clicked_handler)
        self.record_load_btn.clicked.connect(self.record_load_btn_clicked_handler)
        self.record_run_btn.clicked.connect(self.record_run_btn_clicked_handler)

        key_press(self.recorded_item_list).connect(self.recorded_item_list_key_press_handler)

        self.press_release_signal.connect(self.press_release_signal_handler)
        self.click_signal.connect(self.click_signal_handler)

        self.record_list = []

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        dd_path = os.path.join(cur_dir, "3rdparty", "DD64.dll")
        self.dd_obj = ClassDD(dd_path)

        self.hotkey_list = [hotkey.VK_OEM_PLUS, hotkey.VK_OEM_5]
        hotkey.register_hotkey(self.winId(), 0, self.hotkey_list[0])
        hotkey.register_hotkey(self.winId(), 1, self.hotkey_list[1])

    def closeEvent(self, event : QCloseEvent) -> None:
        hotkey.unregister_hotkey(self.winId(), 0)
        hotkey.unregister_hotkey(self.winId(), 1)

    def nativeEvent(self, eventType: Union[QByteArray, bytes], message: int) -> object:
        if eventType == b"windows_generic_MSG":
            msg = wintypes.MSG.from_address(message.__int__())
            if msg.message == hotkey.WM_HOTKEY:
                if msg.wParam == 0:
                    self.record_start_btn_clicked_handler()
                elif msg.wParam == 1:
                    self.record_run_btn_clicked_handler()

        return super().nativeEvent(eventType, message)
        
    @Slot()
    def record_start_btn_clicked_handler(self) -> None:
        is_recording = getattr(self, "is_recording", False)
        if is_recording:
            self.record_start_btn.setText("start (=)")
            self.is_recording = False

            self.recorder.stop()

        else:
            self.record_start_btn.setText("stop (=)")
            self.is_recording = True

            self.recorder = Recorder(lambda data : self.press_release_signal.emit(data)
                                    , lambda data : self.click_signal.emit(data))
            self.recorder.start()


    @Slot()
    def record_save_btn_clicked_handler(self) -> None:
        file_path = QFileDialog.getSaveFileName(self, "Save Record", os.getcwd(), "Json Files (*.json)")[0]
        Recorder.save_record(self.record_list, file_path)

    @Slot()
    def record_load_btn_clicked_handler(self) -> None:
        file_path = QFileDialog.getOpenFileName(self, "Load Record", os.getcwd(), "Json Files (*.json)")[0]
        self.record_list = Recorder.load_record(file_path)
        self.add_items(self.record_list)

    @Slot()
    def record_run_btn_clicked_handler(self):
        is_running = getattr(self, "is_running", False)
        if is_running:
            self.end_runner()
        
        else:
            self.start_runner()

    @Slot(QKeyEvent)
    def recorded_item_list_key_press_handler(self, event : QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Delete:
            self.delete_selected_item()

    def delete_selected_item(self):
        while True:
            selected_items = self.recorded_item_list.selectedItems()
            if len(selected_items) == 0:
                break

            selected_item = selected_items[0]
            row = self.recorded_item_list.row(selected_item)
            self.recorded_item_list.takeItem(row)
            del self.record_list[row]

    def start_runner(self) -> None:
        self.record_run_btn.setText("stop (\\)")
        self.is_running = True

        random_delay_min_max = None
        if self.use_random_delay_check.isChecked():
            random_delay_min = self.ramdom_delay_min_spin.value()
            random_delay_max = self.ramdom_delay_max_spin.value()
            random_delay_min_max = (random_delay_min, random_delay_max)

        self.runner = Runner(self.dd_obj, self.record_list, random_delay_min_max)
        def end_callback():
            self.record_run_btn.setText("run (\\)")
            self.is_running = False

        self.runner.end_callback = end_callback
        self.runner.start()

    def end_runner(self) -> None:
        self.record_run_btn.setText("run (\\)")
        self.is_running = False

        self.runner.stop()

    @Slot(tuple)
    def press_release_signal_handler(self, key_info : tuple[RecordType, str, int, KeyState, float]) -> None:
        vk = key_info[2]
        if vk in self.hotkey_list:
            return

        self.record_list.append(key_info)
        self.add_item(key_info)

    @Slot(tuple)
    def click_signal_handler(self, mouse_info : tuple[RecordType, int, int, MouseButton, MouseState, float]) -> None:
        self.record_list.append(mouse_info)
        self.add_item(mouse_info)

    def add_item(self, record_info : tuple) -> None:
        record_type, *args = record_info
        if record_type == RecordType.KEYBOARD:
            self.add_key_item(args)
        elif record_type == RecordType.MOUSE:
            self.add_mouse_item(args)

    def add_items(self, record_list : list[tuple]) -> None:
        for record_info in record_list:
            self.add_item(record_info)

    def add_key_item(self, key_info : tuple[str, int, KeyState, float]) -> None:
        char, vk, state, delay = key_info

        state_text = state.to_string()
        item_text = f"{RecordType.KEYBOARD.to_string()}\t {state_text}\t {char}\t ({vk})\t {delay}"

        self.recorded_item_list.addItem(item_text)

    def add_mouse_item(self, mouse_info : tuple[int, int, MouseButton, MouseState, float]) -> None:
        x, y, button, state, delay = mouse_info
        state_text = state.to_string()
        button_text = button.to_string()
        item_text = f"{RecordType.MOUSE.to_string()}\t {state_text}\t {button_text}\t ({x}, {y})\t {delay}"

        self.recorded_item_list.addItem(item_text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()