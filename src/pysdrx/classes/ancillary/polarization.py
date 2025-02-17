

from enum import IntEnum, auto


class Polarization(IntEnum):
    UndefinedType = auto()
    RHCP = auto()
    LHCP = auto()
    Linear = auto()
    Horizontal = auto()
    Vertical = auto()
