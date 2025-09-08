# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'title_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_titleWindowContainer(object):
    def setupUi(self, titleWindowContainer):
        if not titleWindowContainer.objectName():
            titleWindowContainer.setObjectName(u"titleWindowContainer")
        titleWindowContainer.resize(846, 116)
        self.gridLayout = QGridLayout(titleWindowContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.softwareTitleContainer = QWidget(titleWindowContainer)
        self.softwareTitleContainer.setObjectName(u"softwareTitleContainer")
        self.gridLayout_3 = QGridLayout(self.softwareTitleContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.softwateTitle = QLabel(self.softwareTitleContainer)
        self.softwateTitle.setObjectName(u"softwateTitle")
        font = QFont()
        font.setFamilies([u"Franklin Gothic"])
        font.setPointSize(22)
        font.setBold(False)
        self.softwateTitle.setFont(font)
        self.softwateTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.softwateTitle, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.softwareTitleContainer, 0, 0, 1, 1)

        self.terapistInfoContainer = QWidget(titleWindowContainer)
        self.terapistInfoContainer.setObjectName(u"terapistInfoContainer")
        self.formLayout = QFormLayout(self.terapistInfoContainer)
        self.formLayout.setObjectName(u"formLayout")
        self.terapistName = QLabel(self.terapistInfoContainer)
        self.terapistName.setObjectName(u"terapistName")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.terapistName)

        self.terapistRole = QLabel(self.terapistInfoContainer)
        self.terapistRole.setObjectName(u"terapistRole")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.terapistRole)

        self.terapistImageContainer = QWidget(self.terapistInfoContainer)
        self.terapistImageContainer.setObjectName(u"terapistImageContainer")
        self.horizontalLayout = QHBoxLayout(self.terapistImageContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.terapistImage = QLabel(self.terapistImageContainer)
        self.terapistImage.setObjectName(u"terapistImage")
        self.terapistImage.setMaximumSize(QSize(40, 40))
        self.terapistImage.setPixmap(QPixmap(u"_internal/resources/imgs/placeholder_profile.png"))
        self.terapistImage.setScaledContents(True)

        self.horizontalLayout.addWidget(self.terapistImage)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.terapistImageContainer)


        self.gridLayout.addWidget(self.terapistInfoContainer, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)

        self.retranslateUi(titleWindowContainer)

        QMetaObject.connectSlotsByName(titleWindowContainer)
    # setupUi

    def retranslateUi(self, titleWindowContainer):
        titleWindowContainer.setWindowTitle(QCoreApplication.translate("titleWindowContainer", u"Form", None))
        self.softwateTitle.setText(QCoreApplication.translate("titleWindowContainer", u"Joystick for hand motor rehabilitation", None))
        self.terapistName.setText(QCoreApplication.translate("titleWindowContainer", u"TherapistName", None))
        self.terapistRole.setText(QCoreApplication.translate("titleWindowContainer", u"TherapistFuntion", None))
        self.terapistImage.setText("")
    # retranslateUi

