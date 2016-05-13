from enum import Enum

__version_info__ = (0,1,0)
__version__ = '.'.join(map(str, __version_info__))

class Mode(Enum):
    COMMAND = 1
    LINK = 2

def sign(x):
    return (x > 0) - (x < 0)
