from modules import bluetooth_comunication
from PySide6.QtWidgets import QWidget, QPushButton
from ui.views.logger_widget_ui import Ui_loggerForm
from PySide6.QtCore import Signal
from modules import log_class

class LoggerWidgetModel(QWidget):

    sideMenuDisableSignal = Signal(bool)

    def __init__(self,serialHandleClass,logModel):#both ConfigWidgetModel and LoggerWidgetModel share the SAME INSTANCE of serialHandleClass
        super().__init__()

        #achar janela
        self.ui = Ui_loggerForm()

        self.ui.setupUi(self)
        
        #shared log model
        self.logModel = logModel

        #find elements from the widget
        self.onOffButton = self.ui.onOffButton
        self.pairButton = self.ui.pairButton
        self.unpairButton = self.ui.unpairButton
        self.pairHidButton = self.ui.pairHidButton
        self.unpairHidButton = self.ui.unpairHidButton
        self.fullPairButton = self.ui.fullPairButton
        
        #connect buttons to functions
        self.onOffButton.clicked.connect(self.onOff_button_handler)
        self.pairButton.clicked.connect(self.pair_button_handler)
        self.unpairButton.clicked.connect(self.unpair_button_handler)
        self.unpairHidButton.clicked.connect(self.unpair_hid_handler)
        self.pairHidButton.clicked.connect(self.pair_hid_handler)
        self.fullPairButton.clicked.connect(self.full_pair_handler)
        
        #bluetooth comm class instance
        self.bluetoothHandleclass = bluetooth_comunication.BluetoothCommClass()

        #serial comm class shared instance 
        self.serialHandleClass = serialHandleClass
        self.serialHandleClass.portSignal.connect(self.port_signal_handler)

    #adds text to widget
    def append_log(self, message):
        self.logModel.append_log(message)

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
        self.append_log("Iniciando processo de emprelhamento, este processo pode demorar.\nMantenha o joystick ligado.\nUma notificação do Windows vai aparecer, clique na mesma e aceite")

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
    def unpair_button_handler(self):
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
        
    #pair hid(keyboard) device handler
    def pair_hid_handler(self):
        self.button_state_toggle()    
        self.append_log("Iniciando processo de emparelhamento do dispositivo HID, este processo pode demorar...")

        def on_error(message):
            self.handle_error_message(message)
        
        def on_result(message):
            self.append_log(message)
            self.button_state_toggle()

        self.bluetoothHandleclass.set_callback(on_error=on_error,on_result=on_result)
        self.bluetoothHandleclass.hid_device_discovery()

    #unpair hid(keyboard) device handler
    def unpair_hid_handler(self):
        self.button_state_toggle()    
        self.append_log("Iniciando processo de desemparelhamento do dispositivo HID, este processo pode demorar...")

        def on_error(message):
            self.handle_error_message(message)
        
        def on_result(message):
            self.append_log(message)
            self.button_state_toggle()

        self.bluetoothHandleclass.set_callback(on_error=on_error,on_result=on_result)
        self.bluetoothHandleclass.hid_device_unpair()
        
    def full_pair_handler(self):
        self.button_state_toggle()
        self.append_log("Processo de conexão com joystick iniciado, este processo pode demorar...")
        self.append_log("Desemparelhando dispositivo HID.")

        def on_error(message):
            if message == "Dispositivo não encontrado":
                message +=". Passando para o próximo passo"
                self.append_log(message)
                self.full_pair_step_2()
            else:
                self.handle_error_message(message)

        def on_result(message):
            self.append_log(message)
            self.full_pair_step_2()
            
        self.bluetoothHandleclass.set_callback(on_error=on_error,on_result=on_result)
        self.bluetoothHandleclass.hid_device_unpair()
        
    def full_pair_step_2(self):
        self.append_log("Desemparelhando dispositivo SPP.")
        def on_error(message):
            if message == "Dispositivo não encontrado":
                message +=". Passando para o próximo passo"
                self.append_log(message)
                self.full_pair_step_3()
            else:
                self.handle_error_message(message)

        def on_result(message):
            self.append_log(message["message"])
            self.full_pair_step_3()
            
        self.bluetoothHandleclass.set_callback(on_error=on_error,on_result=on_result)
        self.bluetoothHandleclass.unpair_device()
        
    def full_pair_step_3(self):
        self.append_log("Iniciando processo de emprelhamento HID.\nMantenha o joystick ligado.\nEste processo pode demorar.")

        def on_error(message):
            self.handle_error_message(message)
            
        def on_result(message):
            self.append_log(message)
            self.full_pair_step_4()
            
        self.bluetoothHandleclass.set_callback(on_result=on_result,on_error=on_error)
        self.bluetoothHandleclass.hid_device_discovery()

    def full_pair_step_4(self):
        self.append_log("Iniciando processo de emprelhamento.\nMantenha o joystick ligado.\nEste processo pode demorar.\nUma notificação do Windows vai aparecer, clique na mesma e aceite")

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
        
        
    def port_signal_handler(self,message):
        self.append_log(message)    
        self.button_state_toggle()
    
    #blocks/unblocks all buttons from this widget    
    def button_state_toggle(self):
        for button in self.findChildren(QPushButton):
            button.setEnabled(not button.isEnabled())
        if self.pairButton.isEnabled():
            self.sideMenuDisableSignal.emit(True)
        else:
            self.sideMenuDisableSignal.emit(False)                
            