from ui.views.config_widget_ui import Ui_configForm

from shared_ui_modules.ui.model.dialogs.key_select_model import SharedKeySelectModel
from shared_ui_modules.ui.model.components.end_config_model import SharedEndConfigModel
from shared_ui_modules.ui.model.stacked_widget_screens.config_widget_model import SharedConfigWidgetModel
from ui.model.custom_widgets.custom_slider_model import CustomSliderModel

from shared_ui_modules.modules.log_class import logger
from modules.json_writer import JsonWriterClass

from PySide6.QtWidgets import QWidget, QRadioButton, QMessageBox
from PySide6.QtCore import QRect, Qt, QCoreApplication, QEvent

finger_base_value = {
    "repeat_key":False,
    "key":None,
    "duration":0
}

nunchuck_base_value = {
    "z_key":None,
    "c_key":None
}

class ConfigWidgetModel(SharedConfigWidgetModel):
    def __init__(self, btSerialHandle, LogModel):
        super().__init__(btSerialHandle, LogModel)

        self.string_list_dialog = [
            QCoreApplication.translate("ConfigJoystickDialogText","Erro"),   
            QCoreApplication.translate("ConfigJoystickDialogText","Escolha a tecla a ser emulada")            
        ]        

        self.string_list_components = [
            QCoreApplication.translate("ConfigJoystickComponents", "Clique para selecionar")
        ]        

        #ui setup
        self.ui = Ui_configForm()
        self.ui.setupUi(self)

        self.key_select_modal = SharedKeySelectModel()
        self.end_modal = SharedEndConfigModel()
        self.logModel = LogModel
        self.btSerialHandle = btSerialHandle
        self.jsonWriter = JsonWriterClass()

        #variables setup
        self._selected_fingers = [False,False,False,False]#radio buttons will populate this, 0 little - 3 index
        self.param_select = finger_base_value.copy()
        self.nunchuck_info_dict = nunchuck_base_value.copy()
        self.p_value_array = [0,0,0,0]
        self.current_user = None
        
        #get ui elements
        #hand radio buttons
        self.radioButtonLittle = self.ui.radioButtonLittle
        self.radioButtonRing = self.ui.radioButtonRing
        self.radioButtonMiddle = self.ui.radioButtonMiddle
        self.radioButtonIndex = self.ui.radioButtonIndex
        
        #hand sliders
        self.verticalSliderLittle = CustomSliderModel()
        self.verticalSliderRing = CustomSliderModel()
        self.verticalSliderMiddle = CustomSliderModel()
        self.verticalSliderIndex = CustomSliderModel()
        
        self.slider_array = [
            self.verticalSliderLittle,
            self.verticalSliderRing,
            self.verticalSliderMiddle,
            self.verticalSliderIndex
        ]
        
        self.finger_radio_array = [
            self.radioButtonLittle,
            self.radioButtonRing,
            self.radioButtonMiddle, 
            self.radioButtonIndex
        ]

        #optionsContainer elements
        self.repeatOffButton = self.ui.repeatOffButton
        self.repeatOnButton = self.ui.repeatOnButton

        #duration slider
        self.durationSlider = self.ui.durationSlider

        #buttons
        self.pressureButton = self.ui.pressureButton
        self.CKeyButton = self.ui.CKeyButton
        self.ZKeyButton = self.ui.ZKeyButton
        self.confirmButton = self.ui.confirmButton

        #finger indexing
        self.radioButtonLittle.setProperty("index",0)
        self.radioButtonRing.setProperty("index",1)
        self.radioButtonMiddle.setProperty("index",2)
        self.radioButtonIndex.setProperty("index",3)

        self.verticalSliderLittle.slider.setProperty("index",0)
        self.verticalSliderRing.slider.setProperty("index",1)
        self.verticalSliderMiddle.slider.setProperty("index",2)
        self.verticalSliderIndex.slider.setProperty("index",3)
        
        #add slider on layout
        self.slider_pos_array = [
            QRect(143, 20, 70, 170),
            QRect(176, 12, 70, 170),
            QRect(205, 11, 70, 170),
            QRect(240, 14, 70, 170),
        ]

        for i,v in enumerate(self.slider_array):
            v.setParent(self.ui.configContainer)
            v.setGeometry(self.slider_pos_array[i])

        #connections
        for slider in self.slider_array:
            slider.setEnabled(False)
            slider.slider.valueChanged.connect(self.pressure_slider_value_change)
        
        for radio in self.ui.fingerButtonContainer_2.findChildren(QRadioButton):
            radio.clicked.connect(self.finger_radio_clicked)

        for radio in self.ui.repeatButtonContainer.findChildren(QRadioButton):
            radio.clicked.connect(self.repeat_button_handler)

        self.pressureButton.setProperty("index", 0)
        self.ZKeyButton.setProperty("index", 1)
        self.CKeyButton.setProperty("index", 2)

        self.durationSlider.valueChanged.connect(self.duration_slider_value_change)
        self.pressureButton.clicked.connect(self.key_select_handler)
        self.ZKeyButton.clicked.connect(self.key_select_handler)
        self.CKeyButton.clicked.connect(self.key_select_handler)
        self.confirmButton.clicked.connect(self.confirm_button_handler)

        self.key_select_modal.accepted.connect(self.handle_modal_finish)
        self.key_select_modal.setWindowModality(Qt.ApplicationModal)
        
        self.ui.optionsContainer.setEnabled(False)

        self.end_modal.finished.connect(self.finish_modal)
        # self.serialHandleClass.mesReceivedSignal.connect(self.message_received_handler)

    #defines selected_finger getter
    @property
    def selected_fingers(self):
        return self._selected_fingers

    #defines selected_finger setter and gives it runs value_reset_watcher
    @selected_fingers.setter
    def selected_fingers(self,index_value):#values must come in this format, setters can only take one argument after self
        index, value = index_value
        self._selected_fingers[index] = value
        self.value_reset_watcher()

    def set_slider_max_value(self,arry):
        for i,slider in enumerate(self.slider_array):
            slider.slider.setMaximum(arry[i])
            slider.maxLabel.setText(str(arry[i]/10))
    
    def finish_modal(self):
        try:
            self.btSerialHandle.mesReceivedSignal.disconnect(self.message_received_handler)
        except Exception as e:
            logger.error(f"ConfigWidgetModel finish_modal error: {e}")
    
    def duration_slider_value_change(self):
        try:
            self.param_select.update({"duration":self.sender().value()})
        except Exception as e:
            logger.error(f"ConfigWidgetModel duration_slider_value_change error: {e}")

    def key_select_handler(self):
        try:
            self.key_select_modal.z_c_key_mode = self.sender().property("index")
            self.key_select_modal.exec()
        except Exception as e:
            logger.error(f"ConfigWidgetModel key_select_handler error: {e}")

    def start_config_process(self):
        try:
            if self.btSerialHandle.socket_none_check():
                self.reset_screen()
                return
            selection_check = any(self._selected_fingers)
            if (selection_check == False):
                logger.debug("Selecione uma combinação de dedos")
            elif self.param_select["key"] == None:
                warning = QMessageBox(self)
                warning.setWindowTitle(self.string_list_dialog[0])
                warning.setText(self.string_list_dialog[1])
                warning.setWindowModality(Qt.ApplicationModal)
                warning.show()
            else:
                self.setEnabled(False)
                messages, bindingDict = self.confirm_messages_generator()
                self.end_modal.sent_message_total = len(messages)  
                for message in messages:
                    self.send_serial_message(message)
                self.jsonWriter.write_bindings(bindingDict)
                self._selected_fingers = [False,False,False,False]#this is done this way as to not trigger reset value multiple times
                self.selected_fingers = (0,False)
                self.btSerialHandle.mesReceivedSignal.connect(self.message_received_handler)
                self.end_modal.exec()
                self.setEnabled(True)
        except Exception as e:
            logger.error(f"ConfigWidgetModel start_config_process error: {e}")
            raise
        
    def pressure_slider_value_change(self):
        try:
            self.p_value_array[self.sender().property("index")] = self.sender().value()
            self.sender().parent().parent().parent().currentLabel.setText(str(self.sender().value()/10))
        except Exception as e:
            logger.error(f"ConfigWidgetModel pressure_slider_value_change error: {e}")

    def finger_radio_clicked(self):
        try:
            index = self.sender().property("index")
            self.selected_fingers = (index, self.sender().isChecked())
            self.slider_array[index].setEnabled(self._selected_fingers[index])
            if self._selected_fingers[index] == False:
                self.slider_array[index].slider.setValue(0)
        except Exception as e:
            logger.error(f"ConfigWidgetModel finger_radio_clicked error: {e}")

    #resets info to be transmited via serial
    def value_reset_watcher(self):
        try:
            selection_check = any(self._selected_fingers)
            if self.ui.optionsContainer.isEnabled() == False:
                self.ui.optionsContainer.setEnabled(True)
            if selection_check == False:
                self.reset_variables()
                self.reset_screen()
                return True
            return False
        except Exception as e:
            logger.error(f"ConfigWidgetModel value_reset_watcher error: {e}")
    
    def reset_variables(self):
        try:
            self.param_select = finger_base_value.copy()
            self.nunchuck_info_dict = nunchuck_base_value.copy()
            self.p_value_array = [0,0,0,0]
        except Exception as e:
            logger.error(f"ConfigWidgetModel reset_variables error: {e}")

    def reset_screen(self):
        try:
            self.repeatOffButton.setChecked(True)
            self.repeatOnButton.setChecked(False)
            self.pressureButton.setText(self.string_list_components[0])
            self.durationSlider.setValue(finger_base_value["duration"])
            self.ui.optionsContainer.setEnabled(False)
            for radio in self.ui.fingerButtonContainer_2.findChildren(QRadioButton):
                radio.setChecked(False)
            for slider in self.slider_array:
                slider.setEnabled(False)
                slider.slider.setValue(0)
        except Exception as e:
            logger.error(f"ConfigWidgetModel reset_screen error: {e}")

    def confirm_messages_generator(self):
        try:
            messages = []
            for i, v in enumerate(self.p_value_array):#!p_values has to come first as to determine the finger combo
                if self._selected_fingers[i] == True:
                    mes = self.message_normalization(v,i+1)                
                    messages.append(mes)
            pairs = [(k, v) for (k, v) in self.param_select.items()]
            for i, (k,v) in enumerate(pairs):
                if v != None:
                    match i:
                        case 0:
                            messages.append(f"*R{int(v)}")
                        case 1:
                            messages.append(f"*K{v}")
                        case 2:
                            messages.append(f"*T{v}")
            if self.nunchuck_info_dict["c_key"] != None: messages.append(f"*C{self.nunchuck_info_dict["c_key"]}")
            if self.nunchuck_info_dict["z_key"] != None: messages.append(f"*Z{self.nunchuck_info_dict["z_key"]}")
            bindingDict = {
                    "duration": self.param_select["duration"],
                    "key": self.param_select["key"],
                    "repeat": self.param_select["repeat_key"],
                    "little": self.p_value_array[0],
                    "ring": self.p_value_array[1],
                    "middle": self.p_value_array[2],
                    "index": self.p_value_array[3]
            }
            return  messages, bindingDict
        except Exception as e:
            logger.error(f"ConfigWidgetModel confirm_messages_generator error: {e}")
            raise     

    def handle_modal_finish(self):#!beter logic maybe?
        try:
            key = self.key_select_modal.selected_key
            key_text = self.arrow_text_conversion(key)
            if self.key_select_modal.z_c_key_mode == 0:
                self.param_select.update({"key":key})
                self.pressureButton.setText(key_text.upper())
            elif self.key_select_modal.z_c_key_mode == 1:
                self.nunchuck_info_dict.update({"z_key":key})
                self.ZKeyButton.setText(key_text.upper())
            else:
                self.nunchuck_info_dict.update({"c_key":key})
                self.CKeyButton.setText(key_text.upper())
            self.key_select_modal.selected_key = None
            self.key_select_modal.z_c_key_mode = 0
        except Exception as e:
            logger.error(f"ConfigWidgetModel confirm_messages_generator error: {e}")

    def assing_card_values(self,config):
        try:
            if config is None:
                raise Exception(f"null config: {config}")
                
            self._selected_fingers = [False,False,False,False]#this is done this way as to not trigger reset value multiple times
            self.selected_fingers = (0,False)#triggers reset
            duration = int(config["duration"])
            repeat = True if config["repeat"] == "True" else False
            key = config["key"]

            for index, finger in enumerate(["little", "ring", "middle" , "index"]):
                value = int(config[finger])
                if int(value) != 0:
                    self.finger_radio_array[index].setChecked(True)
                    self.selected_fingers = (index,True)
                    self.slider_array[index].setEnabled(True)
                    self.slider_array[index].slider.setValue(value)
                    
            self.durationSlider.setValue(duration)

            if repeat == True:
                self.repeatOnButton.setChecked(True)
                self.repeatOffButton.setChecked(False)
                self.param_select["repeat_key"] = True
            else:
                self.repeatOffButton.setChecked(True)
                self.repeatOnButton.setChecked(False)
                self.param_select["repeat_key"] = False
                
            self.key_select_modal.selected_key = key
            self.handle_modal_finish()
        except Exception as e:
            logger.error(f"ConfigWidgetModel assing_card_values error: {e}")

    def changeEvent(self, event):
        if event.type() == QEvent.Type.LanguageChange:
            self.string_list_components = [
                QCoreApplication.translate("ConfigJoystickComponents", "Clique para selecionar")
            ] 

            self.string_list_dialog = [
                QCoreApplication.translate("ConfigJoystickDialogText","Erro"),   
                QCoreApplication.translate("ConfigJoystickDialogText","Escolha a tecla a ser emulada")            
            ]      
            
            self.ui.retranslateUi(self)
            if self.param_select["key"] != None:
                key_text = self.arrow_text_conversion(self.param_select["key"])
                self.pressureButton.setText(key_text.upper())
            if self.nunchuck_info_dict["c_key"] != None:
                key_text = self.arrow_text_conversion(self.nunchuck_info_dict["c_key"])
                self.CKeyButton.setText(key_text.upper())
            if self.nunchuck_info_dict["z_key"] != None:
                key_text = self.arrow_text_conversion(self.nunchuck_info_dict["z_key"])
                self.ZKeyButton.setText(key_text.upper())

        return super().changeEvent(event)
        