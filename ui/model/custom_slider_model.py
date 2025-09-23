from ui.views.custom_slider_widget_ui import Ui_customSliderForm
from modules.log_class import logger
from PySide6.QtWidgets import QWidget, QSlider, QRadioButton, QLabel


class CustomSliderModel(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_customSliderForm()
        self.ui.setupUi(self)
        
        self.slider = self.ui.verticalSlider
        self.maxLabel = self.ui.maxLabel
        self.currentLabel = self.ui.currentLabel
        
        self.setFixedWidth(42)#min
        
        self.maxLabel.setText(str(self.slider.maximum()/10))
        self.currentLabel.setText(str(self.slider.value()/10))