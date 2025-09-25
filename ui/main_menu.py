from ui.model.logger_widget_model import LoggerWidgetModel
from ui.views.main_window_ui import Ui_MainWindow
from ui.model.patient_widget_model import PatientWidgetModel
from ui.model.title_widget_model import TitleWidgetModel
from ui.model.config_widget_model import ConfigWidgetModel
from ui.model.calibration_widget_model import CalibrationWidgetModel

from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QMainWindow
from modules.serial_communication import SerialCommClass

class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #setup shared serialCommClass instance
        self.serialHandleClass = SerialCommClass()
        
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
        self.logger_widget = LoggerWidgetModel(self.serialHandleClass)
        self.patient_widget = PatientWidgetModel()
        self.title_widget = TitleWidgetModel()
        self.config_widget = ConfigWidgetModel(self.serialHandleClass)
        self.calibration_widget = CalibrationWidgetModel(self.serialHandleClass)
        self.side_menu = self.ui.sideMenu_2
        
        #setup stackedWidget
        self.stackedWidget.insertWidget(0, self.logger_widget)
        self.stackedWidget.insertWidget(1, self.config_widget)
        self.stackedWidget.insertWidget(2, self.calibration_widget)
        
        #setups widgets on their containers
        self.patinetWidgetContainer.layout().addWidget(self.patient_widget)
        self.titletWidgetContainer.layout().addWidget(self.title_widget)

        #get buttons
        self.connectionMenuButton = self.ui.connectionMenuButton
        self.configButton = self.ui.configButton
        self.calibrationButton = self.ui.calibrationButton

        #setup button connections
        self.connectionMenuButton.clicked.connect(self.connection_menu_button_handler)
        self.configButton.clicked.connect(self.config_menu_button_handler)
        self.calibrationButton.clicked.connect(self.calibration_menu_button_handler)

        #setup signal connections
        self.calibration_widget.pValuesSignal.connect(self.handle_pValues_signal)

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

    def handle_pValues_signal(self,array):
        self.config_widget.set_slider_max_value(array)

    # toggles side menu buttons accordingly
    def side_menu_button_toggler(self, clicked_button):
        for button in self.side_menu.findChildren(QPushButton):
            if button != clicked_button:
                button.setEnabled(True)
            else:
                clicked_button.setEnabled(False)
        