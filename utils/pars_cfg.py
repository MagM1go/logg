from typing import Literal
import configparser

config = configparser.ConfigParser()
sample = """
[logger.log.colors]
error = "\033[1;31m"
info = "\033[1;32m"
debug = "\033[1;33m"
"""

class Config:
    def __init__(self, filename: str = 'config.ini'):
        self.filename = filename
        
        try:
            open(filename, 'r')
        except FileNotFoundError:
            with open(filename, 'a') as f:
                f.write(sample)

        config.read(filename)
        self.config = config

    def color(self, log_name: Literal['info', 'debug', 'error'], section_name: str = 'logger.log.colors'):
        return self.config[section_name][log_name]
