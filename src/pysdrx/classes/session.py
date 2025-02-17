from datetime import datetime
from src.pysdrx.classes.ancillary.position import Position
from src.pysdrx.classes.system import System


class Session:
    "Utilization instance of a pre-configured system for a period devoted to a particular activity."
    toa: datetime | None
    "Time of applicability for all position and attitude parameters."
    position: Position | None
    "Platform position at tow expressed in ellipsoid frame."
    system: System | None
    "The system used for this session"
    poc: str | None
    "Point of contact. Name of the person or entity."
    contact: str | None
    "poc contact information (email)."
    campaign: str | None
    "Data collection campaign."
    scenario: str | None
    "Specific scenario for this collection."

    def __init__(self, toa: datetime | None = None, position: Position | None = None, system: System | None = None, poc: str | None = None, contact: str | None = None, campaing: str | None = None, scenario: str | None = None):
        self.toa = toa
        self.position = position
        self.system = system
        self.poc = poc
        self.contact = contact
        self.campaign = campaing
        self.scenario = scenario
