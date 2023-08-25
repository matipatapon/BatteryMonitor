from time import sleep
from objects.Logger import Logger

class TimeManager:
    def __init__(self):
        self._logger = Logger("TimeManager")

    def wait(self, seconds):
        self._logger.log(f"Going to sleep for {seconds} seconds")
        sleep(seconds)
        self._logger.log(f"Waking up ^^")
