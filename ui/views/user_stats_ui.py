# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_stats.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_useStatisticsForm(object):
    def setupUi(self, useStatisticsForm):
        if not useStatisticsForm.objectName():
            useStatisticsForm.setObjectName(u"useStatisticsForm")
        useStatisticsForm.resize(776, 575)
        self.gridLayout = QGridLayout(useStatisticsForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.useStatisticsWidgetContianer = QWidget(useStatisticsForm)
        self.useStatisticsWidgetContianer.setObjectName(u"useStatisticsWidgetContianer")
        self.gridLayout_2 = QGridLayout(self.useStatisticsWidgetContianer)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.statsTabWidget = QTabWidget(self.useStatisticsWidgetContianer)
        self.statsTabWidget.setObjectName(u"statsTabWidget")
        self.statsTabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.sessionTab = QWidget()
        self.sessionTab.setObjectName(u"sessionTab")
        self.gridLayout_3 = QGridLayout(self.sessionTab)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sessionChartContainer = QWidget(self.sessionTab)
        self.sessionChartContainer.setObjectName(u"sessionChartContainer")
        self.gridLayout_6 = QGridLayout(self.sessionChartContainer)
        self.gridLayout_6.setObjectName(u"gridLayout_6")

        self.gridLayout_3.addWidget(self.sessionChartContainer, 0, 0, 1, 1)

        self.buttonsContainer = QWidget(self.sessionTab)
        self.buttonsContainer.setObjectName(u"buttonsContainer")
        self.horizontalLayout = QHBoxLayout(self.buttonsContainer)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.listeningButtonContainer = QWidget(self.buttonsContainer)
        self.listeningButtonContainer.setObjectName(u"listeningButtonContainer")
        self.verticalLayout = QVBoxLayout(self.listeningButtonContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.startListening = QPushButton(self.listeningButtonContainer)
        self.startListening.setObjectName(u"startListening")

        self.verticalLayout.addWidget(self.startListening)

        self.stopListening = QPushButton(self.listeningButtonContainer)
        self.stopListening.setObjectName(u"stopListening")

        self.verticalLayout.addWidget(self.stopListening)


        self.horizontalLayout.addWidget(self.listeningButtonContainer)

        self.timelapseContainer = QWidget(self.buttonsContainer)
        self.timelapseContainer.setObjectName(u"timelapseContainer")
        self.gridLayout_4 = QGridLayout(self.timelapseContainer)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.timelapseLabel = QLabel(self.timelapseContainer)
        self.timelapseLabel.setObjectName(u"timelapseLabel")

        self.gridLayout_4.addWidget(self.timelapseLabel, 1, 0, 1, 1)

        self.timelapseDescriptionLabel = QLabel(self.timelapseContainer)
        self.timelapseDescriptionLabel.setObjectName(u"timelapseDescriptionLabel")

        self.gridLayout_4.addWidget(self.timelapseDescriptionLabel, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.timelapseContainer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.buttonsContainer)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)

        self.sessionSelectorContainer = QWidget(self.buttonsContainer)
        self.sessionSelectorContainer.setObjectName(u"sessionSelectorContainer")
        self.gridLayout_5 = QGridLayout(self.sessionSelectorContainer)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sessionComboBox = QComboBox(self.sessionSelectorContainer)
        self.sessionComboBox.setObjectName(u"sessionComboBox")
        self.sessionComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_5.addWidget(self.sessionComboBox, 3, 0, 1, 1)

        self.newSessionButton = QPushButton(self.sessionSelectorContainer)
        self.newSessionButton.setObjectName(u"newSessionButton")

        self.gridLayout_5.addWidget(self.newSessionButton, 1, 0, 1, 1)

        self.deleteSessionButton = QToolButton(self.sessionSelectorContainer)
        self.deleteSessionButton.setObjectName(u"deleteSessionButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.deleteSessionButton.setIcon(icon)

        self.gridLayout_5.addWidget(self.deleteSessionButton, 3, 1, 1, 1)


        self.horizontalLayout.addWidget(self.sessionSelectorContainer)

        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(4, 2)

        self.gridLayout_3.addWidget(self.buttonsContainer, 1, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.statsTabWidget.addTab(self.sessionTab, "")
        self.summaryTab = QWidget()
        self.summaryTab.setObjectName(u"summaryTab")
        self.gridLayout_7 = QGridLayout(self.summaryTab)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.summaryStatsContainer = QWidget(self.summaryTab)
        self.summaryStatsContainer.setObjectName(u"summaryStatsContainer")
        self.gridLayout_8 = QGridLayout(self.summaryStatsContainer)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.summaryChartContainer = QWidget(self.summaryStatsContainer)
        self.summaryChartContainer.setObjectName(u"summaryChartContainer")
        self.gridLayout_10 = QGridLayout(self.summaryChartContainer)
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.gridLayout_8.addWidget(self.summaryChartContainer, 0, 0, 1, 1)

        self.sessionDurationContainer = QWidget(self.summaryStatsContainer)
        self.sessionDurationContainer.setObjectName(u"sessionDurationContainer")
        self.horizontalLayout_2 = QHBoxLayout(self.sessionDurationContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sessionTimeLabel = QLabel(self.sessionDurationContainer)
        self.sessionTimeLabel.setObjectName(u"sessionTimeLabel")

        self.horizontalLayout_2.addWidget(self.sessionTimeLabel)

        self.avgSessionTime = QLabel(self.sessionDurationContainer)
        self.avgSessionTime.setObjectName(u"avgSessionTime")

        self.horizontalLayout_2.addWidget(self.avgSessionTime)

        self.countSessionLabel = QLabel(self.sessionDurationContainer)
        self.countSessionLabel.setObjectName(u"countSessionLabel")

        self.horizontalLayout_2.addWidget(self.countSessionLabel)

        self.countSession = QLabel(self.sessionDurationContainer)
        self.countSession.setObjectName(u"countSession")

        self.horizontalLayout_2.addWidget(self.countSession)


        self.gridLayout_8.addWidget(self.sessionDurationContainer, 1, 0, 1, 1)

        self.gridLayout_8.setRowStretch(0, 1)

        self.gridLayout_7.addWidget(self.summaryStatsContainer, 0, 0, 1, 1)

        self.statsTabWidget.addTab(self.summaryTab, "")

        self.gridLayout_2.addWidget(self.statsTabWidget, 0, 0, 1, 2)

        self.gridLayout_2.setRowStretch(0, 1)

        self.gridLayout.addWidget(self.useStatisticsWidgetContianer, 0, 0, 1, 1)

        self.handSelectorContainer = QWidget(useStatisticsForm)
        self.handSelectorContainer.setObjectName(u"handSelectorContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.handSelectorContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rightHandButton = QRadioButton(self.handSelectorContainer)
        self.handButtonGroup = QButtonGroup(useStatisticsForm)
        self.handButtonGroup.setObjectName(u"handButtonGroup")
        self.handButtonGroup.addButton(self.rightHandButton)
        self.rightHandButton.setObjectName(u"rightHandButton")

        self.horizontalLayout_3.addWidget(self.rightHandButton)

        self.leftHandButton = QRadioButton(self.handSelectorContainer)
        self.handButtonGroup.addButton(self.leftHandButton)
        self.leftHandButton.setObjectName(u"leftHandButton")

        self.horizontalLayout_3.addWidget(self.leftHandButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.handSelectorContainer, 1, 0, 1, 1)


        self.retranslateUi(useStatisticsForm)

        self.statsTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(useStatisticsForm)
    # setupUi

    def retranslateUi(self, useStatisticsForm):
        useStatisticsForm.setWindowTitle(QCoreApplication.translate("useStatisticsForm", u"Form", None))
        self.startListening.setText(QCoreApplication.translate("useStatisticsForm", u"Come\u00e7ar coleta", None))
        self.stopListening.setText(QCoreApplication.translate("useStatisticsForm", u"Interromper coleta", None))
        self.timelapseLabel.setText(QCoreApplication.translate("useStatisticsForm", u"00:00:00", None))
        self.timelapseDescriptionLabel.setText(QCoreApplication.translate("useStatisticsForm", u"Dura\u00e7\u00e3o", None))
        self.label.setText(QCoreApplication.translate("useStatisticsForm", u"Use o bot\u00e3o direito do mouse nos gr\u00e1ficos para exportar dados", None))
        self.newSessionButton.setText(QCoreApplication.translate("useStatisticsForm", u"Nova sess\u00e3o", None))
        self.deleteSessionButton.setText(QCoreApplication.translate("useStatisticsForm", u"...", None))
        self.statsTabWidget.setTabText(self.statsTabWidget.indexOf(self.sessionTab), QCoreApplication.translate("useStatisticsForm", u"Sess\u00f5es", None))
        self.sessionTimeLabel.setText(QCoreApplication.translate("useStatisticsForm", u"Tempo m\u00e9dio de ses\u00f5es", None))
        self.avgSessionTime.setText(QCoreApplication.translate("useStatisticsForm", u"TextLabel", None))
        self.countSessionLabel.setText(QCoreApplication.translate("useStatisticsForm", u"Total de se\u00e7\u00f5es", None))
        self.countSession.setText(QCoreApplication.translate("useStatisticsForm", u"TextLabel", None))
        self.statsTabWidget.setTabText(self.statsTabWidget.indexOf(self.summaryTab), QCoreApplication.translate("useStatisticsForm", u"Resumo", None))
        self.rightHandButton.setText(QCoreApplication.translate("useStatisticsForm", u"M\u00e3o direita", None))
        self.leftHandButton.setText(QCoreApplication.translate("useStatisticsForm", u"M\u00e3o esquerda", None))
    # retranslateUi

