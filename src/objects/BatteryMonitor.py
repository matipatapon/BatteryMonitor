from constants import BATTERY_LEVEL_STEP, BATTERY_LEVEL_CHECK_INTERVAL
from test.runTest import runTest
from test.mocks.BatteryInfoGetterMock import BatteryInfoGetterMock
from test.mocks.SpeakerMock import SpeakerMock
from test.mocks.TimeManagerMock import TimeManagerMock


class BatteryMonitor:
    def __init__(
        self,
        batteryInfoGetter,
        speaker,
        timeManager
    ):
        self._batteryInfoGetter = batteryInfoGetter
        self._speaker = speaker
        self._timeManager = timeManager
        self._previousBatteryLevel = 1000
        self._batteryLevelChange = 0

    def runStage(self, time = BATTERY_LEVEL_CHECK_INTERVAL):
        currentBatteryLevel = self._batteryInfoGetter.getBatteryLevel()
        self._batteryLevelChange += currentBatteryLevel - self._previousBatteryLevel
        if self._batteryLevelChange <= -BATTERY_LEVEL_STEP:
            self._batteryLevelChange = 0
            self._speaker.speakText(f"{currentBatteryLevel}% battery left")
        elif self._batteryLevelChange >= BATTERY_LEVEL_STEP:
            self._batteryLevelChange = 0

        self._previousBatteryLevel = currentBatteryLevel
        self._timeManager.wait(time)

    def run(self):
        while True:
            self.runStage()


def BatteryMonitorTests():
    EntryBatteryLevel = 50

    def BatteryMonitorShould_GetBatteryLevelSpeakItThenWait():
        batteryInfoGetterMock = BatteryInfoGetterMock(EntryBatteryLevel)
        speakerMock = SpeakerMock()
        timeManagerMock = TimeManagerMock()
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock)

        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 1
        assert speakerMock.getSpeakTextCallCount() == 1
        assert timeManagerMock.getWaitCallCount() == 1

        assert f"{EntryBatteryLevel}" in speakerMock.getLastReceivedText()
        assert timeManagerMock.getLastReceivedTime() == BATTERY_LEVEL_CHECK_INTERVAL

    runTest(BatteryMonitorShould_GetBatteryLevelSpeakItThenWait)


    def BatteryMonitorShould_NotSpeakBatteryLevelWhenChangeIsNotGreaterOrEqualToStep():
        batteryInfoGetterMock = BatteryInfoGetterMock(EntryBatteryLevel)
        speakerMock = SpeakerMock()
        timeManagerMock = TimeManagerMock()
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock)

        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(EntryBatteryLevel - BATTERY_LEVEL_STEP + 1)

        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 2
        assert speakerMock.getSpeakTextCallCount() == 1
        assert timeManagerMock.getWaitCallCount() == 2

        assert f"{EntryBatteryLevel}" in speakerMock.getLastReceivedText()
        
    runTest(BatteryMonitorShould_NotSpeakBatteryLevelWhenChangeIsNotGreaterOrEqualToStep)

    def BatteryMonitorShould_NotSpeakBatteryLevelWhenChangeIsNotGreaterThanStep():
        batteryInfoGetterMock = BatteryInfoGetterMock(EntryBatteryLevel)
        speakerMock = SpeakerMock()
        timeManagerMock = TimeManagerMock()
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock)

        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(EntryBatteryLevel - BATTERY_LEVEL_STEP)

        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 2
        assert speakerMock.getSpeakTextCallCount() == 2
        assert timeManagerMock.getWaitCallCount() == 2

        assert f"{EntryBatteryLevel - BATTERY_LEVEL_STEP}" in speakerMock.getLastReceivedText()
        
    runTest(BatteryMonitorShould_NotSpeakBatteryLevelWhenChangeIsNotGreaterThanStep)

    def BatteryMonitorShould_NotSpeakBatteryLevelWhenItsRising():
        batteryInfoGetterMock = BatteryInfoGetterMock(EntryBatteryLevel)
        speakerMock = SpeakerMock()
        timeManagerMock = TimeManagerMock()
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock)

        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(EntryBatteryLevel + BATTERY_LEVEL_STEP)

        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 2
        assert speakerMock.getSpeakTextCallCount() == 1
        assert timeManagerMock.getWaitCallCount() == 2

        assert f"{EntryBatteryLevel}" in speakerMock.getLastReceivedText()
        
    runTest(BatteryMonitorShould_NotSpeakBatteryLevelWhenItsRising)

    def BatteryMonitorShould_SpeakBatteryLevelWhenItRaisedAndDropped():
        batteryInfoGetterMock = BatteryInfoGetterMock(EntryBatteryLevel)
        speakerMock = SpeakerMock()
        timeManagerMock = TimeManagerMock()
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock)

        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(EntryBatteryLevel + BATTERY_LEVEL_STEP)

        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(EntryBatteryLevel)

        sut.runStage()


        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 3
        assert speakerMock.getSpeakTextCallCount() == 2
        assert timeManagerMock.getWaitCallCount() == 3

        assert f"{EntryBatteryLevel}" in speakerMock.getLastReceivedText()
        
    runTest(BatteryMonitorShould_SpeakBatteryLevelWhenItRaisedAndDropped)

    def BatteryMonitorShould_NotSpeakBatteryLevelWhenItRaisedAndDroppedButNotExceededStep():
        batteryInfoGetterMock = BatteryInfoGetterMock(EntryBatteryLevel)
        speakerMock = SpeakerMock()
        timeManagerMock = TimeManagerMock()
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock)

        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(EntryBatteryLevel + BATTERY_LEVEL_STEP - 1)

        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(EntryBatteryLevel - BATTERY_LEVEL_STEP + 1)

        sut.runStage()


        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 3
        assert speakerMock.getSpeakTextCallCount() == 1
        assert timeManagerMock.getWaitCallCount() == 3

        assert f"{EntryBatteryLevel}" in speakerMock.getLastReceivedText()
        
    runTest(BatteryMonitorShould_NotSpeakBatteryLevelWhenItRaisedAndDroppedButNotExceededStep)
