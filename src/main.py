from objects.BatteryMonitor import BatteryMonitor
from objects.BatteryInfoGetter import BatteryInfoGetter
from objects.Speaker import Speaker
from objects.TimeManager import TimeManager
from constants import BATTERY_LEVEL_TRIGGERS


if __name__ == "__main__":
    batteryInfoGetter = BatteryInfoGetter()
    speaker = Speaker()
    timeManager = TimeManager()
    batteryMonitor = BatteryMonitor(batteryInfoGetter, speaker, timeManager, BATTERY_LEVEL_TRIGGERS)

    batteryMonitor.run()
