import subprocess
import pathlib
from .log_class import logger
from PySide6.QtCore import QProcess, Signal, QObject

class ProcessRunnerClass(QObject):
    processFinished = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        #process setup
        self.p = QProcess()

        #connecting funtions to signals
        self.p.finished.connect(self.process_finish_handler)
        self.p.errorOccurred.connect(lambda error: logger.debug(error))
        self.p.readyReadStandardError.connect(self.read_handler)
        self.p.readyReadStandardError.connect(self.read_handler)

    def run(self):
        self.p.start('btpair -p -n"ESP32"')

    #read process stream
    def read_handler(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        logger.debug(stderr)
    
    #emits finish message
    def process_finish_handler(self):
        self.processFinished.emit()
        logger.debug("Processo de pareamento finalizado")