from ui.views.register_dialog_ui import Ui_registerDialog
from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import Signal

infoDictBase = {
    "name": None,
    "details": None,
    "image_path": None
}

class RegisterModel(QDialog):
    def __init__(self):
        super().__init__()
        
        #ui setup
        self.ui = Ui_registerDialog()
        self.ui.setupUi(self)

        self.infoDict = infoDictBase.copy()
        
        self.current_mode = 0 #0 = create, 1 = update
        self.current_table = ""
        
        #get ui elements
        self.nameEdit = self.ui.nameEdit
        self.imageLineEdit = self.ui.imageLineEdit
        self.descriptionEdit = self.ui.descriptionEdit
        self.imageSelectButton = self.ui.imageSelectButton

        #connections
        self.imageSelectButton.clicked.connect(self.select_image_handler)
        self.nameEdit.textChanged.connect(self.name_changed_handler)
        self.descriptionEdit.textChanged.connect(self.description_changed_handler)

    def name_changed_handler(self, text):
        print(f"{self.sender().objectName()} - {text}")
        self.infoDict.update({"name": text})
        
    def description_changed_handler(self, text):
        print(f"{self.sender().objectName()} - {text}")
        self.infoDict.update({"details": text})
        
    def select_image_handler(self):
        fileName = QFileDialog.getOpenFileName(self, "Open Image", "./", "Image Files (*.png *.jpg *.bmp)")
        print(f"{self.sender().objectName()} - {fileName[0]}")
        self.imageLineEdit.setText(f"{fileName[0]}")
        self.infoDict.update({"image_path": fileName[0]})
    
    def reset_values(self):
        self.imageLineEdit.clear()
        self.nameEdit.clear()
        self.descriptionEdit.clear()
        self.infoDict = infoDictBase.copy()
        
    def complete_fields(self):
        self.nameEdit.setText(self.infoDict["name"])
        self.descriptionEdit.setText(self.infoDict["details"])
        self.imageLineEdit.setText(self.infoDict["image_path"])