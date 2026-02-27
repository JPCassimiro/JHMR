# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connection_manager.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_loggerForm(object):
    def setupUi(self, loggerForm):
        if not loggerForm.objectName():
            loggerForm.setObjectName(u"loggerForm")
        loggerForm.resize(652, 453)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loggerForm.sizePolicy().hasHeightForWidth())
        loggerForm.setSizePolicy(sizePolicy)
        loggerForm.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(loggerForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.windowContainer = QWidget(loggerForm)
        self.windowContainer.setObjectName(u"windowContainer")
        self.gridLayout_2 = QGridLayout(self.windowContainer)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.deviceListContainer = QWidget(self.windowContainer)
        self.deviceListContainer.setObjectName(u"deviceListContainer")
        self.gridLayout_3 = QGridLayout(self.deviceListContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.deviceListWidget = QListWidget(self.deviceListContainer)
        self.deviceListWidget.setObjectName(u"deviceListWidget")

        self.gridLayout_3.addWidget(self.deviceListWidget, 0, 0, 1, 1)

        self.deviceListButtonContainer = QWidget(self.deviceListContainer)
        self.deviceListButtonContainer.setObjectName(u"deviceListButtonContainer")
        self.horizontalLayout = QHBoxLayout(self.deviceListButtonContainer)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.reloadListButton = QToolButton(self.deviceListButtonContainer)
        self.reloadListButton.setObjectName(u"reloadListButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.reloadListButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.reloadListButton)

        self.pairDeviceButton = QPushButton(self.deviceListButtonContainer)
        self.pairDeviceButton.setObjectName(u"pairDeviceButton")

        self.horizontalLayout.addWidget(self.pairDeviceButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addWidget(self.deviceListButtonContainer, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.deviceListContainer, 0, 0, 1, 1)

        self.selectedDeviceContainer = QWidget(self.windowContainer)
        self.selectedDeviceContainer.setObjectName(u"selectedDeviceContainer")
        self.verticalLayout_2 = QVBoxLayout(self.selectedDeviceContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.deviceContainer = QWidget(self.selectedDeviceContainer)
        self.deviceContainer.setObjectName(u"deviceContainer")
        self.gridLayout_5 = QGridLayout(self.deviceContainer)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.verticalLayout_2.addWidget(self.deviceContainer)

        self.unpairDeviceButton = QPushButton(self.selectedDeviceContainer)
        self.unpairDeviceButton.setObjectName(u"unpairDeviceButton")

        self.verticalLayout_2.addWidget(self.unpairDeviceButton)

        self.sppStateButton = QPushButton(self.selectedDeviceContainer)
        self.sppStateButton.setObjectName(u"sppStateButton")

        self.verticalLayout_2.addWidget(self.sppStateButton)

        self.hidStateButton = QPushButton(self.selectedDeviceContainer)
        self.hidStateButton.setObjectName(u"hidStateButton")

        self.verticalLayout_2.addWidget(self.hidStateButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.selectedDeviceContainer, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.gridLayout.addWidget(self.windowContainer, 0, 2, 1, 1)


        self.retranslateUi(loggerForm)

        QMetaObject.connectSlotsByName(loggerForm)
    # setupUi

    def retranslateUi(self, loggerForm):
        loggerForm.setWindowTitle(QCoreApplication.translate("loggerForm", u"Form", None))
        self.reloadListButton.setText(QCoreApplication.translate("loggerForm", u"...", None))
        self.pairDeviceButton.setText(QCoreApplication.translate("loggerForm", u"Emparelhar dispositivo", None))
        self.unpairDeviceButton.setText(QCoreApplication.translate("loggerForm", u"Desemparelhar dispositvo", None))
        self.sppStateButton.setText(QCoreApplication.translate("loggerForm", u"Conectar/Desconectar SPP", None))
        self.hidStateButton.setText(QCoreApplication.translate("loggerForm", u"Conectar/Desconectar HID", None))
    # retranslateUi

