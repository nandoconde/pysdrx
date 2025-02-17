
from pysdrx.classes.chunk import Chunk


class Block:
    """
    Parameters needed to skip over non-sample bytes
    present in the sample stream.
    """
    chunk: list[Chunk]
    "One or more chunks."
    cycles: int
    "Integer number of cycles that this patter repeats within a block."
    sizeheader: int
    "Integer number of bytes to skip in order to access first byute of chunk data."
    sizefooter: int
    "Integer number of bytes to skip in order to access first byte of next block."

    def __init__(self, chunk: list[Chunk], cycles: int, sizeheader: int = 0, sizefooter: int = 0):
        self.chunk = chunk
        self.cycles = cycles
        self.sizeheader = sizeheader
        self.sizefooter = sizefooter
