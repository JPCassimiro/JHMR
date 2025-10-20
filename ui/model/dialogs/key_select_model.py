from ui.views.key_select_modal_ui import Ui_keySelectModalDialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QObject, QEvent, Qt

key_map = {
    Qt.Key_Up: "UP",
    Qt.Key_Down: "DOWN",
    Qt.Key_Left: "LEFT",
    Qt.Key_Right: "RIGHT",
    Qt.Key_Return: "ENTER",
    Qt.Key_Space: "SPACE",
    Qt.Key_Escape: "ESCAPE",
    Qt.Key_Tab: "TAB",
    Qt.Key_Backspace: "BACKSPACE",
    Qt.Key_Delete: "DELETE",
    Qt.Key_Shift: "SHIFT",
    Qt.Key_Control: "CTRL",
    Qt.Key_Alt: "ALT",
    Qt.Key_Meta: "META", 
    Qt.Key_F1: "F1",
    Qt.Key_F2: "F2",
    Qt.Key_F3: "F3",
    Qt.Key_F4: "F4",
    Qt.Key_F5: "F5",
    Qt.Key_F6: "F6",
    Qt.Key_F7: "F7",
    Qt.Key_F8: "F8",
    Qt.Key_F9: "F9",
    Qt.Key_F10: "F10",
    Qt.Key_F11: "F11",
    Qt.Key_F12: "F12",
}

class KeySelectModel(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_keySelectModalDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Use o teclado para selecionar")
        self.setWindowModality(Qt.ApplicationModal)

        self.selected_key = None
        self.z_c_key_mode = 0
        #0 = pressure, 1 = z key, 2 = c key
        
        #get ui elements
        self.cleanKeyButton = self.ui.cleanKeyButton
        self.keyDisplayer = self.ui.keyDisplayer
        self.buttonBox = self.ui.buttonBox
        self.warningLabel = self.ui.warningLabel
        
        self.warningLabel.hide()
        
        self.cleanKeyButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyDisplayer.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.warningLabel.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        for b in self.buttonBox.buttons():
            b.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        # self.cancelButton.clicked.connect(self.cancel_button_handler)
        # self.confirmButton.clicked.connect(self.confirm_button_handler)
        self.buttonBox.rejected.connect(self.cancel_button_handler)
        self.buttonBox.accepted.connect(self.confirm_button_handler)
        self.cleanKeyButton.clicked.connect(self.clean_button_handler)
        
        self.eventFilter = KeyPressHandler(parent=self)
        self.installEventFilter(self.eventFilter)
        
        self.rejected.connect(self.cancel_operation_handler)
        self.accepted.connect(self.accepted_operation_handler)
        

    def showEvent(self, arg__1):
        for b in self.buttonBox.buttons():
            b.clearFocus()
        return super().showEvent(arg__1)
    
        
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
            if event.key() != Qt.Key_Enter:
                if not key.strip():
                    key = self.key_text_fix(event)
                widget.selected_key = key
                widget.keyDisplayer.clear()
                if key not in ["UP", "DOWN", "LEFT", "RIGHT"]:
                    widget.keyDisplayer.append(key.upper())
                elif key == "UP":
                    widget.keyDisplayer.append(str("↑"))
                elif key == "DOWN":
                    widget.keyDisplayer.append(str("↓"))
                elif key == "LEFT":
                    widget.keyDisplayer.append(str("←"))
                elif key == "RIGHT":
                    widget.keyDisplayer.append(str("→"))
        return False
    
    def key_text_fix(self, key_event):
        key_code = key_event.key()
        if key_code in key_map:
            return key_map[key_code]
