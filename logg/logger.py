from typing import Optional
from datetime import datetime

from utils.pars_cfg import Config


class Logger:

    SAMPLE = "[{time}] {loglevel} "

    def __init__(self, config: Optional[Config] = Config()) -> None:
        self.config = config

    def __sample_string_format(self, level: str):
        sample_format = self.SAMPLE.format(
            time=datetime.now().strftime("%a, %d %b %Y, %H:%M:%S"), 
            loglevel=level
        )

        return sample_format

    def info(self, message: str):
        print(f'{self.config.color("info")}{self.__sample_string_format("INFO")}[{message}]')

    def error(self, message: str):
        print(f'{self.config.color("error")}{self.__sample_string_format("ERROR")}[{message}]')

    def debug(self, message: str):
        print(f'{self.config.color("debug")}{self.__sample_string_format("DEBUG")}[{message}]')
