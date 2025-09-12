import serial
import wmi
from modules.log_class import logger
from PySide6.QtCore import Signal, QObject

buffer_len = 255
class SerialCommClass(QObject):
    
    portSignal = Signal(str)
    mesReceivedSignal = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__()
        self.ser = serial.Serial()
        self.ser.baudrate = 600
        self.ser.port = 'com20'
        self.ser.timeout = 1
        self.device_mac_addr = "d48afc9d936a"
        
    def send_message(self, message):
        print("enviando mensagem: " + message)
        data = bytes(message,'utf-8')
        self.ser.open()
        self.ser.write(data)
        self.recieve_message()
        self.ser.close()
        
    def recieve_message(self):
        print("recebendo mensagem: ")
        char = self.ser.read(buffer_len)
        char.decode()
        self.mesReceivedSignal.emit(char)

    def find_port(self):
        if self.device_mac_addr != "":
            c = wmi.WMI()
            for device in c.Win32_PnPEntity():
                if device.Name and "COM" in device.Name:
                    if self.device_mac_addr in str(device.deviceID).lower():#found com port 
                        start =  str(device.Name).lower().find("(com")
                        end =  str(device.Name).lower().find(")",start)
                        self.ser.port = str(device.Name[start+1:end]).lower()
                        self.portSignal.emit(f"Porta do ESP32: {self.ser.port}")
        else:
            logger.error("Encontre o endereço do MAC primeiro")