from ui.model.components.calibration_result_model import CalibrationResultModel

from shared_ui_modules.modules.log_class import logger
from shared_ui_modules.ui.model.stacked_widget_screens.calibration_shared_model import SharedCalibrationModel

from PySide6.QtCore import QCoreApplication, QEvent

class CalibrationWidgetModel(SharedCalibrationModel):

    def __init__(self,logModel,btSerialhandle):
        super().__init__( logModel, btSerialhandle)
        
        #variables
        self.message_counter = 0

        self.s_list = [
            "Aperte os botões com toda força por 5 segundos",
            "Use seu dedão e indicador com toda força por 5 segundos"
        ]

        self.imgLabel.setStyleSheet("""
            QWidget#imgLabel{
                border: 1px solid black;
                border-radius: 50%;
            }""")
        
        self.setup_model()

    def get_step_1_presusre(self):
        return [[0],[0],[0],[0]]

    def get_image_data(self):
        return [["_internal/resources/imgs/calibration_instruction_1.png",250,345,54],["_internal/resources/imgs/calibration_instruction_2.png",300,250,50]]

    def get_serial_messages(self):
        return ["*S1","*S2","*S3","*S4"]
    
    def get_str_array(self):
        return [
                QCoreApplication.translate("InstructionText", text)
                for text in self.s_list
                ]

    def get_result_model(self):
        return CalibrationResultModel()
        
    def cancel_current_step(self):
        try:
            self.timer.stop()
            self.timeout_counter = 0
            self.message_counter = 0
            if self.calibration_step == 0:
                self.step_1_pressure = self.get_step_1_presusre()
            else:
                self.step_2_pressure = [0]
            self.step_running_watcher = False
            self.btSerialhandle.mesReceivedSignal.disconnect(self.recieve_serial_message)
            self.btSerialhandle.port_error.disconnect(self.port_error_handle)
            self.error_flag = False
        except Exception as e:
            logger.error(f"SharedCalibrationModel cancel_current_step error: {e}")
            raise
    
    def handle_pressure_message_1(self, pressure):
        try:
            if self.message_counter > 3:
                self.message_counter = 0
            self.step_1_pressure[self.message_counter].append(int(pressure[:3]))
            self.message_counter += 1
        except Exception as e:
            logger.error(f"CalibrationWidgetModel handle_pressure_message_1 error: {e}")
            
    def get_max_pressure_values(self):
        try:
            max_val_array = []
            if self.step_1_pressure:
                for array in self.step_1_pressure:
                    max_val_array.append(max(array))
                max_val_array.append(max(self.step_2_pressure))
                return max_val_array
        except Exception as e:
            logger.error(f"CalibrationWidgetModel get_max_pressure_values error: {e}")

    def reset_variables(self):
        try:
            self.step_1_pressure = self.get_step_1_presusre()
            self.step_2_pressure = [0]
            self.message_counter = 0
            self.timeout_counter = 0
            self.calibration_step = 0
        except Exception as e:
            logger.error(f"CalibrationWidgetModel reset_variables error: {e}")