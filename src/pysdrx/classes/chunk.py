from src.pysdrx.classes.lump import Lump
from src.pysdrx.classes.ancillary.streamsettings import Endianness, WordShift
from src.pysdrx.classes.ancillary.streamsettings import Padding


class Chunk:
    """Segment of data consisting of one or more lumps.

    Each lump has been packed using one of four unsigned integer data types:
        - uint8_t
        - uint16_t
        - uint32_t
        - uint64_t
    """
    lumps: list[Lump]
    "One or more lumps."
    sizeword: int
    """
    Size, in bytes, of the fundamental integer
    data-type (word) that shall be read.
    Either 1, 2, 4, or 8.
    """
    countwords: int
    "Total number of words to be read in order to read/decode this chunk."
    endian: Endianness
    "Endianness of words stored in a chunk."
    padding: Padding
    "Padding applied during encoding."
    wordshift: WordShift
    "Shift direction."

    def __init__(self, lumps: list[Lump], sizeword: int, countwords: int, wordshift: WordShift, endian: Endianness = Endianness.Little, padding: Padding = Padding.NONE):
        self.lumps = lumps
        self.sizeword = sizeword
        self.countwords = countwords
        self.wordshift = wordshift
        self.endian = endian
        self.padding = padding
