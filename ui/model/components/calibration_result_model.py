from ui.views.calibration_result_widget_ui import Ui_calibrationResultWidget
from PySide6.QtWidgets import QWidget
from ui.model.custom_widgets.custom_slider_model import CustomSliderModel
from PySide6.QtCore import QRect
from modules.log_class import logger

class CalibrationResultModel(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_calibrationResultWidget()
        self.ui.setupUi(self)

        self.handImage = self.ui.handImageLabel
        
        #hand sliders
        self.verticalSliderLittle = CustomSliderModel()
        self.verticalSliderRing = CustomSliderModel()
        self.verticalSliderMiddle = CustomSliderModel()
        self.verticalSliderIndex = CustomSliderModel()
        self.verticalSliderThumb = CustomSliderModel()
        
        self.slider_array = [
            self.verticalSliderLittle,
            self.verticalSliderRing,
            self.verticalSliderMiddle,
            self.verticalSliderIndex,
            self.verticalSliderThumb
        ]
        
        self.verticalSliderLittle.slider.setProperty("index",0)
        self.verticalSliderRing.slider.setProperty("index",1)
        self.verticalSliderMiddle.slider.setProperty("index",2)
        self.verticalSliderIndex.slider.setProperty("index",3)
        self.verticalSliderThumb.slider.setProperty("index",4)
        
        #add slider on layout
        self.slider_pos_array = [
            QRect(40, 6, 45, 80),
            QRect(70, -20, 45, 80),
            QRect(105, -21, 45, 80),
            QRect(145, -20, 45, 80),
            QRect(185, 40, 45, 80),
        ]

        for i,v in enumerate(self.slider_array):
            v.setParent(self.ui.resultContainer)
            v.setGeometry(self.slider_pos_array[i])

        for slider in self.slider_array:
            slider.slider.setEnabled(False)

    def set_pressure_values(self, value_array=None):
        try:
            if value_array:
                logger.debug(f"Valores de pressão recebidos, mínimo até polegar: ")
                for i,slider in enumerate(self.slider_array):
                    slider.slider.setValue(value_array[i])
                    slider.currentLabel.setText(str(value_array[i]/10))
                    slider.maxLabel.setText(str(slider.slider.maximum()/10))
                    logger.debug(f"{value_array[i]/10} KG")
            else:
                logger.error(f"Valores de pressão não foram recebidos na tela de resultados - value_array: {value_array}")
        except Exception as e:
            logger.error(f"Erro ao tentar apresentar o resultado da calibração: {e}")
