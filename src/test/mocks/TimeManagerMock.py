class TimeManagerMock:
    def __init__(self):
        self._waitCallCount = 0
        self._lastReceivedTime = 0
    
    def wait(self, timeInSeconds):
        self._waitCallCount += 1
        self._lastReceivedTime = timeInSeconds
    
    def getWaitCallCount(self):
        return self._waitCallCount

    def getLastReceivedTime(self):
        return self._lastReceivedTime
