# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_card_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_configCardWidgetForm(object):
    def setupUi(self, configCardWidgetForm):
        if not configCardWidgetForm.objectName():
            configCardWidgetForm.setObjectName(u"configCardWidgetForm")
        configCardWidgetForm.resize(195, 96)
        self.gridLayout_2 = QGridLayout(configCardWidgetForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.configCardContainer = QWidget(configCardWidgetForm)
        self.configCardContainer.setObjectName(u"configCardContainer")
        self.gridLayout = QGridLayout(self.configCardContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.littleLabel = QLabel(self.configCardContainer)
        self.littleLabel.setObjectName(u"littleLabel")

        self.gridLayout.addWidget(self.littleLabel, 0, 0, 1, 1)

        self.keyLabel = QLabel(self.configCardContainer)
        self.keyLabel.setObjectName(u"keyLabel")

        self.gridLayout.addWidget(self.keyLabel, 1, 3, 1, 1)

        self.ringLabel = QLabel(self.configCardContainer)
        self.ringLabel.setObjectName(u"ringLabel")

        self.gridLayout.addWidget(self.ringLabel, 0, 1, 1, 1)

        self.middleLabel = QLabel(self.configCardContainer)
        self.middleLabel.setObjectName(u"middleLabel")

        self.gridLayout.addWidget(self.middleLabel, 1, 0, 1, 1)

        self.indexLabel = QLabel(self.configCardContainer)
        self.indexLabel.setObjectName(u"indexLabel")

        self.gridLayout.addWidget(self.indexLabel, 1, 1, 1, 1)

        self.repeatLabel = QLabel(self.configCardContainer)
        self.repeatLabel.setObjectName(u"repeatLabel")

        self.gridLayout.addWidget(self.repeatLabel, 2, 0, 1, 1)

        self.durationLabel = QLabel(self.configCardContainer)
        self.durationLabel.setObjectName(u"durationLabel")

        self.gridLayout.addWidget(self.durationLabel, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.configCardContainer, 0, 0, 1, 1)


        self.retranslateUi(configCardWidgetForm)

        QMetaObject.connectSlotsByName(configCardWidgetForm)
    # setupUi

    def retranslateUi(self, configCardWidgetForm):
        configCardWidgetForm.setWindowTitle(QCoreApplication.translate("configCardWidgetForm", u"Form", None))
        self.littleLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"TextLabel", None))
        self.keyLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"TextLabel", None))
        self.ringLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"TextLabel", None))
        self.middleLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"TextLabel", None))
        self.indexLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"TextLabel", None))
        self.repeatLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"TextLabel", None))
        self.durationLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"TextLabel", None))
    # retranslateUi

