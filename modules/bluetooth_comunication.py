import asyncio
import PySide6.QtBluetooth
from PySide6.QtBluetooth import QBluetoothDeviceInfo, QBluetoothLocalDevice
from PySide6.QtCore import Slot, QObject, Signal

class BluetoothCommClass(QObject):
    complete = Signal(list)
    errorMessage = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.discovery_agent = PySide6.QtBluetooth.QBluetoothDeviceDiscoveryAgent()
        self.devices = []
        self.local_device = QBluetoothLocalDevice()

        self.discovery_agent.deviceDiscovered.connect(self.device_discovered)
        self.discovery_agent.finished.connect(self.end_discovery)
        self.discovery_agent.errorOccurred.connect(self.discovery_error)
        
        
    def device_discovered(self,device: QBluetoothDeviceInfo):
        self.devices.append(device)

    async def start_discovery(self):

        if not self.local_device:
            self.errorMessage.emit("Adaptador Bluetooth não encontrado")

        device_mode = self.local_device.hostMode() 
        
        if device_mode != QBluetoothLocalDevice.HostMode.HostConnectable:
            self.errorMessage.emit("Adaptador Bluetooth esta desligado")
        else:
            self.devices.clear()
            self.discovery_agent.start()
            
    def start_discovery_task_handler(self):
        asyncio.create_task(self.start_discovery())
            
    def end_discovery(self):
        self.complete.emit(self.devices)
        
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
            












#implementação antiga
        # radios = await Radio.get_radios_async()
        # b_radio = None

        # for radio in radios:
        #     if radio.name == "Bluetooth":
        #         b_radio = radio
        #         break
        
        # if not b_radio:
        #     return "Adaptador Bluetooth não encontrado"
            
        # if b_radio.state == RadioState.ON:
        #     await  b_radio.set_state_async(RadioState.OFF)
        #     return "Adaptador Bluetooth desligado"
        # else:
        #     await  b_radio.set_state_async(RadioState.ON)
        #     return "Adaptador Bluetooth ligado"
