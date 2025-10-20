import json
from modules.log_class import logger
from PySide6.QtCore import QObject
from pathlib import Path

class JsonWriterClass(QObject):
    def __init__(self):
        super().__init__()
        
        self.base_path = Path("_internal/resources/latest_bindings")
        
    def update_config_file(self,userId,bindingDict):
        json_path = self.base_path / f"user_{userId}"
        json_path.mkdir(parents=True, exist_ok=True)
        json_file = json_path / f"user_bindings.json"
        data = {
            "user": userId,
            "bindings": {}
        }
        
        binding_translate = ''.join(['1' if b else '0' for b in bindingDict["combo"]])
        
        if json_file.exists():
            with open(json_file, 'r') as file:
                data = json.load(file)

                if binding_translate in data["bindings"]:
                    data["bindings"][binding_translate].update({
                        "duration": f"{bindingDict["duration"]}",
                        "key": f"{bindingDict["key"]}",
                        "repeat": f"{bindingDict["repeat"]}",
                        "pressure_1": f"{bindingDict['pressure_1']}",
                        "pressure_2": f"{bindingDict['pressure_2']}",
                        "pressure_3": f"{bindingDict['pressure_3']}",
                        "pressure_4": f"{bindingDict['pressure_4']}"
                    })
                    
                else:
                    data["bindings"][binding_translate] = {
                        "duration":f"{bindingDict["duration"]}",
                        "key": f"{bindingDict["key"]}",
                        "repeat": f"{bindingDict["repeat"]}",
                        "pressure_1": f"{bindingDict['pressure_1']}",
                        "pressure_2": f"{bindingDict['pressure_2']}",
                        "pressure_3": f"{bindingDict['pressure_3']}",
                        "pressure_4": f"{bindingDict['pressure_4']}"
                    }
                    
                with open(json_file, 'w') as file:
                    json.dump(data, file, indent=4)
        else:
            data["bindings"][binding_translate] = {
                        "duration":f"{bindingDict["duration"]}",
                        "key": f"{bindingDict["key"]}",
                        "repeat": f"{bindingDict["repeat"]}",
                        "pressure_1": f"{bindingDict['pressure_1']}",
                        "pressure_2": f"{bindingDict['pressure_2']}",
                        "pressure_3": f"{bindingDict['pressure_3']}",
                        "pressure_4": f"{bindingDict['pressure_4']}"
                    }

            data_str = json.dumps(data, indent=4)
            with open(json_file, 'w+') as file:
                file.write(data_str)
            
        logger.info(f"Arquivo de configuração do usuário {userId} atualizado.")
        
    