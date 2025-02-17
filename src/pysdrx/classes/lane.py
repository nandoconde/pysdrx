from src.pysdrx.classes.block import Block
from src.pysdrx.classes.session import Session
from src.pysdrx.classes.system import System


class Lane:
    "Conduit that transports data comprised of one or more types of blocks."
    block: list[Block]
    "One or more types of blocks in this lane (in order)."
    bandsrc: str
    "Associates predefined bands with sources."
    session: Session
    "Session informtion for this lane."
    system: System
    "System information for this lane."

    def __init__(self, block: list[Block], bandsrc: str, session: Session, system: System):
        self.block = block
        self.bandsrc = bandsrc
        self.session = session
        self.system = system
