from PySide6.QtWidgets import QWidget, QSlider, QRadioButton
from ui.views.config_widget_ui import Ui_configForm
from ui.model.key_select_model import KeySelectModel
from modules.log_class import logger

finger_base_value = {
    "finger_combo":None,
    "repeat_key":False,
    "key":None,
    "duration":None
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

        self.modal = KeySelectModel()
        self.serialHandleClass = serialHandleClass

        #variables setup
        self.selected_fingers = [False,False,False,False,False]#radio buttons will populate this, 0 little - 4 thumb
        self.finger_info_dict = finger_base_value
        self.nunchuck_info_dict = nunchuck_base_value
        self.p_value_array = [0,0,0,0,0]
        
        #get ui elements
        #hand radio buttons
        self.radioButtonLittle = self.ui.radioButtonLittle
        self.radioButtonRing = self.ui.radioButtonRing
        self.radioButtonMiddle = self.ui.radioButtonMiddle
        self.radioButtonIndex = self.ui.radioButtonIndex

        #hand sliders
        self.verticalSliderLittle = self.ui.verticalSliderLittle
        self.verticalSliderRing = self.ui.verticalSliderRing
        self.verticalSliderMiddle = self.ui.verticalSliderMiddle
        self.verticalSliderIndex = self.ui.verticalSliderIndex

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

        self.verticalSliderLittle.setProperty("index",0)
        self.verticalSliderRing.setProperty("index",1)
        self.verticalSliderMiddle.setProperty("index",2)
        self.verticalSliderIndex.setProperty("index",3)

        #connections
        for slider in self.ui.slidersContainer.findChildren(QSlider):
            slider.valueChanged.connect(self.pressure_slider_value_change)
        
        for radio in self.ui.fingerButtonContainer_2.findChildren(QRadioButton):
            radio.clicked.connect(self.finger_radio_clicked)

        for radio in self.ui.repeatButtonContainer.findChildren(QRadioButton):
            radio.clicked.connect(self.repeat_button_handler)

        self.durationSlider.valueChanged.connect(self.duration_slider_value_change)
        self.pressureButton.clicked.connect(self.pressure_button_handler)
        self.ZKeyButton.clicked.connect(self.zKey_button_handler)
        self.CKeyButton.clicked.connect(self.cKey_button_handler)
        self.confirmButton.clicked.connect(self.confirm_button_handler)

        self.modal.accepted.connect(self.handle_modal_finish)

        self.serialHandleClass.mesReceivedSignal.connect(self.message_received_handler)

    def duration_slider_value_change(self):
        print(f"slider: {self.sender().objectName()} - value: {self.sender().value()}")
        self.finger_info_dict.update({"duration":self.sender().value()})
        print(self.finger_info_dict)

    def zKey_button_handler(self):
        print(f"sender: {self.sender().objectName()} pressed!")
        self.modal.z_c_key_mode = 1
        self.modal.open()
    
    def cKey_button_handler(self):
        print(f"sender: {self.sender().objectName()} pressed!")
        self.modal.z_c_key_mode = 2
        self.modal.open()

    def confirm_button_handler(self):
        selection_check = any(self.selected_fingers)
        if (selection_check == False):
            logger.debug("Selecione uma combinação de teclas")
        else:
            print(f"sender: {self.sender().objectName()} pressed!")
            for radio in self.ui.repeatButtonContainer.findChildren(QRadioButton):
                radio.setChecked(False)
            for radio in self.ui.fingerButtonContainer_2.findChildren(QRadioButton):
                radio.setChecked(False)
            self.setEnabled(False)
            messages = self.confirm_messages_generator()
            for message in messages:
                self.send_serial_message(message)
            self.value_reset_watcher()
            self.setEnabled(True)

    def pressure_button_handler(self):
        print(f"sender: {self.sender().objectName()} pressed!")
        self.modal.z_c_key_mode = 0
        self.modal.open()
    
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
        message = self.pressure_slider_message_generator(self.sender().property("index"),self.p_value_array[self.sender().property("index")])
        self.send_serial_message(message)
        
    def finger_radio_clicked(self):
        self.selected_fingers[self.sender().property("index")] = self.sender().isChecked()
        print(self.selected_fingers)
        if self.value_reset_watcher() != True:
            self.finger_info_dict.update({"finger_combo":self.selected_fingers})
            print(self.finger_info_dict)

    def message_received_handler(self,response):
        logger.debug(f"mensagem recebida: {response}")

    #resets info to be transmited via serial
    def value_reset_watcher(self):
        counter = 0
        for radio in self.ui.fingerButtonContainer_2.findChildren(QRadioButton):
            if radio.isChecked():
                counter += 1
        if counter == 0:
            self.finger_info_dict = finger_base_value
            self.selected_fingers = [False,False,False,False,False]
            self.repeatOffButton.setChecked(True)
            self.repeatOnButton.setChecked(False)
            self.pressureButton.setText("Clique para selecionar")
            self.ZKeyButton.setText("Clique para selecionar")
            self.CKeyButton.setText("Clique para selecionar")
            self.durationSlider.setValue(1)
            print(self.finger_info_dict)
            return True
        return False
    
    def send_serial_message(self,message):
        self.serialHandleClass.open_port()
        logger.debug(f"mensagem enviada: {message}")
        self.serialHandleClass.send_message(message)
        
    def confirm_messages_generator(self):#!this does not account for the pressure values
        messages = []
        pairs = [(k, v) for (k, v) in self.finger_info_dict.items()]
        for i, (k,v)in enumerate(pairs):
            if v != None:
                match i:
                    case 0:
                        print("\n")
                        # messages.append(f"*")
                    case 1:
                        messages.append(f"*R{int(v)}")
                    case 2:
                        messages.append(f"*K{v}")
                    case 3:
                        messages.append(f"*T{v}")
        if self.nunchuck_info_dict["c_key"] != None: messages.append(f"*C{self.nunchuck_info_dict["c_key"]}")
        if self.nunchuck_info_dict["z_key"] != None: messages.append(f"*C{self.nunchuck_info_dict["z_key"]}")
        return  messages

    #when sending the serial message, finger indexes start at 1
    def pressure_slider_message_generator(self,finger,value):
        valueStr = value
        if(value < 10):#value always needs to be sent in a 3 digit format 
            valueStr = f"00{value}"
        elif(value < 100):
            valueStr = f"0{value}"
        message = "*M{}{}".format(finger+1,valueStr)
        return message

    def handle_modal_finish(self):#!beter logic maybe?
        key = self.modal.selected_key
        if self.modal.z_c_key_mode == 0:
            self.finger_info_dict.update({"key":key})
            self.pressureButton.setText(key)
            print(self.finger_info_dict)
        elif self.modal.z_c_key_mode == 1:
            self.nunchuck_info_dict.update({"z_key":key})
            self.ZKeyButton.setText(key)
            print(self.nunchuck_info_dict)
        else:
            self.nunchuck_info_dict.update({"c_key":key})
            self.CKeyButton.setText(key)
            print(self.nunchuck_info_dict)
        self.modal.selected_key = None
        self.modal.z_c_key_mode = 0
