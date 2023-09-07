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
