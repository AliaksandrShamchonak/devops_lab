import configparser
import os


class ConfigFile:
    """Common base class for file config.ini"""

    def __init__(self):
        config = configparser.ConfigParser()
        ospath = os.path.abspath(os.path.dirname(__file__))
        config.read(os.path.join(ospath, 'config.ini'))
        self.interval = int(config['COMMON']['Interval'])
        self.confout = config['COMMON']['Output']

    def getInterval(self):
        return self.interval

    def getConfout(self):
        return self.confout
