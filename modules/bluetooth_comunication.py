import asyncio
import PySide6.QtBluetooth
from PySide6.QtBluetooth import QBluetoothDeviceInfo, QBluetoothLocalDevice, QBluetoothServiceDiscoveryAgent, QBluetoothServiceInfo, QBluetoothSocket
from PySide6.QtCore import QObject, Signal, QIODeviceBase
import socket
from modules.process_class import ProcessRunnerClass

target_device_name = "ESP32"
target_service_device_name = "ESP32SPP"
target_service = "RFCOMM"

class BluetoothCommClass(QObject):
    complete = Signal(list)
    errorMessage = Signal(str)
    pairComplete = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.runner = ProcessRunnerClass()
        self.local_device = QBluetoothLocalDevice()
        # self.discovery_agent = PySide6.QtBluetooth.QBluetoothDeviceDiscoveryAgent()
        # self.devices = []
        # self.desired_device = PySide6.QtBluetooth

        self.service_discovery = QBluetoothServiceDiscoveryAgent()
        self.services = []
        self.desired_service = QBluetoothServiceInfo
        self.bt_socket = QBluetoothSocket(QBluetoothServiceInfo.RfcommProtocol)

        # self.discovery_agent.deviceDiscovered.connect(self.device_discovered)
        # self.discovery_agent.finished.connect(self.end_discovery)
        # self.discovery_agent.errorOccurred.connect(self.discovery_error)
        
        self.service_discovery.serviceDiscovered.connect(self.on_service_found)
        self.service_discovery.finished.connect(self.end_discovery)
        self.service_discovery.errorOccurred.connect(self.discovery_error)
        
        self.runner.processFinished.connect(self.pair_finish)
        
    def device_discovered(self, device: QBluetoothDeviceInfo):
        self.devices.append(device)

    def on_service_found(self, service: QBluetoothServiceInfo):
        self.services.append(service)
        if("rfcomm" in str(service.socketProtocol()).lower()):#!mudar isso para if name = ESP32SPP
            self.desired_service = service
            
    async def start_discovery(self):
        if not self.local_device:
            self.errorMessage.emit("Adaptador Bluetooth não encontrado")

        device_mode = self.local_device.hostMode() 
        
        if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
            self.errorMessage.emit("Adaptador Bluetooth esta desligado")
        else:
            # self.devices.clear()
            self.services.clear()
            # self.discovery_agent.start()
            self.service_discovery.start()
            
    def end_discovery(self):
        self.complete.emit(self.services)
        self.get_device_from_list()
        
    def discovery_error(self, error):
        print(str(error))

    async def toggle_bluetooth(self):
        if not self.local_device:
            return "Adaptador Bluetooth não encontrado"

        device_mode = self.local_device.hostMode() 
        
        if device_mode == QBluetoothLocalDevice.HostMode.HostConnectable:
            self.local_device.setHostMode(QBluetoothLocalDevice.HostMode.HostPoweredOff)
            return "Adaptador Bluetooth desligado"
            
        elif device_mode == QBluetoothLocalDevice.HostMode.HostPoweredOff:
            self.local_device.setHostMode(QBluetoothLocalDevice.HostMode.HostConnectable)
            return "Adaptador Bluetooth ligado"
         
    def start_discovery_task_handler(self):
        asyncio.create_task(self.start_discovery())     
         
    def pair_device(self):
        self.runner.run()
        
    def pair_finish(self):
        self.pairComplete.emit("Processo quase finalizado")

    # def get_device_from_list(self):
    #     self.desired_device = QBluetoothDeviceInfo()
    #     for device in self.devices:
    #         if device.name() == target_device_name:
    #             self.desired_device = device
    #             break

    #     if not self.desired_device:
    #         self.errorMessage.emit("Dispositivo não encontrado")
    #         return

