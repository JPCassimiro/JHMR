from ui.views.placeholderui_ui import Ui_Form
from PySide6.QtWidgets import QWidget


class PlaceholderWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)