from ui.views.calibration_widget_ui import Ui_calibrationForm
from ui.model.calibration_result_model import CalibrationResultModel
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from modules.log_class import logger
from PySide6.QtCore import QTimer

class CalibrationWidgetModel(QWidget):
    def __init__(self,serialHandleClass):
        super().__init__()
        
        #setup ui
        self.ui = Ui_calibrationForm()
        self.ui.setupUi(self)
        
        #modules setup
        self.serialHandleClass = serialHandleClass
        self.timer = QTimer()
        self.uiTimer = QTimer()
        
        #custom ui element setup
        self.resultModel = CalibrationResultModel()

        #variables
        self.recived_presure_array = [[],[],[],[]]
        self.thumb_pressure = []
        self.message_couter = 0
        self.timeout_counter = 0
        self.serial_messages = ["*S1","*S2","*S3","*S4"]
        self.calibration_step = 0

        #get ui elements
        self.instructionImage = self.ui.imageLabel
        self.startButton = self.ui.startButton
        self.instructionText = self.ui.instructionLabel
        self.cancelButton = self.ui.cancelButton
        self.restartButton = self.ui.restartButton

        self.cancelButton.setEnabled(False)

        self.instructionText.setText("Aperte todos os botões com toda sua força por 5 segundos")
        self.set_instruction_image("_internal/resources/imgs/calibration_instruction_1.png")

        #connections
        self.startButton.clicked.connect(self.start_button_handler)
        self.timer.timeout.connect(self.timeout_handler)
        self.restartButton.clicked.connect(self.restart_calibration)
        
    def set_instruction_image(self,img_path):
        try:
            img = QPixmap()
            if img.load(img_path):
                self.instructionImage.setPixmap(img)
                self.instructionImage.setScaledContents(True)
            else:
                logger.error(f"Erro ao cerregar imagem no caminho: {img_path}")
        except Exception as e:
            logger.error(f"Erro ao atribuir uma imagem de instrução: {e}")
        
    def cancel_button_handler(self):
        self.timer.stop()
        self.setEnabled(True)
        self.timeout_counter = 0
        self.message_couter = 0
        self.ui_counter = 0        
        if self.calibration_step == 0:
            self.recived_presure_array = [[],[],[],[]]
        else:
            self.thumb_pressure = []
        self.cancelButton.setEnabled(False)
        
    #starts the timer
    #500ms timer for sending the messages
    def start_button_handler(self):
        print(self.serialHandleClass.ser.portName())
        self.startButton.setEnabled(False)
        self.restartButton.setEnabled(False)
        self.send_serial_message("*L1")
        self.serialHandleClass.mesReceivedSignal.connect(self.recieve_serial_message)
        self.cancelButton.setEnabled(True)
        self.timer.start(500)
        
    #messages are to be sent in *S1 to *S4 order
    def send_serial_message(self,message):
        self.serialHandleClass.open_port()
        logger.debug(f"mensagem enviada: {message}")
        self.serialHandleClass.send_message(message)
    
    #messages will be recieved in the same order as they are sent, per serial rules
    def recieve_serial_message(self,recieved):
        if self.message_couter > 3:
            self.message_couter = 0
        if self.calibration_step == 0:
            self.recived_presure_array[self.message_couter].append(int(recieved[:3]))
        else:
            self.thumb_pressure.append(int(recieved[:3]))
        print(f"recived_presure_array[{self.message_couter}]: {self.recived_presure_array[self.message_couter]}")
        self.message_couter += 1
        
    def restart_calibration(self):
        self.reset_screen()
        self.reset_variables()
        
    def reset_variables(self):
        self.recived_presure_array = [[],[],[],[]]
        self.thumb_pressure = []
        self.message_couter = 0
        self.timeout_counter = 0
        self.calibration_step = 0
        
    def reset_screen(self):
        self.instructionText.setText("Aperte todos os botões com toda sua força por 5 segundos")
        self.set_instruction_image("_internal/resources/imgs/calibration_instruction_1.png")
        self.resultModel.hide()
        self.instructionText.show()
        self.instructionImage.show()
        
    def present_results(self):
        self.instructionImage.hide()
        self.instructionText.hide()
        self.ui.visualsContainer.layout().addWidget(self.resultModel)
        max_val_array = self.get_max_pressure_values()
        self.resultModel.set_pressure_values([max_val_array[3],max_val_array[2],max_val_array[1],max_val_array[0],max_val_array[4]])
        
    def get_max_pressure_values(self):
        max_val_array = []
        for array in self.recived_presure_array:
            max_val_array.append(max(array))
        max_val_array.append(max(self.thumb_pressure))
        return max_val_array

    #11 timeouts in total
    #so 5.5 seconds total duration
    #first timer does nothing
    #starting from the second timer, or first timeout
        #sends 4 mesages
    #on final timeout
        #reenable screen    
    def timeout_handler(self):
        if self.calibration_step == 0:
            if self.timeout_counter < 10:
                for m in self.serial_messages:
                    self.send_serial_message(m)
                self.timeout_counter += 1
                return
            else:
                self.timeout_counter = 0
                self.startButton.setEnabled(True)
                self.restartButton.setEnabled(True)
                self.cancelButton.setEnabled(False)
                self.set_instruction_image("_internal/resources/imgs/calibration_instruction_2.png")
                self.instructionText.setText("Use seu dedão e indicador com toda sua força por 5 segundos")
                self.calibration_step = 1
                self.timer.stop()
                self.serialHandleClass.mesReceivedSignal.disconnect(self.recieve_serial_message)
                return
        elif self.calibration_step == 1:
            if self.timeout_counter < 10:
                self.send_serial_message("*S1")
                self.timeout_counter += 1
                return
            else:
                self.timeout_counter = 0
                self.calibration_step = 0
                self.timer.stop()
                self.serialHandleClass.mesReceivedSignal.disconnect(self.recieve_serial_message)
                self.startButton.setEnabled(True)
                self.restartButton.setEnabled(True)
                self.cancelButton.setEnabled(False)
                self.present_results()
                return