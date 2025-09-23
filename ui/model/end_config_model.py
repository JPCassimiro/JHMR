from ui.views.end_config_modal_ui import Ui_endConfigModalDialog
# from PySide6.QtCore 
from PySide6.QtWidgets import QDialog


class EndConfigModel(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_endConfigModalDialog()
        self.ui.setupUi(self)

        #get ui elements
        self.messageField = self.ui.messageField 

        self.finished.connect(self.finished_handler)

    def append_end_message(self,message):
        self.messageField.append(message)

    def finished_handler(self):
        self.messageField.clear()