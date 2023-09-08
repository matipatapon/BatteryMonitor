from objects.Logger import Logger
from constants import BATTERY_LEVEL_CHECK_INTERVAL


class BatteryTrigger:
    def __init__(
        self,
        batteryLevel
    ):
        self.batteryLevel = batteryLevel
        self.triggered = False

    def reset(self):
        self.triggered = False


class BatteryMonitor:
    def __init__(
        self,
        batteryInfoGetter,
        speaker,
        timeManager,
        batteryLevelsToTriggerNotification
    ):
        self._batteryInfoGetter = batteryInfoGetter
        self._speaker = speaker
        self._timeManager = timeManager
        self._logger = Logger("BatteryMonitor")
        self._batteryTriggers = [BatteryTrigger(batteryLevel) for batteryLevel in batteryLevelsToTriggerNotification]

    def runStage(self, time = BATTERY_LEVEL_CHECK_INTERVAL):
        currentBatteryLevel = self._batteryInfoGetter.getBatteryLevel()
        self._sayBatteryLevelOnTrigger(currentBatteryLevel)
        self._resetBatteryTriggers(currentBatteryLevel)
        self._timeManager.wait(time)

    def _sayBatteryLevelOnTrigger(self, batteryLevel):
        wasBatteryLevelSaid = False
        for batteryTrigger in self._batteryTriggers:
            if batteryTrigger.batteryLevel >= batteryLevel and not batteryTrigger.triggered:
                if not wasBatteryLevelSaid :
                    self._speaker.speakText(f"{batteryLevel} percent of battery left")
                    wasBatteryLevelSaid = True
                batteryTrigger.triggered = True
                self._logger.log(f"BatteryTrigger #{batteryTrigger.batteryLevel}# triggered")

    def _resetBatteryTriggers(self, batteryLevel):
        for batteryTrigger in self._batteryTriggers:
            if batteryTrigger.batteryLevel < batteryLevel and batteryTrigger.triggered:
                batteryTrigger.reset()
                self._logger.log(f"BatteryTrigger #{batteryTrigger.batteryLevel}# restarted")

    def run(self):
        while True:
            self.runStage()
