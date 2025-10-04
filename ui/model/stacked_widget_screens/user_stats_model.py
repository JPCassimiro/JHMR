from ui.views.user_stats_ui import Ui_useStatisticsForm
from modules.use_data_collector import DataCollectorClass
from PySide6.QtWidgets import QWidget, QPushButton
from modules.log_class import logger

class UserStatsModel(QWidget):
    def __init__(self, dbHandleClass, SerialCommClass, LogModel):
        super().__init__()
        
        #ui setup
        self.ui = Ui_useStatisticsForm()
        self.ui.setupUi(self)
        
        #modules setup
        self.dataCollectorHandler = DataCollectorClass(dbHandleClass, SerialCommClass, LogModel)
        self.dbHandleClass = dbHandleClass
        
        #variables setup
        self.current_user = False

        #get ui elements
        self.maxPressure = self.ui.maxPressure
        self.minPressure = self.ui.minPressure
        self.startListening = self.ui.startListening
        self.stopListening = self.ui.stopListening
        
        self.maxPressure.hide()
        self.minPressure.hide()

        #connections setup
        self.startListening.clicked.connect(self.start_button_handler)
        self.stopListening.clicked.connect(self.stop_button_handler)
        
    def stop_button_handler(self):
        self.dataCollectorHandler.stop_data_collection()
        self.button_toggler(self.stopListening)
        
    def start_button_handler(self):
        self.dataCollectorHandler.start_watch = True
        self.button_toggler(self.startListening)

    def assing_user(self,user_index):
        self.current_user = user_index
        self.dataCollectorHandler.current_user_index = self.current_user
        session_id = self.create_session()
        self.dataCollectorHandler.current_session_index = session_id

    def create_session(self):
        q = f"""
            insert into session (patient_id) select ? where not exists
            (select id from session where date(session_date) = date('now') and patient_id = ?) 
            returning patient_id,id;"""
        res = self.dbHandleClass.execute_single_query(q,[self.current_user,self.current_user])
        if res:
            logger.debug(f"Seção criada para o usuário {res[0][0]}")
            return res[0][0]
        else:
            q = f"""
            select id from session where patient_id = (?);"""
            res = self.dbHandleClass.execute_single_query(q,[self.current_user])
            return res[0][0]

    def update_ui(self):
        qMax = f"select max(pressure) from use_data inner join session on session.id = use_data.session_id where session.patient_id = (?) and session_date = date('now');"
        qMin = f"select min(pressure) from use_data inner join session on session.id = use_data.session_id where session.patient_id = (?) and session_date = date('now');"
        resMax = self.dbHandleClass.execute_single_query(qMax,[self.current_user])
        resMin = self.dbHandleClass.execute_single_query(qMin,[self.current_user])
        print(f"{resMax}_{resMin}")

    def button_toggler(self, clicked_button):
        for button in self.ui.buttonsContainer.findChildren(QPushButton):
            if button != clicked_button:
                button.setEnabled(True)
            else:
                clicked_button.setEnabled(False)