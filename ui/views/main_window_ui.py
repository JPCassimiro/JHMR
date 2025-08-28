# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Lato"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 8, 8, 8)
        self.titleWidget = QWidget(self.centralwidget)
        self.titleWidget.setObjectName(u"titleWidget")
        self.verticalLayout_2 = QVBoxLayout(self.titleWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout.addWidget(self.titleWidget, 0, 1, 1, 1)

        self.stackedWidgetContainer = QWidget(self.centralwidget)
        self.stackedWidgetContainer.setObjectName(u"stackedWidgetContainer")
        self.stackedWidgetContainer.setSizeIncrement(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.stackedWidgetContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget = QStackedWidget(self.stackedWidgetContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.stackedWidget.addWidget(self.widget_2)
        self.widget_3 = QWidget()
        self.widget_3.setObjectName(u"widget_3")
        self.stackedWidget.addWidget(self.widget_3)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.stackedWidgetContainer, 2, 1, 1, 1)

        self.patientWidget = QWidget(self.centralwidget)
        self.patientWidget.setObjectName(u"patientWidget")
        self.horizontalLayout = QHBoxLayout(self.patientWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout.addWidget(self.patientWidget, 3, 1, 1, 1)

        self.sideMenu_2 = QWidget(self.centralwidget)
        self.sideMenu_2.setObjectName(u"sideMenu_2")
        self.sideMenu = QVBoxLayout(self.sideMenu_2)
        self.sideMenu.setObjectName(u"sideMenu")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.sideMenu.addItem(self.verticalSpacer_2)

        self.connectionMenuButton = QPushButton(self.sideMenu_2)
        self.connectionMenuButton.setObjectName(u"connectionMenuButton")

        self.sideMenu.addWidget(self.connectionMenuButton)

        self.placeholderButton = QPushButton(self.sideMenu_2)
        self.placeholderButton.setObjectName(u"placeholderButton")

        self.sideMenu.addWidget(self.placeholderButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sideMenu.addItem(self.verticalSpacer_3)

        self.sideMenuLine = QFrame(self.sideMenu_2)
        self.sideMenuLine.setObjectName(u"sideMenuLine")
        self.sideMenuLine.setLineWidth(1)
        self.sideMenuLine.setFrameShape(QFrame.Shape.HLine)
        self.sideMenuLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.sideMenu.addWidget(self.sideMenuLine)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sideMenu.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.sideMenu_2, 0, 0, 4, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(2, 8)
        self.gridLayout.setRowStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.connectionMenuButton.setText(QCoreApplication.translate("MainWindow", u"Conex\u00e3o com joystick", None))
        self.placeholderButton.setText(QCoreApplication.translate("MainWindow", u"Placeholder Screen", None))
    # retranslateUi

