from os import listdir
from os.path import isfile, join
from objects.Logger import Logger

BATTERY_PARENT_FOLDER = "/sys/class/power_supply/"


class BatteryInfoGetter:
    def __init__(self):
        self._logger = Logger("BatteryInfoGetter")

    def getBatteryLevel(self):
        return self._readBatteryLevelFromFile(self._getBatteryFolder() + "/capacity")

    def _getBatteryFolder(self):
        batteryFolders = [BATTERY_PARENT_FOLDER + batteryFolder for batteryFolder in listdir(BATTERY_PARENT_FOLDER) if not isfile(join(BATTERY_PARENT_FOLDER, batteryFolder)) and "BAT" in batteryFolder]
        assert len(batteryFolders) == 1
        return batteryFolders[0]

    def _readBatteryLevelFromFile(self, path):
        f = open(path, "r")
        capacity = int(f.read())
        f.close()
        self._logger.log(f"Capacity is {capacity} readed from {path}")
        return capacity


def BatteryInfoGetterITs():
    def BatteryInfoShould_ReadBatteryLevelFromFile():
        sut = BatteryInfoGetter()
        batteryLevel = sut.getBatteryLevel()
        assert batteryLevel >= 0 and batteryLevel <= 100
