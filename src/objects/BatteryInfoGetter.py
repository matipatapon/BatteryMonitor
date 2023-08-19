from os import listdir
from os.path import isfile, join


BATTERY_PARENT_FOLDER = "/sys/class/power_supply/"


class BatteryInfoGetter:
    def getBatteryLevel(self):
        batteryFolders = self._getListOfBatteries()
        assert len(batteryFolders) == 1

        f = open(batteryFolder[0] + "/capacity", "r")
        return int(f.read())

    def _getListOfBatteries(self):
        return [BATTERY_PARENT_FOLDER + batteryFolder for batteryFolder in listdir(BATTERY_PARENT_FOLDER) if not isfile(join(BATTERY_PARENT_FOLDER, batteryFolder))]

    
def BatteryInfoGetterTests():
    def BatteryInfoShould_ReadBatteryLevelFromFile():
        sut = BatteryInfoGetter()
        
        batteryLevel = sut.getBatteryLevel()
        
        assert batteryLevel >= 0 and batteryLevel <= 100
