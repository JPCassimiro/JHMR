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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_configCardWidgetForm(object):
    def setupUi(self, configCardWidgetForm):
        if not configCardWidgetForm.objectName():
            configCardWidgetForm.setObjectName(u"configCardWidgetForm")
        configCardWidgetForm.resize(184, 101)
        self.gridLayout_2 = QGridLayout(configCardWidgetForm)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.configCardContainer = QWidget(configCardWidgetForm)
        self.configCardContainer.setObjectName(u"configCardContainer")
        self.gridLayout = QGridLayout(self.configCardContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.otherInfoLabelContainer = QWidget(self.configCardContainer)
        self.otherInfoLabelContainer.setObjectName(u"otherInfoLabelContainer")
        self.horizontalLayout = QHBoxLayout(self.otherInfoLabelContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.durationIconLabel = QLabel(self.otherInfoLabelContainer)
        self.durationIconLabel.setObjectName(u"durationIconLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.durationIconLabel.sizePolicy().hasHeightForWidth())
        self.durationIconLabel.setSizePolicy(sizePolicy)
        self.durationIconLabel.setMinimumSize(QSize(16, 16))
        self.durationIconLabel.setMaximumSize(QSize(16, 16))
        self.durationIconLabel.setPixmap(QPixmap(u"_internal/resources/icons/timer.png"))
        self.durationIconLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.durationIconLabel)

        self.durationLabel = QLabel(self.otherInfoLabelContainer)
        self.durationLabel.setObjectName(u"durationLabel")
        self.durationLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.durationLabel)

        self.repeatIconLabel = QLabel(self.otherInfoLabelContainer)
        self.repeatIconLabel.setObjectName(u"repeatIconLabel")
        self.repeatIconLabel.setMinimumSize(QSize(16, 16))
        self.repeatIconLabel.setMaximumSize(QSize(16, 16))
        self.repeatIconLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.repeatIconLabel)

        self.keyLabel = QLabel(self.otherInfoLabelContainer)
        self.keyLabel.setObjectName(u"keyLabel")

        self.horizontalLayout.addWidget(self.keyLabel)


        self.gridLayout.addWidget(self.otherInfoLabelContainer, 1, 2, 1, 1)

        self.pressureLabelContainer = QWidget(self.configCardContainer)
        self.pressureLabelContainer.setObjectName(u"pressureLabelContainer")
        self.gridLayout_3 = QGridLayout(self.pressureLabelContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ringLabel = QLabel(self.pressureLabelContainer)
        self.ringLabel.setObjectName(u"ringLabel")
        self.ringLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.ringLabel, 0, 1, 1, 1)

        self.middleLabel = QLabel(self.pressureLabelContainer)
        self.middleLabel.setObjectName(u"middleLabel")
        self.middleLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.middleLabel, 1, 0, 1, 1)

        self.indexLabel = QLabel(self.pressureLabelContainer)
        self.indexLabel.setObjectName(u"indexLabel")
        self.indexLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.indexLabel, 1, 1, 1, 1)

        self.littleLabel = QLabel(self.pressureLabelContainer)
        self.littleLabel.setObjectName(u"littleLabel")
        self.littleLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.littleLabel, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.pressureLabelContainer, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.configCardContainer, 0, 0, 1, 1)


        self.retranslateUi(configCardWidgetForm)

        QMetaObject.connectSlotsByName(configCardWidgetForm)
    # setupUi

    def retranslateUi(self, configCardWidgetForm):
        configCardWidgetForm.setWindowTitle(QCoreApplication.translate("configCardWidgetForm", u"Form", None))
        self.durationIconLabel.setText("")
        self.durationLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"TextLabel", None))
        self.repeatIconLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"TextLabel", None))
        self.keyLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"TextLabel", None))
        self.ringLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"A:", None))
        self.middleLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"Meio:", None))
        self.indexLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"I:", None))
        self.littleLabel.setText(QCoreApplication.translate("configCardWidgetForm", u"Min:", None))
    # retranslateUi

