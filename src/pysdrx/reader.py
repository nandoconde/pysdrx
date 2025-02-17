import xml.etree.ElementTree as ET
from pysdrx.classes.fileset import parse_fileset_from_element
from pysdrx.classes.metadata import parse_sdrmetadata_from_root
from pysdrx.classes.sdrx import SDRX


def load(filename: str) -> SDRX:
    """Load a SDRX file and return a SDRX object."""
    tree = ET.parse(filename)
    root = tree.getroot()

    # TODO check XSD schema

    # check if it is a fileSet descriptor
    for child in root:
        if child.tag == "fileSet":
            return parse_fileset_from_element(child)

    # not a fileSet, return an SDRMetadata object
    return parse_sdrmetadata_from_root(root)
