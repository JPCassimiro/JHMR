import datetime
from modules import bluetooth_comunication
from PySide6.QtWidgets import QWidget, QPushButton
from ui.views.logger_ui import Ui_loggerForm
from modules import log_class

class LoggerWindow(QWidget):
    def __init__(self):
        super().__init__()

        #achar janela
        self.ui = Ui_loggerForm()

        self.ui.setupUi(self)

        #find elements from the widget
        self.logWindow = self.ui.logWindow
        self.findButton = self.ui.findButton
        self.onOffButton = self.ui.onOffButton
        self.pairButton = self.ui.pairButton
        self.unpairButton = self.ui.unpairButton
        
        self.findButton.hide()
        
        #connect buttons to functions
        self.findButton.clicked.connect(self.find_button_handler)
        self.onOffButton.clicked.connect(self.onOff_button_handler)
        self.pairButton.clicked.connect(self.pair_button_handler)
        self.unpairButton.clicked.connect(self.unapir_button_handler)
        
        #bluetooth comm class instance
        self.bluetoothHandleclass = bluetooth_comunication.BluetoothCommClass()

    #adds text to widget
    def append_log(self, message):
        currentDate = datetime.datetime.now().strftime("%c")
        self.logWindow.appendPlainText(currentDate + '\n' + message + '\n')

    #simple end task on error
    def handle_error_message(self, message):
        self.button_state_toggle()
        self.append_log(message)

    #calls findDevices and sets callbacks for signals
    def find_button_handler(self):
        self.button_state_toggle()
        self.append_log("Procurando dispositivos...")
        
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
       
    #puts all devices on a list and appends them o screen             
    def end_discovery_handler(self,services):
        try:
            device_names = "\n".join([s.name() for s in services])
            self.append_log("Dispositivos encontrados: \n" + str(device_names))
            self.button_state_toggle()
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
            
        def on_result(message):
            self.button_state_toggle()
            self.append_log(message)

        self.bluetoothHandleclass.set_callback(on_result=on_result,on_error=on_error)
        self.bluetoothHandleclass.pair_device()

    #same as above
    def unapir_button_handler(self):
        self.button_state_toggle()
        self.append_log("Iniciando processo de desemprelhamento, este processo pode demorar...")

        def on_error(message):
            self.handle_error_message(message)
            
        def on_result(message):
            self.button_state_toggle()
            self.append_log(message)

        self.bluetoothHandleclass.set_callback(on_result=on_result,on_error=on_error)
        self.bluetoothHandleclass.unpair_device()
        
    #blocks/unblocks all buttons from this widget    
    def button_state_toggle(self):
        for button in self.findChildren(QPushButton):
            button.setEnabled(not button.isEnabled())