from pysdrx.classes.ancillary.streamsettings import LumpShift
from pysdrx.classes.stream import Stream


class Lump:
    """
    Ordered containment of all samples occurring within
    an interval ts = 1/fs.
    """
    streams: list[Stream]
    "One or more streams present in this lump."
    shift: LumpShift
    "Shift direction."

    def __init__(self, streams: list[Stream], shift: LumpShift):
        self.streams = streams
        self.shift = shift
