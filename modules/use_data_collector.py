from PySide6.QtCore import QObject, QTimer
from modules.log_class import logger

class DataCollectorClass(QObject):
    def __init__(self, dbHandleClass, SerialCommClass,logModel):
        super().__init__()
        
        #variable setup
        self._start_watch = False
        self.message_buffer = [[],[],[],[]]
        self.current_user_index = None
        self.current_session_index = None
        self.selected_hand = 0
        
        self.logModel = logModel
        
        #module setup
        self.timer = QTimer()
        self.dbHandleClass = dbHandleClass
        self.serialHandleClass = SerialCommClass

        #connections setup
        self.timer.timeout.connect(self.timeout_handle)
    
    #value watcher setup
    #when atributed will check value
    #true = start
    @property
    def start_watch(self):
        return self._start_watch
    
    @start_watch.setter
    def start_watch(self,val):
        self._start_watch = val
        self.start_checker()
        
    def start_checker(self):
        if self._start_watch != False:
            self.start_data_collection(2500)
            self.serialHandleClass.swap_message_listner(1)
            self.serialHandleClass.mesReceivedSignal.connect(self.message_received_handler)
        else:
            self.timer.stop()
            self.serialHandleClass.swap_message_listner(0)
            self.serialHandleClass.mesReceivedSignal.disconnect(self.message_received_handler)

    def generate_query(self,index,middle,ring,little):
        q = "insert into user_data (session_id,finger,pressure,hand) values (?,?,?,?);"
        if self.current_session_index:
            data = []
            #4 same size arrays with x items
            for i in range(len(index)):
                if int(index[i]) > 0:
                    data.append(({self.current_session_index}, 'index', int(index[i]), self.selected_hand))
                if int(middle[i]) > 0:
                    data.append(({self.current_session_index}, 'middle', int(middle[i]), self.selected_hand))
                if int(ring[i]) > 0:
                    data.append(({self.current_session_index}, 'ring', int(ring[i]), self.selected_hand))
                if int(little[i]) > 0:
                    data.append(({self.current_session_index}, 'little', int(little[i]), self.selected_hand))
            return q,data
        else:
            logger.error(f"Não pode gerar um query para estatisticas de uso, paciente não selecionado")
            
    def start_data_collection(self,ms):
        self.timer.start(ms)
        
    # start the process to send messages to the database
    def timeout_handle(self):
        if self.message_buffer:
            index_array = self.message_buffer[0]
            middle_array = self.message_buffer[1]
            ring_array = self.message_buffer[2]
            little_array = self.message_buffer[3]
            q,data = self.generate_query(index_array,middle_array,ring_array,little_array)
            if q != "":
                self.insert_data(q,data)
                self.message_buffer = [[],[],[],[]]
        else:
            logger.debug(f"Message buffer vazio: {self.message_buffer}")

    def insert_data(self,q,data):
        res = self.dbHandleClass.execute_multiple_queries(q,data)
        if res:
            logger.debug(f"estatisticas de uso inseridos na tabela: {res[0][0]}")
        
    
    def stop_data_collection(self):
        self.start_watch = False

    #appends messages on the buffer
    #*I000000000000 format every time
    #splits message on each array
    #each message has 3 digits
    def message_received_handler(self,message):
        self.logModel.append_log(message)
        for m in message:
            messages = [m[0:3],m[3:6],m[6:9],m[9:]] 
            for i in enumerate(messages):
                self.message_buffer[i].append(messages[i])
                logger.debug(f"Mensagem adicionada ao buffer no indice {i}: {messages[i]}")
                logger.debug(f"Pressões recebidas - Indicador/Polegar: {messages[0]/10} KG - Médio: {messages[1]/10} KG - Anelar: {messages[2]/10} KG - Mínimo: {messages[3]/10} KG")
                



            
