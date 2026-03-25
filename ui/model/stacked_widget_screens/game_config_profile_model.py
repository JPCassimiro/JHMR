from ui.views.game_profile_widget_ui import Ui_gameProfileWidgetForm

from modules.log_class import logger

from PySide6.QtWidgets import QWidget, QListWidgetItem

import json
from pathlib import Path

class GameProfileModel(QWidget):
    def __init__(self, logModel, dbHandle):
        super().__init__()

        #module setup
        self.logModel = logModel
        self.dbHandle = dbHandle

        #ui setup
        self.ui = Ui_gameProfileWidgetForm()
        self.ui.setupUi(self)

        #get ui elements
        self.profileListView = self.ui.profileListView
        self.gameProfileList = self.ui.gameProfileList

        #variable setup
        self.profile_list = []
        self.current_user = None

    def assing_user(self,user_index):
        self.current_user = user_index
        self.populate_game_profile_list()

    def get_profile_list(self):
        try:
            self.profile_list = []
            q = """select 
                        g.id,
                        g.name
                        from game_profile as g
                            where patient_id = ?;"""
            res = self.dbHandle.execute_single_query(q,[self.current_user])

            if res:
                self.profile_list.append([res[0][0], res[0][1]])
        except Exception as e:
            logger.error(f"erro ao obter lista de perfís: {e}")

    def populate_game_profile_list(self):
        try:
            logger.debug(f"populate_game_profile_list self.current_user:{self.current_user}")
            self.gameProfileList.clear()
            self.get_profile_list()
            if len(self.profile_list) > 0:
                for profile in self.profile_list:
                    logger.debug(f"populate_game_profile_list profile:{profile}")
                    item = QListWidgetItem()
                    item.setData(0,profile[0])
                    item.setText(profile[1])
                    self.gameProfileList.addItem(item)
        except Exception as e:
            logger.error(f"erro ao atualizar lista: {e}")
                
    def read_json_file(self):
        path = Path("_internal/resources/latest_bindings")        
        file = path / f"user_bindings.json"

        with open(file, 'r') as f:
            data = json.load(f)
        
        return data
        
    # def create_new_profile(self):
        

    def create_new_config(self):
        config = self.read_json_file()

        q = """insert into bindings ()"""
                
        
        
