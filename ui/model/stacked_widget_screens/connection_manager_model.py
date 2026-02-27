from ui.views.connection_manager_ui import Ui_loggerForm

from modules.bluetooth_comunication import BluetoothCommClass
from modules.log_class import logger

from ui.model.components.listed_device_item_model import ListedDeviceItemModel
from ui.model.components.connected_device_item_model import ConnectedDeviceModel

from PySide6.QtWidgets import QWidget, QListWidgetItem, QPushButton
from PySide6.QtCore import Qt, Signal

#basic widget funcionalitty
    #list all available joysticks
    #allow joystick connection using button
    #conncetion 
        #disconnect currently connected joystikc
        #connect new joystick

class ConnectionManagerModel(QWidget):

    sideMenuDisableSignal = Signal(bool)

    def __init__(self, serialHandleClass, logModel):

        super().__init__()

        #modules setup
        self.bluetoothHandle = BluetoothCommClass()
        self.serialHandleClass = serialHandleClass
        self.logModel = logModel
        
        #setup ui
        self.ui = Ui_loggerForm()
        self.ui.setupUi(self)

        #get ui elements
        self.pairDeviceButton = self.ui.pairDeviceButton
        self.reloadListButton = self.ui.reloadListButton
        self.sppStateButton = self.ui.sppStateButton
        self.unpairDeviceButton = self.ui.unpairDeviceButton
        self.hidStateButton = self.ui.hidStateButton
        self.deviceListWidget = self.ui.deviceListWidget
        self.deviceContainer = self.ui.deviceContainer
        
        #hide 2 buttons
        self.sppStateButton.hide()
        self.hidStateButton.hide()
        
        #variable setup
        self.selected_device = [None,None]#0: device 1: service
        self._selected_list_item = None
        self.power_test_counter = 0
        self._connected_device_watcher = False

        #will be used as watchers for hid and spp discovery signals
        self.device_search_in_progress = False
        self.service_search_in_progress = False

        #connection setup_selected_device
        self.reloadListButton.clicked.connect(self.reload_button_handle)
        self.deviceListWidget.doubleClicked.connect(self.device_select_handle)
        self.pairDeviceButton.clicked.connect(self.pair_selected_device)
        self.serialHandleClass.portSignal.connect(self.port_found_signal)
        self.bluetoothHandle.discoveryEnd.connect(self.discovery_end_handler)#recives a dict with type(spp/hid)(string) and res(true/false)
        self.unpairDeviceButton.clicked.connect(self.full_unpair)

        self.selected_list_item = None
        self.connected_device_watcher = False

    @property
    def selected_list_item(self):
        return self._selected_list_item

    @selected_list_item.setter
    def selected_list_item(self, index):
        self._selected_list_item = index
        self.pair_button_state_watcher()
        
    def pair_button_state_watcher(self):
        if self._selected_list_item != None:
            self.pairDeviceButton.setEnabled(True)
        else:
            self.pairDeviceButton.setEnabled(False)

    @property
    def connected_device_watcher(self):
        return self._connected_device_watcher
    
    @connected_device_watcher.setter
    def connected_device_watcher(self, state):
        self._connected_device_watcher = state
        self.unpair_device_button_watcher()

    def unpair_device_button_watcher(self):
        if self._connected_device_watcher:
            self.unpairDeviceButton.setEnabled(True)
        else:
            self.unpairDeviceButton.setEnabled(False)
        

    #clears every relevant variable, releses ui and clears list
    def nuke_screen_on_error(self):
        self.selected_device = [None, None]
        self.deviceListWidget.clear()
        self.service_search_in_progress = False
        self.device_search_in_progress = False
        self.selected_list_item = None
        self.release_screen()

    #full pair error fallback
    def handle_process_ending_error(self,message):
        self.logModel.append_log(message)
        logger.error(message)
        self.nuke_screen_on_error()

    # to garantee button state consistency, both pair and unpair button get called on disable and enable screen,
    #controlVal parameter gets passed se we block unpair device even when the variable is not null
    def disable_screen(self, pairControl = True, unpairControl = True):
        # for button in self.ui.windowContainer.findChildren(QPushButton):
        #     button.setEnabled(False)
        self.pairDeviceButton.setEnabled(False)
        self.unpairDeviceButton.setEnabled(False)
        self.reloadListButton.setEnabled(False)
        self.deviceListWidget.setEnabled(False)
        if pairControl == True:
            self.pair_button_state_watcher()
        if unpairControl == True:
            self.unpair_device_button_watcher()
        self.sideMenuDisableSignal.emit(False)
        
    def release_screen(self):
        # for button in self.ui.windowContainer.findChildren(QPushButton):
        #     button.setEnabled(True)
        self.pairDeviceButton.setEnabled(True)
        self.unpairDeviceButton.setEnabled(True)
        self.reloadListButton.setEnabled(True)
        self.deviceListWidget.setEnabled(True)
        self.pair_button_state_watcher()
        self.unpair_device_button_watcher()
        self.sideMenuDisableSignal.emit(True)
        
    #gets called twice, one for device discovery and other for service discovery
    #will release the ui and update the list after the discoveries have finished
    def discovery_end_handler(self,dict):
        if dict["type"] == "spp":
            self.service_search_in_progress = False        
        if dict["type"] == "hid":
            self.device_search_in_progress = False    
        if self.device_search_in_progress == False and self.service_search_in_progress == False:
            self.power_test_counter = len(self.bluetoothHandle.hid_device_list)
            logger.debug(f"discovery_end_handler self.power_test_counter:{self.power_test_counter}")
            if self.power_test_counter > 0:
                for device in self.bluetoothHandle.hid_device_list:
                    self.device_power_check(device)
            else:
                self.release_screen()
                
    
    def power_counter_watcher(self):
        logger.debug(f"power_counter_watcher power_test_counter:{self.power_test_counter}")
        if self.power_test_counter == 0:
            self.bluetoothHandle.low_energy_controller.connected.disconnect(self.bluetoothHandle.low_energy_connect_handle)
            self.bluetoothHandle.low_energy_controller.errorOccurred.disconnect(self.bluetoothHandle.low_energy_error_handle)
            self.bluetoothHandle.low_energy_controller = None
            self.update_list()
            self.release_screen()

    #adds connected device widget to the layout
    def show_connected_device(self):
        #generete device info dict
        deviceInfoDict = {
            "mac": self.serialHandleClass.device_mac_addr,
            "name": self.selected_device[0].name(),
            "port": self.serialHandleClass.ser.portName(),
            "hid_device": self.selected_device[0],
            "service": self.selected_device[1]
        }
        #create device item
        self.connected_item = ConnectedDeviceModel(deviceInfoDict)
        self.deviceContainer.layout().addWidget(self.connected_item)
        self.connected_device_watcher = True

    #clears port addr and mac
    def clear_serial_info(self):
        self.serialHandleClass.device_mac_addr = None#clear device info from serialHandleClass
        self.serialHandleClass.ser.port = ''
        if self.serialHandleClass.ser.isOpen():
            self.serialHandleClass.ser.close()
        self.serialHandleClass.ser.setPortName('')

    #when pressed, start looking for devices and block the ui
    def reload_button_handle(self):
        def on_error(message):
            self.bluetoothHandle.service_discovery.stop()
            self.bluetoothHandle.discovery_agent.stop()
            self.handle_process_ending_error(message)

        self.bluetoothHandle.set_callback(on_error= on_error)
        self.device_search_in_progress = True
        self.spp_search_in_progress = True
        self.bluetoothHandle.hid_device_discovery()
        self.bluetoothHandle.spp_service_discovery()
        self.disable_screen(pairControl = False, unpairControl = False)
        self.logModel.append_log("Procurando por dispositivos")
            
    #gets info from the currently selected device from the list and updates self.selected_device
    def device_select_handle(self, index):
        item = self.sender().item(index.row())
        widget = self.sender().itemWidget(item)
        device_id = widget.deviceDict["id"]
        service_id = widget.deviceDict["service_id"]
        self.selected_device[0] = self.bluetoothHandle.hid_device_list[device_id]
        self.selected_device[1] = self.bluetoothHandle.spp_service_list[service_id]
        self.selected_list_item = index.row()
        self.logModel.append_log(f"Dispositivo selecionado:{self._selected_list_item}")
        logger.debug(f"device_select_handle self.selected_device{self.selected_device}")

    #checks for selected devices and starts the full pair
    def pair_selected_device(self):
        if self.selected_device[0] and self.selected_device[1]:
            self.disable_screen(pairControl=False)
            self.full_pair_handler(nextStepOnResult=self.full_pair_step_3,errorHandler=self.handle_process_ending_error)

    #starts the whole process
    #steps define on_error and on_resut callbacks that will stop or continue the process
    #process happen one after the other creating quite a long chain of sequential functions
    #somehwat slow
    #2 first steps get reused for unpair_device
        #recieves next function handler that will be used in step 2, ends the unpair_handler but continues the pair 
        #recives errorHandler that appropriately deals with the unpair_handler errors 
        #from step 3 onwards just continues the process as normal
    #!add main screen but state toggle to start and finish
    def full_pair_handler(self,nextStepOnResult,errorHandler):
        logger.debug(f"full_pair_handler iniciado device:{self.selected_device[0]}")
        # self.button_state_toggle()
        self.logModel.append_log("Processo de conexão com joystick iniciado, este processo pode demorar...")
        self.logModel.append_log("Desemparelhando dispositivo HID.")

        def on_error(message):
            if message == "Dispositivo não encontrado":
                message +=". Passando para o próximo passo"
                self.logModel.append_log(message)
                self.full_pair_step_2(nextStepOnResult=nextStepOnResult,errorHandler=errorHandler)
            else:
                # self.handle_process_ending_error(message)
                errorHandler(message)

        def on_result(message):
            self.logModel.append_log(message)
            logger.debug(f"on_result message:{message}")
            self.check_connection(errorHandler,nextStepOnResult)
            
        self.bluetoothHandle.set_callback(on_error=on_error,on_result=on_result)
        self.bluetoothHandle.hid_device_unpair(self.selected_device[0])
        
    #checks for hid device disconnections
    def check_connection(self,errorHandler,nextStepOnResult):
        logger.debug(f"check_connection iniciado device:{self.selected_device[0]}")
        def on_error(message):
            # self.handle_process_ending_error(message)
            errorHandler(message)
            
        def on_result(message):
            self.logModel.append_log(message)
            self.full_pair_step_2(nextStepOnResult=nextStepOnResult,errorHandler=errorHandler)
            
        self.bluetoothHandle.set_callback(on_error=on_error, on_result=on_result)
        self.bluetoothHandle.check_device_connection(self.selected_device[0])

    #tries to unpair spp service, uses process_runner with btpair
    def full_pair_step_2(self,nextStepOnResult,errorHandler):
        self.logModel.append_log("Desemparelhando dispositivo SPP.")
        logger.debug("Desemparelhando dispositivo SPP.")
        def on_error(message):
            if message == "Dispositivo não encontrado":
                message +=". Passando para o próximo passo"
                self.logModel.append_log(message)
                # self.full_pair_step_3()
                nextStepOnResult()
            else:
                # self.handle_process_ending_error(message)
                errorHandler(message)

        def on_result(message):
            self.logModel.append_log(message["message"])
            self.bluetoothHandle.desired_service = None
            self.clear_serial_info()
            # self.full_pair_step_3()
            nextStepOnResult()
            
        self.bluetoothHandle.set_callback(on_error=on_error,on_result=on_result)
        if self.selected_device[0] == None:
            self.bluetoothHandle.unpair_device(self.bluetoothHandle.paired_device.address().toString().lower())
        else:
            self.bluetoothHandle.unpair_device(self.selected_device[0].address().toString().lower())

        
    #pairs hid device, uses local_device
    def full_pair_step_3(self):
        self.logModel.append_log("Iniciando processo de emprelhamento HID.\nMantenha o joystick ligado.\nEste processo pode demorar.")

        def on_error(message):
            self.handle_process_ending_error(message)
            
        def on_result(message):
            self.full_pair_step_4()
            
        self.bluetoothHandle.set_callback(on_error=on_error,on_result=on_result)
        self.bluetoothHandle.hid_device_pair(self.selected_device[0])

    #pairs the spp service, uses process runner with btcom
    def full_pair_step_4(self):
        self.logModel.append_log("Iniciando processo de emprelhamento SPP.\nMantenha o joystick ligado.\nEste processo pode demorar.\nUma notificação do Windows vai aparecer, clique na mesma e aceite")

        def on_error(message):
            self.logModel.append_log(message)
            
        def on_result(processDict):
            self.logModel.append_log(processDict["message"])
            if processDict["status"] == False:
                self.handle_process_ending_error(processDict["message"])
            else:
                self.logModel.append_log("Encontrando o endereço MAC e porta serial do dispositivo, aguarde...")
                self.end_full_pair(self.selected_device[1].device().address().toString().replace(":","").lower())

        self.bluetoothHandle.set_callback(on_error=on_error,on_result=on_result)
        self.bluetoothHandle.pair_device(self.selected_device[1].serviceUuid().toString(),self.selected_device[0].address().toString())

    #gets device addr            
    def end_full_pair(self,addr):
        logger.debug(f"end_full_pair addr:{addr}")
        try:
            self.serialHandleClass.device_mac_addr = addr
            self.serialHandleClass.find_port()
        except Exception as e:
            self.handle_process_ending_error(f"Erro ao encontrar dispositivos\nErro: {e}")


    #will recive the signal from serial handle that indicates if the port was found successfully
    def port_found_signal(self,signal):
        if signal == True:
            self.successful_pair()
        elif signal == False:
            self.handle_process_ending_error("Erro ao tentar obter porta serial do joystick")

    def successful_pair(self):
        self.show_connected_device()
        item = self.deviceListWidget.takeItem(self._selected_list_item)
        del item
        self.bluetoothHandle.paired_device = self.selected_device[0]
        self.selected_device = [None,None]
        self.selected_list_item = None
        self.logModel.append_log("Sucesso no emparelhamento")
        self.release_screen()

    # def service_toggle(self):
    #     if self.self.connected_item.service_state == 1:
            
    #         def on_error(message):
    #             self.logModel.append_log(message)
    #             self.release_screen()
                
    #         def on_result(message):
    #             self.logModel.append_log(message)
    #             self.self.connected_item.service_state = 0
    #             self.clear_serial_info()
    #             self.release_screen()
            
    #         self.bluetoothHandle.set_callback(on_error=on_error, on_result=on_result)
    #         self.bluetoothHandle.unpair_device(self.connected_item.device_info_dict["hid_device"].address().toString().lower())
    #     else:
                        
    #         def on_error(message):
    #             self.logModel.append_log(message)
    #             self.release_screen()
                
    #         def on_result(message):
    #             self.logModel.append_log(message)
    #             self.serialHandleClass.portsignal.disconnect(self.port_found_signal)
    #             self.serialHandleClass.portsignal.connect(self.service_toggle_signal_handler)
            
    #         self.bluetoothHandle.set_callback(on_error=on_error, on_result=on_result)
    #         self.bluetoothHandle.pair_device(self.connected_item.device_info_dict["service"].serviceUuid().toString(),self.connected_item.device_info_dict["hid_device"].address().toString())
        
    # def service_toggle_signal_handler(self,signal):
    #     self.serialHandleClass.portsignal.disconnect(self.service_toggle_signal_handler)
    #     self.serialHandleClass.portsignal.connect(self.port_found_signal)
    #     if signal == True:
    #         self.self.connected_item.service_state = 1
    #         self.logModel.append_log("Sucesso ao obter porta COM")
    #         self.self.connected_item.comPortLabel.setText(self.serialHandleClass.ser.portName())
    #     elif signal == False:
    #         self.logModel.append_log("Erro ao tentar obter porta COM")
    #     self.release_screen()
        
    # def hid_toggle(self):
    #     if self.self.connected_item.device_state == 1:
            
    #         def on_error(message):
    #             self.logModel.append_log(message)
    #             self.release_screen()
                
    #         def on_result(message):
    #             self.logModel.append_log(message)
    #             self.self.connected_item.device_state = 0
    #             self.release_screen()
            
    #         self.bluetoothHandle.set_callback(on_error=on_error, on_result=on_result)
    #         self.bluetoothHandle.hid_device_unpair(self.connected_item.device_info_dict["hid_device"])
    #     else:
                        
    #         def on_error(message):
    #             self.logModel.append_log(message)
    #             self.release_screen()
                
    #         def on_result(message):
    #             self.logModel.append_log(message)
    #             self.self.connected_item.device_state = 1
    #             self.release_screen()
            
    #         self.bluetoothHandle.set_callback(on_error=on_error, on_result=on_result)
    #         self.bluetoothHandle.hid_device_pair(self.connected_item.device_info_dict["hid_device"])
        
    def full_unpair(self):
        self.logModel.append_log("Desemparelhando dispositivo")
        self.disable_screen(unpairControl=False)
        self.full_pair_handler(errorHandler=self.unpair_error_handler,nextStepOnResult=self.unpair_finish_handler)
           
    def unpair_finish_handler(self):
        self.clear_serial_info()
        self.selected_device = [None,None]
        self.connected_item.deleteLater()
        self.selected_list_item = None
        self.bluetoothHandle.paired_device = None
        self.connected_device_watcher = False
        self.release_screen()
        
    def unpair_error_handler(self,message):
        self.logModel.append_log(message)
        self.release_screen()
    
    #visually updates the list and atributes deviceDict to each item
    def update_list(self):
        try:
            self.deviceListWidget.clear()
            
            powered_off_mac_dict =  set(self.bluetoothHandle.powered_device_list)
            logger.debug(f"update_list powered_off_mac_dict:{powered_off_mac_dict}")
            logger.debug(f"update_list self.bluetoothHandle.powered_device_list:{self.bluetoothHandle.powered_device_list}")

            for i, device in enumerate(self.bluetoothHandle.hid_device_list):
                if self.bluetoothHandle.paired_device == None or self.bluetoothHandle.paired_device.address() != device.address(): 
                    
                    deviceDict = {
                        "listName": f"Dispositivo {i+1}",
                        "name": device.name(),
                        "mac": device.address().toString(),
                        "id": i,
                        "turned_on": False if device.address() in powered_off_mac_dict else True
                    }
                    if device.address() == self.bluetoothHandle.spp_service_list[i].device().address():
                        deviceDict["uuid"] = self.bluetoothHandle.spp_service_list[i].serviceUuid().toString()
                        deviceDict["service_id"] = i
                    item = ListedDeviceItemModel(deviceDict)
                    item_container = QListWidgetItem(self.deviceListWidget)
                    item_container.setSizeHint(item.sizeHint())
                    if deviceDict["turned_on"] == False:
                        item_container.setFlags(item_container.flags() & ~(Qt.ItemIsSelectable | Qt.ItemIsEnabled))
                    self.deviceListWidget.addItem(item_container)
                    self.deviceListWidget.setItemWidget(item_container,item)
        except Exception as e:
            self.handle_process_ending_error("Erro no processo de paremaneto")
                
    def device_power_check(self,device):
        logger.debug(f"device_power_check device:{device}")
        def on_error(message):
            if message == False:
                #break process on actual error
                self.handle_process_ending_error("Erro no processo de pareamento")
            else:
                self.bluetoothHandle.powered_device_list.append(device.address())
                self.power_test_counter -= 1
                self.power_counter_watcher()

        def on_result(message):
            self.power_test_counter -= 1
            self.power_counter_watcher()
    
        self.bluetoothHandle.set_callback(on_error=on_error,on_result=on_result)
        self.bluetoothHandle.low_energy_check(device)
        
        
        
                
        