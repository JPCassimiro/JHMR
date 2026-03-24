from ui.views.game_profile_widget_ui import Ui_gameProfileWidgetForm

from PySide6.QtWidgets import QWidget

class GameProfileModel(QWidget):
    def __init__(self, logModel, dbHandle):
        super().__init__()

        #ui setup
        self.ui = Ui_gameProfileWidgetForm()
        self.ui.setupUi(self)

        
