# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_configForm(object):
    def setupUi(self, configForm):
        if not configForm.objectName():
            configForm.setObjectName(u"configForm")
        configForm.resize(697, 539)
        self.gridLayout = QGridLayout(configForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configContainer = QWidget(configForm)
        self.configContainer.setObjectName(u"configContainer")
        self.gridLayout_2 = QGridLayout(self.configContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.optionsContainer = QWidget(self.configContainer)
        self.optionsContainer.setObjectName(u"optionsContainer")
        self.verticalLayout = QVBoxLayout(self.optionsContainer)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.optionsButtonsContainer = QWidget(self.optionsContainer)
        self.optionsButtonsContainer.setObjectName(u"optionsButtonsContainer")
        self.verticalLayout_2 = QVBoxLayout(self.optionsButtonsContainer)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.repeatLabelContainer = QWidget(self.optionsButtonsContainer)
        self.repeatLabelContainer.setObjectName(u"repeatLabelContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.repeatLabelContainer)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.repeatButtonLabel = QLabel(self.repeatLabelContainer)
        self.repeatButtonLabel.setObjectName(u"repeatButtonLabel")
        font = QFont()
        font.setBold(True)
        self.repeatButtonLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.repeatButtonLabel)

        self.repeatHelperLabel = QLabel(self.repeatLabelContainer)
        self.repeatHelperLabel.setObjectName(u"repeatHelperLabel")
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(True)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.repeatHelperLabel.setFont(font1)
        self.repeatHelperLabel.setStyleSheet(u"")
        self.repeatHelperLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.repeatHelperLabel)


        self.verticalLayout_2.addWidget(self.repeatLabelContainer)

        self.repeatButtonContainer = QWidget(self.optionsButtonsContainer)
        self.repeatButtonContainer.setObjectName(u"repeatButtonContainer")
        self.horizontalLayout = QHBoxLayout(self.repeatButtonContainer)
        self.horizontalLayout.setSpacing(10)
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


        self.verticalLayout_2.addWidget(self.repeatButtonContainer)

        self.durationLabalContainer = QWidget(self.optionsButtonsContainer)
        self.durationLabalContainer.setObjectName(u"durationLabalContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.durationLabalContainer)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.durationLabel = QLabel(self.durationLabalContainer)
        self.durationLabel.setObjectName(u"durationLabel")
        self.durationLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.durationLabel)

        self.durationHelperLabel = QLabel(self.durationLabalContainer)
        self.durationHelperLabel.setObjectName(u"durationHelperLabel")
        self.durationHelperLabel.setFont(font1)
        self.durationHelperLabel.setStyleSheet(u"")
        self.durationHelperLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.durationHelperLabel)


        self.verticalLayout_2.addWidget(self.durationLabalContainer)

        self.durationSliderContainer = QWidget(self.optionsButtonsContainer)
        self.durationSliderContainer.setObjectName(u"durationSliderContainer")
        self.durationSliderContainer.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.durationSliderContainer)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.zeroLabel = QLabel(self.durationSliderContainer)
        self.zeroLabel.setObjectName(u"zeroLabel")

        self.horizontalLayout_2.addWidget(self.zeroLabel)

        self.durationSlider = QSlider(self.durationSliderContainer)
        self.durationSlider.setObjectName(u"durationSlider")
        self.durationSlider.setMinimum(0)
        self.durationSlider.setMaximum(9)
        self.durationSlider.setValue(0)
        self.durationSlider.setSliderPosition(0)
        self.durationSlider.setOrientation(Qt.Orientation.Horizontal)
        self.durationSlider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.durationSlider.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.durationSlider)

        self.nineLabel = QLabel(self.durationSliderContainer)
        self.nineLabel.setObjectName(u"nineLabel")

        self.horizontalLayout_2.addWidget(self.nineLabel)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.durationSliderContainer)

        self.pressureLabel = QLabel(self.optionsButtonsContainer)
        self.pressureLabel.setObjectName(u"pressureLabel")
        self.pressureLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.pressureLabel)

        self.pressureButton = QPushButton(self.optionsButtonsContainer)
        self.pressureButton.setObjectName(u"pressureButton")

        self.verticalLayout_2.addWidget(self.pressureButton)

        self.CButtonlable = QLabel(self.optionsButtonsContainer)
        self.CButtonlable.setObjectName(u"CButtonlable")
        self.CButtonlable.setFont(font)

        self.verticalLayout_2.addWidget(self.CButtonlable)

        self.CKeyButton = QPushButton(self.optionsButtonsContainer)
        self.CKeyButton.setObjectName(u"CKeyButton")

        self.verticalLayout_2.addWidget(self.CKeyButton)

        self.ZButtonLabel = QLabel(self.optionsButtonsContainer)
        self.ZButtonLabel.setObjectName(u"ZButtonLabel")
        self.ZButtonLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.ZButtonLabel)

        self.ZKeyButton = QPushButton(self.optionsButtonsContainer)
        self.ZKeyButton.setObjectName(u"ZKeyButton")

        self.verticalLayout_2.addWidget(self.ZKeyButton)

        self.confirmButton = QPushButton(self.optionsButtonsContainer)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_2.addWidget(self.confirmButton)


        self.verticalLayout.addWidget(self.optionsButtonsContainer)

        self.verticalLayout.setStretch(0, 3)

        self.gridLayout_2.addWidget(self.optionsContainer, 0, 1, 1, 1)

        self.pressureFingerContainer = QWidget(self.configContainer)
        self.pressureFingerContainer.setObjectName(u"pressureFingerContainer")
        self.verticalLayout_3 = QVBoxLayout(self.pressureFingerContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.slidersContainer = QWidget(self.pressureFingerContainer)
        self.slidersContainer.setObjectName(u"slidersContainer")
        self.handImageLabel = QLabel(self.slidersContainer)
        self.handImageLabel.setObjectName(u"handImageLabel")
        self.handImageLabel.setGeometry(QRect(110, 150, 201, 151))
        self.handImageLabel.setPixmap(QPixmap(u"_internal/resources/imgs/hand.png"))
        self.handImageLabel.setScaledContents(True)
        self.handImageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.handImageLabel.setWordWrap(False)
        self.massLabel = QLabel(self.slidersContainer)
        self.massLabel.setObjectName(u"massLabel")
        self.massLabel.setGeometry(QRect(270, 10, 81, 31))
        self.massLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.slidersContainer)

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
        self.radioButtonLittle.setFont(font)

        self.fingerButtonContainer.addWidget(self.radioButtonLittle)

        self.radioButtonRing = QRadioButton(self.fingerButtonContainer_2)
        self.fingerButtonGroup.addButton(self.radioButtonRing)
        self.radioButtonRing.setObjectName(u"radioButtonRing")
        self.radioButtonRing.setFont(font)

        self.fingerButtonContainer.addWidget(self.radioButtonRing)

        self.radioButtonMiddle = QRadioButton(self.fingerButtonContainer_2)
        self.fingerButtonGroup.addButton(self.radioButtonMiddle)
        self.radioButtonMiddle.setObjectName(u"radioButtonMiddle")
        self.radioButtonMiddle.setFont(font)

        self.fingerButtonContainer.addWidget(self.radioButtonMiddle)

        self.radioButtonIndex = QRadioButton(self.fingerButtonContainer_2)
        self.fingerButtonGroup.addButton(self.radioButtonIndex)
        self.radioButtonIndex.setObjectName(u"radioButtonIndex")
        self.radioButtonIndex.setFont(font)

        self.fingerButtonContainer.addWidget(self.radioButtonIndex)


        self.verticalLayout_3.addWidget(self.fingerButtonContainer_2)

        self.verticalLayout_3.setStretch(0, 1)

        self.gridLayout_2.addWidget(self.pressureFingerContainer, 0, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 3)

        self.gridLayout.addWidget(self.configContainer, 1, 0, 1, 1)


        self.retranslateUi(configForm)

        QMetaObject.connectSlotsByName(configForm)
    # setupUi

    def retranslateUi(self, configForm):
        configForm.setWindowTitle(QCoreApplication.translate("configForm", u"Form", None))
        self.repeatButtonLabel.setText(QCoreApplication.translate("configForm", u"Repetir", None))
