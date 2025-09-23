import wmi
from modules.log_class import logger
from PySide6.QtCore import Signal, QObject
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import QIODevice

buffer_len = 255
baud_rate = 600
timeout = 1000

#! port opening needs to be revised 
#! device listner would help solve this

class SerialCommClass(QObject):
    
    portSignal = Signal(str)
    mesReceivedSignal = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__()
        
        #port setup
        #baud rate
        #port
        #timeout
        #device mac addrs
        self.ser = QSerialPort()
        self.ser.setBaudRate(baud_rate)

        self.device_mac_addr = ''

        #for testing
        # self.device_mac_addr = "d48afc9d936a"
        # self.ser.setPortName(r"\\.\COM20")

        
        #when a new char message is ready to be read on the serial port
        self.ser.readyRead.connect(self.recieve_message)
        self.ser.errorOccurred.connect(self.handle_serial_error)

    #toggles port state
    def alter_port_state(self):
        if self.ser.isOpen():
            self.ser.close()
        else:
            self.ser.open()
        
    # if port not open
    def open_port(self):
        if not self.ser.isOpen():
           if not self.ser.open(QIODevice.ReadWrite):
               print(f"error: {self.ser.errorString()}")

    #gets message from model class and writes it
    def send_message(self, message):
        encodedMessage = message.encode('utf-8')
        self.ser.write(encodedMessage)
        
    #gets message, decodes, sends signal
    def recieve_message(self):
        data = self.ser.readAll()
        dataStr = data.toStdString()
        self.mesReceivedSignal.emit(dataStr)
             
    #logs error on serial
    def handle_serial_error(self,err):
        logger.error(err)        
        
    #ports that are >=10 must be inputed this way due to a windows quirk of finding ports, Qt does not automatically deals with this like pyserial
    def port_name_normalization(self,portName):
        portNumber = int(portName[3:])
        if portNumber >= 10:
            portName = r"\\.\{}".format(portName)
        return portName
    
    def find_port(self):
        if self.device_mac_addr != "":
            c = wmi.WMI()
            for device in c.Win32_PnPEntity():
                if device.Name and "COM" in device.Name:
                    if self.device_mac_addr in str(device.deviceID).lower():#found com port 
                        start =  str(device.Name).lower().find("(com")
                        end =  str(device.Name).lower().find(")",start)
                        self.ser.setPortName(self.port_name_normalization(str(device.Name[start+1:end]).lower()))
                        self.portSignal.emit(f"Porta do ESP32: {self.ser.portName()}")
        else:
            logger.error("Encontre o endereço do MAC primeiro")
