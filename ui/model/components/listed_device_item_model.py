from ui.views.listed_device_item_ui import Ui_listedDeviceForm

from PySide6.QtWidgets import QWidget

class ListedDeviceItemModel(QWidget):
    

    def __init__(self, deviceDict):
        
        super().__init__()

        #ui setup
        self.ui = Ui_listedDeviceForm()
        self.ui.setupUi(self)

        #get ui elements
        self.listedDeviceNameLabel = self.ui.listedDeviceNameLabel
        self.listedDeviceIconLabel = self.ui.listedDeviceIconLabel
        self.listedDeviceAddressLabel = self.ui.listedDeviceAddressLabel
        
        self.listedDeviceIconLabel.hide()

        self.deviceDict = deviceDict
        
        # self.deviceDict["name"]    
        # self.deviceDict["mac"]
        # self.deviceDict["listName"]
        # self.deviceDict["id"]
        # self.deviceDict["uuid"]
        # self.deviceDict["serviceId"]
        # self.deviceDict["turned_on"]
    
        self.listedDeviceNameLabel.setText(self.deviceDict["listName"] if self.deviceDict["turned_on"] == True else f"{self.deviceDict["listName"]}: Desligado")
        self.listedDeviceAddressLabel.setText(self.deviceDict["mac"])
        