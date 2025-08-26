import serial
from serial.tools import list_ports 
import pprint

buffer_len = 255

class SerialCommClass():
    def __init__(self, parent=None):
        super().__init__()
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.port = ''
        self.ser.timeout = 1

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
        device_port = []
        port_list = list_ports.comports()
        for port in port_list:
            pprint.pprint(vars(port))
            hwid = port.hwid.lower()
            if(hwid.find("eterlogic") == -1):
                print("not found")
            else:
                device_port.append(port)
        print(device_port)


com = SerialCommClass()
# com.open_port()
com.find_port()
# com.send_message(b'asd')
# com.test()