# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_stats.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_useStatisticsForm(object):
    def setupUi(self, useStatisticsForm):
        if not useStatisticsForm.objectName():
            useStatisticsForm.setObjectName(u"useStatisticsForm")
        useStatisticsForm.resize(622, 382)
        self.gridLayout = QGridLayout(useStatisticsForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.useStatisticsWidgetContianer = QWidget(useStatisticsForm)
        self.useStatisticsWidgetContianer.setObjectName(u"useStatisticsWidgetContianer")
        self.gridLayout_2 = QGridLayout(self.useStatisticsWidgetContianer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttonsContainer = QWidget(self.useStatisticsWidgetContianer)
        self.buttonsContainer.setObjectName(u"buttonsContainer")
        self.verticalLayout = QVBoxLayout(self.buttonsContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.startListening = QPushButton(self.buttonsContainer)
        self.startListening.setObjectName(u"startListening")

        self.verticalLayout.addWidget(self.startListening)

        self.stopListening = QPushButton(self.buttonsContainer)
        self.stopListening.setObjectName(u"stopListening")

        self.verticalLayout.addWidget(self.stopListening)


        self.gridLayout_2.addWidget(self.buttonsContainer, 0, 0, 1, 1)

        self.statsViewContainer = QWidget(self.useStatisticsWidgetContianer)
        self.statsViewContainer.setObjectName(u"statsViewContainer")
        self.gridLayout_3 = QGridLayout(self.statsViewContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.maxPressure = QLabel(self.statsViewContainer)
        self.maxPressure.setObjectName(u"maxPressure")

        self.gridLayout_3.addWidget(self.maxPressure, 1, 0, 1, 1)

        self.minPressure = QLabel(self.statsViewContainer)
        self.minPressure.setObjectName(u"minPressure")

        self.gridLayout_3.addWidget(self.minPressure, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.statsViewContainer, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.gridLayout.addWidget(self.useStatisticsWidgetContianer, 0, 0, 1, 1)


        self.retranslateUi(useStatisticsForm)

        QMetaObject.connectSlotsByName(useStatisticsForm)
    # setupUi

    def retranslateUi(self, useStatisticsForm):
        useStatisticsForm.setWindowTitle(QCoreApplication.translate("useStatisticsForm", u"Form", None))
        self.startListening.setText(QCoreApplication.translate("useStatisticsForm", u"Come\u00e7ar coleta", None))
        self.stopListening.setText(QCoreApplication.translate("useStatisticsForm", u"Interromper coleta", None))
        self.maxPressure.setText(QCoreApplication.translate("useStatisticsForm", u"maxPressure", None))
        self.minPressure.setText(QCoreApplication.translate("useStatisticsForm", u"minPressure", None))
    # retranslateUi

