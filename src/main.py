import os
import sys

from PySide6.QtCore import QTranslator
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QCloseEvent

from form.main_form import Ui_MainWindow
from record_tab import RecordTab
from record_file_tab import RecordFileTab

from class_dd import ClassDD


def root_dir() -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return base_path
        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.action_exit.triggered.connect(self.close)
        self.action_lang_eng.triggered.connect(lambda : self.change_lang("eng"))
        self.action_lang_kor.triggered.connect(lambda : self.change_lang("kor"))

        cur_dir = root_dir()
        dd_path = os.path.join(cur_dir, "3rdparty", "DD64.dll")
        dd_obj = ClassDD(dd_path)

        self.tabWidget.addTab(RecordTab(), self.tr("record"))
        self.tabWidget.addTab(RecordFileTab(), self.tr("record_file"))

        self.change_lang("kor")

    def closeEvent(self, event : QCloseEvent) -> None:
        tab_count = self.tabWidget.count()
        for i in range(tab_count):
            self.tabWidget.widget(i).close()

        return super().closeEvent(event)

    def change_lang(self, lang : str) -> None:
        app = QApplication.instance()

        if hasattr(self, "trasnlator"):
            app.removeTranslator(self.trasnlator)

        trasnlator = QTranslator()
        lang_path = os.path.join(root_dir(), "translations", f"lang_{lang}.qm")
        trasnlator.load(lang_path)
        app.installTranslator(trasnlator)
        self.trasnlator = trasnlator

        teb_count = self.tabWidget.count()
        tab_name_list = [self.tr("record"), self.tr("record_file")]
        for idx in range(teb_count):
            self.tabWidget.setTabText(idx, tab_name_list[idx])
            tab = self.tabWidget.widget(idx)
            tab.retranslateUi(tab)

        self.retranslateUi(self)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()