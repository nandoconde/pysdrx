from pysdrx.classes.ancillary.duration import Duration
from pysdrx.classes.ancillary.frequency import Frequency


class Band:
    """Span of RF spectrum."""
    centerfreq: Frequency
    "Center frequency of band incident at source."
    translatedfreq: Frequency
    "Translated center frequency of band."
    inverted: bool
    "Binary flag indicating spectral inversion."
    delaybias: Duration
    "Delay of band measured from source to sampled stream, specified at toa."
    bandwidth: Frequency | None
    "Approximate double-sided half power bandwidth."

    def __init__(self, centerfreq: Frequency, translatedfreq: Frequency, inverted: bool = False, delaybias: Duration = Duration(0), bandwidth: Frequency | None = None):
        self.centerfreq = centerfreq
        self.translatedfreq = translatedfreq
        self.inverted = inverted
        self.delaybias = delaybias
        self.bandwidth = bandwidth
