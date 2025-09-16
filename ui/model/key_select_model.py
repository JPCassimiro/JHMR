from ui.views.key_select_modal_ui import Ui_keySelectModalDialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QObject, QEvent

class KeySelectModel(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_keySelectModalDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Use o teclado para selecionar")

        self.selected_key = None
        self.z_c_key_mode = 0
        #0 = pressure, 1 = z key, 2 = c key
        
        #get ui elements
        # self.cancelButton = self.ui.cancelButton
        # self.confirmButton = self.ui.confirmButton
        self.cleanKeyButton = self.ui.cleanKeyButton
        self.keyDisplayer = self.ui.keyDisplayer
        self.buttonBox = self.ui.buttonBox
        self.warningLabel = self.ui.warningLabel
        
        self.warningLabel.hide()
        
        # self.cancelButton.clicked.connect(self.cancel_button_handler)
        # self.confirmButton.clicked.connect(self.confirm_button_handler)
        self.buttonBox.rejected.connect(self.cancel_button_handler)
        self.buttonBox.accepted.connect(self.confirm_button_handler)
        self.cleanKeyButton.clicked.connect(self.clean_button_handler)
        
        self.eventFilter = KeyPressHandler(parent=self)
        self.installEventFilter(self.eventFilter)
        
        self.rejected.connect(self.cancel_operation_handler)
        self.accepted.connect(self.accepted_operation_handler)
        
    def confirm_button_handler(self):
        if self.selected_key == None:
            self.warningLabel.show()
        else:
            self.warningLabel.hide()
            self.accept()
        print(f"{self.sender().objectName()}")
        
    def cancel_button_handler(self):
        self.warningLabel.hide()
        self.reject()
        print(f"{self.sender().objectName()}")

    def clean_button_handler(self):
        self.selected_key = None
        self.keyDisplayer.clear()
        print(f"{self.sender().objectName()}")
        
    def cancel_operation_handler(self):
        self.z_c_key_mode = 0
        self.keyDisplayer.clear()
        self.selected_key = None
        
    def accepted_operation_handler(self):
        self.keyDisplayer.clear()


class KeyPressHandler(QObject):
    
    def eventFilter(self, widget, event):
        if event.type() == QEvent.Type.KeyPress:
            key = event.text()
            widget.selected_key = key
            widget.keyDisplayer.clear()
            widget.keyDisplayer.append(key.upper())
        return False
