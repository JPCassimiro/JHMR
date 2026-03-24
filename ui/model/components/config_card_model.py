from ui.views.config_card_widget_ui import Ui_configCardWidgetForm

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QEvent

class ConfigCardModel(QWidget):
    
    def __init__(self):
        super().__init__()

        #setup ui
        self.ui = Ui_configCardWidgetForm()
        self.ui.setupUi(self)

        #get ui elements
        self.keyLabel = self.ui.keyLabel
        self.ringLabel = self.ui.ringLabel
        self.indexLabel = self.ui.indexLabel
        self.repeatLabel = self.ui.repeatLabel
        self.littleLabel = self.ui.littleLabel
        self.durationLabel = self.ui.durationLabel

    def changeEvent(self, event):
        if event.type() == QEvent.Type.LanguageChange:
            self.ui.retranslateUi(self)
        return super().changeEvent(event)
        