from enum import Enum


class Color(Enum):
    Default = "\033[0;00m"
    Red = "\033[0;31m"
    Green = "\033[0;32m"
    Blue = "\033[0;34m"
