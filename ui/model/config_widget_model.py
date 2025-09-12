from ui.views.config_widget_ui import Ui_configForm
from PySide6.QtWidgets import QWidget

class ConfigWidgetModel(QWidget):
    def __init__(self,serialHandleClass):#both ConfigWidgetModel and LoggerWidgetModel share the SAME INSTANCE of serialHandleClass
        super().__init__()
        
        #ui setup
        self.ui = Ui_configForm()
        self.ui.setupUi(self)
        
        #find ui elements
        self.sendMessageButton = self.ui.sendMessageButton
        self.messageBox = self.ui.textEdit

        #connect ui elements
        self.sendMessageButton.clicked.connect(self.send_message_button_handler)
        
        #import necessary modules
        
        #serial comm class shared instance 
        self.serialHandleClass = serialHandleClass
        
        self.serialHandleClass.mesReceivedSignal.connect(self.message_received_handler)

    def send_message_button_handler(self):
        self.serialHandleClass.open_port()
        self.serialHandleClass.send_message("*KA")

    def message_received_handler(self,response):
        self.append_message(response)
        
    def append_message(self,message):
        self.messageBox.append(message)