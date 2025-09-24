# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration_result_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_calibrationResultWidget(object):
    def setupUi(self, calibrationResultWidget):
        if not calibrationResultWidget.objectName():
            calibrationResultWidget.setObjectName(u"calibrationResultWidget")
        calibrationResultWidget.resize(382, 400)
        self.gridLayout = QGridLayout(calibrationResultWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.resultContainer = QWidget(calibrationResultWidget)
        self.resultContainer.setObjectName(u"resultContainer")
        self.imageLabel = QLabel(self.resultContainer)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(30, 130, 221, 181))
        self.imageLabel.setPixmap(QPixmap(u"_internal/resources/imgs/hand.png"))
        self.imageLabel.setScaledContents(True)

        self.gridLayout.addWidget(self.resultContainer, 0, 0, 1, 1)


        self.retranslateUi(calibrationResultWidget)

        QMetaObject.connectSlotsByName(calibrationResultWidget)
    # setupUi

    def retranslateUi(self, calibrationResultWidget):
        calibrationResultWidget.setWindowTitle(QCoreApplication.translate("calibrationResultWidget", u"Form", None))
        self.imageLabel.setText("")
    # retranslateUi

