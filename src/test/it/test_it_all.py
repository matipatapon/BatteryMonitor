from objects.BatteryMonitor import BatteryMonitor
from objects.BatteryInfoGetter import BatteryInfoGetter
from objects.Speaker import Speaker
from objects.TimeManager import TimeManager

def test_runBatteryMonitorStage():
    batteryInfoGetter = BatteryInfoGetter()
    speaker = Speaker()
    timeManager = TimeManager()
    batteryMonitor = BatteryMonitor(batteryInfoGetter, speaker, timeManager, [50, 30, 10])

    batteryMonitor.runStage(1)

def test_readBatteryLevelFromFile():
    sut = BatteryInfoGetter()
    batteryLevel = sut.getBatteryLevel()
    assert batteryLevel >= 0 and batteryLevel <= 100

def test_speakerSayText():
    sut = Speaker()
    sut.speakText("Speaker works if you hear it and also Ryszard is the best")
