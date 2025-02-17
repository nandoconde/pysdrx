from xml.etree.ElementTree import Element
from pysdrx.classes.sdrx import SDRX


class SDRMetadata(SDRX):
    """Class representing an SDR metadata object."""
    metadata: dict

    def __init__(self, metadata: dict):
        self.metadata = metadata

    def is_fileset(self) -> bool:
        return False

    def is_file(self) -> bool:
        return True

def parse_sdrmetadata_from_root(root: Element) -> SDRMetadata:
    """Parse an SDRMetadata object from an XML Element."""
    pass
