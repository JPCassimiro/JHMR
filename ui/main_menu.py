from ui.model.stacked_widget_screens.logger_widget_model import LoggerWidgetModel
from ui.views.main_window_ui import Ui_MainWindow
from ui.model.components.patient_widget_model import PatientWidgetModel
from ui.model.components.title_widget_model import TitleWidgetModel
from ui.model.stacked_widget_screens.config_widget_model import ConfigWidgetModel
from ui.model.stacked_widget_screens.calibration_widget_model import CalibrationWidgetModel
from ui.model.stacked_widget_screens.user_actions_widget_model import UserActionsModel
from ui.model.stacked_widget_screens.user_stats_model import UserStatsModel
from ui.model.dialogs.log_model import LogModel

from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QMainWindow

from modules.serial_communication import SerialCommClass
from modules.db_functions import DbClass

class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #setup shared instances
        self.serialHandleClass = SerialCommClass()
        self.dbHandleClass = DbClass()
        self.logModel = LogModel()

        #set main windows
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("JHMR")
        
        #get stackabledWidget
        self.stackedWidget = self.ui.stackedWidget
        
        #get container widgets
        self.patinetWidgetContainer = self.ui.patientWidget
        self.titletWidgetContainer = self.ui.titleWidget
        
        #get widgets
        self.logger_widget = LoggerWidgetModel(self.serialHandleClass, self.logModel)
        self.patient_widget = PatientWidgetModel()
        self.title_widget = TitleWidgetModel()
        self.config_widget = ConfigWidgetModel(self.serialHandleClass,self.logModel)
        self.calibration_widget = CalibrationWidgetModel(self.serialHandleClass,self.logModel)
        self.user_actions_widget = UserActionsModel(self.dbHandleClass)
        self.user_stats_widget = UserStatsModel(self.dbHandleClass,self.serialHandleClass,self.logModel)
        self.side_menu = self.ui.sideMenu_2
        
        #setup signal connections
        self.calibration_widget.pValuesSignal.connect(self.handle_pValues_signal)
        self.user_actions_widget.therapistSelected.connect(self.therapist_select_handler)
        self.user_actions_widget.patientSelected.connect(self.patient_select_handler)
        self.user_actions_widget.assin_default_user()
        
        #setup stackedWidget
        self.stackedWidget.insertWidget(0, self.logger_widget)
        self.stackedWidget.insertWidget(1, self.config_widget)
        self.stackedWidget.insertWidget(2, self.calibration_widget)
        self.stackedWidget.insertWidget(3, self.user_actions_widget)
        self.stackedWidget.insertWidget(4, self.user_stats_widget)
        
        #setups widgets on their containers
        self.patinetWidgetContainer.layout().addWidget(self.patient_widget)
        self.titletWidgetContainer.layout().addWidget(self.title_widget)

        #get buttons
        self.connectionMenuButton = self.ui.connectionMenuButton
        self.configButton = self.ui.configButton
        self.calibrationButton = self.ui.calibrationButton
        self.userActionsButton = self.ui.userActionsButton
        self.statsButton = self.ui.statsButton
        self.logModalButton = self.ui.logModalButton
        
        #setup button connections
        self.connectionMenuButton.clicked.connect(self.connection_menu_button_handler)
        self.configButton.clicked.connect(self.config_menu_button_handler)
        self.calibrationButton.clicked.connect(self.calibration_menu_button_handler)
        self.userActionsButton.clicked.connect(self.user_menu_button_handler)
        self.statsButton.clicked.connect(self.stats_menu_button_handler)
        self.logModalButton.clicked.connect(self.log_button_handler)

        #button toggling connections
        self.calibration_widget.sideMenuDisableSignal.connect(lambda state: self.side_menu_button_disabler(state, self.calibrationButton))
        self.user_stats_widget.sideMenuDisableSignal.connect(lambda state: self.side_menu_button_disabler(state, self.statsButton))
        self.logger_widget.sideMenuDisableSignal.connect(lambda state: self.side_menu_button_disabler(state, self.connectionMenuButton))

        self.stackedWidget.setCurrentIndex(0)

    
    def connection_menu_button_handler(self):
        self.side_menu_button_toggler(self.connectionMenuButton)
        self.stackedWidget.setCurrentIndex(0)
        
    def config_menu_button_handler(self):
        self.side_menu_button_toggler(self.configButton)
        self.stackedWidget.setCurrentIndex(1)

    def calibration_menu_button_handler(self):
        self.side_menu_button_toggler(self.calibrationButton)
        self.stackedWidget.setCurrentIndex(2)     
        
    def user_menu_button_handler(self):
        self.side_menu_button_toggler(self.userActionsButton)
        self.stackedWidget.setCurrentIndex(3)     

    def handle_pValues_signal(self,array):
        self.config_widget.set_slider_max_value(array)

    def therapist_select_handler(self,infoDict):
        self.title_widget.info_dict = infoDict.copy()
        self.title_widget.update_fields()
        
    def patient_select_handler(self,infoDict):
        self.patient_widget.info_dict = infoDict.copy()
        self.patient_widget.update_fields()
        if "id" in infoDict:
            self.user_stats_widget.assing_user(infoDict["id"])
            self.config_widget.current_user = infoDict["id"]
        
    def stats_menu_button_handler(self):
        self.side_menu_button_toggler(self.statsButton)
        self.stackedWidget.setCurrentIndex(4)       
                                     
    def log_button_handler(self):
        self.logModel.open()

    # toggles side menu buttons accordingly
    def side_menu_button_toggler(self, clicked_button):
        for button in self.side_menu.findChildren(QPushButton):
            if button != clicked_button:
                button.setEnabled(True)
            else:
                clicked_button.setEnabled(False)
                
    def side_menu_button_disabler(self, state, clicked_button):
        for button in self.side_menu.findChildren(QPushButton):
            if button == clicked_button:
                clicked_button.setEnabled(False)
            else:
                button.setEnabled(state)
        