from xml.etree.ElementTree import Element


class Position:
    
    """Class to specify the location of a platform with respect to the Earth's ellipsoid.

    Parameters
    ----------
    lat : float
        The latitude coordinate of the position in degrees.
    lon : float
        The longitude coordinate of the position in degrees.
    height : float
        The height coordinate of the position in meters above the ellipsoid.
    datum : str, optional
        Datum used for the ellipsoid (default is "WGS-84").
    """
    lat: float
    lon: float
    height: float
    datum: str

    def __init__(self, lat: float, lon: float, height: float, datum: str = "WGS-84"):
        self.lat = lat
        self.lon = lon
        self.height = height
        self.datum = datum

def parse_position_from_element(el: Element) -> Position:
    """Parse a Position object from an XML Element."""
    pass