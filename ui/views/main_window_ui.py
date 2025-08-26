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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.connectionMenu = QWidget()
        self.connectionMenu.setObjectName(u"connectionMenu")
        self.stackedWidget.addWidget(self.connectionMenu)
        self.placeholderMenu = QWidget()
        self.placeholderMenu.setObjectName(u"placeholderMenu")
        self.stackedWidget.addWidget(self.placeholderMenu)

        self.gridLayout.addWidget(self.stackedWidget, 2, 1, 1, 1)

        self.sideMenu_2 = QWidget(self.centralwidget)
        self.sideMenu_2.setObjectName(u"sideMenu_2")
        self.sideMenu = QVBoxLayout(self.sideMenu_2)
        self.sideMenu.setObjectName(u"sideMenu")
        self.connectionMenuButton = QPushButton(self.sideMenu_2)
        self.connectionMenuButton.setObjectName(u"connectionMenuButton")

        self.sideMenu.addWidget(self.connectionMenuButton)

        self.placeholderButton = QPushButton(self.sideMenu_2)
        self.placeholderButton.setObjectName(u"placeholderButton")

        self.sideMenu.addWidget(self.placeholderButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sideMenu.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.sideMenu_2, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.connectionMenuButton.setText(QCoreApplication.translate("MainWindow", u"Conex\u00e3o com joystick", None))
        self.placeholderButton.setText(QCoreApplication.translate("MainWindow", u"Placeholder Screen", None))
    # retranslateUi

