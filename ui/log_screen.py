import asyncio
import datetime
from modules import bluetooth_comunication
from PySide6.QtWidgets import QMainWindow, QWidget
from ui.views.logger_ui import Ui_Form
from modules import log_class

class Loggerwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #ler arquivo
        # ui_path = Path().joinpath(Path.__base__,"/ui_files/logger.ui")  
        # ui_path = Path(__file__).resolve().parent / "ui_files" / "logger.ui"
        # ui_path = "D:/utfpr_atual/THEEND/SourceProject/JHMR/ui/ui_files/logger.ui" #isso deve ser alterado, quando o método acima é utilizado, funciona no terminal, mas não funciona no deploy
        # ui_file = QFile(str(ui_path))
        # ui_file.open(QFile.ReadOnly)
        
        # if not ui_file.open(QFile.ReadOnly):
        #     print(f"Não consegue abrir {ui_file}: {ui_file.errorString}")

        # loader = QUiLoader()
        # self.centralWidget = loader.load(ui_file)
        # ui_file.close()

        # if not self.centralWidget:
        #     print(loader.errorString())
        #     sys.exit(-1)

        #achar janela
        self.ui = Ui_Form()
        self.centralWidget = QWidget()

        self.ui.setupUi(self.centralWidget)
        self.setCentralWidget(self.centralWidget)

        self.setWindowTitle("JHMR")

        #achar elementos da janela
        self.logWindow = self.ui.logWindow
        self.findButton = self.ui.findButton
        self.onOffButton = self.ui.onOffButton
        
        #connect nas funções
        self.findButton.clicked.connect(self.find_button_handler)
        self.onOffButton.clicked.connect(self.onOff_button_handler)
        
        #logica descoberta de dispositivos
        self.bluetoothHandleclass = bluetooth_comunication.BluetoothCommClass()
        self.bluetoothHandleclass.complete.connect(self.end_discovery_handler)
        self.bluetoothHandleclass.errorMessage.connect(self.handle_error_message)

    def append_log(self, message):
        currentDate = datetime.datetime.now().strftime("%c")
        self.logWindow.appendPlainText(currentDate + '\n' + message + '\n')

    def handle_error_message(self, message):
        self.onOffButton.setEnabled(True)
        self.findButton.setEnabled(True)
        self.append_log(message)

    #chama findDevices e manda mensagem
    def find_button_handler(self):
        self.findButton.setEnabled(False)
        self.onOffButton.setEnabled(False)
        self.append_log("Procurando dispositivos...")
        self.bluetoothHandleclass.start_discovery_task_handler()

    async def async_toggle_bluetooth(self):
        try:
            self.onOffButton.setEnabled(False)
            self.findButton.setEnabled(False)
            result = await self.bluetoothHandleclass.toggle_bluetooth()
            self.append_log(result)
            self.onOffButton.setEnabled(True)
            self.findButton.setEnabled(True)
        except Exception as e:
            log_class.logger.exception(f"Erro ao alterar estado do Bluetooth\nErro: {e}")
        finally:
            log_class.logger.debug("Alteração do estado Bluetooth bem sucedido")

    def onOff_button_handler(self):
        asyncio.create_task(self.async_toggle_bluetooth())
    
    def end_discovery_handler(self,devices):
        try:
            device_names = ''
            for device in devices:
                device_names += (device.name() + '\n')
            self.append_log("Dispositivos encontrados: \n" + str(device_names))
            self.onOffButton.setEnabled(True)
            self.findButton.setEnabled(True)
        except Exception as e:
            log_class.logger.exception(f"Erro ao encontrar dispositivos\nErro: {e}")
        finally:
            log_class.logger.debug(f"Sucesso na operação de descoberta, observe a janela do software")