#if QT_CONFIG(tooltip)
        self.repeatHelperLabel.setToolTip(QCoreApplication.translate("configForm", u"Quando ligado, a entrada configurada ser\u00e1 repetida m\u00faltiplas vezes enquanto o sensor estiver pressionado", u"ConfigScreenHelper"))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.repeatHelperLabel.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.repeatHelperLabel.setText(QCoreApplication.translate("configForm", u"?", None))
        self.repeatOnButton.setText(QCoreApplication.translate("configForm", u"Ligado", None))
        self.repeatOffButton.setText(QCoreApplication.translate("configForm", u"Desligado", None))
        self.durationLabel.setText(QCoreApplication.translate("configForm", u"Dura\u00e7\u00e3o (s)", None))
#if QT_CONFIG(tooltip)
        self.durationHelperLabel.setToolTip(QCoreApplication.translate("configForm", u"Quantos segundos de press\u00e3o cont\u00ednua s\u00e3o necess\u00e1rios para que o controle registre uma entrada", u"ConfigScreenHelper"))
#endif // QT_CONFIG(tooltip)
        self.durationHelperLabel.setText(QCoreApplication.translate("configForm", u"?", None))
        self.zeroLabel.setText(QCoreApplication.translate("configForm", u"0", None))
        self.nineLabel.setText(QCoreApplication.translate("configForm", u"9", None))
        self.pressureLabel.setText(QCoreApplication.translate("configForm", u"Tecla", None))
