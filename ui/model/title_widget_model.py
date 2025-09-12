from ui.views.title_widget_ui import Ui_titleWindowContainer
from PySide6.QtWidgets import QWidget

class TitleWidgetModel(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_titleWindowContainer()
        self.ui.setupUi(self)