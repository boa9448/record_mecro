# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_lang_kor = QAction(MainWindow)
        self.action_lang_kor.setObjectName(u"action_lang_kor")
        self.action_lang_eng = QAction(MainWindow)
        self.action_lang_eng.setObjectName(u"action_lang_eng")
        self.action_info = QAction(MainWindow)
        self.action_info.setObjectName(u"action_info")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"\uad74\ub9bc"])
        self.tabWidget.setFont(font)

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_lang = QMenu(self.menubar)
        self.menu_lang.setObjectName(u"menu_lang")
        self.menu_info = QMenu(self.menubar)
        self.menu_info.setObjectName(u"menu_info")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_lang.menuAction())
        self.menubar.addAction(self.menu_info.menuAction())
        self.menu_file.addAction(self.action_exit)
        self.menu_lang.addAction(self.action_lang_kor)
        self.menu_lang.addAction(self.action_lang_eng)
        self.menu_info.addAction(self.action_info)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.action_lang_kor.setText(QCoreApplication.translate("MainWindow", u"kor", None))
        self.action_lang_eng.setText(QCoreApplication.translate("MainWindow", u"eng", None))
        self.action_info.setText(QCoreApplication.translate("MainWindow", u"info", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
        self.menu_lang.setTitle(QCoreApplication.translate("MainWindow", u"lang", None))
        self.menu_info.setTitle(QCoreApplication.translate("MainWindow", u"info", None))
    # retranslateUi

