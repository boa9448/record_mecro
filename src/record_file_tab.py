import os
from glob import glob

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QShowEvent, QHideEvent, QCloseEvent

from form.record_file_form import Ui_record_file_form
import hotkey

class RecordFileTab(QWidget, Ui_record_file_form):
    def __init__(self):
        super(RecordFileTab, self).__init__()
        self.setupUi(self)

        self.record_open_folder_btn.clicked.connect(self.record_open_folde_btn_clicked_handler)

        self.file_list = []

    def showEvent(self, event: QShowEvent) -> None:
        hotkey.register_hotkey(self.winId(), 0, hotkey.VK_OEM_5)
        return super().showEvent(event)

    def hideEvent(self, event : QHideEvent) -> None:
        hotkey.unregister_hotkey(self.winId(), 0)
        return super().hideEvent(event)

    def closeEvent(self, event : QCloseEvent) -> None:
        hotkey.unregister_hotkey(self.winId(), 0)
        return super().closeEvent(event)

    @Slot()
    def record_open_folde_btn_clicked_handler(self) -> None:
        dir_path = QFileDialog.getExistingDirectory(self, self.tr("Open Directory"), "", QFileDialog.ShowDirsOnly)
        if dir_path:
            self.record_file_list.clear()

            json_file_list = glob(os.path.join(dir_path, "*.json"))
            self.add_items(json_file_list)

    def add_item(self, file_path):
        self.file_list.append(file_path)
        self.record_file_list.addItem(file_path)

    def add_items(self, file_path_list):
        self.file_list.extend(file_path_list)
        self.record_file_list.addItems(file_path_list)