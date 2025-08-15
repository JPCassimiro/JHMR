from pathlib import Path
import sys
import asyncio
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import datetime
from modules import bluetooth_comunication
from PySide6.QtWidgets import QMainWindow, QPushButton, QPlainTextEdit

class Loggerwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #ler arquivo        
        ui_path = Path(__file__).resolve().parent / "ui_files" / "logger.ui"
        ui_file = QFile(str(ui_path))
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.centralWidget = loader.load(ui_file)
        ui_file.close()

        #achar janela
        self.setWindowTitle("Logger Bluetooth")
        self.setCentralWidget(self.centralWidget)

        #achar elementos da janela
        self.loggerWindow = self.centralWidget.findChild(QPlainTextEdit, "logWindow")
        self.findButton = self.centralWidget.findChild(QPushButton, "findButton")
        self.onOffButton = self.centralWidget.findChild(QPushButton, "onOffButton")
        
        #connect nas funções
        self.findButton.clicked.connect(self.find_button_handler)
        self.onOffButton.clicked.connect(self.onOff_button_handler)
        
        #logica descoberta de dispositivos
        self.bluetoothHandleclass = bluetooth_comunication.BluetoothCommClass()
        self.bluetoothHandleclass.complete.connect(self.end_discovery_handler)
        self.bluetoothHandleclass.errorMessage.connect(self.append_log)

    def append_log(self, message):
        currentDate = datetime.datetime.now().strftime("%c")
        self.loggerWindow.appendPlainText(currentDate + '\n' + message + '\n')

    #chama findDevices e manda mensagem
    def find_button_handler(self):
        self.findButton.setEnabled(False)
        self.onOffButton.setEnabled(False)
        self.append_log("Procurando dispositivos...")
        self.bluetoothHandleclass.start_discovery_task_handler()

    async def async_toggle_bluetooth(self):
        self.onOffButton.setEnabled(False)
        self.findButton.setEnabled(False)
        result = await self.bluetoothHandleclass.toggle_bluetooth()
        self.append_log(result)
        self.onOffButton.setEnabled(True)
        self.findButton.setEnabled(True)

    def onOff_button_handler(self):
        asyncio.create_task(self.async_toggle_bluetooth())
    
    def end_discovery_handler(self,devices):
        self.append_log("Dispositivos encontrados: \n" + str(devices))
        self.onOffButton.setEnabled(True)
        self.findButton.setEnabled(True)