import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from ui import log_screen
import qasync
import asyncio
from modules import log_class

def main():
    try:
        app = QApplication(sys.argv)
        loop = qasync.QEventLoop(app)
        asyncio.set_event_loop(loop)
        window = log_screen.Loggerwindow()
        window.show()

        main_qss_path = Path(__file__).parent / "ui" / "qss" / "main.qss"
        with open(main_qss_path,'r') as f:
            _style = f.read()
            app.setStyleSheet(_style)

        app_close_event = asyncio.Event()
        app.aboutToQuit.connect(app_close_event.set)

        with loop:
            loop.run_forever()
    except Exception as e:
        log_class.logger.exception(f"Erro na execução do Main\nErro: {e}")


if __name__ == "__main__":
    main()