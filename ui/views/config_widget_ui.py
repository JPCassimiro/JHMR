# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_configForm(object):
    def setupUi(self, configForm):
        if not configForm.objectName():
            configForm.setObjectName(u"configForm")
        configForm.resize(400, 300)
        self.gridLayout = QGridLayout(configForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configContainer = QWidget(configForm)
        self.configContainer.setObjectName(u"configContainer")
        self.gridLayout_2 = QGridLayout(self.configContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sendMessageButton = QPushButton(self.configContainer)
        self.sendMessageButton.setObjectName(u"sendMessageButton")

        self.gridLayout_2.addWidget(self.sendMessageButton, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.configContainer)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.configContainer, 0, 0, 1, 1)


        self.retranslateUi(configForm)

        QMetaObject.connectSlotsByName(configForm)
    # setupUi

    def retranslateUi(self, configForm):
        configForm.setWindowTitle(QCoreApplication.translate("configForm", u"Form", None))
        self.sendMessageButton.setText(QCoreApplication.translate("configForm", u"SendMessage", None))
    # retranslateUi

