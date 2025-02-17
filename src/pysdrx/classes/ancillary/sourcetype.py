

from enum import IntEnum, auto


class SourceType(IntEnum):
    UndefinedType = auto()
    Patch = auto()
    Dipole = auto()
    Helical = auto()
    Quadrifilar = auto()
    Simulator = auto()
    Other = auto()
