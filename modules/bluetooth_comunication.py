from PySide6.QtBluetooth import (QBluetoothLocalDevice, QBluetoothServiceDiscoveryAgent, QBluetoothServiceInfo,
                                 QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo, QLowEnergyController)
from PySide6.QtCore import QObject, Signal

from modules.process_class import ProcessRunnerClass
from modules.log_class import logger

target_device_name = "ESP32"#needs to be upper case for btpair, else use lower()
target_service_device_name = "esp32spp"
target_service = "rfcomm"

class BluetoothCommClass(QObject):
    taskFinished = Signal(object)#generic error and task finished signals, used in every function
    taskError = Signal(str)
    
    discoveryEnd = Signal(object)
        
    def __init__(self, parent=None):
        super().__init__(parent)

        self.on_result = None
        self.on_error = None

        self.runner = ProcessRunnerClass()
        
        #local bluetooth device setup
        self.local_device = QBluetoothLocalDevice()
        

        #service discovery setup for esp32spp
        self.service_discovery = QBluetoothServiceDiscoveryAgent()
        self.service_discovery.serviceDiscovered.connect(self.on_service_found)
        self.service_discovery.finished.connect(self.end_discovery)
        self.service_discovery.errorOccurred.connect(self.discovery_error)
        self.spp_service_list = []

        #device discovery setup for esp32 hid device
        self.discovery_agent = QBluetoothDeviceDiscoveryAgent()
        self.discovery_agent.deviceDiscovered.connect(self.on_hid_device_found)
        self.discovery_agent.errorOccurred.connect(self.hid_discovery_error)
        self.discovery_agent.finished.connect(self.hid_discovery_end)
        # self.discovery_agent.deviceUpdated.connect(self.updated_device_handle)
        self.hid_device_list = []

        #currently paired device
        self.paired_device = None
        
        #powered on device list
        self.powered_device_list = []

        #local device pairing event finished handler 
        self.local_device.pairingFinished.connect(self.hid_pairEvent_finish)
        self.local_device.errorOccurred.connect(self.local_device_error)

        #process class run finish signal
        self.runner.processFinished.connect(self.process_run_finish)
        
        self.check_current_paired()
        
    def updated_device_handle(self,device,fields):
        logger.debug(f"updated_device_handle device:{device} - fields:{device.rssi()}")
        
    ############################ discovery functions ###############################    
    #appens bt serial services from available joysticks on a list
    def on_service_found(self, service: QBluetoothServiceInfo):
        print(f"on_service_found: {service.serviceName().lower()}")
        # if(target_service_device_name in str(service.serviceName()).lower()):
        #     # self.desired_service = service
        #     self.spp_service_list.append(service)
            
    def spp_service_discovery(self):
        try:
            if not self.local_device:
                self.emit_error("Adaptador bluetooth não encontrado")

            device_mode = self.local_device.hostMode() 
            
            if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
                self.emit_error("Adaptador Bluetooth esta desligado")
            else:
                self.service_discovery = None
                self.service_discovery = QBluetoothServiceDiscoveryAgent()
                # self.desired_service = None
                self.service_discovery.serviceDiscovered.connect(self.on_service_found)
                self.service_discovery.errorOccurred.connect(self.discovery_error)
                self.service_discovery.finished.connect(self.end_discovery)
                self.spp_service_list = []
                logger.debug("Começar descoberta por serviços")
                self.service_discovery.start()
        except Exception as e:
            logger.error(f"Erro ao começar descoberta de serviços bluetooth\nErr: {e}")
            
    def end_discovery(self):
        discoveredServices = self.service_discovery.discoveredServices()
        sorted_list = sorted(discoveredServices,key=lambda s: s.device().address().toString())
        for service in sorted_list:
            if (target_service_device_name in str(service.serviceName()).lower()):
                self.spp_service_list.append(service)
        if any(self.spp_service_list):
            self.discoveryEnd.emit({"type":"spp","res":True})
        else:
            self.discoveryEnd.emit({"type":"spp","res":False})
        # if self.desired_service:
        #     addr = self.desired_service.device().address().toString().replace(":","").lower()
        #     self.emit_result(addr)
        #     logger.debug(f"retornando mac: {addr}")
        
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
    def pair_device(self,serviceUuid,deviceMacString):
        try:
            if not self.local_device:
                self.emit_error("Adaptador Bluetooth não encontrado")
                return
            
            device_mode = self.local_device.hostMode() 
            
            if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
                self.emit_error("Adaptador Bluetooth esta desligado")
            else:
                argumentList = ['-c','-s',f'{serviceUuid}','-b',f'{deviceMacString}']
                argStr = ["_internal/resources/bin/btcom.exe",argumentList]
                self.runner.run(argStr=argStr)
        except Exception as e:
            self.emit_error(f"Erro no processo de conexão: {e}")
        
    def process_run_finish(self, object):
        try:
            logger.debug(f"process_run_finish:{object}")
            self.emit_result(object)
        except Exception as e:
            self.emit_error(f"Erro no processo de conexão: {e}")

    def unpair_device(self,deviceMacString):
        try:
            if not self.local_device:
                self.emit_error("Adaptador Bluetooth não encontrado")
                return
            
            device_mode = self.local_device.hostMode() 
            
            if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
                self.emit_error("Adaptador Bluetooth esta desligado")
            else:
                argumentList = ['-u','-b',f'{deviceMacString}']
                argStr = ["_internal/resources/bin/btpair.exe",argumentList]
                self.runner.run(argStr=argStr)
        except Exception as e:
            self.emit_error(f"Erro no processo de conexão: {e}")
            
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
                # self.desired_service = None
                self.hid_device_list = []
                self.powered_device_list = []
                self.discovery_agent.start()
        except Exception as e:
            logger.error(f"Erro ao iniciar a descoberta de dispositivos: {e}")
        
    def on_hid_device_found(self, device = QBluetoothDeviceInfo):
        if device.name().lower() == target_device_name.lower():
            logger.debug(f"on_hid_device_found device.rssi: {device.rssi()}")
            # self.hid_device_list.append(device)
        
    def hid_discovery_end(self):
        discoveredDevices = self.discovery_agent.discoveredDevices()
        sorted_list = sorted(discoveredDevices, key=lambda d: d.address().toString())
        for device in sorted_list:
            if device.name().lower() == target_device_name.lower():
                self.hid_device_list.append(device)
        if any(self.hid_device_list):
            logger.debug(f"hid_discovery_end self.hid_device_list:{self.hid_device_list}")
            self.discoveryEnd.emit({"type":"hid","res":True})
        else:
            self.discoveryEnd.emit({"type":"hid","res":False})
        #     # logger.debug(f"dispositivo encontrado: {self.desired_device.name()}")
        #     self.emit_result("Dispositivos encontrados")
        # else:
        #     self.emit_error("Dispositivos não encontrado")

    def hid_device_pair(self,device):
        try:
            logger.debug(f"hid_device_pair device:{device.name()}")
            if device:
                self.local_device.requestPairing(device.address(), self.local_device.Pairing.Paired)
            else:
                self.emit_error("Dispositivo não encontrado para o paremaneto")
        except Exception as e:
            self.emit_error(f"Erro no processo de conexão: {e}")

    def hid_device_unpair(self,device):
        try:
            device_mode = self.local_device.hostMode() 
            
            if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
                self.emit_error("Adaptador Bluetooth esta desligado")
                return
            
            if device:
                logger.debug(f"hid_device_unpair {device.name()}")
                if self.local_device.pairingStatus(device.address()) == self.local_device.Pairing.AuthorizedPaired:
                    logger.debug(f"hid_device_unpair unpairing -> {device.name()}")
                    self.local_device.requestPairing(device.address(), self.local_device.Pairing.Unpaired)
                else:
                    self.emit_error("Dispositivo não encontrado")
            elif self.paired_device:
                self.local_device.requestPairing(self.paired_device.address(), self.local_device.Pairing.Unpaired)
            else:
                self.emit_error("Variavel nula")
        except Exception as e:
                self.emit_error("Erro no processo de desemparelhamento")

    def hid_discovery_error(self):
        self.emit_error("Erro na descoberta de dispositivos HID")
            
    #returns the proper message for when the device has been paired or unpaired
    # def hid_pairEvent_finish(self):
    #     logger.debug("hid_pairEvent_finish")
    #     if self.desired_device:
    #         logger.debug(f"hid_pairEvent_finish self.desired_device true - self.local_device.pairingStatus(self.desired_device.address()){self.local_device.pairingStatus(self.desired_device.address())}")
    #         if self.local_device.pairingStatus(self.desired_device.address()) == self.local_device.Pairing.AuthorizedPaired:
    #             logger.debug("hid_pairEvent_finish self.desired_device DEVICE PAIRED")
    #             self.emit_result(f"Dispositivo HID {self.desired_device.name()} emparelhado")
    #         else:
    #             self.emit_result(f"Dispositivo HID desemparelhado")
    #             self.desired_device = None
    #     else:
    #         self.emit_result(f"Dispositivo HID não encontrado")
        
    def hid_pairEvent_finish(self,address,pair):
        logger.debug(f"hid_pairEvent_finish address,pair:{address,pair}")
        try:
            self.emit_result("processo de pareamento finalizado")
        except Exception as e:
            self.emit_error(f"Erro no processo de conexão: {e}")

    def local_device_error(self):
        logger.debug(f"local_device_error")
        self.emit_error(f"Erro no processo de conexão")

    #checks if the hid device connections status
    #!revise this function maybe?
    def check_device_connection(self,device):
        try:
            if device:
                logger.debug(f"hid_pairEvent_finish device true - self.local_device.pairingStatus(device.address()){self.local_device.pairingStatus(device.address())}")
                if self.local_device.pairingStatus(device.address()) == self.local_device.Pairing.AuthorizedPaired:
                    logger.debug("hid_pairEvent_finish device DEVICE PAIRED")
                    self.emit_result(f"Dispositivo HID {device.name()} emparelhado")
                else:
                    self.emit_result(f"Dispositivo HID desemparelhado")
            elif self.paired_device:
                if self.local_device.pairingStatus(self.paired_device.address()) != self.local_device.Pairing.AuthorizedPaired:
                    self.emit_result(f"Dispositivo HID desemparelhado")
                else:
                    self.emit_result(f"Erro no desemparelhamento do dispositivo HID")
            else:
                self.emit_error(f"Dispositivo HID não encontrado")
        except Exception as e:
                self.emit_error(f"Erro no processo de emparelhamento de dispositivo")

    #check for currently paired device
    def check_current_paired(self):
        device_mode = self.local_device.hostMode() 
        if device_mode == QBluetoothLocalDevice.HostMode.HostPoweredOff:
            self.local_device.setHostMode(QBluetoothLocalDevice.HostMode.HostConnectable)
            self.emit_result("Adaptador bluetooth ligado")

    ################################## LE Functions #################################
    def low_energy_check(self,device):
        try:
            #low energy controller setup for checking power state
            self.low_energy_controller = None
            self.low_energy_controller = QLowEnergyController.createCentral(device)
            self.low_energy_controller.connected.connect(self.low_energy_connect_handle)
            self.low_energy_controller.errorOccurred.connect(self.low_energy_error_handle)
            self.low_energy_controller.connectToDevice()
        except Exception as e:
            self.emit_error(False)
        
    def low_energy_error_handle(self):
        logger.debug(f"low_energy_error_handle signal")
        self.emit_error("Dispositivo desligado ou fora de alcance")

    def low_energy_connect_handle(self):
        logger.debug(f"low_energy_connect_handle signal")
        self.emit_result("Dispositivo ligado")
        
    #sets the functions that will be used as callback on the model class
    def set_callback(self, on_result = None, on_error = None):
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
