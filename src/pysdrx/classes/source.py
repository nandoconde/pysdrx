from pysdrx.classes.ancillary.sourcetype import SourceType
from src.pysdrx.classes.ancillary.polarization import Polarization


class Source:
    id: str
    "Cluster that this source belongs to."
    type: SourceType
    "Electrical type of this source."
    polarization: Polarization
    "Element polarization."
    origin: str | None
    "Origin of source frame w.r.t. cluster frame."
    orientation: str | None
    "Orientation of source frame w.r.t. cluster frame."

    def __init__(self, id: str, type: SourceType = SourceType.UndefinedType, polarization: Polarization = Polarization.UndefinedType, origin: str | None = None, orientation: str | None = None):
        self.id = id
        self.type = type
        self.polarization = polarization
        self.origin = origin
        self.orientation = orientation
