import pyttsx3
from constants import COMMUNICATE_FILE
from objects.Logger import Logger

class Speaker:
    def __init__(self):
        self._logger = Logger("Speaker")
        self._pyttsx3 = pyttsx3.init()
        self._pyttsx3.setProperty("rate", 125)
        self._pyttsx3.setProperty("volume", 1)

    def speakText(self, text):
        self._logger.log(f"Speaking '{text}'")
        self._pyttsx3.say(text)
        self._pyttsx3.runAndWait()
