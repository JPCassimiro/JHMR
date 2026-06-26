from PySide6.QtCore import QObject, QByteArray, Signal
from PySide6.QtTest import QSignalSpy

from modules.use_data_collector import DataCollectorClass
from modules.db_functions import DbClass
from modules.bluetooth_serial_communication import BtSerialComm

import pytestqt
from unittest.mock import Mock 

class FakeLogClass(QObject):
    
    def append_log(self,message):
        print(message)

class FakeDb(DbClass):
    
    def get_db_name(self):
        return "test_db"

class FakeSocket(QObject):
    
    readyRead = Signal()
    
    def __init__(self):
        super().__init__()

        self.data = None

    def readAll(self):
        if self.data:
            return QByteArray(self.data)
    
    def isOpen(self):
        return True

class TestUseDataCollector:
    
    def setup_method(self, method):
        self.fake_socket = FakeSocket()
        self.bt_class = BtSerialComm()
        self.bt_class.bt_socket = self.fake_socket
        self.db_class = FakeDb()
        self.fake_log_model = FakeLogClass()
        self.data_collector_class = DataCollectorClass(self.db_class, self.bt_class, logModel = self.fake_log_model)
        for s in ["delete from therapist;","delete from patient;","delete from session;","delete from use_data;","delete from bindings;","""insert into patient (id, name, details, image_path) values (1, 'paciente padrão', 'valor padrão', '_internal/resources/imgs/placeholder_profile.png');""","""insert into therapist (id, name, details, image_path) values (1, 'terapeuta padrão', 'valor padrão', '_internal/resources/imgs/placeholder_profile.png');"""]:
            self.db_class.execute_single_query(s)

    def test_generate_query_success(self,qtbot):
        self.data_collector_class.current_user_index = 0
        self.data_collector_class.current_session_index = 0
        self.data_collector_class.selected_hand = 0
        
        res1, res2 = self.data_collector_class.generate_query(["000","100"],["200","000"],["000","300"],["400","000"])

        assert res1 == "insert into use_data (session_id,finger,pressure,hand) values (?,?,?,?);"
        assert res2 == [(0,'index',400,0),(0,'ring',200,0),(0,'middle',300,0),(0,'little',100,0)]

    def test_timeout_handle_success(self):

        generate_query_mock = Mock()
        insert_data_mock = Mock()

        self.data_collector_class.generate_query = generate_query_mock
        self.data_collector_class.insert_data = insert_data_mock

        self.data_collector_class.timeout_handle()

        assert generate_query_mock.call_count == 0
        assert insert_data_mock.call_count == 0

        self.data_collector_class.message_buffer = [["100"],["200"],["300"],["400"]]

        self.data_collector_class.timeout_handle()

        generate_query_mock.assert_called_once()

    def test_message_recieved_handler(self,qtbot):
        self.data_collector_class.message_received_handler(["*I000100200300"])

        assert self.data_collector_class.message_buffer[0] == ["000"]
        assert self.data_collector_class.message_buffer[1] == ["100"]
        assert self.data_collector_class.message_buffer[2] == ["200"]
        assert self.data_collector_class.message_buffer[3] == ["300"]