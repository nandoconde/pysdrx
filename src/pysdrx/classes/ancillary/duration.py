from enum import IntEnum, auto


class DurationUnits(IntEnum):
    """Enum class to specify the units of time."""
    ns = auto()
    us = auto()
    ms = auto()
    sec = auto()

class Duration:
    """Class to specify intervals of time."""
    value: float
    "Numeric value of the time interval."
    format: DurationUnits
    "Units of the time interval."

    def __init__(self, value: float, format: DurationUnits = DurationUnits.sec):
        self.value = value
        self.format = format

    def __str__(self):
        return f"{self.value} {self.format.name}"

    def __repr__(self):
        return f"{self.value} {self.format.name}"
