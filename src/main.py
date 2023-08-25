from objects.BatteryMonitor import BatteryMonitor
from objects.BatteryInfoGetter import BatteryInfoGetter
from objects.Speaker import Speaker
from objects.TimeManager import TimeManager
from test.runTest import runTest


def MainITs():
    def RunBatteryMonitorStage():
        batteryInfoGetter = BatteryInfoGetter()
        speaker = Speaker()
        timeManager = TimeManager()
        batteryMonitor = BatteryMonitor(batteryInfoGetter, speaker, timeManager)

        batteryMonitor.runStage(1)

    runTest(RunBatteryMonitorStage)


if __name__ == "__main__":
    batteryInfoGetter = BatteryInfoGetter()
    speaker = Speaker()
    timeManager = TimeManager()
    batteryMonitor = BatteryMonitor(batteryInfoGetter, speaker, timeManager)

    batteryMonitor.run()
