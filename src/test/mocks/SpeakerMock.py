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
