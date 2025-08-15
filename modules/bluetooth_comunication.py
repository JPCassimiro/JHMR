import bluetooth
import asyncio
from winrt.windows.devices.radios import Radio, RadioState
import PySide6.QtBluetooth
from PySide6.QtBluetooth import QBluetoothDeviceInfo
from PySide6.QtCore import Slot, QObject, Signal

class BluetoothCommClass(QObject):
    complete = Signal(list)
    errorMessage = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.discovery_agent = PySide6.QtBluetooth.QBluetoothDeviceDiscoveryAgent()
        self.devices = []

        self.discovery_agent.deviceDiscovered.connect(self.device_discovered)
        self.discovery_agent.finished.connect(self.end_discovery)
        self.discovery_agent.errorOccurred.connect(self.discovery_error)
        
        
    def device_discovered(self,device: QBluetoothDeviceInfo):
        self.devices.append(device)

    async def start_discovery(self):
        radios = await Radio.get_radios_async()
        b_radio = None

        for radio in radios:
            if radio.name == "Bluetooth":
                b_radio = radio
                break
        
        if not b_radio:
            self.end_discovery()
            self.errorMessage.emit("Adaptador Bluetooth não encontrado")
            return
        
        if b_radio.state == RadioState.OFF:
            self.errorMessage.emit("Adaptador Bluetooth desligado")
            self.end_discovery()
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
        radios = await Radio.get_radios_async()
        b_radio = None

        for radio in radios:
            if radio.name == "Bluetooth":
                b_radio = radio
                break
        
        if not b_radio:
            return "Adaptador Bluetooth não encontrado"
            
        if b_radio.state == RadioState.ON:
            await  b_radio.set_state_async(RadioState.OFF)
            return "Adaptador Bluetooth desligado"
        else:
            await  b_radio.set_state_async(RadioState.ON)
            return "Adaptador Bluetooth ligado"

        
        

# def find_devices():
#     nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
#                                         flush_cache=True, lookup_class=False)
#     # print("Found {} devices".format(len(nearby_devices)))
#     return nearby_devices


        
        
        
    #     self.discovery_agent.deviceDiscovered.connect(self.on_device_discovered)
    #     self.discovery_agent.deviceDiscovered.connect(self.on_error)
    #     self.discovery_agent.deviceDiscovered.connect(self.on_scan_finished)

    # @Slot()
    # def start_scan(self):
    #     self.devices.clear()
    #     self.discovery_agent.start()

    # @Slot()
    # def on_device_discovered(self, device):
    #     self.devices.append(device)

    # @Slot()
    # def on_error(self,error):
    #     print("\nErro ao procurar dispositivos" + error)

    # @Slot()
    # def on_scan_finished(self):
    #     self.finished.emit()