from ui.views.user_stats_ui import Ui_useStatisticsForm
from modules.use_data_collector import DataCollectorClass
from PySide6.QtWidgets import QWidget, QPushButton
from modules.log_class import logger
from PySide6.QtCore import Signal
import pyqtgraph as pg
import numpy as np
class UserStatsModel(QWidget):

    sideMenuDisableSignal = Signal(bool)

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
        self.selected_hand = 0
        self.latest_session = False

        #get ui elements
        self.startListening = self.ui.startListening
        self.stopListening = self.ui.stopListening
        self.sessionComboBox = self.ui.sessionComboBox
        self.timelapseLabel = self.ui.timelapseLabel
        self.statsTabWidget = self.ui.statsTabWidget
        self.countSession = self.ui.countSession
        self.avgSessionTime = self.ui.avgSessionTime
        self.leftHandButton = self.ui.leftHandButton
        self.rightHandButton = self.ui.rightHandButton
        self.newSessionButton = self.ui.newSessionButton

        #ui element setup
        self.timelapse = "00:00:00"
        self.sessionCount = "0"
        self.avgTimelapse = "00:00:00"
        self.timelapseLabel.setText(self.timelapse)
        self.countSession.setText(self.sessionCount)
        self.avgSessionTime.setText(self.avgTimelapse)
        
        self.rightHandButton.toggle()
        
        self.startListening.setEnabled(False)
        self.stopListening.setEnabled(False)
        
        #connections setup
        self.startListening.clicked.connect(self.start_button_handler)
        self.stopListening.clicked.connect(self.stop_button_handler)
        self.sessionComboBox.currentIndexChanged.connect(self.comboBox_change_handler)
        self.statsTabWidget.tabBarClicked.connect(self.update_summary_charts)
        self.leftHandButton.toggled.connect(self.hand_selector)
        self.rightHandButton.toggled.connect(self.hand_selector)
        self.newSessionButton.clicked.connect(self.new_session_button_handler)

        #session chart widget        
        pg.setConfigOption('background', '#F5F5F5')
        pg.setConfigOption('foreground', 'black')
        self.session_chart_layout_widget =  pg.GraphicsLayoutWidget()
        self.ui.sessionChartContainer.layout().addWidget(self.session_chart_layout_widget)
        x_range = np.array([0,1,2,3])
        self.finger_name_labels = [(x_range[0],"Mindinho"),(x_range[1],"Anelar"),(x_range[2],"Meio"),(x_range[3],"Indicador")]

        #create charts
        #avarage pressure by finger chart
        self.avg_pressure = [0,0,0,0]
        self.avg_chart = pg.BarGraphItem(x= x_range,height=self.avg_pressure,width = 0.2,brush="#F89E59")
        
        #max pressure by finger chart
        self.max_pressure = [0,0,0,0]
        self.max_chart = pg.BarGraphItem(x= x_range+0.2,height=self.max_pressure,width = 0.2,brush="#F37F27")
        
        #min pressure by finger chart
        self.min_pressure = [0,0,0,0]
        self.min_chart = pg.BarGraphItem(x= x_range-0.2,height=self.max_pressure,width = 0.2,brush="#F6E1A4")
        
        #times finger has been used
        self.times_pressed = [0,0,0,0]
        self.times_used_chart = pg.BarGraphItem(x= x_range,height=self.times_pressed,width = 0.3,brush="#F89E59")

        #add charts to layout
        self.plot_item_pressure = self.session_chart_layout_widget.addPlot()
        self.plot_item_pressure.setMouseEnabled(x=False,y=False)
        self.plot_item_pressure.addItem(self.avg_chart)
        self.plot_item_pressure.addItem(self.min_chart)
        self.plot_item_pressure.addItem(self.max_chart)
        self.plot_item_pressure.getAxis('bottom').setTicks([self.finger_name_labels])
        self.plot_item_pressure.getAxis('left').setLabel(text="Média de pressão por dedo", units = "KG")
        
        #legend pressure chart session
        self.legendSessionPressure = self.plot_item_pressure.addLegend()
        self.legendSessionPressure.anchor(itemPos=(1,0), parentPos=(1,0), offset=(0,-11))
        self.legendSessionPressure.addItem(self.avg_chart,"Média")
        self.legendSessionPressure.addItem(self.max_chart,"Maxima")
        self.legendSessionPressure.addItem(self.min_chart,"Minima")
        
        #finger use times session
        self.plot_item_times_used = self.session_chart_layout_widget.addPlot()
        self.plot_item_times_used.setMouseEnabled(x=False,y=False)
        self.plot_item_times_used.addItem(self.times_used_chart)
        self.plot_item_times_used.getAxis('bottom').setTicks([self.finger_name_labels])
        self.plot_item_times_used.getAxis('left').setLabel(text="Uso de dedos")
        self.plot_item_times_used.getAxis('left').setStyle(maxTickLevel=0)
        
        #sumarry chart widget
        self.summary_chart_layout_widget =  pg.GraphicsLayoutWidget()
        self.ui.summaryChartContainer.layout().addWidget(self.summary_chart_layout_widget)
        
        #create line charts
        self.little_info_array = [[1,2],[1,2]]
        self.ring_info_array = [[1,2],[1,2]]
        self.middle_info_array = [[1,2],[1,2]]
        self.index_info_array = [[1,2],[1,2]]

        self.plot_item_avg_line = self.summary_chart_layout_widget.addPlot()
        self.plot_item_avg_line.getAxis('bottom').setLabel("Sessão")
        self.plot_item_avg_line.getAxis('left').setLabel("Média de pressão por dedo", units = "KG")
        self.plot_item_avg_line.showGrid(y = True,x = True)
        self.avg_line_legend = self.plot_item_avg_line.addLegend()
        self.avg_line_legend.anchor(itemPos=(1,0), parentPos=(1,0), offset=(0,-10))

        self.plot_item_avg_line.plot(self.little_info_array[0],self.little_info_array[1],pen ='r',name="Mindinho")
        self.plot_item_avg_line.plot(self.ring_info_array[0],self.ring_info_array[1],pen ='g',name="Anelar")
        self.plot_item_avg_line.plot(self.middle_info_array[0],self.middle_info_array[1],pen ='b',name="Meio")
        self.plot_item_avg_line.plot(self.index_info_array[0],self.index_info_array[1],pen ='purple',name="Indicador")
            
        #avg bar chart 
        self.plot_item_avg_bar = self.summary_chart_layout_widget.addPlot()
        self.avg_pressure_summary = [0,0,0,0]
        self.avg_chart_summary = pg.BarGraphItem(x= x_range,height=self.avg_pressure_summary,width = 0.2,brush="#F89E59")
        self.plot_item_avg_bar.addItem(self.avg_chart_summary)
        self.plot_item_avg_bar.getAxis('bottom').setTicks([self.finger_name_labels])
        self.plot_item_avg_bar.getAxis('left').setLabel(text="Média de pressão por dedo", units = "KG")
        self.plot_item_avg_bar.setMouseEnabled(x=False,y=False)
        
        #total times used chart
        self.plot_item_total_uses = self.summary_chart_layout_widget.addPlot()
        self.total_uses_summary = [0,0,0,0]
        self.uses_chart_summary = pg.BarGraphItem(x= x_range,height=self.total_uses_summary,width = 0.2,brush="#F89E59")
        self.plot_item_total_uses.addItem(self.uses_chart_summary)
        self.plot_item_total_uses.getAxis('bottom').setTicks([self.finger_name_labels])
        self.plot_item_total_uses.getAxis('left').setLabel(text="Total de uso por dedo")
        self.plot_item_total_uses.setMouseEnabled(x=False,y=False)
        
    def stop_button_handler(self):
        self.dataCollectorHandler.stop_data_collection()
        self.button_toggler(self.stopListening)
        self.update_session_chart_value()
        
    def comboBox_change_handler(self):
        current_index = self.sessionComboBox.currentData()
        print(f"comboBox_change_handler current_index:{current_index} - latest:{self.latest_session}")
        if (current_index != self.latest_session):
            self.startListening.setEnabled(False)
        else:
            self.startListening.setEnabled(True)
        self.update_session_chart_value()    
    
    def start_button_handler(self):
        self.dataCollectorHandler.start_watch = True
        self.button_toggler(self.startListening)
        
    def new_session_button_handler(self):
        session_id = self.create_session()
        if session_id:
            self.populate_comboBox()

    def assing_user(self,user_index):
        self.current_user = user_index
        self.dataCollectorHandler.current_user_index = self.current_user
        self.populate_comboBox()

    def create_session(self):
        q = f"""insert into session (patient_id, session_date) values (?,datetime(current_timestamp,'localtime')) returning patient_id,id;"""
        res = self.dbHandleClass.execute_single_query(q,[self.current_user])
        if res:
            logger.debug(f"Seção criada para o usuário {res[0][0]}")
            return res[0][1]
        else:
            return False

    def get_summary_chart_value(self):
        qAvg = f"""SELECT 
            s.id AS session_id,
            u.finger,
            AVG(u.pressure) AS avg_pressure
        FROM 
            use_data u
        JOIN 
            session s ON u.session_id = s.id
        JOIN 
            patient p ON s.patient_id = p.id
        WHERE 
            p.id = ? and u.hand = ?
        GROUP BY 
            s.session_date, u.finger
        ORDER BY 
            s.session_date;"""
        qAvgTotal = f"""SELECT 
            u.finger,
            AVG(u.pressure) AS avg_pressure
        FROM 
            use_data u
        JOIN 
            session s ON u.session_id = s.id
        JOIN 
            patient p ON s.patient_id = p.id
        WHERE 
            p.id = ? and u.hand = ?
        GROUP BY 
            u.finger
        ORDER BY 
            u.finger;"""
        qTotalCount = f"""SELECT 
            u.finger,
            COUNT(*) AS total_finger_uses
        FROM 
            use_data u
        JOIN 
            session s ON u.session_id = s.id
        JOIN 
            patient p ON s.patient_id = p.id
        WHERE 
            p.id = ? and u.hand = ?
        GROUP BY 
            u.finger
        ORDER BY 
            u.finger;"""
        qSessionCount = f"select count(id) from session where patient_id = ?;"
        qAvgTimelapse = f"""SELECT
            printf('%02d:%02d:%02d',
                AVG(duration_seconds) / 3600,                
                (AVG(duration_seconds) % 3600) / 60,       
                AVG(duration_seconds) % 60               
            ) AS avg_duration_hhmmss
        FROM (
            SELECT
                CAST((JULIANDAY(MAX(use_data.timestamp)) - JULIANDAY(MIN(use_data.timestamp))) * 86400 AS INTEGER) AS duration_seconds
            FROM
                session
            JOIN
                use_data ON session.id = use_data.session_id
            WHERE
                session.patient_id = ?
            GROUP BY
                session.id
        );"""
        resAvg = self.dbHandleClass.execute_single_query(qAvg,[self.current_user, self.selected_hand])
        resAvgTotal = self.dbHandleClass.execute_single_query(qAvgTotal,[self.current_user, self.selected_hand])
        resTotalCount = self.dbHandleClass.execute_single_query(qTotalCount,[self.current_user, self.selected_hand])
        resSessionCount = self.dbHandleClass.execute_single_query(qSessionCount,[self.current_user])
        resAvgTimelapse = self.dbHandleClass.execute_single_query(qAvgTimelapse,[self.current_user])
        
        if resAvg and resAvgTotal and resTotalCount and resSessionCount and resAvgTimelapse:
            # print(f"resAvg:{resAvg}\nresAvgTotal:{resAvgTotal}\nresSessionCount:{resSessionCount}\nresAvgTimelapse:{resAvgTimelapse}")
            index_array = [[],[]]
            little_array = [[],[]]
            middle_array = [[],[]]
            ring_array = [[],[]]
            total_count = [False,False,False,False]
            avg_total = [False,False,False,False]
            sessionCount = False
            avgTimelapse = False
            
            for i,t in enumerate(resAvg):
                if t[1] == "index":#i,t[2]/10
                    index_array[0].append(i)
                    index_array[1].append(t[2]/10)
                if t[1] == "little":
                    little_array[0].append(i)
                    little_array[1].append(t[2]/10)
                if t[1] == "middle":
                    middle_array[0].append(i)
                    middle_array[1].append(t[2]/10)
                if t[1] == "ring":
                    ring_array[0].append(i)
                    ring_array[1].append(t[2]/10)

            for t in resAvgTotal:
                if t[0] == 'index':
                    avg_total[3] = t[1]/10
                elif t[0] == 'little':
                    avg_total[0] = t[1]/10
                elif t[0] == 'middle':
                    avg_total[2] = t[1]/10
                elif t[0] == 'ring':
                    avg_total[1] = t[1]/10
            for t in resTotalCount:
                if t[0] == 'index':
                    total_count[3] = t[1]
                elif t[0] == 'little':
                    total_count[0] = t[1]
                elif t[0] == 'middle':
                    total_count[2] = t[1]
                elif t[0] == 'ring':
                    total_count[1] = t[1]
            sessionCount = resSessionCount[0][0]
            avgTimelapse = resAvgTimelapse[0][0]

            return index_array, little_array, middle_array, ring_array, total_count, avg_total, sessionCount, avgTimelapse
        
        else:
            return False,False,False,False,False,False,False,False          
                
    def update_summary_charts(self):
        index_array, little_array, middle_array, ring_array, total_count, avg_total, sessionCount, avgTimelapse = self.get_summary_chart_value()
        if index_array and little_array and middle_array and ring_array and total_count and avg_total and sessionCount and avgTimelapse:
            self.little_info_array = little_array
            self.ring_info_array = ring_array
            self.middle_info_array = middle_array
            self.index_info_array = index_array
            self.avg_pressure_summary = avg_total
            self.total_uses_summary = total_count
            self.sessionCount = sessionCount
            self.avgTimelapse = avgTimelapse
        else:
            self.little_info_array = [[1,2],[1,1]]
            self.ring_info_array = [[1,2],[1,1]]
            self.middle_info_array = [[1,2],[1,1]]
            self.index_info_array = [[1,2],[1,1]]
            self.avg_pressure_summary = [0,0,0,0]
            self.total_uses_summary = [0,0,0,0]
            self.sessionCount = "0"
            self.avgTimelapse = "00:00:00"
            
        self.avg_chart_summary.setOpts(height = self.avg_pressure_summary) 
        self.uses_chart_summary.setOpts(height = self.total_uses_summary)
        self.plot_item_avg_line.clear()
        self.plot_item_avg_line.plot(self.little_info_array[0],self.little_info_array[1],pen ='r',name="Mindinho")
        self.plot_item_avg_line.plot(self.ring_info_array[0],self.ring_info_array[1],pen ='g',name="Anelar")
        self.plot_item_avg_line.plot(self.middle_info_array[0],self.middle_info_array[1],pen ='b',name="Meio")
        self.plot_item_avg_line.plot(self.index_info_array[0],self.index_info_array[1],pen ='purple',name="Indicador")
        self.countSession.setText(str(self.sessionCount))
        self.avgSessionTime.setText(self.avgTimelapse)
        
    
    def get_session_chart_value(self):
        self.sessionComboBox.setEnabled(False)
        qCount = f"select finger, COUNT(*) AS count from use_data where session_id = ? and hand = ? GROUP BY finger;"
        qPres = f"SELECT finger, MAX(pressure) AS max_pressure, MIN(pressure) AS min_pressure, AVG(pressure) AS avg_pressure FROM use_data where session_id = ? and hand = ? group by finger;"
        qTimelapse = f"""SELECT 
            session_id,
            printf('%02d:%02d:%02d',
                duration_seconds / 3600,
                (duration_seconds % 3600) / 60,
                duration_seconds % 60
            ) AS duration_hms
        FROM (
            SELECT 
                session_id,
                CAST((strftime('%s', MAX(timestamp)) - strftime('%s', MIN(timestamp))) AS INTEGER) AS duration_seconds
            FROM use_data
            where session_id = ? and hand = ?
        );"""
        presRes = self.dbHandleClass.execute_single_query(qPres,[self.sessionComboBox.currentData(),self.selected_hand])
        countRes = self.dbHandleClass.execute_single_query(qCount,[self.sessionComboBox.currentData(),self.selected_hand])
        timelapseRes = self.dbHandleClass.execute_single_query(qTimelapse,[self.sessionComboBox.currentData(),self.selected_hand])
        if presRes and countRes and timelapseRes:
            max_press_array = [None,None,None,None]
            min_press_array = [None,None,None,None]
            avg_press_array = [None,None,None,None]
            finger_count_array = [None,None,None,None]
            for t in presRes:
                if t[0] == 'index':
                    max_press_array[3] = t[1]/10
                    min_press_array[3] = t[2]/10
                    avg_press_array[3] = t[3]/10
                elif t[0] == 'little':
                    max_press_array[0] = t[1]/10
                    min_press_array[0] = t[2]/10
                    avg_press_array[0] = t[3]/10
                elif t[0] == 'middle':
                    max_press_array[2] = t[1]/10
                    min_press_array[2] = t[2]/10
                    avg_press_array[2] = t[3]/10
                elif t[0] == 'ring':
                    max_press_array[1] = t[1]/10
                    min_press_array[1] = t[2]/10
                    avg_press_array[1] = t[3]/10
            for t in countRes:
                if t[0] == 'index':
                    finger_count_array[3] = t[1]
                elif t[0] == 'little':
                    finger_count_array[0] = t[1]
                elif t[0] == 'middle':
                    finger_count_array[2] = t[1]
                elif t[0] == 'ring':
                    finger_count_array[1] = t[1]

            self.sessionComboBox.setEnabled(True)
            return  max_press_array, min_press_array, avg_press_array, finger_count_array, timelapseRes

        else:
            self.sessionComboBox.setEnabled(True)
            return False,False,False,False,False

    def update_session_chart_value(self):
        max_press_array, min_press_array, avg_press_array, finger_count_array, timelapse = self.get_session_chart_value()
        if max_press_array and min_press_array and avg_press_array and finger_count_array and timelapse:
            self.max_pressure = max_press_array
            self.avg_pressure = avg_press_array
            self.min_pressure = min_press_array
            self.times_pressed = finger_count_array
            self.timelapse = timelapse[0][1]
        else:
            self.max_pressure = [0,0,0,0]
            self.avg_pressure = [0,0,0,0]
            self.times_pressed = [0,0,0,0]
            self.min_pressure = [0,0,0,0]
            self.timelapse = "00:00:00"
        self.min_chart.setOpts(height = self.min_pressure)
        self.avg_chart.setOpts(height = self.avg_pressure)
        self.max_chart.setOpts(height = self.max_pressure) 
        self.times_used_chart.setOpts(height = self.times_pressed)
        self.timelapseLabel.setText(self.timelapse)
        
    def hand_selector(self):
        if self.sender().objectName() == "rightHandButton":
            self.selected_hand = 0
            self.dataCollectorHandler.selected_hand = 0
        else:
            self.selected_hand = 1
            self.dataCollectorHandler.selected_hand = 1
        if self.statsTabWidget.currentIndex() == 0:
            self.update_session_chart_value()
        else:
            self.update_summary_charts()
            
                    
    def button_toggler(self, clicked_button):
        for button in self.ui.buttonsContainer.findChildren(QPushButton):
            if button != clicked_button:
                button.setEnabled(True)
            else:
                clicked_button.setEnabled(False)
        self.sessionComboBox.setEnabled(not self.sessionComboBox.isEnabled())
        if self.startListening.isEnabled():
            self.sideMenuDisableSignal.emit(True)
        else:
            self.sideMenuDisableSignal.emit(False)                
            
    def get_sessions(self):
        qSessions = f"select * from session where patient_id = ?;"
        resSessions = self.dbHandleClass.execute_single_query(qSessions,[self.current_user])
        if resSessions:
            return resSessions
    
    def populate_comboBox(self):
        self.sessionComboBox.clear()
        sessions = self.get_sessions()
        if sessions:
            for s in sessions:
                text = str(s[2])
                latest_session = s[0]
                self.assing_latest_session(latest_session)
                self.sessionComboBox.addItem(text[:len(text)-3],s[0])
            self.sessionComboBox.setCurrentIndex(self.sessionComboBox.count()-1)
            
    def assing_latest_session(self,latest_session):
        print(f"assing_latest_session:{latest_session}")
        self.latest_session = latest_session
        self.dataCollectorHandler.current_session_index = latest_session
            