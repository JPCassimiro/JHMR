from PySide6.QtCore import QObject, QByteArray, Signal, Qt
from PySide6.QtTest import QSignalSpy

from ui.model.stacked_widget_screens.config_widget_model import ConfigWidgetModel

from shared_ui_modules.modules.bluetooth_serial_communication import SharedBtSerialComm

import pytestqt

class FakeSocket(QObject):
    
    readyRead = Signal()
    
    def __init__(self):
        super().__init__()

        self.data = None

    def readAll(self):
        if self.data:
            return QByteArray(self.data)
    
    def isOpen(self):
        return True

class FakeLogClass(QObject):
    
    def append_log(self,message):
        print(message)

class TestConfigWidget:
    
    def setup_method(self,method):
        self.serial_handle = SharedBtSerialComm()
        self.serial_handle.bt_socket = FakeSocket()
        self.fake_log = FakeLogClass()
        self.config_widget = ConfigWidgetModel(btSerialHandle=self.serial_handle,LogModel=self.fake_log)

    def test_pressure_value_change_success(self,qtbot):
        qtbot.addWidget(self.config_widget)

        assert self.config_widget.ZKeyButton.isEnabled() == False
        assert self.config_widget.CKeyButton.isEnabled() == False
        assert self.config_widget.pressureButton.isEnabled() == False
        assert self.config_widget.slider_array[0].slider.isEnabled() == False
        
        radio_button_little_pos = self.config_widget.radioButtonLittle.rect()      
        qtbot.mouseClick(
            self.config_widget.radioButtonLittle,
            Qt.LeftButton,
            pos = radio_button_little_pos.center()
        )
        
        assert self.config_widget.slider_array[0].slider.isEnabled() == True
        assert self.config_widget._selected_fingers == [True,False,False,False]

        slider_0_pos = self.config_widget.slider_array[0].slider.rect()

        qtbot.mouseClick(
            self.config_widget.slider_array[0].slider,
            Qt.LeftButton,
            pos = slider_0_pos.center()
        )
        
        assert self.config_widget.p_value_array[0] == 106
        assert self.config_widget.ZKeyButton.isEnabled() == True
        assert self.config_widget.CKeyButton.isEnabled() == True
        assert self.config_widget.pressureButton.isEnabled() == True
        

    def test_key_select_success(self,qtbot,monkeypatch):
        #add both stacked screen widget and key select modal
        qtbot.addWidget(self.config_widget)
        qtbot.addWidget(self.config_widget.key_select_modal)

        #patch the key_select_modal 
        #change the exec() function to none so the modal dosent get triggered and crashes the test
        monkeypatch.setattr(
            self.config_widget.key_select_modal,
            "exec",
            lambda: None
        )

        radio_button_little_pos = self.config_widget.radioButtonLittle.rect()      
        qtbot.mouseClick(
            self.config_widget.radioButtonLittle,
            Qt.LeftButton,
            pos = radio_button_little_pos.center()
        )

        slider_0_pos = self.config_widget.slider_array[0].slider.rect()

        qtbot.mouseClick(
            self.config_widget.slider_array[0].slider,
            Qt.LeftButton,
            pos = slider_0_pos.center()
        )

        pressure_button_pos = self.config_widget.pressureButton.rect()

        qtbot.mouseClick(
            self.config_widget.pressureButton,
            Qt.LeftButton,
            pos = pressure_button_pos.center()
        )
        
        qtbot.keyPress(self.config_widget.key_select_modal,"A")

        assert self.config_widget.key_select_modal.keyDisplayer.text().upper() == "A"

        assert self.config_widget.key_select_modal.selected_key == "A"

        self.config_widget.key_select_modal.buttonBox.buttons()[0].click()

        assert self.config_widget.param_select["key"] == "A"

    def test_value_reset_success(self,qtbot,monkeypatch):
        finger_base_value = {
            "repeat_key":False,
            "key":None,
            "duration":0
        }

        nunchuck_base_value = {
            "z_key":None,
            "c_key":None
        }
        #add both stacked screen widget and key select modal
        qtbot.addWidget(self.config_widget)
        qtbot.addWidget(self.config_widget.key_select_modal)

        #patch the key_select_modal 
        #change the exec() function to none so the modal dosent get triggered and crashes the test
        monkeypatch.setattr(
            self.config_widget.key_select_modal,
            "exec",
            lambda: None
        )

        radio_button_little_pos = self.config_widget.radioButtonLittle.rect()      
        qtbot.mouseClick(
            self.config_widget.radioButtonLittle,
            Qt.LeftButton,
            pos = radio_button_little_pos.center()
        )

        slider_0_pos = self.config_widget.slider_array[0].slider.rect()

        qtbot.mouseClick(
            self.config_widget.slider_array[0].slider,
            Qt.LeftButton,
            pos = slider_0_pos.center()
        )

        pressure_button_pos = self.config_widget.pressureButton.rect()

        qtbot.mouseClick(
            self.config_widget.pressureButton,
            Qt.LeftButton,
            pos = pressure_button_pos.center()
        )
        
        qtbot.keyPress(self.config_widget.key_select_modal,"A")

        assert self.config_widget.key_select_modal.keyDisplayer.text().upper() == "A"

        assert self.config_widget.key_select_modal.selected_key == "A"

        self.config_widget.key_select_modal.buttonBox.buttons()[0].click()

        assert self.config_widget.param_select["key"] == "A"
        
        qtbot.mouseClick(
            self.config_widget.slider_array[0].slider,
            Qt.LeftButton,
            pos = slider_0_pos.bottomRight()
        )

        self.config_widget.slider_array[0].slider.setFocus()
        
        for a in range(0,6):
            qtbot.keyClick(
                self.config_widget.slider_array[0].slider,
                Qt.Key_Down,
            )
        
        assert self.config_widget.p_value_array == [0,0,0,0]

        qtbot.mouseClick(
            self.config_widget.radioButtonLittle,
            Qt.LeftButton,
            pos = radio_button_little_pos.center()
        )

        assert self.config_widget.slider_array[0].slider.isEnabled() == False
        assert self.config_widget.ZKeyButton.isEnabled() == False
        assert self.config_widget.CKeyButton.isEnabled() == False
        assert self.config_widget.pressureButton.isEnabled() == False
        assert self.config_widget.slider_array[0].slider.isEnabled() == False
        assert self.config_widget.param_select == finger_base_value
        assert self.config_widget.nunchuck_info_dict == nunchuck_base_value
        
    def test_confirm_messages_generator_success(self,qtbot):
        qtbot.addWidget(self.config_widget)
        
        self.config_widget._selected_fingers = [True,True,True,True]
        self.config_widget.p_value_array = [100,10,20,30]
        self.config_widget.param_select["key"] = "A"


        res1, res2 = self.config_widget.confirm_messages_generator()

        expectedRes1 = ["*M1100","*M2010","*M3020","*M4030","*R0","*KA","*T0"]
        expectedRes2 = {
            "duration":0,
            "key":"A",
            "repeat":False,
            "little": 100,
            "ring":10,
            "middle":20,
            "index":30
        }

        assert res1 == expectedRes1
        assert res2 == expectedRes2

    def test_handle_modal_finish(self,qtbot,monkeypatch):
        qtbot.addWidget(self.config_widget)
        self.config_widget.key_select_modal.selected_key = "A"
        self.config_widget.key_select_modal.z_c_key_mode = 0

        self.config_widget.handle_modal_finish()

        assert self.config_widget.pressureButton.text() == "A"
        assert self.config_widget.param_select["key"] == "A"

    def test_assing_card_value_success(self,qtbot,monkeypatch):
        qtbot.addWidget(self.config_widget)

        config = {
            "duration": 0,
            "repeat": "True",
            "key": "A",
            "little": 10,
            "ring": 20,
            "middle": 30,
            "index": 40
        }

        self.config_widget.assing_card_values(config)

        assert self.config_widget.radioButtonIndex.isChecked() == True
        assert self.config_widget.radioButtonLittle.isChecked() == True
        assert self.config_widget.radioButtonRing.isChecked() == True
        assert self.config_widget.radioButtonMiddle.isChecked() == True
        for slider in self.config_widget.slider_array:
            assert slider.slider.isEnabled() == True
        assert self.config_widget.pressureButton.isEnabled() == True
        assert self.config_widget.pressureButton.text() == config["key"]
        assert self.config_widget.slider_array[0].slider.value() == 10
        assert self.config_widget.slider_array[1].slider.value() == 20
        assert self.config_widget.slider_array[2].slider.value() == 30
        assert self.config_widget.slider_array[3].slider.value() == 40

    def test_reset_screen_sucess(self,qtbot,monkeypatch):
        qtbot.addWidget(self.config_widget)
        
        self.config_widget.reset_screen()

        assert self.config_widget.radioButtonIndex.isChecked() == False
        assert self.config_widget.radioButtonLittle.isChecked() == False
        assert self.config_widget.radioButtonRing.isChecked() == False
        assert self.config_widget.radioButtonMiddle.isChecked() == False
        for slider in self.config_widget.slider_array:
            assert slider.slider.isEnabled() == False
            assert slider.slider.value() == 0
        assert self.config_widget.repeatOffButton.isChecked() == True        
        assert self.config_widget.repeatOnButton.isChecked() == False        
        assert self.config_widget.durationSlider.value() == 0
        assert self.config_widget.repeatOffButton.isEnabled() == False
        assert self.config_widget.repeatOnButton.isEnabled() == False
        assert self.config_widget.durationSlider.isEnabled() == False
    
    def test_finger_radio_button_click(self,qtbot,monkeypatch):
        qtbot.addWidget(self.config_widget)

        radio_buttons = []

        for radio in self.config_widget.finger_radio_array:
            radio_buttons.append(radio)

        for button in radio_buttons:
            qtbot.mouseClick(
                button,
                Qt.LeftButton,
                pos = button.rect().center()
            )

        for radio in self.config_widget.finger_radio_array:
            assert radio.isChecked() == True

        for slider in self.config_widget.slider_array:
            slider.slider.isEnabled() == True

    def test_duration_slider_value_change_success(self,qtbot,monkeypatch):
        qtbot.addWidget(self.config_widget)

        qtbot.mouseClick(
            self.config_widget.radioButtonLittle,
            Qt.LeftButton,
            pos = self.config_widget.radioButtonLittle.rect().center()
        )

        qtbot.mouseClick(
            self.config_widget.durationSlider,
            Qt.LeftButton,
            pos = self.config_widget.durationSlider.rect().center()
        )

        self.config_widget.param_select["duration"] == 4