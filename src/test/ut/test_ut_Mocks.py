import pytest
from test.mocks.BatteryInfoGetterMock import BatteryInfoGetterMock
from test.mocks.SpeakerMock import SpeakerMock
from test.mocks.TimeManagerMock import TimeManagerMock

@pytest.fixture
def batteryInfoGetterMock():
    return BatteryInfoGetterMock(1)

class TestBatteryInfoGetterMock:
    def test_setBatteryLevelInConstructor(self, batteryInfoGetterMock):
        assert batteryInfoGetterMock.getBatteryLevel() == 1
        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 1

    def test_setBatteryLevel(self, batteryInfoGetterMock):
        batteryInfoGetterMock.setBatteryLevel(2)

        assert batteryInfoGetterMock.getBatteryLevel() == 2
        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 1


    def test_handleMultipleGetBatteryLevelCalls(self, batteryInfoGetterMock):
        batteryInfoGetterMock.getBatteryLevel()
        batteryInfoGetterMock.getBatteryLevel()
        
        assert batteryInfoGetterMock.getBatteryLevelCallCount() == 2

@pytest.fixture
def speakerMock():
    return SpeakerMock()

class TestSpeakerMock:
    def test_returnDefaultCallCount(self, speakerMock):
        assert speakerMock.getSpeakTextCallCount() == 0

    def test_returnCallCount(self, speakerMock):
        speakerMock.speakText("SomeText")
        assert speakerMock.getSpeakTextCallCount() == 1

    def test_returnLastReceivedText(self, speakerMock):
        speakerMock.speakText("SomeText")
        assert speakerMock.getLastReceivedText() == "SomeText"

@pytest.fixture
def timeManagerMock():
    return TimeManagerMock()

class TestTimeManagerMock:
    def test_returnDefaultCallCount(self, timeManagerMock):
        assert timeManagerMock.getWaitCallCount() == 0

    def test_returnCallCount(self, timeManagerMock):
        timeManagerMock.wait(5)
        assert timeManagerMock.getWaitCallCount() == 1

    def test_returnLastReceivedTime(self, timeManagerMock):
        timeManagerMock.wait(5)
        assert timeManagerMock.getLastReceivedTime() == 5
