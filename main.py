import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from ui import main_menu
from modules import log_class

def main():
    try:
        app = QApplication(sys.argv)
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