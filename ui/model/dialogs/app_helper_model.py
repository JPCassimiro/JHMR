from shared_ui_modules.ui.model.dialogs.app_helper_model import SharedAppHelperModel

from PySide6.QtCore import QCoreApplication

class AppHelperModule(SharedAppHelperModel):
    def __init__(self):
        super().__init__()
        
        QCoreApplication.translate("AppHelperDialogText","<a href='https://github.com/JPCassimiro/jhmr'>Repostório do Github<a/>")
        
        self.initialize_module()

    def get_repo_string(self):
        return QCoreApplication.translate("AppHelperDialogText","<a href='https://github.com/JPCassimiro/jhmr'>Repostório do Github<a/>")