import asyncio
import datetime
from modules import bluetooth_comunication
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton
from ui.views.logger_ui import Ui_loggerForm
from modules import log_class
class LoggerWindow(QWidget):
    def __init__(self):
        super().__init__()

        #achar janela
        self.ui = Ui_loggerForm()

        self.ui.setupUi(self)

        #achar elementos da janela
        self.logWindow = self.ui.logWindow
        self.findButton = self.ui.findButton
        self.onOffButton = self.ui.onOffButton
        self.pairButton = self.ui.pairButton
        self.unpairButton = self.ui.unpairButton
        
        self.findButton.hide()
        
        #connect nas funções
        self.findButton.clicked.connect(self.find_button_handler)
        self.onOffButton.clicked.connect(self.onOff_button_handler)
        self.pairButton.clicked.connect(self.pair_button_handler)
        self.unpairButton.clicked.connect(self.unapir_button_handler)
        
        #logica descoberta de dispositivos
        self.bluetoothHandleclass = bluetooth_comunication.BluetoothCommClass()
        self.bluetoothHandleclass.complete.connect(self.end_discovery_handler)
        self.bluetoothHandleclass.errorMessage.connect(self.handle_error_message)
        self.bluetoothHandleclass.pairComplete.connect(self.handle_error_message)

    def append_log(self, message):
        currentDate = datetime.datetime.now().strftime("%c")
        self.logWindow.appendPlainText(currentDate + '\n' + message + '\n')

    def handle_error_message(self, message):
        self.button_state_toggle()
        self.append_log(message)

    #chama findDevices e manda mensagem
    def find_button_handler(self):
        self.button_state_toggle()
        self.append_log("Procurando dispositivos...")
        self.bluetoothHandleclass.start_discovery_task_handler()

    async def async_toggle_bluetooth(self):
        try:
            self.button_state_toggle()
            result = await self.bluetoothHandleclass.toggle_bluetooth()
            self.append_log(result)
            self.button_state_toggle()
        except Exception as e:
            log_class.logger.exception(f"Erro ao alterar estado do Bluetooth\nErro: {e}")
        finally:
            log_class.logger.debug("Alteração do estado Bluetooth bem sucedido")

    def onOff_button_handler(self):#!ou remover isso desta classe, ou colocar todos aqui
        asyncio.create_task(self.async_toggle_bluetooth())
    
    def end_discovery_handler(self,services):
        try:
            device_names = ''
            for service in services:
                device_names += (service.name() + '\n')
            self.append_log("Dispositivos encontrados: \n" + str(device_names))
            self.button_state_toggle()
        except Exception as e:
            log_class.logger.exception(f"Erro ao encontrar dispositivos\nErro: {e}")
        finally:
            log_class.logger.debug(f"Sucesso na operação de descoberta, observe a janela do software")

    def button_state_toggle(self):
        for button in self.findChildren(QPushButton):
            button.setEnabled(not button.isEnabled())
        
    def pair_button_handler(self):
        self.button_state_toggle()
        self.append_log("Iniciando processo de emprelhamento, este processo pode demorar. Uma notificação do Windows vai aparecer, clique na mesma e aceite")
        self.bluetoothHandleclass.pair_device()

    def unapir_button_handler(self):
        self.button_state_toggle()
        self.append_log("Iniciando processo de desemprelhamento, este processo pode demorar...")
        self.bluetoothHandleclass.unpair_device()