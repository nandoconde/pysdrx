

from src.pysdrx.classes.ancillary.frequency import Frequency
from pysdrx.classes.cluster import Cluster
from pysdrx.classes.source import Source


class System:
    """Complete data collection apparatus.

    The system comprises all antennas, sensors and other information-outputting
    equipment down to the disk arrays that store SDR files. The system may also
    include GNSS signal simulators.
    """
    sources: list[Source]
    "One or more sources of sampled data."
    clusters: list[Cluster]
    "Zero or more clusters of antenna sources."
    freqbase: Frequency
    """
    Base frequency.

    All sampling frequencies are specified as an
    integer multiple of freqbase.
    """
    equipment: str | None
    "Equipment used for this data collection."

    def __init__(self, sources: list[Source], clusters: list[Cluster], freqbase: Frequency, equipment: str | None = None):
        self.sources = sources
        self.clusters = clusters
        self.freqbase = freqbase
        self.equipment = equipment
