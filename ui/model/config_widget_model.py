from PySide6.QtWidgets import QWidget, QSlider, QRadioButton, QLabel
from ui.views.config_widget_ui import Ui_configForm
from ui.model.key_select_model import KeySelectModel
from ui.model.end_config_model import EndConfigModel
from modules.log_class import logger
from ui.model.custom_slider_model import CustomSliderModel
from PySide6.QtCore import QRect

finger_base_value = {
    "repeat_key":False,
    "key":None,
    "duration":1
}

nunchuck_base_value = {
    "z_key":None,
    "c_key":None
}

class ConfigWidgetModel(QWidget):
    def __init__(self,serialHandleClass):
        super().__init__()

        #ui setup
        self.ui = Ui_configForm()
        self.ui.setupUi(self)

        self.key_select_modal = KeySelectModel()
        self.end_modal = EndConfigModel()
        self.serialHandleClass = serialHandleClass

        #variables setup
        self._selected_fingers = [False,False,False,False]#radio buttons will populate this, 0 little - 3 index
        self.finger_info_dict = finger_base_value.copy()
        self.nunchuck_info_dict = nunchuck_base_value.copy()
        self.p_value_array = [0,0,0,0,0]
        
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

        self.durationSlider.valueChanged.connect(self.duration_slider_value_change)
        self.pressureButton.clicked.connect(self.pressure_button_handler)
        self.ZKeyButton.clicked.connect(self.zKey_button_handler)
        self.CKeyButton.clicked.connect(self.cKey_button_handler)
        self.confirmButton.clicked.connect(self.confirm_button_handler)

        self.key_select_modal.accepted.connect(self.handle_modal_finish)

        self.serialHandleClass.mesReceivedSignal.connect(self.message_received_handler)
        
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

    def set_slider_max_value(self,value):
        for slider in self.slider_array:
            slider.slider.setMaximum(value)
            slider.maxLabel.setText(str(value/10))

    def duration_slider_value_change(self):
        print(f"slider: {self.sender().objectName()} - value: {self.sender().value()}")
        self.finger_info_dict.update({"duration":self.sender().value()})
        print(self.finger_info_dict)

    def zKey_button_handler(self):
        print(f"sender: {self.sender().objectName()} pressed!")
        self.key_select_modal.z_c_key_mode = 1
        self.key_select_modal.open()
    
    def cKey_button_handler(self):
        print(f"sender: {self.sender().objectName()} pressed!")
        self.key_select_modal.z_c_key_mode = 2
        self.key_select_modal.open()

    def confirm_button_handler(self):
        selection_check = any(self._selected_fingers)
        if (selection_check == False):
            logger.debug("Selecione uma combinação de dedos")
        else:
            print(f"sender: {self.sender().objectName()} pressed!")
            self.setEnabled(False)
            messages = self.confirm_messages_generator()
            for message in messages:
                self.send_serial_message(message)
            self._selected_fingers = [False,False,False,False]#this is done this way as to not trigger reset value multiple times
            self.selected_fingers = (0,False)
            self.end_modal.open()
            self.setEnabled(True)

    def pressure_button_handler(self):
        print(f"sender: {self.sender().objectName()} pressed!")
        self.key_select_modal.z_c_key_mode = 0
        self.key_select_modal.open()
    
    def repeat_button_handler(self):
        print(f"radio: {self.sender().objectName} - state: {self.sender().isChecked()}")
        if self.sender().objectName() == "repeatOffButton":
            self.finger_info_dict.update({"repeat_key":False})
        else:
            self.finger_info_dict.update({"repeat_key":True})
        print(self.finger_info_dict)
        
    def pressure_slider_value_change(self):
        print(f"slider: {self.sender().objectName()} - value: {self.sender().value()} - index: {self.sender().property("index")}")
        self.p_value_array[self.sender().property("index")] = self.sender().value()
        self.sender().parent().parent().parent().currentLabel.setText(str(self.sender().value()/10))#why 3 parents?

    def finger_radio_clicked(self):
        index = self.sender().property("index")
        self.selected_fingers = (index, self.sender().isChecked())
        self.slider_array[index].setEnabled(self._selected_fingers[index])
        if self._selected_fingers[index] == False:
            self.slider_array[index].slider.setValue(0)
        print(self._selected_fingers)

    def message_received_handler(self,response):
        self.end_modal.recieve_end_message(response)
        logger.debug(f"mensagem recebida: {response}")

    #resets info to be transmited via serial
    def value_reset_watcher(self):
        selection_check = any(self._selected_fingers)
        if selection_check == False:
            self.reset_variables()
            self.reset_screen()
            print(f"after reset:{self.finger_info_dict}")
            return True
        return False
    
    def reset_variables(self):
        self.finger_info_dict = finger_base_value.copy()
        self.nunchuck_info_dict = nunchuck_base_value.copy()
        self.p_value_array = [0,0,0,0]
        
    def reset_screen(self):
        self.repeatOffButton.setChecked(True)
        self.repeatOnButton.setChecked(False)
        self.pressureButton.setText("Clique para selecionar")
        self.durationSlider.setValue(1)
        for radio in self.ui.fingerButtonContainer_2.findChildren(QRadioButton):
            radio.setChecked(False)
        for slider in self.slider_array:
            slider.setEnabled(False)
            slider.slider.setValue(0)

    def send_serial_message(self,message):
        self.serialHandleClass.open_port()
        logger.debug(f"mensagem enviada: {message}")
        self.serialHandleClass.send_message(message)
        
    def confirm_messages_generator(self):
        messages = []
        for i, v in enumerate(self.p_value_array):#!p_values have to come first as to determin the finger combo
            if v != 0:
                valueStr = v
                if(v < 10):#value always needs to be sent in a 3 digit format 
                    valueStr = f"00{v}"
                elif(v < 100):
                    valueStr = f"0{v}"
                #when sending the serial message, finger indexes start at 1
                messages.append("*M{}{}".format(i+1,v))
        pairs = [(k, v) for (k, v) in self.finger_info_dict.items()]
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
        if self.nunchuck_info_dict["z_key"] != None: messages.append(f"*C{self.nunchuck_info_dict["z_key"]}")
        return  messages
    
    def handle_modal_finish(self):#!beter logic maybe?
        key = self.key_select_modal.selected_key
        if self.key_select_modal.z_c_key_mode == 0:
            self.finger_info_dict.update({"key":key})
            self.pressureButton.setText(key)
            print(self.finger_info_dict)
        elif self.key_select_modal.z_c_key_mode == 1:
            self.nunchuck_info_dict.update({"z_key":key})
            self.ZKeyButton.setText(key)
            print(self.nunchuck_info_dict)
        else:
            self.nunchuck_info_dict.update({"c_key":key})
            self.CKeyButton.setText(key)
            print(self.nunchuck_info_dict)
        self.key_select_modal.selected_key = None
        self.key_select_modal.z_c_key_mode = 0