import serial
import wmi
from modules.log_class import logger
from PySide6.QtCore import Signal, QObject

buffer_len = 255
class SerialCommClass(QObject):
    
    portSignal = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__()
        self.ser = serial.Serial()
        self.ser.baudrate = 600
        self.ser.port = ''
        self.ser.timeout = 1
        self.device_mac_addr = ""
        
    def send_message(self, message):
        self.ser.open()
        self.ser.write(message)
        
    def recieve_message(self):
        char = self.ser.read(buffer_len)
        char.decode()

    def open_port(self):
        self.ser.open()
        while True:
            self.ser.readline()
            line = self.ser.readline()
            print(str(line,'utf-8'))
            
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