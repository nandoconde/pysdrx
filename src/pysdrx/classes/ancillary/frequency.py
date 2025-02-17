from enum import IntEnum, auto


class FrequencyUnits(IntEnum):
    """Enum class to specify the units of frequency."""
    Hz = auto()
    kHz = auto()
    MHz = auto()
    GHz = auto()


class Frequency:
    "Class to specify frequencies."
    value: float
    "Numeric value of the frequency."
    format: FrequencyUnits
    "Units of the frequency."

    def __init__(self, value: float, format: FrequencyUnits):
        self.value = value
        self.format = format

    def __str__(self):
        return f"{self.value} {self.format.name}"

    def __repr__(self):
        return f"{self.value} {self.format.name}"
