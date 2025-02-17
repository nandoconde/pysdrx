from datetime import datetime

from pysdrx.classes.lane import Lane
from xml.etree.ElementTree import Element


class SdrxFile:
    url: str
    "Unique identifier for the file (path/filename)."
    timestamp: datetime | None
    "Time the file was generated."
    offset: int
    "Byte offset to start of first block."
    lane: Lane
    "Identifies which lane the data came from."
    previous: str | None
    "Name of previous file (for temporally split files)."
    next: str | None
    "Name of next file (for temporally split files)."
    owner: str | None
    "String specifying the owner of this file."
    copyright: str | None
    "Copyright information."

    def __init__(
        self,
        url: str,
        lane: Lane,
        timestamp: datetime | None = None,
        offset: int = 0,
        previous: str | None = None,
        next: str | None = None,
        owner: str | None = None,
    ):
        self.url = url
        self.timestamp = timestamp
        self.offset = offset
        self.lane = lane
        self.previous = previous
        self.next = next
        self.owner = owner
        self.copyright = None

def parse_file_from_element(el: Element) -> SdrxFile:
    """Parse an SdrxFile object from an XML Element."""
    url = None
    timestamp = None
    offset = 0
    lane = None
    previous = None
    next = None
    owner = None
    copyright = None
    for c in el:
        if c.tag == "file":
            files.append(c.text)

    return SdrxFile(files)
