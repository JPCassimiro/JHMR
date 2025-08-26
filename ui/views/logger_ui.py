# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logger.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 246)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(450, 227))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.logWindow = QPlainTextEdit(Form)
        self.logWindow.setObjectName(u"logWindow")
        self.logWindow.setReadOnly(True)

        self.gridLayout.addWidget(self.logWindow, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.onOffButton = QPushButton(Form)
        self.onOffButton.setObjectName(u"onOffButton")

        self.verticalLayout.addWidget(self.onOffButton)

        self.findButton = QPushButton(Form)
        self.findButton.setObjectName(u"findButton")

        self.verticalLayout.addWidget(self.findButton)

        self.pairButton = QPushButton(Form)
        self.pairButton.setObjectName(u"pairButton")

        self.verticalLayout.addWidget(self.pairButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logWindow.setPlainText("")
        self.onOffButton.setText(QCoreApplication.translate("Form", u"Ligar/Desligar Bluetooth", None))
        self.findButton.setText(QCoreApplication.translate("Form", u"Encontrar dispositivos", None))
        self.pairButton.setText(QCoreApplication.translate("Form", u"Emparelhar dispositivo", None))
    # retranslateUi

