from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QShowEvent, QHideEvent, QCloseEvent

from form.record_file_form import Ui_record_file_form
import hotkey

class RecordFileTab(QWidget, Ui_record_file_form):
    def __init__(self):
        super(RecordFileTab, self).__init__()
        self.setupUi(self)

    def showEvent(self, event: QShowEvent) -> None:
        hotkey.register_hotkey(self.winId(), 0, hotkey.VK_OEM_5)
        return super().showEvent(event)

    def hideEvent(self, event : QHideEvent) -> None:
        hotkey.unregister_hotkey(self.winId(), 0)
        return super().hideEvent(event)

    def closeEvent(self, event : QCloseEvent) -> None:
        hotkey.unregister_hotkey(self.winId(), 0)
        return super().closeEvent(event)