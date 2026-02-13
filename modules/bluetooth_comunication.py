from PySide6.QtBluetooth import QBluetoothLocalDevice, QBluetoothServiceDiscoveryAgent, QBluetoothServiceInfo, QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo
from PySide6.QtCore import QObject, Signal

from modules.process_class import ProcessRunnerClass
from modules.log_class import logger

target_device_name = "ESP32"#needs to be upper case for btpair, else use lower()
target_service_device_name = "esp32spp"
target_service = "rfcomm"

class BluetoothCommClass(QObject):
    taskFinished = Signal(object)#generic error and task finished signals, used in every function
    taskError = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.on_result = None
        self.on_error = None

        self.runner = ProcessRunnerClass()
        
        #local bluetooth device setup
        self.local_device = QBluetoothLocalDevice()

        #service discovery setup for esp32spp
        self.service_discovery = QBluetoothServiceDiscoveryAgent()
        self.desired_service = None
        self.service_discovery.serviceDiscovered.connect(self.on_service_found)
        self.service_discovery.finished.connect(lambda: self.emit_error("Dispositivo não encontrado") if not self.desired_service else None)
        self.service_discovery.canceled.connect(self.end_discovery)
        self.service_discovery.errorOccurred.connect(self.discovery_error)

        #device discovery setup for esp32 hid device
        self.discovery_agent = QBluetoothDeviceDiscoveryAgent()
        self.desired_device = None
        self.discovery_agent.deviceDiscovered.connect(self.on_hid_device_found)
        self.discovery_agent.errorOccurred.connect(self.hid_discovery_error)
        self.discovery_agent.finished.connect(lambda: self.emit_error("Dispositivo não encontrado"))
        self.discovery_agent.canceled.connect(self.hid_discovery_end)
        
        #local device pairing event finished handler 
        self.local_device.pairingFinished.connect(self.hid_pairEvent_finish)

        #process class run finish signal
        self.runner.processFinished.connect(self.process_run_finish)
        
        self.check_current_paired()
    
    ############################ discovery functions ###############################    
    #tries to get the desired service
    def on_service_found(self, service: QBluetoothServiceInfo):
        if(target_service_device_name in str(service.serviceName()).lower()):
            self.desired_service = service
            self.service_discovery.stop()
            logger.debug(f"Serviço encontrado, finalizando processo")
            
    def start_discovery(self):
        try:
            if not self.local_device:
                self.emit_error("Adaptador bluetooth não encontrado")

            device_mode = self.local_device.hostMode() 
            
            if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
                self.emit_error("Adaptador Bluetooth esta desligado")
            else:
                logger.debug("Começar descoberta por serviços")
                self.desired_service = None
                self.service_discovery.start()
        except Exception as e:
            logger.error(f"Erro ao começar descoberta de serviços bluetooth\nErr: {e}")
            
    def end_discovery(self):
        if self.desired_service:
            addr = self.desired_service.device().address().toString().replace(":","").lower()
            self.emit_result(addr)
            logger.debug(f"retornando mac: {addr}")
        
    def discovery_error(self, error):
        self.emit_error("Erro na descoberta de serviços bluetooth")
        logger.error("Erro na descoberta de serviços bluetooth\nErr: " + error)

    ############################ toggle functions ###############################    
    def toggle_bluetooth(self):
        try:
            if not self.local_device:
                self.emit_error("Adaptador Bluetooth não encontrado")

            device_mode = self.local_device.hostMode() 
            
            if device_mode == QBluetoothLocalDevice.HostMode.HostConnectable:
                self.local_device.setHostMode(QBluetoothLocalDevice.HostMode.HostPoweredOff)
                self.emit_result("Adaptador bluetooth desligado")
                
            elif device_mode == QBluetoothLocalDevice.HostMode.HostPoweredOff:
                self.local_device.setHostMode(QBluetoothLocalDevice.HostMode.HostConnectable)
                self.emit_result("Adaptador bluetooth ligado")

            logger.debug("Sucesso em alterar o estado do adaptador bluetooth")
        except Exception as e:
            logger.error("Erro ao alterar o estado do adptador bluetooth\nErr: " + e)
         
         
    ############################ pair/unpair functions ###############################    
    def pair_device(self):
        if not self.local_device:
            self.emit_error("Adaptador Bluetooth não encontrado")
            return
        
        device_mode = self.local_device.hostMode() 
        
        if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
            self.emit_error("Adaptador Bluetooth esta desligado")
        else:
            argumentList = ['-p','-n',f'{target_device_name}']
            argStr = ["_internal/resources/bin/btpair.exe",argumentList]
            self.runner.run(argStr=argStr)
        
    def process_run_finish(self, object):
        self.emit_result(object)
        logger.debug(f"process_run_finish:{object}")

    def unpair_device(self):
        if not self.local_device:
            self.emit_error("Adaptador Bluetooth não encontrado")
            return
        
        device_mode = self.local_device.hostMode() 
        
        if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
            self.emit_error("Adaptador Bluetooth esta desligado")
        else:
            argumentList = ['-u','-n',f'{target_device_name}']
            argStr = ["_internal/resources/bin/btpair.exe",argumentList]
            self.runner.run(argStr=argStr)
            
            
    ############################ hid functions ###############################           
    def hid_device_discovery(self):
        try:
            if not self.local_device:
                self.emit_error("Adaptador Bluetooth não encontrado")

            device_mode = self.local_device.hostMode() 

            if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
                self.emit_error("Adaptador Bluetooth esta desligado")
            else:
                logger.debug("Começar descoberta por dispositvos")
                self.desired_service = None
                self.discovery_agent.start()
        except Exception as e:
            logger.error(f"Erro ao iniciar a descoberta de dispositivos: {e}")
        
    def on_hid_device_found(self, device = QBluetoothDeviceInfo):
        if device.name().lower() == target_device_name.lower():
            self.desired_device = device
            self.discovery_agent.stop()
        
    def hid_discovery_end(self):
        if self.desired_device:
            logger.debug(f"dispositivo encontrado: {self.desired_device.name()}")
            self.emit_result(True)
        else:
            self.emit_error("Dispositivo não encontrado")

    def hid_discovery_error(self, err):
        self.emit_error("Erro durante a descoberta de dispositivos bluetooth")
        logger.error(f"Erro durante device_discovery: {err}")

    def hid_device_pair(self):
        if self.desired_device:
            self.local_device.requestPairing(self.desired_device.address(), self.local_device.Pairing.Paired)
        else:
            self.emit_error("Dispositivo não encontrado para o paremaneto")

    def hid_device_unpair(self):
        device_mode = self.local_device.hostMode() 
        
        if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
            self.emit_error("Adaptador Bluetooth esta desligado")
            return
        
        if self.desired_device:
            self.local_device.requestPairing(self.desired_device.address(), self.local_device.Pairing.Unpaired)
        else:
            self.emit_error("Dispositivo não encontrado")
            
    #returns the proper message for when the device has been paired or unpaired
    def hid_pairEvent_finish(self):
        if self.local_device.pairingStatus(self.desired_device.address()) == self.local_device.Pairing.Paired:
            self.emit_result(f"Dispositivo HID {self.desired_device.name()} emparelhado")
        else:
            self.emit_result(f"Dispositivo HID {self.desired_device.name()} desemparelhado")
            self.desired_device = None
        
    #check for currently paired device
    def check_current_paired(self):
        device_mode = self.local_device.hostMode() 
        if device_mode == QBluetoothLocalDevice.HostMode.HostPoweredOff:
            self.local_device.setHostMode(QBluetoothLocalDevice.HostMode.HostConnectable)
            self.emit_result("Adaptador bluetooth ligado")
        self.discovery_agent.start()
        
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
