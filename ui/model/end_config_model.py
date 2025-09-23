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

    def recieve_end_message(self,message):
        if("N" in message):
            self.messageField.append(f"Erro ao configurar atributo")
        else:
            self.messageField.append(f"Atributo configurado com sucesso")




    def finished_handler(self):
        self.messageField.clear()