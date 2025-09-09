import PySide6.QtBluetooth
from PySide6.QtBluetooth import QBluetoothDeviceInfo, QBluetoothLocalDevice, QBluetoothServiceDiscoveryAgent, QBluetoothServiceInfo, QBluetoothSocket
from PySide6.QtCore import QObject, Signal
from modules.process_class import ProcessRunnerClass
from modules.log_class import logger

target_device_name = "ESP32"
target_service_device_name = "ESP32SPP"
target_service = "RFCOMM"

class BluetoothCommClass(QObject):
    taskFinished = Signal(object)
    taskError = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.on_result = None
        self.on_error = None

        self.runner = ProcessRunnerClass()
        
        #local bluetooth device setup
        self.local_device = QBluetoothLocalDevice()
        self.discovery_agent = PySide6.QtBluetooth.QBluetoothDeviceDiscoveryAgent()
        self.devices = []
        self.desired_device = PySide6.QtBluetooth

        #service discovery setup
        self.service_discovery = QBluetoothServiceDiscoveryAgent()
        self.services = []
        self.desired_service = QBluetoothServiceInfo

        self.discovery_agent.deviceDiscovered.connect(self.device_discovered)
        self.discovery_agent.finished.connect(self.end_discovery)
        self.discovery_agent.errorOccurred.connect(self.discovery_error)
        
        self.service_discovery.serviceDiscovered.connect(self.on_service_found)
        self.service_discovery.finished.connect(self.end_discovery)
        self.service_discovery.errorOccurred.connect(self.discovery_error)
        
        self.runner.processFinished.connect(self.process_run_finish)
        
    def device_discovered(self, device: QBluetoothDeviceInfo):
        self.devices.append(device)

    #tries to get the desired service
    def on_service_found(self, service: QBluetoothServiceInfo):
        self.services.append(service)
        if("rfcomm" in str(service.socketProtocol()).lower()):#!mudar isso para if name = ESP32SPP
            self.desired_service = service
            
    def start_discovery(self):
        try:
            if not self.local_device:
                self.emit_error("Adaptador bluetooth não encontrado")

            device_mode = self.local_device.hostMode() 
            
            if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
                self.emit_error("Adaptador Bluetooth esta desligado")
            else:
                logger.debug("Começar descoberta por dispositvos")
                self.devices.clear()
                self.services.clear()
                self.discovery_agent.start()
                # self.service_discovery.start()
        except Exception as e:
            logger.error(f"Erro ao começar descorberta por dispositivos e serviços bluetooth\nErr: {e}")
            
    def end_discovery(self):
        self.emit_result(self.devices)
        # self.get_device_from_list()
        
    def discovery_error(self, error):
        self.emit_error("Erro na descorberta por dispositivos bluetooth")
        logger.error("Erro na descorberta por dispositivos bluetooth\nErr: " + error)

    def toggle_bluetooth(self):
        try:
            if not self.local_device:
                self.emit_error("Adaptador Bluetooth não encontrado")

            device_mode = self.local_device.hostMode() 
            
            if device_mode == QBluetoothLocalDevice.HostMode.HostConnectable:
                self.local_device.setHostMode(QBluetoothLocalDevice.HostMode.HostPoweredOff)
                self.emit_result("Adaptador bluetooth ligado")
                
            elif device_mode == QBluetoothLocalDevice.HostMode.HostPoweredOff:
                self.local_device.setHostMode(QBluetoothLocalDevice.HostMode.HostConnectable)
                self.emit_result("Adaptador bluetooth ligado")

            logger.debug("Sucesso em alterar o estado do adaptador bluetooth")
        except Exception as e:
            logger.error("Erro ao alterar o estado do adptador bluetooth\nErr: " + e)
         
    def pair_device(self):
        if not self.local_device:
            self.emit_error("Adaptador Bluetooth não encontrado")
            return
        
        device_mode = self.local_device.hostMode() 
        
        if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
            self.emit_error("Adaptador Bluetooth esta desligado")
        else:
            # argStr = "./modules/batch_files/pair_device.bat"
            argumentList = ['-p','-n',f'{target_device_name}']
            argStr = ["_internal/resources/bin/btpair.exe",argumentList]
            self.runner.run(argStr=argStr)
        
    def process_run_finish(self):
        self.emit_result("Processo finalizado")

    def unpair_device(self):
        if not self.local_device:
            self.emit_error("Adaptador Bluetooth não encontrado")
            return
        
        device_mode = self.local_device.hostMode() 
        
        if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
            self.emit_error("Adaptador Bluetooth esta desligado")
        else:
            argumentList = ['-u','-n',f'{target_device_name}']
            argStr = ["_internal/resources/bin/btpair.exe",argumentList]#'./bin/btpair.exe' production
            #'_internal/resources/bin/btpair.exe' deploy
            self.runner.run(argStr=argStr)

    #sets the functions that will be used as callback on the model class
    def set_callback(self, on_result, on_error):
        self.on_error = on_error
        self.on_result = on_result
    
    #emits the result as long as there is a callback function
    def emit_result(self, result):
        if self.on_result:
            self.on_result(result)
        self.taskFinished.emit(result)
    
    #same as above
    def emit_error(self, error):
        if self.on_error:
            self.on_error(error)
        self.taskError.emit(error)

    # def get_device_from_list(self):
    #     self.desired_device = QBluetoothDeviceInfo()
    #     for device in self.devices:
    #         if device.name() == target_device_name:
    #             self.desired_device = device
    #             break

    #     if not self.desired_device:
    #         self.emit_error("Dispositivo não encontrado")
    #         return

