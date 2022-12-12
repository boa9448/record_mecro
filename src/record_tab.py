import os
from typing import Callable
from ctypes import wintypes

from PySide6.QtCore import Qt, Slot, Signal, QByteArray, QObject, QEvent
from PySide6.QtWidgets import QFileDialog, QWidget
from PySide6.QtGui import QCloseEvent, QKeyEvent, QShowEvent, QHideEvent

from form.record_form import Ui_record_form
from class_dd import ClassDD
from recorder import (Recorder
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


class RecordTab(QWidget, Ui_record_form):
    press_release_signal = Signal(tuple)
    click_signal = Signal(tuple)

    RECORD_START_HOTKEY_ID = 0
    RECORD_RUN_HOTKEY_ID = 1

    RECORD_START_HOTKEY = hotkey.VK_OEM_PLUS
    RECORD_RUN_HOTKEY = hotkey.VK_OEM_5

    def __init__(self) -> None:
        super(RecordTab, self).__init__()
        self.setupUi(self)

        self.record_start_btn.clicked.connect(self.record_start_btn_clicked_handler)
        self.record_save_btn.clicked.connect(self.record_save_btn_clicked_handler)
        self.record_load_btn.clicked.connect(self.record_load_btn_clicked_handler)
        self.record_run_btn.clicked.connect(self.record_run_btn_clicked_handler)

        key_press(self.recorded_item_list).connect(self.recorded_item_list_key_press_handler)

        self.press_release_signal.connect(self.press_release_signal_handler)
        self.click_signal.connect(self.click_signal_handler)

        self.record = []

        self.hotkey_list = [self.RECORD_START_HOTKEY, self.RECORD_RUN_HOTKEY]

        self.RECORD_START_BUTTON_TR_TEXT = self.tr("start (=)")
        self.RECORD_STOP_BUTTON_TR_TEXT = self.tr("stop (=)")
        self.PLAY_RUN_BUTTON_TR_TEXT = self.tr("run (\\)")
        self.PLAY_STOP_BUTTON_TR_TEXT = self.tr("stop (\\)")

    def showEvent(self, event: QShowEvent) -> None:
        hotkey.register_hotkey(self.winId(), self.RECORD_START_HOTKEY_ID, self.RECORD_START_HOTKEY)
        hotkey.register_hotkey(self.winId(), self.RECORD_RUN_HOTKEY_ID, self.RECORD_RUN_HOTKEY)
        return super().showEvent(event)

    def hideEvent(self, event : QHideEvent) -> None:
        hotkey.unregister_hotkey(self.winId(), self.RECORD_START_HOTKEY_ID)
        hotkey.unregister_hotkey(self.winId(), self.RECORD_RUN_HOTKEY_ID)

    def closeEvent(self, event: QCloseEvent) -> None:
        hotkey.unregister_hotkey(self.winId(), self.RECORD_START_HOTKEY_ID)
        hotkey.unregister_hotkey(self.winId(), self.RECORD_RUN_HOTKEY_ID)

    def nativeEvent(self, eventType: QByteArray, message: int) -> object:
        if eventType == b"windows_generic_MSG":
            msg = wintypes.MSG.from_address(message.__int__())
            if msg.message == hotkey.WM_HOTKEY:
                if msg.wParam == self.RECORD_START_HOTKEY_ID:
                    self.record_start_btn_clicked_handler()
                elif msg.wParam == self.RECORD_RUN_HOTKEY_ID:
                    self.record_run_btn_clicked_handler()

        return super().nativeEvent(eventType, message)
        
    @Slot()
    def record_start_btn_clicked_handler(self) -> None:
        is_recording = getattr(self, "is_recording", False)
        if is_recording:
            self.record_start_btn.setText(self.RECORD_START_BUTTON_TR_TEXT)
            self.is_recording = False

            self.recorder.stop()

        else:
            self.record_start_btn.setText(self.RECORD_STOP_BUTTON_TR_TEXT)
            self.is_recording = True

            self.recorder = Recorder(lambda data : self.press_release_signal.emit(data)
                                    , lambda data : self.click_signal.emit(data))
            self.recorder.start()

    @Slot()
    def record_save_btn_clicked_handler(self) -> None:
        file_path = QFileDialog.getSaveFileName(self, self.tr("Save Record"), os.getcwd(), self.tr("Json Files (*.json)"))[0]
        if not file_path:
            return
        Recorder.save_record(self.record, file_path)

    @Slot()
    def record_load_btn_clicked_handler(self) -> None:
        file_path = QFileDialog.getOpenFileName(self, self.tr("Load Record"), os.getcwd(), self.tr("Json Files (*.json)"))[0]
        if not file_path:
            return
        self.record = Recorder.load_record(file_path)
        self.add_record(self.record)

    @Slot()
    def record_run_btn_clicked_handler(self) -> None:
        print("record_run_btn_clicked_handler")
        is_running = getattr(self, "is_running", False)
        if is_running:
            self.exit_runner()
        
        else:
            def end_callback():
                self.record_run_btn.setText(self.PLAY_RUN_BUTTON_TR_TEXT)
                self.is_running = False

            self.start_runner(end_callback)

        self.is_running = not is_running

    def start_runner(self, end_callback : Callable | None = None) -> None:
        self.record_run_btn.setText(self.PLAY_STOP_BUTTON_TR_TEXT)

        random_delay_min = 0
        random_delay_max = 0
        if self.use_random_delay_check.isChecked():
            random_delay_min = self.ramdom_delay_min_spin.value()
            random_delay_max = self.ramdom_delay_max_spin.value()

        self.runner = Runner(ClassDD(None))
        self.runner.add_record(self.record)
        self.runner.set_random_delay(random_delay_min, random_delay_max)
        self.runner.set_end_callback(end_callback)
        self.runner.start()

    def exit_runner(self) -> None:
        self.record_run_btn.setText(self.PLAY_RUN_BUTTON_TR_TEXT)
        self.runner.exit()

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
            del self.record[row]

    @Slot(tuple)
    def press_release_signal_handler(self, key_info : tuple[RecordType, str, int, KeyState, float]) -> None:
        vk = key_info[2]
        if vk in self.hotkey_list:
            return

        self.record.append(key_info)
        self.add_item(key_info)

    @Slot(tuple)
    def click_signal_handler(self, mouse_info : tuple[RecordType, int, int, MouseButton, MouseState, float]) -> None:
        self.record.append(mouse_info)
        self.add_item(mouse_info)

    def add_item(self, item : tuple) -> None:
        record_type, *args = item
        if record_type == RecordType.KEYBOARD:
            self.add_key_item(args)
        elif record_type == RecordType.MOUSE:
            self.add_mouse_item(args)

    def add_record(self, record : list[tuple]) -> None:
        for item in record:
            self.add_item(item)

    def add_key_item(self, key_info : tuple[str, int, KeyState, float]) -> None:
        char, vk, state, event_time = key_info

        state_text = state.to_string()
        item_text = f"{RecordType.KEYBOARD.to_string()}\t {state_text}\t {char}\t ({vk})\t {event_time}"

        self.recorded_item_list.addItem(item_text)

    def add_mouse_item(self, mouse_info : tuple[int, int, MouseButton, MouseState, float]) -> None:
        x, y, button, state, event_time = mouse_info
        state_text = state.to_string()
        button_text = button.to_string()
        item_text = f"{RecordType.MOUSE.to_string()}\t {state_text}\t {button_text}\t ({x}, {y})\t {event_time}"

        self.recorded_item_list.addItem(item_text)