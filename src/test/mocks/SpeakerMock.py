from ..runTest import runTest


class SpeakerMock:
    def __init__(self):
        self._speakTextCallCount = 0
        self._lastReceivedText = ""
    
    def speakText(self, text):
        self._speakTextCallCount += 1
        self._lastReceivedText = text
    
    def getSpeakTextCallCount(self):
        return self._speakTextCallCount

    def getLastReceivedText(self):
        return self._lastReceivedText


def SpeakerMockUTs():
    def SpeakerMockShould_ReturnDefaultCallCount():
        sut = SpeakerMock()

        assert sut.getSpeakTextCallCount() == 0

    runTest(SpeakerMockShould_ReturnDefaultCallCount)

    def SpeakerMockShould_ReturnCallCount():
        sut = SpeakerMock()

        sut.speakText("SomeText")
        
        assert sut.getSpeakTextCallCount() == 1

    runTest(SpeakerMockShould_ReturnCallCount)

    def SpeakerMockShould_ReturnLastReceivedText():
        sut = SpeakerMock()

        sut.speakText("SomeText")
        
        assert sut.getLastReceivedText() == "SomeText"

    runTest(SpeakerMockShould_ReturnLastReceivedText)
