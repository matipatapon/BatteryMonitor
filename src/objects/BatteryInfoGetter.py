from os import listdir
from os.path import isfile, join
from objects.Logger import Logger

BATTERY_PARENT_FOLDER = "/sys/class/power_supply/"


class BatteryInfoGetter:
    def __init__(self):
        self._logger = Logger("BatteryInfoGetter")

    def getBatteryLevel(self):
        batteryFolders = self._getListOfBatteries()
        assert len(batteryFolders) == 1
        
        capacityFolder = batteryFolders[0] + "/capacity"
        f = open(capacityFolder, "r")
        capacity = int(f.read())
        self._logger.log(f"Capacity is {capacity} readed from {capacityFolder}")
        return capacity

    def _getListOfBatteries(self):
        return [BATTERY_PARENT_FOLDER + batteryFolder for batteryFolder in listdir(BATTERY_PARENT_FOLDER) if not isfile(join(BATTERY_PARENT_FOLDER, batteryFolder)) and "BAT" in batteryFolder]

    
def BatteryInfoGetterITs():
    def BatteryInfoShould_ReadBatteryLevelFromFile():
        sut = BatteryInfoGetter()
        
        batteryLevel = sut.getBatteryLevel()
        
        assert batteryLevel >= 0 and batteryLevel <= 100
