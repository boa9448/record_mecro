import os
from typing import Callable
from glob import glob
from ctypes import wintypes

from PySide6.QtCore import Slot, QByteArray
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QShowEvent, QHideEvent, QCloseEvent

from form.record_file_form import Ui_record_file_form
from recorder import Recorder, Runner
from class_dd import ClassDD
import hotkey

class RecordFileTab(QWidget, Ui_record_file_form):
    RECORD_FILE_RUN_HOTKEY_ID = 0
    RECORD_FILE_RUN_HOTKEY = hotkey.VK_OEM_5

    def __init__(self):
        super(RecordFileTab, self).__init__()
        self.setupUi(self)

        self.record_open_folder_btn.clicked.connect(self.record_open_folde_btn_clicked_handler)
        self.record_file_run_btn.clicked.connect(self.record_file_run_btn_clicked_handler)

        self.init_combo()

        self.record_list = []

        self.PLAY_RUN_BUTTON_TR_TEXT = self.tr("run (\\)")
        self.PLAY_STOP_BUTTON_TR_TEXT = self.tr("stop (\\)")

    def showEvent(self, event: QShowEvent) -> None:
        hotkey.register_hotkey(self.winId(), self.RECORD_FILE_RUN_HOTKEY_ID, self.RECORD_FILE_RUN_HOTKEY)
        return super().showEvent(event)

    def hideEvent(self, event : QHideEvent) -> None:
        hotkey.unregister_hotkey(self.winId(), self.RECORD_FILE_RUN_HOTKEY_ID)
        return super().hideEvent(event)

    def closeEvent(self, event : QCloseEvent) -> None:
        hotkey.unregister_hotkey(self.winId(), self.RECORD_FILE_RUN_HOTKEY_ID)
        return super().closeEvent(event)

    def nativeEvent(self, eventType: QByteArray, message: int) -> object:
        if eventType == b"windows_generic_MSG":
            msg = wintypes.MSG.from_address(message.__int__())
            if msg.message == hotkey.WM_HOTKEY:
                if msg.wParam == self.RECORD_FILE_RUN_HOTKEY_ID:
                    self.record_file_run_btn_clicked_handler()

        return super().nativeEvent(eventType, message)

    def retranslateUi(self, record_file_form):
        self.init_combo()
        return super().retranslateUi(record_file_form)

    def init_combo(self) -> None:
        self.run_type_combo.clear()
        self.run_type_combo_data = [self.tr("First selected only")
                                    , self.tr("selected all")
                                    , self.tr("all")
                                    , self.tr("all loop")]
        self.run_type_combo.addItems(self.run_type_combo_data)

    @Slot()
    def record_open_folde_btn_clicked_handler(self) -> None:
        dir_path = QFileDialog.getExistingDirectory(self, self.tr("Open Directory"), "", QFileDialog.ShowDirsOnly)
        if dir_path:
            self.record_file_list.clear()

            json_file_list = glob(os.path.join(dir_path, "*.json"))
            self.add_record_list(json_file_list)

    def add_record(self, file_path : str) -> None:
        record = Recorder.load_record(file_path)
        self.record_list.append(record)
        self.record_file_list.addItem(file_path)

    def add_record_list(self, file_path_list : list[str]) -> None:
        for file_path in file_path_list:
            self.add_record(file_path)

    @Slot()
    def record_file_run_btn_clicked_handler(self) -> None:
        is_running = getattr(self, "is_running", False)
        if is_running:
            self.exit_runner()
        else:
            def end_callback() -> None:
                self.record_file_run_btn.setText(self.PLAY_RUN_BUTTON_TR_TEXT)
                self.is_running = False
            self.start_runner(end_callback)

        self.is_running = not is_running

    def start_runner(self, end_callback : Callable | None = None) -> None:
        self.record_file_run_btn.setText(self.PLAY_STOP_BUTTON_TR_TEXT)

        random_delay_min = 0
        random_delay_max = 0
        if self.use_random_delay_check.isChecked():
            random_delay_min = self.ramdom_delay_min_spin.value()
            random_delay_max = self.ramdom_delay_max_spin.value()

        self.runner = Runner(ClassDD(None))
        self.runner.add_record_list(self.record_list)
        self.runner.set_random_delay(random_delay_min, random_delay_max)
        self.runner.set_end_callback(end_callback)
        self.runner.start()

    def exit_runner(self) -> None:
        self.record_file_run_btn.setText(self.PLAY_RUN_BUTTON_TR_TEXT)
        self.runner.exit()