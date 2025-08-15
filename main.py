import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from ui import log_screen
import qasync
import asyncio

def main():
    app = QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)
    window = log_screen.Loggerwindow()
    window.show()

    with loop:
        loop.run_forever()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()