from shared_ui_modules.ui.model.stacked_widget_screens.game_config_profile_model import SharedGameProfileModel

from shared_ui_modules.modules.log_class import logger
from ui.model.components.config_card_model import ConfigCardModel


from modules.json_writer import JsonWriterClass

class GameProfileModel(SharedGameProfileModel):

    def __init__(self, logModel, dbHandle, btSerialHandle):
        super().__init__(logModel, dbHandle, btSerialHandle)

        self.initialize_module()
        
    def get_config_card(self, args):
        return ConfigCardModel(args[0],args[1])

    def get_json_writer(self):
        return JsonWriterClass()

    def standardize_serial_message(self,binding_dict):
        messages = []

        for index, finger in enumerate(["little", "ring", "middle" , "index"]):
            value = binding_dict[finger]
            if int(value) != 0:
                valueStr = int(value)
                if(int(value) < 10):#value always needs to be sent in a 3 digit format 
                    valueStr = f"00{int(value)}"
                elif(int(value) < 100):
                    valueStr = f"0{int(value)}"
                messages.append("*M{}{}".format(index+1, valueStr))
        
        if binding_dict["repeat"] == "True":
            messages.append("*R1")
        else:
            messages.append("*R0")
        
        messages.append("*K" + binding_dict["key"])
        messages.append("*T" + binding_dict["duration"])
        
        return messages
