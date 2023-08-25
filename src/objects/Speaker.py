from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS 
from constants import COMMUNICATE_FILE
from objects.Logger import Logger

class Speaker:
    def __init__(self):
        self._logger = Logger("Speaker")

    def speakText(self, text):
        gtts = gTTS(text=text, lang='en', slow=False)
        gtts.save(COMMUNICATE_FILE)
        self._logger.log(f"Speaking '{text}'")
        play(AudioSegment.from_mp3(COMMUNICATE_FILE))
