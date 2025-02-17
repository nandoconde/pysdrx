
from pysdrx.classes.ancillary.streamsettings import (
    SampleAlignment,
    SampleEncoding,
    SampleFormat,
    SampleShift,
)
from pysdrx.classes.band import Band


class Stream:
    """
    Discrete-time discrete-amplitude series that is the sampled
    representation of a combination of one or more bands.
    """
    bands: list[Band]
    ratefactor: int
    quantization: int
    packedbits: int
    alignment: SampleAlignment
    shift: SampleShift
    format: SampleFormat
    encoding: SampleEncoding

    def __init__(self, bands: list[Band], ratefactor: int, quantization: int, packedbits: int, alignment: SampleAlignment,
                 shift: SampleShift, format: SampleFormat, encoding: SampleEncoding):
        self.bands = bands
        self.ratefactor = ratefactor
        self.quantization = quantization
        self.packedbits = packedbits
        self.alignment = alignment
        self.shift = shift
        self.format = format
        self.encoding = encoding
