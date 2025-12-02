from ui.views.app_config_modal_ui import Ui_AppConfigDialog

from modules.app_config_module import AppConfigClass

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QCoreApplication, Qt

class AppConfigModel(QDialog):
    def __init__(self):
        super().__init__()

        self.string_list_components = [
            QCoreApplication.translate("AppConfigDialogText","Configuração do aplicativo")
        ]

        #setup ui
        self.ui = Ui_AppConfigDialog()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        
        self.setWindowTitle(self.string_list_components[0])

        self.appConfigInstance = AppConfigClass()

        #get ui elements
        self.languageComboBox = self.ui.languageSelectionComboBox

        self.populate_language_comboBox()

        #setup connections
        self.languageComboBox.currentIndexChanged.connect(self.language_comboBox_change_handler)


    def language_comboBox_change_handler(self):
        self.select_language()

    def select_language(self):
        print(f"{self.sender().objectName()} - {self.sender().currentIndex()}")        
        self.appConfigInstance.change_language(self.languageComboBox.currentData())

    def populate_language_comboBox(self):
        self.languageComboBox.clear() 
        if self.appConfigInstance.language_list:
            for l in self.appConfigInstance.language_list:
                self.languageComboBox.addItem(l["name"],l["path"])
            self.languageComboBox.setCurrentIndex(-1)    
            