import asyncio
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QStackedLayout
from ui.model.log_screen import LoggerWindow
from ui.views.main_window_ui import Ui_MainWindow
from ui.model.placeholder_screen import PlaceholderWindow
from ui.model.patient_info import PatientWidget
from ui.model.title import TitleWidget

class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
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
        self.logger_window = LoggerWindow()
        self.placeholder_window = PlaceholderWindow()
        self.patient_widget = PatientWidget()
        self.title_widget = TitleWidget()
        
        #setup stackedWidget
        self.stackedWidget.insertWidget(0, self.logger_window)
        self.stackedWidget.insertWidget(1, self.placeholder_window)
        
        #setups widgets on their containers
        self.patinetWidgetContainer.layout().addWidget(self.patient_widget)
        self.titletWidgetContainer.layout().addWidget(self.title_widget)

        self.current_selected_widget = 0

        #get buttons
        self.connectionMenuButton = self.ui.connectionMenuButton
        self.placeholderButton =  self.ui.placeholderButton

        #setup button connections
        self.connectionMenuButton.clicked.connect(self.connection_menu_button_handler)
        self.placeholderButton.clicked.connect(self.placeholder_menu_button_handler)
        

        self.stackedWidget.setCurrentIndex(0)
    
    def connection_menu_button_handler(self):
        self.connectionMenuButton.setDisabled(True)
        self.placeholderButton.setDisabled(False)
        self.stackedWidget.setCurrentIndex(0)

    def placeholder_menu_button_handler(self):
        self.connectionMenuButton.setDisabled(False)
        self.placeholderButton.setDisabled(True)
        self.stackedWidget.setCurrentIndex(1)
        
    
        
        