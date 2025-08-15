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
from PySide6.QtWidgets import (QApplication, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(450, 227))
        self.logWindow = QPlainTextEdit(Form)
        self.logWindow.setObjectName(u"logWindow")
        self.logWindow.setGeometry(QRect(20, 10, 261, 201))
        self.logWindow.setReadOnly(True)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(290, 10, 139, 56))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.findButton = QPushButton(self.layoutWidget)
        self.findButton.setObjectName(u"findButton")

        self.verticalLayout.addWidget(self.findButton)

        self.onOffButton = QPushButton(self.layoutWidget)
        self.onOffButton.setObjectName(u"onOffButton")

        self.verticalLayout.addWidget(self.onOffButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logWindow.setPlainText("")
        self.findButton.setText(QCoreApplication.translate("Form", u"Encontrar dispositovos", None))
        self.onOffButton.setText(QCoreApplication.translate("Form", u"Ligar/Desligar Bluetooth", None))
    # retranslateUi

