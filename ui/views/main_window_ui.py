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
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Lato"])
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.workplaceContainer = QWidget(self.centralwidget)
        self.workplaceContainer.setObjectName(u"workplaceContainer")
        self.gridLayout_3 = QGridLayout(self.workplaceContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.patientWidget = QWidget(self.workplaceContainer)
        self.patientWidget.setObjectName(u"patientWidget")
        self.horizontalLayout = QHBoxLayout(self.patientWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout_3.addWidget(self.patientWidget, 1, 1, 1, 1)

        self.stackedWidgetContainer = QWidget(self.workplaceContainer)
        self.stackedWidgetContainer.setObjectName(u"stackedWidgetContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidgetContainer.sizePolicy().hasHeightForWidth())
        self.stackedWidgetContainer.setSizePolicy(sizePolicy1)
        self.stackedWidgetContainer.setSizeIncrement(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.stackedWidgetContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.stackedWidget = QStackedWidget(self.stackedWidgetContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMidLineWidth(5)
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.stackedWidget.addWidget(self.widget_2)
        self.widget_3 = QWidget()
        self.widget_3.setObjectName(u"widget_3")
        self.stackedWidget.addWidget(self.widget_3)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.stackedWidgetContainer, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.workplaceContainer, 1, 1, 1, 1)

        self.titleWidget = QWidget(self.centralwidget)
        self.titleWidget.setObjectName(u"titleWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleWidget.sizePolicy().hasHeightForWidth())
        self.titleWidget.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.titleWidget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 3, 0, 3)

        self.gridLayout.addWidget(self.titleWidget, 0, 1, 1, 1)

        self.sideMenu_2 = QWidget(self.centralwidget)
        self.sideMenu_2.setObjectName(u"sideMenu_2")
        self.sideMenu = QVBoxLayout(self.sideMenu_2)
        self.sideMenu.setObjectName(u"sideMenu")
        self.sideMenu.setContentsMargins(0, 5, 5, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.sideMenu.addItem(self.verticalSpacer_2)

        self.logoLabel = QLabel(self.sideMenu_2)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sideMenu.addWidget(self.logoLabel)

        self.connectionMenuButton = QPushButton(self.sideMenu_2)
        self.connectionMenuButton.setObjectName(u"connectionMenuButton")
        font1 = QFont()
        font1.setFamilies([u"Lato"])
        font1.setPointSize(11)
        self.connectionMenuButton.setFont(font1)
        self.connectionMenuButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.connectionMenuButton.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"../../_internal/resources/icons/knob_orange.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.connectionMenuButton.setIcon(icon)
        self.connectionMenuButton.setIconSize(QSize(32, 32))

        self.sideMenu.addWidget(self.connectionMenuButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.calibrationButton = QPushButton(self.sideMenu_2)
        self.calibrationButton.setObjectName(u"calibrationButton")
        icon1 = QIcon()
        icon1.addFile(u"../../_internal/resources/icons/resilience_orange.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.calibrationButton.setIcon(icon1)

        self.sideMenu.addWidget(self.calibrationButton)

        self.placeholderButton = QPushButton(self.sideMenu_2)
        self.placeholderButton.setObjectName(u"placeholderButton")
        self.placeholderButton.setEnabled(True)
        self.placeholderButton.setFont(font1)
        self.placeholderButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.placeholderButton.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u"../../resources/icons/resilience_orange.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.placeholderButton.setIcon(icon2)
        self.placeholderButton.setIconSize(QSize(32, 32))
        self.placeholderButton.setCheckable(False)
        self.placeholderButton.setChecked(False)
        self.placeholderButton.setFlat(False)

        self.sideMenu.addWidget(self.placeholderButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sideMenu.addItem(self.verticalSpacer_3)

        self.sideMenuLine = QFrame(self.sideMenu_2)
        self.sideMenuLine.setObjectName(u"sideMenuLine")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sideMenuLine.sizePolicy().hasHeightForWidth())
        self.sideMenuLine.setSizePolicy(sizePolicy3)
        self.sideMenuLine.setSizeIncrement(QSize(0, 0))
        self.sideMenuLine.setLineWidth(1)
        self.sideMenuLine.setMidLineWidth(0)
        self.sideMenuLine.setFrameShape(QFrame.Shape.HLine)
        self.sideMenuLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.sideMenu.addWidget(self.sideMenuLine)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sideMenu.addItem(self.verticalSpacer)

        self.sideMenu.setStretch(2, 1)

        self.gridLayout.addWidget(self.sideMenu_2, 0, 0, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 18))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"JHMR", None))
        self.connectionMenuButton.setText(QCoreApplication.translate("MainWindow", u"Conex\u00e3o com joystick", None))
        self.calibrationButton.setText(QCoreApplication.translate("MainWindow", u"Calibra\u00e7\u00e3o", None))
        self.placeholderButton.setText(QCoreApplication.translate("MainWindow", u"Placeholder Screen", None))
    # retranslateUi

