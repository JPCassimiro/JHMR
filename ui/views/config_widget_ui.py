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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_configForm(object):
    def setupUi(self, configForm):
        if not configForm.objectName():
            configForm.setObjectName(u"configForm")
        configForm.resize(849, 539)
        self.gridLayout = QGridLayout(configForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configContainer = QWidget(configForm)
        self.configContainer.setObjectName(u"configContainer")
        self.gridLayout_2 = QGridLayout(self.configContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pressureFingerContainer = QWidget(self.configContainer)
        self.pressureFingerContainer.setObjectName(u"pressureFingerContainer")
        self.verticalLayout_3 = QVBoxLayout(self.pressureFingerContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.slidersContainer = QWidget(self.pressureFingerContainer)
        self.slidersContainer.setObjectName(u"slidersContainer")
        self.horizontalLayout_2 = QHBoxLayout(self.slidersContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalSliderLittle = QSlider(self.slidersContainer)
        self.verticalSliderLittle.setObjectName(u"verticalSliderLittle")
        self.verticalSliderLittle.setMaximum(200)
        self.verticalSliderLittle.setOrientation(Qt.Orientation.Vertical)
        self.verticalSliderLittle.setTickPosition(QSlider.TickPosition.NoTicks)
        self.verticalSliderLittle.setTickInterval(0)

        self.horizontalLayout_2.addWidget(self.verticalSliderLittle)

        self.verticalSliderRing = QSlider(self.slidersContainer)
        self.verticalSliderRing.setObjectName(u"verticalSliderRing")
        self.verticalSliderRing.setMaximum(200)
        self.verticalSliderRing.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_2.addWidget(self.verticalSliderRing)

        self.verticalSliderMiddle = QSlider(self.slidersContainer)
        self.verticalSliderMiddle.setObjectName(u"verticalSliderMiddle")
        self.verticalSliderMiddle.setMaximum(200)
        self.verticalSliderMiddle.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_2.addWidget(self.verticalSliderMiddle)

        self.verticalSliderIndex = QSlider(self.slidersContainer)
        self.verticalSliderIndex.setObjectName(u"verticalSliderIndex")
        self.verticalSliderIndex.setMaximum(200)
        self.verticalSliderIndex.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_2.addWidget(self.verticalSliderIndex)

        self.verticalSliderThumb = QSlider(self.slidersContainer)
        self.verticalSliderThumb.setObjectName(u"verticalSliderThumb")
        self.verticalSliderThumb.setMaximum(200)
        self.verticalSliderThumb.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_2.addWidget(self.verticalSliderThumb)


        self.verticalLayout_3.addWidget(self.slidersContainer)

        self.handImageContainer = QWidget(self.pressureFingerContainer)
        self.handImageContainer.setObjectName(u"handImageContainer")
        self.gridLayout_4 = QGridLayout(self.handImageContainer)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.handImageLabel = QLabel(self.handImageContainer)
        self.handImageLabel.setObjectName(u"handImageLabel")

        self.gridLayout_4.addWidget(self.handImageLabel, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.handImageContainer)

        self.fingerButtonContainer_2 = QWidget(self.pressureFingerContainer)
        self.fingerButtonContainer_2.setObjectName(u"fingerButtonContainer_2")
        self.fingerButtonContainer = QHBoxLayout(self.fingerButtonContainer_2)
        self.fingerButtonContainer.setObjectName(u"fingerButtonContainer")
        self.radioButtonLittle = QRadioButton(self.fingerButtonContainer_2)
        self.fingerButtonGroup = QButtonGroup(configForm)
        self.fingerButtonGroup.setObjectName(u"fingerButtonGroup")
        self.fingerButtonGroup.setExclusive(False)
        self.fingerButtonGroup.addButton(self.radioButtonLittle)
        self.radioButtonLittle.setObjectName(u"radioButtonLittle")

        self.fingerButtonContainer.addWidget(self.radioButtonLittle)

        self.radioButtonRing = QRadioButton(self.fingerButtonContainer_2)
        self.fingerButtonGroup.addButton(self.radioButtonRing)
        self.radioButtonRing.setObjectName(u"radioButtonRing")

        self.fingerButtonContainer.addWidget(self.radioButtonRing)

        self.radioButtonMiddle = QRadioButton(self.fingerButtonContainer_2)
        self.fingerButtonGroup.addButton(self.radioButtonMiddle)
        self.radioButtonMiddle.setObjectName(u"radioButtonMiddle")

        self.fingerButtonContainer.addWidget(self.radioButtonMiddle)

        self.radioButtonIndex = QRadioButton(self.fingerButtonContainer_2)
        self.fingerButtonGroup.addButton(self.radioButtonIndex)
        self.radioButtonIndex.setObjectName(u"radioButtonIndex")

        self.fingerButtonContainer.addWidget(self.radioButtonIndex)

        self.radioButtonThumb = QRadioButton(self.fingerButtonContainer_2)
        self.fingerButtonGroup.addButton(self.radioButtonThumb)
        self.radioButtonThumb.setObjectName(u"radioButtonThumb")

        self.fingerButtonContainer.addWidget(self.radioButtonThumb)


        self.verticalLayout_3.addWidget(self.fingerButtonContainer_2)


        self.gridLayout_2.addWidget(self.pressureFingerContainer, 0, 0, 1, 1)

        self.optionsContainer = QWidget(self.configContainer)
        self.optionsContainer.setObjectName(u"optionsContainer")
        self.verticalLayout = QVBoxLayout(self.optionsContainer)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.repeatButtonLabel = QLabel(self.optionsContainer)
        self.repeatButtonLabel.setObjectName(u"repeatButtonLabel")

        self.verticalLayout.addWidget(self.repeatButtonLabel)

        self.repeatButtonContainer = QWidget(self.optionsContainer)
        self.repeatButtonContainer.setObjectName(u"repeatButtonContainer")
        self.horizontalLayout = QHBoxLayout(self.repeatButtonContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.repeatOnButton = QRadioButton(self.repeatButtonContainer)
        self.repeatButtonGroup = QButtonGroup(configForm)
        self.repeatButtonGroup.setObjectName(u"repeatButtonGroup")
        self.repeatButtonGroup.addButton(self.repeatOnButton)
        self.repeatOnButton.setObjectName(u"repeatOnButton")
        self.repeatOnButton.setChecked(False)

        self.horizontalLayout.addWidget(self.repeatOnButton)

        self.repeatOffButton = QRadioButton(self.repeatButtonContainer)
        self.repeatButtonGroup.addButton(self.repeatOffButton)
        self.repeatOffButton.setObjectName(u"repeatOffButton")
        self.repeatOffButton.setChecked(True)

        self.horizontalLayout.addWidget(self.repeatOffButton)


        self.verticalLayout.addWidget(self.repeatButtonContainer)

        self.optionsButtonsContainer = QWidget(self.optionsContainer)
        self.optionsButtonsContainer.setObjectName(u"optionsButtonsContainer")
        self.verticalLayout_2 = QVBoxLayout(self.optionsButtonsContainer)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.durationLabel = QLabel(self.optionsButtonsContainer)
        self.durationLabel.setObjectName(u"durationLabel")

        self.verticalLayout_2.addWidget(self.durationLabel)

        self.durationSlider = QSlider(self.optionsButtonsContainer)
        self.durationSlider.setObjectName(u"durationSlider")
        self.durationSlider.setMinimum(1)
        self.durationSlider.setMaximum(9)
        self.durationSlider.setValue(1)
        self.durationSlider.setSliderPosition(1)
        self.durationSlider.setOrientation(Qt.Orientation.Horizontal)
        self.durationSlider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.durationSlider.setTickInterval(1)

        self.verticalLayout_2.addWidget(self.durationSlider)

        self.pressureLabel = QLabel(self.optionsButtonsContainer)
        self.pressureLabel.setObjectName(u"pressureLabel")

        self.verticalLayout_2.addWidget(self.pressureLabel)

        self.pressureButton = QPushButton(self.optionsButtonsContainer)
        self.pressureButton.setObjectName(u"pressureButton")

        self.verticalLayout_2.addWidget(self.pressureButton)

        self.CButtonlable = QLabel(self.optionsButtonsContainer)
        self.CButtonlable.setObjectName(u"CButtonlable")

        self.verticalLayout_2.addWidget(self.CButtonlable)

        self.CKeyButton = QPushButton(self.optionsButtonsContainer)
        self.CKeyButton.setObjectName(u"CKeyButton")

        self.verticalLayout_2.addWidget(self.CKeyButton)

        self.ZButtonLabel = QLabel(self.optionsButtonsContainer)
        self.ZButtonLabel.setObjectName(u"ZButtonLabel")

        self.verticalLayout_2.addWidget(self.ZButtonLabel)

        self.ZKeyButton = QPushButton(self.optionsButtonsContainer)
        self.ZKeyButton.setObjectName(u"ZKeyButton")

        self.verticalLayout_2.addWidget(self.ZKeyButton)

        self.confirmButton = QPushButton(self.optionsButtonsContainer)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_2.addWidget(self.confirmButton)


        self.verticalLayout.addWidget(self.optionsButtonsContainer)

        self.verticalLayout.setStretch(2, 3)

        self.gridLayout_2.addWidget(self.optionsContainer, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.gridLayout.addWidget(self.configContainer, 1, 0, 1, 1)


        self.retranslateUi(configForm)

        QMetaObject.connectSlotsByName(configForm)
    # setupUi

    def retranslateUi(self, configForm):
        configForm.setWindowTitle(QCoreApplication.translate("configForm", u"Form", None))
        self.handImageLabel.setText(QCoreApplication.translate("configForm", u"ImagemM\u00e3o", None))
        self.radioButtonLittle.setText(QCoreApplication.translate("configForm", u"Mindinho", None))
        self.radioButtonRing.setText(QCoreApplication.translate("configForm", u"Anelar", None))
        self.radioButtonMiddle.setText(QCoreApplication.translate("configForm", u"Meio", None))
        self.radioButtonIndex.setText(QCoreApplication.translate("configForm", u"Indicador", None))
        self.radioButtonThumb.setText(QCoreApplication.translate("configForm", u"Ded\u00e3o", None))
        self.repeatButtonLabel.setText(QCoreApplication.translate("configForm", u"Repetir", None))
        self.repeatOnButton.setText(QCoreApplication.translate("configForm", u"Ligado", None))
        self.repeatOffButton.setText(QCoreApplication.translate("configForm", u"Desligado", None))
        self.durationLabel.setText(QCoreApplication.translate("configForm", u"Dura\u00e7\u00e3o", None))
        self.pressureLabel.setText(QCoreApplication.translate("configForm", u"Tecla", None))
        self.pressureButton.setText(QCoreApplication.translate("configForm", u"Clique para selecionar", None))
        self.CButtonlable.setText(QCoreApplication.translate("configForm", u"Bot\u00e3o C", None))
        self.CKeyButton.setText(QCoreApplication.translate("configForm", u"Clique para selecionar", None))
        self.ZButtonLabel.setText(QCoreApplication.translate("configForm", u"Bot\u00e3o Z", None))
        self.ZKeyButton.setText(QCoreApplication.translate("configForm", u"Clique para selecionar", None))
        self.confirmButton.setText(QCoreApplication.translate("configForm", u"Confirmar", None))
    # retranslateUi

