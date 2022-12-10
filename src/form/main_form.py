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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDoubleSpinBox,
    QFormLayout, QGridLayout, QGroupBox, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QWidget)

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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"\uad74\ub9bc"])
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.record_load_btn = QPushButton(self.groupBox_2)
        self.record_load_btn.setObjectName(u"record_load_btn")

        self.gridLayout_4.addWidget(self.record_load_btn, 2, 0, 1, 1)

        self.record_save_btn = QPushButton(self.groupBox_2)
        self.record_save_btn.setObjectName(u"record_save_btn")

        self.gridLayout_4.addWidget(self.record_save_btn, 1, 0, 1, 1)

        self.record_start_btn = QPushButton(self.groupBox_2)
        self.record_start_btn.setObjectName(u"record_start_btn")

        self.gridLayout_4.addWidget(self.record_start_btn, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.ramdom_delay_min_spin = QDoubleSpinBox(self.groupBox_3)
        self.ramdom_delay_min_spin.setObjectName(u"ramdom_delay_min_spin")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ramdom_delay_min_spin)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.ramdom_delay_max_spin = QDoubleSpinBox(self.groupBox_3)
        self.ramdom_delay_max_spin.setObjectName(u"ramdom_delay_max_spin")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ramdom_delay_max_spin)


        self.gridLayout_5.addLayout(self.formLayout, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 141, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.use_random_delay_check = QCheckBox(self.groupBox_3)
        self.use_random_delay_check.setObjectName(u"use_random_delay_check")

        self.gridLayout_5.addWidget(self.use_random_delay_check, 1, 0, 1, 1)

        self.record_run_btn = QPushButton(self.groupBox_3)
        self.record_run_btn.setObjectName(u"record_run_btn")

        self.gridLayout_5.addWidget(self.record_run_btn, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.recorded_item_list = QListWidget(self.groupBox)
        self.recorded_item_list.setObjectName(u"recorded_item_list")
        self.recorded_item_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.gridLayout_2.addWidget(self.recorded_item_list, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 2, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

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

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.action_lang_kor.setText(QCoreApplication.translate("MainWindow", u"kor", None))
        self.action_lang_eng.setText(QCoreApplication.translate("MainWindow", u"eng", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"record", None))
        self.record_load_btn.setText(QCoreApplication.translate("MainWindow", u"load", None))
        self.record_save_btn.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.record_start_btn.setText(QCoreApplication.translate("MainWindow", u"start (=)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"run", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"random delay min : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"random delay max : ", None))
        self.use_random_delay_check.setText(QCoreApplication.translate("MainWindow", u"use random delay", None))
        self.record_run_btn.setText(QCoreApplication.translate("MainWindow", u"run (\\)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"recorded item", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"record", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"recoreded files", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
        self.menu_lang.setTitle(QCoreApplication.translate("MainWindow", u"lang", None))
        self.menu_info.setTitle(QCoreApplication.translate("MainWindow", u"info", None))
    # retranslateUi
