import wmi
import re
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
    mesReceivedSignal = Signal(object)
    
    def __init__(self, parent=None):
        super().__init__()
        
        #port setup
        #baud rate
        #port
        #timeout
        #device mac addrs
        self.ser = QSerialPort()
        self.ser.setBaudRate(baud_rate)
        self.message_buffer = ""
        self.use_data_buffer = ""
        self.device_mac_addr = ''

        self.use_data_regex = r"\*I\d{12}"

        self.c = wmi.WMI()

        #for testing
        # self.device_mac_addr = "d48afc9d936a"
        self.ser.setPortName(r"\\.\COM20")

        
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
        message_substrings = []#mesages to be sent
        data = self.ser.readAll()#these messages can be recieved in any way at any time, so it can be split or concateneted
        dataStr = data.toStdString()
        self.message_buffer += dataStr
        print(f"recive_message:{self.message_buffer}")
        while "N" in self.message_buffer or "A" in self.message_buffer:
            last_index = 0
            for i, c in enumerate(self.message_buffer):#get the substring up to the limiter
                if c == "A" or c == "N":
                    message_substrings.append(self.message_buffer[:i+1])
                    last_index = i
                    break
            self.message_buffer = self.message_buffer[last_index+1:]
        for m in message_substrings:
            self.mesReceivedSignal.emit(m)
            logger.debug(f"Mensagem recebida: {m}")
             
    def recieve_use_data_message(self):
        messages = []
        data = self.ser.readAll()
        dataStr = data.toStdString()
        self.use_data_buffer += dataStr
        matches = list(re.finditer(self.use_data_regex,self.use_data_buffer))
        print(f"recieve_use_data_message self.use_data_buffer:{self.use_data_buffer}\ndataStr:{dataStr}\nmatches:{matches}")
        if matches:
            last_match = matches[-1]
            start, end = last_match.span()
            self.use_data_buffer = self.message_buffer[end+1:]
        for m in matches:
            messages.append(m.group())
            logger.debug(f"Mensagem recebida: {m.group()}")
        if messages:
            self.mesReceivedSignal.emit(messages)
            
                
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
            com_devices = self.c.query("SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%(COM%'")
            for com_device in com_devices:
                if self.device_mac_addr in str(com_device.deviceID).lower():#found com port 
                    start =  str(com_device.Name).lower().find("(com")
                    end =  str(com_device.Name).lower().find(")",start)
                    self.ser.setPortName(self.port_name_normalization(str(com_device.Name[start+1:end]).lower()))
                    self.portSignal.emit(f"Porta do ESP32: {self.ser.portName()}")
        else:
            logger.error("Encontre o endereço MAC primeiro")

    def swap_message_listner(self,op = 0):
        self.ser.readyRead.disconnect()
        if op == 0:#default
            self.ser.readyRead.connect(self.recieve_message)
        elif op == 1:#use_data_collector
            self.ser.readyRead.connect(self.recieve_use_data_message)
            