#if QT_CONFIG(tooltip)
        self.pressureButton.setToolTip(QCoreApplication.translate("configForm", u"Seleciona a tecla que deseja associar \u00e0 combina\u00e7\u00e3o de dedos, caso j\u00e1 selecionada, apresenta a tecla escolhida", u"ConfigScreenHelper"))
#endif // QT_CONFIG(tooltip)
        self.pressureButton.setText(QCoreApplication.translate("configForm", u"Clique para selecionar", None))
        self.CButtonlable.setText(QCoreApplication.translate("configForm", u"Bot\u00e3o C", None))
#if QT_CONFIG(tooltip)
        self.CKeyButton.setToolTip(QCoreApplication.translate("configForm", u"Seleciona a tecla que deseja associar \u00e0 combina\u00e7\u00e3o de dedos, caso j\u00e1 selecionada, apresenta a tecla escolhida", u"ConfigScreenHelper"))
#endif // QT_CONFIG(tooltip)
        self.CKeyButton.setText(QCoreApplication.translate("configForm", u"Clique para selecionar", None))
        self.ZButtonLabel.setText(QCoreApplication.translate("configForm", u"Bot\u00e3o Z", None))
#if QT_CONFIG(tooltip)
        self.ZKeyButton.setToolTip(QCoreApplication.translate("configForm", u"Seleciona a tecla que deseja associar \u00e0 combina\u00e7\u00e3o de dedos, caso j\u00e1 selecionada, apresenta a tecla escolhida", u"ConfigScreenHelper"))
#endif // QT_CONFIG(tooltip)
        self.ZKeyButton.setText(QCoreApplication.translate("configForm", u"Clique para selecionar", None))
#if QT_CONFIG(tooltip)
        self.confirmButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.confirmButton.setText(QCoreApplication.translate("configForm", u"Confirmar", None))
        self.handImageLabel.setText("")
        self.massLabel.setText(QCoreApplication.translate("configForm", u"Massa em KG", None))
        self.radioButtonLittle.setText(QCoreApplication.translate("configForm", u"M\u00ednimo", None))
        self.radioButtonRing.setText(QCoreApplication.translate("configForm", u"Anelar", None))
        self.radioButtonMiddle.setText(QCoreApplication.translate("configForm", u"M\u00e9dio", None))
        self.radioButtonIndex.setText(QCoreApplication.translate("configForm", u"Indicador/Polegar", None))
    # retranslateUi

