from ui.views.end_config_modal_ui import Ui_endConfigModalDialog
from modules.log_class import logger

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QCoreApplication, QEvent


class EndConfigModel(QDialog):
    def __init__(self):
        super().__init__()
        
        #setup translatable strins
        self.string_list_components = [
            QCoreApplication.translate("EndConfigDialogText","Finalizado"),
        ]
        
        self.ui = Ui_endConfigModalDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(self.string_list_components[0])

        #get ui elements
        self.messageField = self.ui.messageField 

        self.finished.connect(self.finished_handler)
        
    def set_ui_text(self):
        self.setWindowTitle(self.string_list_components[0])

    def recieve_end_message(self,message):
        self.string_list_messages = [
            QCoreApplication.translate("EndConfigDialogText","Erro ao configurar atributo"),
            QCoreApplication.translate("EndConfigDialogText","Atributo configurado com sucesso")
        ]
        if("N" in message):
            self.messageField.append(self.string_list_messages[0])
            logger.debug(f"Erro ao configurar atributo")
        else:
            self.messageField.append(self.string_list_messages[1])
            logger.debug(f"Atributo configurado com sucesso")

    def finished_handler(self):
        self.messageField.clear()

    def changeEvent(self, event):
        if event.type() == QEvent.Type.LanguageChange:
            self.ui.retranslateUi(self)
            self.string_list_components = [
                QCoreApplication.translate("EndConfigDialogText","Finalizado"),
            ]
            self.set_ui_text()
        return super().changeEvent(event)