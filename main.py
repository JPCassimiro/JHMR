import sys
from pathlib import Path

from ui import main_menu
from modules import log_class

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings, QTranslator

def init_settings(path, app):
    settings = QSettings(path, QSettings.IniFormat)
    language = settings.value("language")
    print(f"init_settings - language: {language} type: {type(language)}")
    if language != "None":
        translation = QTranslator(app)
        res = translation.load(language)
        if res:
            print(f"init_settings res: {res}")
            app.installTranslator(translation)
        

def main():
    base_path_config = Path("_internal/resources/config/config.ini")

    try:
        app = QApplication(sys.argv)
        init_settings(str(base_path_config),app)
        window = main_menu.MainMenuWindow()
        window.show()

        main_qss_path = Path(__file__).parent / "ui" / "qss" / "main.qss"
        with open(main_qss_path,'r') as f:
            _style = f.read()
            app.setStyleSheet(_style)
            
        app.exec()
    except Exception as e:
        log_class.logger.exception(f"Erro na execução do Main\nErro: {e}")


if __name__ == "__main__":
    main()