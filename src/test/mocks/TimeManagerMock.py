from ..runTest import runTest


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


def TimeManagerMockTests():
    def TimeManagerMockShould_ReturnDefaultCallCount():
        sut = TimeManagerMock()

        assert sut.getWaitCallCount() == 0

    runTest(TimeManagerMockShould_ReturnDefaultCallCount)

    def TimeManagerMockShould_ReturnCallCount():
        sut = TimeManagerMock()

        sut.wait(5)
        
        assert sut.getWaitCallCount() == 1

    runTest(TimeManagerMockShould_ReturnCallCount)

    def TimeManagerMockShould_ReturnLastReceivedTime():
        sut = TimeManagerMock()

        sut.wait(5)
        
        assert sut.getLastReceivedTime() == 5

    runTest(TimeManagerMockShould_ReturnLastReceivedTime)
