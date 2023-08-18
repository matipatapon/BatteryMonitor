import os
from gtts import gTTS 
from constants import COMMUNICATE_FILE

class Speaker:
    def speakText(self, text):
        gtts = gTTS(text=text, lang='en', slow=False)
        gtts.save(COMMUNICATE_FILE)
        os.system(f"$(mpg123 -q {COMMUNICATE_FILE})")
