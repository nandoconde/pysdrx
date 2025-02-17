from enum import IntEnum, auto

class SampleAlignment(IntEnum):
    Left = auto()
    Right = auto()
    Undefined = auto()


class SampleShift(IntEnum):
    Left = auto()
    Right = auto()
    Undefined = auto()


class SampleFormat(IntEnum):
    """Format of packed samples.

    - `n` means inversion
    - ?
    """
    IF = auto()
    IFn = auto()
    IQ = auto()
    IQn = auto()
    InQ = auto()
    InQn = auto()
    QI = auto()
    QIn = auto()
    QnI = auto()
    QnIn = auto()

class SampleEncoding(IntEnum):
    """Stream encoding formats.

    - SIGN: sign
    - OB: Offset-Binary
    - SM: Sign-Magnitude
    - MS: Magnitude-Sign
    - TC: Two's Complement
    - OG: Offset-Gray Code
    - OBA: Offset-Binary Adjusted
    - SMA: Sign-Magnitude Adjusted
    - MSA: Magnitude-Sign Adjusted
    - TCA: Two's Complement Adjusted
    - OGA: Offset-Gray Code Adjusted
    - FP: Floating Point according to IEEE 754,
          bit length (32 or 64 bit) defined by the quantization.
    """
    SIGN = auto()
    OB = auto()
    SM = auto()
    MS = auto()
    TC = auto()
    OG = auto()
    OBA = auto()
    SMA = auto()
    MSA = auto()
    TCA = auto()
    OGA = auto()
    FP = auto()


class LumpShift(IntEnum):
    "Shift direction for lumps."
    Left = auto()
    Right = auto()

class Endianness(IntEnum):
    "Endiannes of words stored in a chunk."
    Big = auto()
    Little = auto()
    Undefined = auto()

class Padding(IntEnum):
    "Padding of words stored in a chunk."
    NONE = auto()
    Head = auto()
    Tail = auto()

class WordShift(IntEnum):
    "Shift direction for words."
    Left = auto()
    Right = auto()
