from PySide6.QtWidgets import QWidget

from form.record_file_form import Ui_record_file_form


class RecordFileTab(QWidget, Ui_record_file_form):
    def __init__(self):
        super(RecordFileTab, self).__init__()
        self.setupUi(self)