import os
from glob import glob
from ctypes import wintypes

from PySide6.QtCore import Slot, QByteArray
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QShowEvent, QHideEvent, QCloseEvent

from form.record_file_form import Ui_record_file_form
from record import Recorder, Runner
import hotkey

class RecordFileTab(QWidget, Ui_record_file_form):
    RECORD_FILE_RUN_HOTKEY_ID = 0
    RECORD_FILE_RUN_HOTKEY = hotkey.VK_OEM_5

    def __init__(self):
        super(RecordFileTab, self).__init__()
        self.setupUi(self)

        self.record_open_folder_btn.clicked.connect(self.record_open_folde_btn_clicked_handler)
        self.record_file_run_btn.clicked.connect(self.record_file_run_btn_clicked_handler)

        self.run_type_combo_data = [self.tr("First selected only")
                                    , self.tr("selected all")
                                    , self.tr("all")
                                    , self.tr("all loop")]
        self.run_type_combo.addItems(self.run_type_combo_data)

        self.runner_list = []

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

    @Slot()
    def record_open_folde_btn_clicked_handler(self) -> None:
        dir_path = QFileDialog.getExistingDirectory(self, self.tr("Open Directory"), "", QFileDialog.ShowDirsOnly)
        if dir_path:
            self.record_file_list.clear()

            json_file_list = glob(os.path.join(dir_path, "*.json"))
            self.add_items(json_file_list)

    def add_item(self, file_path : str) -> None:
        runner = self.load_runner(file_path)
        self.runner_list.append(runner)
        self.record_file_list.addItem(file_path)

    def add_items(self, file_path_list : list[str]) -> None:
        self.runner_list.extend([self.load_runner(file_path) for file_path in file_path_list])
        self.record_file_list.addItems(file_path_list)

    def load_runner(self, file_path : str) -> Runner:
        record_item_list = Recorder.load_record(file_path)
        runner = Runner(record_item_list)
        return runner

    @Slot()
    def record_file_run_btn_clicked_handler(self) -> None:
        print("record_file_run_btn_clicked_handler")