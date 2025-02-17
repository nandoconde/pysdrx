from abc import ABC, abstractmethod

class SDRX(ABC):
    """Base class for SDRX objects."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def is_fileset(self) -> bool:
        pass

    @abstractmethod
    def is_file(self) -> bool:
        pass
