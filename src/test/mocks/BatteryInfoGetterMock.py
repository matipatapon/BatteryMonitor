from ..runTest import runTest


class BatteryInfoGetterMock:
    def __init__(self, batteryLevel):
        self.setBatteryLevel(batteryLevel)
        self._batteryLevelCallCount = 0

    def setBatteryLevel(self, batteryLevel):
        self._batteryLevel = batteryLevel

    def getBatteryLevel(self):
        self._batteryLevelCallCount += 1
        return self._batteryLevel

    def getBatteryLevelCallCount(self):
        return self._batteryLevelCallCount

def BatteryInfoGetterMockUTs():
    def BatteryInfoGetterMockShould_SetBatteryLevelInConstructor():
        sut = BatteryInfoGetterMock(1)

        assert sut.getBatteryLevel() == 1
        assert sut.getBatteryLevelCallCount() == 1

    runTest(BatteryInfoGetterMockShould_SetBatteryLevelInConstructor)

    def BatteryInfoGetterMockShould_SetBatteryLevel():
        sut = BatteryInfoGetterMock(1)

        sut.setBatteryLevel(2)

        assert sut.getBatteryLevel() == 2
        assert sut.getBatteryLevelCallCount() == 1

    runTest(BatteryInfoGetterMockShould_SetBatteryLevel)

    def BatteryInfoGetterMockShould_HandleMultipleGetBatteryLevelCalls():
        sut = BatteryInfoGetterMock(1)

        sut.getBatteryLevel()
        sut.getBatteryLevel()
        
        assert sut.getBatteryLevelCallCount() == 2

    runTest(BatteryInfoGetterMockShould_HandleMultipleGetBatteryLevelCalls)
