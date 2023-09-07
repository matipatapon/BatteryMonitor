import pytest
from objects.BatteryMonitor import BatteryMonitor
from test.mocks.BatteryInfoGetterMock import BatteryInfoGetterMock
from constants import BATTERY_LEVEL_CHECK_INTERVAL
from test.mocks.SpeakerMock import SpeakerMock
from test.mocks.TimeManagerMock import TimeManagerMock

@pytest.fixture
def batteryInfoGetterMock():
    return BatteryInfoGetterMock(100)

@pytest.fixture
def speakerMock():
    return SpeakerMock()

@pytest.fixture
def timeManagerMock():
    return TimeManagerMock()

class TestBatteryMonitor :
    def test_speakBatteryLevelWhenItIsBelowTrigger(self, batteryInfoGetterMock, speakerMock, timeManagerMock):
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock, [100])

        batteryInfoGetterMock.setBatteryLevel(90)
        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 1
        assert speakerMock.getSpeakTextCallCount() == 1
        assert timeManagerMock.getWaitCallCount() == 1
        assert f"{90}" in speakerMock.getLastReceivedText()

    def test_speakBatteryLevelWhenItHittedTheTrigger(self, batteryInfoGetterMock, speakerMock, timeManagerMock):
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock, [100])

        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 1
        assert speakerMock.getSpeakTextCallCount() == 1
        assert timeManagerMock.getWaitCallCount() == 1

        assert f"{100}" in speakerMock.getLastReceivedText()

    def test_doNotSpeakBatteryLevelWhenItIsAboveTrigger(self, batteryInfoGetterMock, speakerMock, timeManagerMock):
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock, [90])

        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 1
        assert speakerMock.getSpeakTextCallCount() == 0
        assert timeManagerMock.getWaitCallCount() == 1

    def test_doNotReactMultipleTimesToSameTrigger(self, batteryInfoGetterMock, speakerMock, timeManagerMock):
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock, [100])

        sut.runStage()
        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 2
        assert speakerMock.getSpeakTextCallCount() == 1
        assert timeManagerMock.getWaitCallCount() == 2

        assert f"{100}" in speakerMock.getLastReceivedText()

    def test_resetTriggerWhenBatteryLevelIsGreaterOrEqualToThatTrigger(self, batteryInfoGetterMock, speakerMock, timeManagerMock):
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock, [50])

        batteryInfoGetterMock.setBatteryLevel(40)
        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(60)
        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(45)
        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 3
        assert speakerMock.getSpeakTextCallCount() == 2
        assert timeManagerMock.getWaitCallCount() == 3

        assert f"{45}" in speakerMock.getLastReceivedText()

    def test_speakTextForMultipleTriggers(self, batteryInfoGetterMock, speakerMock, timeManagerMock):
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock, [40, 50])

        batteryInfoGetterMock.setBatteryLevel(50)
        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(40)
        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 2
        assert speakerMock.getSpeakTextCallCount() == 2
        assert timeManagerMock.getWaitCallCount() == 2

        assert f"{40}" in speakerMock.getLastReceivedText()

    def test_triggerAllTriggersAboveBatteryLevel(self, batteryInfoGetterMock, speakerMock, timeManagerMock):
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock, [40, 50])

        batteryInfoGetterMock.setBatteryLevel(40)
        sut.runStage()

        batteryInfoGetterMock.setBatteryLevel(30)
        sut.runStage()

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 2
        assert speakerMock.getSpeakTextCallCount() == 1
        assert timeManagerMock.getWaitCallCount() == 2

        assert f"{40}" in speakerMock.getLastReceivedText()

    def test_handleComplexScenario(self, batteryInfoGetterMock, speakerMock, timeManagerMock):
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock, [50, 30, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        sut.runStage()
        assert speakerMock.getSpeakTextCallCount() == 0

        batteryInfoGetterMock.setBatteryLevel(5)
        sut.runStage()
        assert speakerMock.getSpeakTextCallCount() == 1

        batteryInfoGetterMock.setBatteryLevel(8)
        sut.runStage()
        assert speakerMock.getSpeakTextCallCount() == 1

        batteryInfoGetterMock.setBatteryLevel(5)
        sut.runStage()
        assert speakerMock.getSpeakTextCallCount() == 2

        batteryInfoGetterMock.setBatteryLevel(1)
        sut.runStage()
        assert speakerMock.getSpeakTextCallCount() == 3

        batteryInfoGetterMock.setBatteryLevel(50)
        sut.runStage()
        assert speakerMock.getSpeakTextCallCount() == 3

        batteryInfoGetterMock.setBatteryLevel(50)
        sut.runStage()
        assert speakerMock.getSpeakTextCallCount() == 3

        batteryInfoGetterMock.setBatteryLevel(60)
        sut.runStage()
        assert speakerMock.getSpeakTextCallCount() == 3

        batteryInfoGetterMock.setBatteryLevel(50)
        sut.runStage()
        assert speakerMock.getSpeakTextCallCount() == 4

        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 9
        assert timeManagerMock.getWaitCallCount() == 9

        assert f"{5}" in speakerMock.getLastReceivedText()

    def test_waitCustomAmountOfTime(self, batteryInfoGetterMock, speakerMock, timeManagerMock):
        sut = BatteryMonitor(batteryInfoGetterMock, speakerMock, timeManagerMock, [])

        sut.runStage(69)
    
        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 1
        assert speakerMock.getSpeakTextCallCount() == 0
        assert timeManagerMock.getWaitCallCount() == 1
        assert timeManagerMock.getLastReceivedTime() == 69
