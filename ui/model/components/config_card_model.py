from ui.views.config_card_widget_ui import Ui_configCardWidgetForm

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QEvent
from PySide6.QtGui import QPixmap

class ConfigCardModel(QWidget):
    #info should already have been converted into to string to you wish to present
    def __init__(self, id, infoDict):
        super().__init__()

        #setup ui
        self.ui = Ui_configCardWidgetForm()
        self.ui.setupUi(self)

        #get ui elements
        self.keyLabel = self.ui.keyLabel
        self.ringLabel = self.ui.ringLabel
        self.indexLabel = self.ui.indexLabel
        self.repeatIconLabel = self.ui.repeatIconLabel
        self.littleLabel = self.ui.littleLabel
        self.durationLabel = self.ui.durationLabel
        self.middleLabel = self.ui.middleLabel

        #variable setup
        self.info_dict = infoDict
        self.id = id
        self.repeat_pixmap = QPixmap()
        self.repeat_pixmap.load("_internal/resources/icons/loop.png")
        self.no_repeat_pixmap = QPixmap()
        self.no_repeat_pixmap.load("_internal/resources/icons/noloop.png")
        
        self.assign_text()

    def assign_text(self):
        key = self.arrow_text_conversion(self.info_dict["key"])
        self.keyLabel.setText(key.upper())

        if self.info_dict["repeat"] == "True":
            self.assing_repeat_image(self.repeat_pixmap)
        else:
            self.assing_repeat_image(self.no_repeat_pixmap)

        self.durationLabel.setText(str(self.info_dict["duration"]))

        self.littleLabel.setText(self.littleLabel.text() + str(float(self.info_dict["little"])/10))
        self.ringLabel.setText(self.ringLabel.text() + str(float(self.info_dict["ring"])/10))
        self.middleLabel.setText(self.middleLabel.text() + str(float(self.info_dict["middle"])/10))
        self.indexLabel.setText(self.indexLabel.text() + str(float(self.info_dict["index"])/10))

    def arrow_text_conversion(self,key):#chages literal word for directional arrows to icons
        key_text = key
        if key == "UP":
            key_text = str("↑")
        elif key == "DOWN":
            key_text = str("↓")
        elif key == "LEFT":
            key_text = str("←")
        elif key == "RIGHT":
            key_text = str("→")
        return key_text

    def assing_repeat_image(self, image):
        self.repeatIconLabel.setMaximumHeight(16)
        self.repeatIconLabel.setMaximumWidth(16)
        self.repeatIconLabel.setMinimumHeight(16)
        self.repeatIconLabel.setMinimumWidth(16)
        self.repeatIconLabel.setPixmap(image)
        self.repeatIconLabel.setScaledContents(True)
    

    def changeEvent(self, event):
        if event.type() == QEvent.Type.LanguageChange:
            self.ui.retranslateUi(self)
            self.assign_text()
        return super().changeEvent(event)
        