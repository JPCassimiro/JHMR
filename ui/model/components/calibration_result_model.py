from shared_ui_modules.modules.log_class import logger
from ui.model.components.hand_slider_widget import HandSliderComponentModel

class CalibrationResultModel(HandSliderComponentModel):
    def __init__(self,parent = None):
        super().__init__(parent=parent)

        for i, slider in enumerate(self.slider_array):
            slider.slider.setProperty("index",i)
        
        for slider in self.slider_array:
            slider.slider.setEnabled(False)

    def set_pressure_values(self, value_array=None):
        logger.debug(f"CalibrationResultModel geometry: {self.geometry()}")
        try:
            if value_array:
                logger.debug(f"Valores de pressão recebidos, mínimo até polegar: ")
                for i,slider in enumerate(self.slider_array):
                    slider.slider.setValue(value_array[i])
                    # slider.maxLabel.setText(str(slider.slider.maximum()/10) + "KG")
                    logger.debug(f"{value_array[i]/10} KG")
            else:
                logger.error(f"Valores de pressão não foram recebidos na tela de resultados - value_array: {value_array}")
        except Exception as e:
            logger.error(f"Erro ao tentar apresentar o resultado da calibração: {e}")
