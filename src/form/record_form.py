# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'record_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDoubleSpinBox,
    QFormLayout, QGridLayout, QGroupBox, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_record_form(object):
    def setupUi(self, record_form):
        if not record_form.objectName():
            record_form.setObjectName(u"record_form")
        record_form.resize(400, 300)
        self.gridLayout = QGridLayout(record_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(record_form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.recorded_item_list = QListWidget(self.groupBox)
        self.recorded_item_list.setObjectName(u"recorded_item_list")
        self.recorded_item_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.gridLayout_2.addWidget(self.recorded_item_list, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)

        self.groupBox_2 = QGroupBox(record_form)
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


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(record_form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.use_random_delay_check = QCheckBox(self.groupBox_3)
        self.use_random_delay_check.setObjectName(u"use_random_delay_check")

        self.gridLayout_5.addWidget(self.use_random_delay_check, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 141, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.ramdom_delay_min_spin = QDoubleSpinBox(self.groupBox_3)
        self.ramdom_delay_min_spin.setObjectName(u"ramdom_delay_min_spin")
        self.ramdom_delay_min_spin.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ramdom_delay_min_spin)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.ramdom_delay_max_spin = QDoubleSpinBox(self.groupBox_3)
        self.ramdom_delay_max_spin.setObjectName(u"ramdom_delay_max_spin")
        self.ramdom_delay_max_spin.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ramdom_delay_max_spin)


        self.gridLayout_5.addLayout(self.formLayout, 2, 0, 1, 1)

        self.record_run_btn = QPushButton(self.groupBox_3)
        self.record_run_btn.setObjectName(u"record_run_btn")

        self.gridLayout_5.addWidget(self.record_run_btn, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)


        self.retranslateUi(record_form)

        QMetaObject.connectSlotsByName(record_form)
    # setupUi

    def retranslateUi(self, record_form):
        record_form.setWindowTitle(QCoreApplication.translate("record_form", u"record", None))
        self.groupBox.setTitle(QCoreApplication.translate("record_form", u"recorded item", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("record_form", u"record", None))
        self.record_load_btn.setText(QCoreApplication.translate("record_form", u"load", None))
        self.record_save_btn.setText(QCoreApplication.translate("record_form", u"save", None))
        self.record_start_btn.setText(QCoreApplication.translate("record_form", u"start (=)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("record_form", u"run", None))
        self.use_random_delay_check.setText(QCoreApplication.translate("record_form", u"use random delay", None))
        self.label.setText(QCoreApplication.translate("record_form", u"random delay min : ", None))
        self.label_2.setText(QCoreApplication.translate("record_form", u"random delay max : ", None))
        self.record_run_btn.setText(QCoreApplication.translate("record_form", u"run (\\)", None))
    # retranslateUi

