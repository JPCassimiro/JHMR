from ui.views.user_item_ui import Ui_userItemForm
from ui.model.dialogs.register_model import RegisterModel
from modules.log_class import logger
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal

class UserItemModel(QWidget):
    
    updateList = Signal(int)
    
    def __init__(self, infoDict, DbHandleClass):
        super().__init__()
        
        #ui setup
        self.ui = Ui_userItemForm()
        self.ui.setupUi(self)
        
        self.register_modal = RegisterModel()
        
        self.dbHandleClass = DbHandleClass

        self.item_id = infoDict["id"]
        self.item_table = infoDict["table"]
        
        self.info_dict = infoDict.copy()
        
        #get elements
        self.imageLabel = self.ui.itemImageLabel
        self.nameLabel = self.ui.nameLabel
        self.functionLabel = self.ui.functionLabel
        self.removeButton = self.ui.removeButton
        self.editButton = self.ui.editButton
        
        self.imageLabel.setMaximumHeight(100)
        self.imageLabel.setMaximumWidth(100)
        
        self.fill_fields(infoDict)
        
        #connections
        self.removeButton.clicked.connect(self.remove_button_handler)
        self.editButton.clicked.connect(self.edit_button_handler)
        self.register_modal.accepted.connect(self.edit_user)
        
    def fill_fields(self,infoDict):
        self.set_image(infoDict["image_path"])
        self.nameLabel.setText(infoDict["name"])
        self.functionLabel.setText(infoDict["details"])

    def set_image(self,img_path):
        try:
            img = QPixmap()
            if img.load(img_path):
                self.imageLabel.setPixmap(img)
                self.imageLabel.setScaledContents(True)
            else:
                logger.error(f"Erro ao cerregar imagem no caminho: {img_path}")
        except Exception as e:
            logger.error(f"Erro ao atribuir uma imagem na lista: {e}")
        
    def remove_button_handler(self):
        q = f"delete from {self.item_table} where id = ? returning name;"
        res = self.dbHandleClass.execute_single_query(q,[self.item_id])
        if res: 
            logger.debug(f"{res[0][0]} removido")
            self.info_dict = None
            self.updateList.emit(self.item_id)
        
    def edit_user(self):
        update_info = self.register_modal.infoDict.copy()
        q = f"update {self.item_table} set name = ?, details = ?, image_path = ? where id = ? returning id;"
        res = self.dbHandleClass.execute_single_query(q,[update_info["name"],update_info["details"],update_info["image_path"],self.item_id])
        if res:
            self.info_dict = update_info.copy()
            logger.debug(f"info do id {res[0][0]} da tabela {self.item_table} foi atualizado")
            self.updateList.emit(self.item_id)
    
    def edit_button_handler(self):
        self.register_modal.infoDict = self.info_dict.copy()
        self.register_modal.complete_fields()
        self.register_modal.exec()
