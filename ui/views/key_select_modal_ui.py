# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'key_select_modal.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_keySelectModalDialog(object):
    def setupUi(self, keySelectModalDialog):
        if not keySelectModalDialog.objectName():
            keySelectModalDialog.setObjectName(u"keySelectModalDialog")
        keySelectModalDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        keySelectModalDialog.resize(350, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(keySelectModalDialog.sizePolicy().hasHeightForWidth())
        keySelectModalDialog.setSizePolicy(sizePolicy)
        keySelectModalDialog.setMinimumSize(QSize(350, 200))
        keySelectModalDialog.setModal(True)
        self.gridLayout = QGridLayout(keySelectModalDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(keySelectModalDialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.keyConfigButtonContainer = QVBoxLayout()
        self.keyConfigButtonContainer.setObjectName(u"keyConfigButtonContainer")
        self.cleanKeyButton = QPushButton(self.widget)
        self.cleanKeyButton.setObjectName(u"cleanKeyButton")

        self.keyConfigButtonContainer.addWidget(self.cleanKeyButton)

        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.keyConfigButtonContainer.addWidget(self.buttonBox)


        self.gridLayout_2.addLayout(self.keyConfigButtonContainer, 0, 0, 1, 1)

        self.keyDisplayContainer = QWidget(self.widget)
        self.keyDisplayContainer.setObjectName(u"keyDisplayContainer")
        self.gridLayout_3 = QGridLayout(self.keyDisplayContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.keyDisplayer = QTextEdit(self.keyDisplayContainer)
        self.keyDisplayer.setObjectName(u"keyDisplayer")
        font = QFont()
        font.setPointSize(21)
        self.keyDisplayer.setFont(font)
        self.keyDisplayer.setReadOnly(True)

        self.gridLayout_3.addWidget(self.keyDisplayer, 0, 0, 1, 1)

        self.warningLabel = QLabel(self.keyDisplayContainer)
        self.warningLabel.setObjectName(u"warningLabel")

        self.gridLayout_3.addWidget(self.warningLabel, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.keyDisplayContainer, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(keySelectModalDialog)

        QMetaObject.connectSlotsByName(keySelectModalDialog)
    # setupUi

    def retranslateUi(self, keySelectModalDialog):
        keySelectModalDialog.setWindowTitle(QCoreApplication.translate("keySelectModalDialog", u"Dialog", None))
        self.cleanKeyButton.setText(QCoreApplication.translate("keySelectModalDialog", u"Limpar tecla", None))
        self.warningLabel.setText(QCoreApplication.translate("keySelectModalDialog", u"Selecione uma tecla", None))
    # retranslateUi

