from ui.views.patient_widget_ui import Ui_patientWindowContainer
from PySide6.QtWidgets import QWidget

class PatientWidgetModel(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_patientWindowContainer()
        self.ui.setupUi(self)