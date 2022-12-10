import os
import sys

from PySide6.QtCore import QTranslator
from PySide6.QtWidgets import QApplication, QMainWindow

from form.main_form import Ui_MainWindow
from record_tab import RecordTab
from record_file_tab import RecordFileTab

from class_dd import ClassDD


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.change_lang("kor")

        self.action_lang_eng.triggered.connect(lambda : self.change_lang("eng"))
        self.action_lang_kor.triggered.connect(lambda : self.change_lang("kor"))

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        dd_path = os.path.join(cur_dir, "3rdparty", "DD64.dll")
        dd_obj = ClassDD(dd_path)

        self.tabWidget.addTab(RecordTab(), self.tr("record"))
        self.tabWidget.addTab(RecordFileTab(), self.tr("record_file"))

    def change_lang(self, lang : str) -> None:
        app = QApplication.instance()

        if hasattr(self, "trasnlator"):
            app.removeTranslator(self.trasnlator)

        trasnlator = QTranslator()
        trasnlator.load(f"lang_{lang}.qm")
        app.installTranslator(trasnlator)
        self.trasnlator = trasnlator

        self.retranslateUi(self)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()