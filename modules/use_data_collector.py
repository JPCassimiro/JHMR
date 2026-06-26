from PySide6.QtCore import QObject, QTimer, Signal

from shared_ui_modules.modules.log_class import logger
from shared_ui_modules.modules.use_data_colector import SharedDataCollectorClass

class DataCollectorClass(SharedDataCollectorClass):
    errorOcurred = Signal(bool)

    def __init__(self, dbHandleClass, btSerialHandle, logModel):
        super().__init__(dbHandleClass, btSerialHandle, logModel)
        
        #variable setup
        self._start_watch = False
        self.message_buffer = [[],[],[],[]]
        self.current_user_index = None
        self.current_session_index = None
        self.selected_hand = 0
        
        #module setup
        self.timer = QTimer()

        #connections setup
        self.timer.timeout.connect(self.timeout_handle)
        
        self.initilize_module()

    def get_message_buffer(self):
        return [[],[],[],[]]

    def generate_query(self,little,ring,middle,index):
        try:
            if self.current_session_index is None:
                raise Exception(f"null current_session: {self.current_session_index}")

            q = "insert into use_data (session_id,finger,pressure,hand) values (?,?,?,?);"
            data = []
            #4 same size arrays with x items
            for i,v in enumerate(index):
                if int(index[i]) > 0:
                    data.append((self.current_session_index, 'index', int(index[i]), self.selected_hand))
                if int(middle[i]) > 0:
                    data.append((self.current_session_index, 'middle', int(middle[i]), self.selected_hand))
                if int(ring[i]) > 0:
                    data.append((self.current_session_index, 'ring', int(ring[i]), self.selected_hand))
                if int(little[i]) > 0:
                    data.append((self.current_session_index, 'little', int(little[i]), self.selected_hand))
            return q,data
        except Exception as e:
            logger.error(f"DataCollectorClass generate_query error: {e}")
            self.message_buffer = [[],[],[],[]]
            self.errorOcurred.emit(True)
        
    # start the process to send messages to the database
    def timeout_handle(self):
        try:
            if any(self.message_buffer):
                little_array = self.message_buffer[0]
                ring_array = self.message_buffer[1]
                middle_array = self.message_buffer[2]
                index_array = self.message_buffer[3]
                q,data = self.generate_query(little_array,ring_array,middle_array,index_array)
                if q != "" and data:
                    self.insert_data(q,data)
                    self.message_buffer = [[],[],[],[]]
            else:
                logger.debug(f"Message buffer vazio: {self.message_buffer}")
        except Exception as e:
            logger.error(f"DataCollectorClass timeout_handle error: {e}")
            self.message_buffer = [[],[],[],[]]
            self.errorOcurred.emit(True)

    #appends messages on the buffer
    #*I000000000000 format every time
    #splits message on each array
    #each message has 3 digits
    def message_received_handler(self,message):
        try:
            logger.debug(f"DataCollectorClass message_received_handler message:{message}")
            self.logModel.append_log(message)
            for m in message:
                messages = [m[2:5],m[5:8],m[8:11],m[11:]] 
                for i, msg in enumerate(messages):
                    self.message_buffer[i].append(messages[i])
                    logger.debug(f"Mensagem adicionada ao buffer no indice {i}: {messages[i]}")
                    logger.debug(f"Pressões recebidas - Mínimo: {int(messages[0])/10} - Anelar: {int(messages[1])/10} KG - Médio: {int(messages[2])/10} KG - KG Indicador/Polegar: {int(messages[3])/10} KG")
        except Exception as e:
            logger.error(f"DataCollectorClass message_received_handler error: {e}")