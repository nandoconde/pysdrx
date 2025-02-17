

from xml.etree.ElementTree import Element
from pysdrx.classes.sdrx import SDRX


class SdrxFileSet(SDRX):
    """Class representing a fileSet object."""
    files: list[str]

    def __init__(self, files: list[str]):
        self.files = files

    def is_fileset(self) -> bool:
        return True

    def is_file(self) -> bool:
        return False


def parse_fileset_from_element(el: Element) -> SdrxFileSet:
    """Parse an SdrxFileSet object from an XML Element."""
    files = []
    for c in el:
        if c.tag == "file":
            files.append(c.text)

    return SdrxFileSet(files)
