class Logger:
    def __init__(self, prefix):
        self._prefix = prefix
    
    def log(self, text):
        print(f"|{self._prefix}|",text)
