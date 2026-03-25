# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_profile_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QListView,
    QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_gameProfileWidgetForm(object):
    def setupUi(self, gameProfileWidgetForm):
        if not gameProfileWidgetForm.objectName():
            gameProfileWidgetForm.setObjectName(u"gameProfileWidgetForm")
        gameProfileWidgetForm.resize(739, 491)
        self.gridLayout = QGridLayout(gameProfileWidgetForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gameProfileContainer = QWidget(gameProfileWidgetForm)
        self.gameProfileContainer.setObjectName(u"gameProfileContainer")
        self.horizontalLayout = QHBoxLayout(self.gameProfileContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gameProfileListContainer = QWidget(self.gameProfileContainer)
        self.gameProfileListContainer.setObjectName(u"gameProfileListContainer")
        self.verticalLayout = QVBoxLayout(self.gameProfileListContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gameProfileList = QListWidget(self.gameProfileListContainer)
        self.gameProfileList.setObjectName(u"gameProfileList")

        self.verticalLayout.addWidget(self.gameProfileList)


        self.horizontalLayout.addWidget(self.gameProfileListContainer)

        self.controlContainer = QWidget(self.gameProfileContainer)
        self.controlContainer.setObjectName(u"controlContainer")
        self.gridLayout_2 = QGridLayout(self.controlContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.profileListView = QListView(self.controlContainer)
        self.profileListView.setObjectName(u"profileListView")

        self.gridLayout_2.addWidget(self.profileListView, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.controlContainer)

        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout.addWidget(self.gameProfileContainer, 0, 0, 1, 1)


        self.retranslateUi(gameProfileWidgetForm)

        QMetaObject.connectSlotsByName(gameProfileWidgetForm)
    # setupUi

    def retranslateUi(self, gameProfileWidgetForm):
        gameProfileWidgetForm.setWindowTitle(QCoreApplication.translate("gameProfileWidgetForm", u"Form", None))
    # retranslateUi

