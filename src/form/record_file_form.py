# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'record_file_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QGridLayout, QGroupBox, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_record_file_form(object):
    def setupUi(self, record_file_form):
        if not record_file_form.objectName():
            record_file_form.setObjectName(u"record_file_form")
        record_file_form.resize(400, 300)
        self.gridLayout = QGridLayout(record_file_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_4 = QGroupBox(record_file_form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.record_file_list = QListWidget(self.groupBox_4)
        self.record_file_list.setObjectName(u"record_file_list")

        self.gridLayout_7.addWidget(self.record_file_list, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(record_file_form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_8 = QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.use_random_delay_check = QCheckBox(self.groupBox_5)
        self.use_random_delay_check.setObjectName(u"use_random_delay_check")

        self.gridLayout_8.addWidget(self.use_random_delay_check, 1, 0, 1, 1)

        self.record_file_run_btn = QPushButton(self.groupBox_5)
        self.record_file_run_btn.setObjectName(u"record_file_run_btn")

        self.gridLayout_8.addWidget(self.record_file_run_btn, 4, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.ramdom_delay_min_spin = QDoubleSpinBox(self.groupBox_5)
        self.ramdom_delay_min_spin.setObjectName(u"ramdom_delay_min_spin")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.ramdom_delay_min_spin)

        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.ramdom_delay_max_spin = QDoubleSpinBox(self.groupBox_5)
        self.ramdom_delay_max_spin.setObjectName(u"ramdom_delay_max_spin")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.ramdom_delay_max_spin)


        self.gridLayout_8.addLayout(self.formLayout_2, 2, 0, 1, 1)

        self.run_type_combo = QComboBox(self.groupBox_5)
        self.run_type_combo.setObjectName(u"run_type_combo")

        self.gridLayout_8.addWidget(self.run_type_combo, 3, 0, 1, 1)

        self.record_open_folde_btn = QPushButton(self.groupBox_5)
        self.record_open_folde_btn.setObjectName(u"record_open_folde_btn")

        self.gridLayout_8.addWidget(self.record_open_folde_btn, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_5, 0, 1, 1, 1)


        self.retranslateUi(record_file_form)

        QMetaObject.connectSlotsByName(record_file_form)
    # setupUi

    def retranslateUi(self, record_file_form):
        record_file_form.setWindowTitle(QCoreApplication.translate("record_file_form", u"record_file", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("record_file_form", u"recorded files", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("record_file_form", u"run", None))
        self.use_random_delay_check.setText(QCoreApplication.translate("record_file_form", u"use random delay", None))
        self.record_file_run_btn.setText(QCoreApplication.translate("record_file_form", u"run (\\)", None))
        self.label_3.setText(QCoreApplication.translate("record_file_form", u"random delay min : ", None))
        self.label_4.setText(QCoreApplication.translate("record_file_form", u"random delay max : ", None))
        self.record_open_folde_btn.setText(QCoreApplication.translate("record_file_form", u"open folder", None))
    # retranslateUi

