from PySide6.QtCore import QObject, QSettings
from PySide6.QtWidgets import QApplication

from pathlib import Path

class AppConfigClass(QObject):

    def __init__(self, parent = None):
        super().__init__()

        self.base_path_tr = Path("_internal/resources/translations")
        self.base_path_config = Path("_internal/resources/config/config.ini")

        self.settings = QSettings(str(self.base_path_config), QSettings.IniFormat)
        
        self.language_list = [
            {"name":"Portugês","path":None},
            {"name":"English","path":"en_tr.qm"}
        ]
        
        self.current_translator = None
    
    def write_ini_file(self, property, value):
        self.settings.setValue(property, value)
            
    def change_language(self,file):
        print(f"change_language - file: {file}")
        if file:
            file_path = self.base_path_tr / file
            self.write_ini_file("language",str(file_path))
        else:
            self.write_ini_file("language","None")
            
    # def change_language(self,file):
    #     app = QApplication.instance()

    #     if self.current_translator:
    #         app.removeTranslator(self.current_translator)
    #         self.current_translator = None

    #     if file:
    #         translator = QTranslator(app)
    #         file_path = self.base_path_tr / file
    #         res = translator.load(str(file_path))
    #         if res:
    #             self.current_translator = translator
    #             print(f"change_language res: {res} - self.current_translator: {self.current_translator}")

    # def write_config(self):