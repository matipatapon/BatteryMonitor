from gtts import gTTS 
from time import sleep
import os

COMMUNICATE_FILE = 'communicate.mp3'
BATTERY_LEVEL_CHECK_INTERVAL = 300
BATTERY_LEVEL_STEP = 10
BATTERY_LEVEL_START_SPEAK = 40


def speakText(text):
    gtts = gTTS(text=text, lang='en', slow=False)
    gtts.save(COMMUNICATE_FILE)
    os.system(f"mpg123 {COMMUNICATE_FILE}")


def getBatteryLevel():
    return os.system("")


def wait(seconds):
    sleep(seconds)


def run():
    lastBatteryLevel = -999
    while True:
        currentBatteryLevel = getBatteryLevel()
        if currentBatteryLevel <= BATTERY_LEVEL_START_SPEAK:
            batteryChange = abs(currentBatteryLevel - lastBatteryLevel)
            if batteryChange >= BATTERY_LEVEL_STEP:
                speakText(f"{getBatteryLevel()}% battery left")
                lastBatteryLevel = currentBatteryLevel
        wait(BATTERY_LEVEL_CHECK_INTERVAL)


run()
