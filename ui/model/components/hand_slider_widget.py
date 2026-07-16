from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import QWidget, QBoxLayout, QLabel
from PySide6.QtGui import QPixmap

from ui.model.custom_widgets.custom_slider_model import CustomSliderModel

from shared_ui_modules.modules.log_class import logger

class HandSliderComponentModel(QWidget):
    def __init__(self,parent: QWidget = None):
        super().__init__(parent)

        self.hand_label = QLabel(self)
        self.hand_pixmap = QPixmap(u"_internal/resources/imgs/hand.png")

        self.hand_label.setScaledContents(True)
        self.hand_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hand_label.setPixmap(self.hand_pixmap)
        self.hand_label.setObjectName("handImageLabel")

        self.verticalSliderLittle = CustomSliderModel("KG")
        self.verticalSliderRing = CustomSliderModel("KG")
        self.verticalSliderMiddle = CustomSliderModel("KG")
        self.verticalSliderIndex = CustomSliderModel("KG")

        self.slider_array = [
            self.verticalSliderLittle,
            self.verticalSliderRing,
            self.verticalSliderMiddle,
            self.verticalSliderIndex
        ]
        
        for slider in self.slider_array:
            slider.setObjectName("PressureSlider")
            slider.setParent(self)
    
    def assing_image_position(self):
        hand_width = int(self.hand_pixmap.width()*0.45)
        hand_height = int(self.hand_pixmap.height()*0.45)
        
        x = (self.width() - hand_width) // 2
        y = (self.height() - hand_height)

        self.hand_label.setGeometry(QRect(x,y,hand_width,hand_height))

    #widgets start being drawn from the top
    def assing_slider_position(self):
        hand_rect = self.hand_label.geometry()
        
        slider_w = self.verticalSliderLittle.width()
        slider_h = self.verticalSliderLittle.height()
        
        #for the y coords
            # + top of the widget so its closer to the fingertips
            # - slider height so the bottom of the slider is close to the finger tip
            # + offset for each finger based on image height
        slider_geometry = [
            [hand_rect.left() - 20, hand_rect.top() - slider_h + 63],
            [hand_rect.left() + 20, hand_rect.top() - slider_h + 27],
            [hand_rect.right() - 134, hand_rect.top() - slider_h + 13],
            [hand_rect.right() - 90, hand_rect.top() - slider_h + 27]
        ]
        
        for i in range(0,4):
            self.slider_array[i].move(slider_geometry[i][0],slider_geometry[i][1])

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.assing_image_position()
        self.assing_slider_position()
       
        