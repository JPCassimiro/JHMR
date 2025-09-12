import datetime
from modules import bluetooth_comunication
from PySide6.QtWidgets import QWidget, QPushButton
from ui.views.logger_widget_ui import Ui_loggerForm
from modules import log_class
from modules.serial_communication import SerialCommClass

class LoggerWidgetModel(QWidget):
    def __init__(self,serialHandleClass):#both ConfigWidgetModel and LoggerWidgetModel share the SAME INSTANCE of serialHandleClass
        super().__init__()

        #achar janela
        self.ui = Ui_loggerForm()

        self.ui.setupUi(self)

        #find elements from the widget
        self.logWindow = self.ui.logWindow
        self.onOffButton = self.ui.onOffButton
        self.pairButton = self.ui.pairButton
        self.unpairButton = self.ui.unpairButton
        
        #connect buttons to functions
        self.onOffButton.clicked.connect(self.onOff_button_handler)
        self.pairButton.clicked.connect(self.pair_button_handler)
        self.unpairButton.clicked.connect(self.unapir_button_handler)
        
        #bluetooth comm class instance
        self.bluetoothHandleclass = bluetooth_comunication.BluetoothCommClass()

        #serial comm class shared instance 
        self.serialHandleClass = serialHandleClass
        self.serialHandleClass.portSignal.connect(self.port_signal_handler)

    #adds text to widget
    def append_log(self, message):
        currentDate = datetime.datetime.now().strftime("%c")
        self.logWindow.appendPlainText(currentDate + '\n' + message + '\n')

    #simple end task on error
    def handle_error_message(self, message):
        self.button_state_toggle()
        self.append_log(message)

    #calls findDevices and sets callbacks for signals
    def find_device_handler(self):
        def on_error(message):
            self.handle_error_message(message)
            
        def on_result(devices):
            self.end_discovery_handler(devices)
            
        self.bluetoothHandleclass.set_callback(on_result=on_result,on_error=on_error)
        self.bluetoothHandleclass.start_discovery()
        
    #alter bluetooth state
    def onOff_button_handler(self):
        self.button_state_toggle()
        
        def handle_toggle_result(message):
            self.append_log(message)
            self.button_state_toggle()
            
        def handle_toggle_error(message):
            self.handle_error_message(message)
            
        self.bluetoothHandleclass.set_callback(on_error=handle_toggle_error,on_result=handle_toggle_result)
        self.bluetoothHandleclass.toggle_bluetooth()
       
    #gets device addr            
    def end_discovery_handler(self,addr):
        try:
            self.serialHandleClass.device_mac_addr = addr
            self.serialHandleClass.find_port()
        except Exception as e:
            log_class.logger.exception(f"Erro ao encontrar dispositivos\nErro: {e}")
        finally:
            log_class.logger.debug(f"Sucesso na operação de descoberta, observe a janela do software")

    #attemps to pair the esp32, also sets callbacks for the signals
    def pair_button_handler(self):
        self.button_state_toggle()
        self.append_log("Iniciando processo de emprelhamento, este processo pode demorar. Uma notificação do Windows vai aparecer, clique na mesma e aceite")

        def on_error(message):
            self.handle_error_message(message)
            
        def on_result(processDict):
            self.append_log(processDict["message"])
            if processDict["status"] == False:
                self.button_state_toggle()#if a error message appears, break process
            else:
                self.append_log("Encontrando o endereço MAC e porta serial do dispositivo, aguarde...")
                self.find_device_handler()
            
        self.bluetoothHandleclass.set_callback(on_result=on_result,on_error=on_error)
        self.bluetoothHandleclass.pair_device()

    #same as above
    def unapir_button_handler(self):
        self.button_state_toggle()
        self.append_log("Iniciando processo de desemprelhamento, este processo pode demorar...")

        def on_error(message):
            self.handle_error_message(message)
            
        def on_result(message):
            self.serialHandleClass.device_mac_addr = None#clear device info from serialHandleClass
            self.serialHandleClass.ser.port = ''
            self.button_state_toggle()
            self.append_log(message)

        self.bluetoothHandleclass.set_callback(on_result=on_result,on_error=on_error)
        self.bluetoothHandleclass.unpair_device()
        
    def port_signal_handler(self,message):
        self.append_log(message)    
        self.button_state_toggle()
    
    #blocks/unblocks all buttons from this widget    
    def button_state_toggle(self):
        for button in self.findChildren(QPushButton):
            button.setEnabled(not button.isEnabled())
            