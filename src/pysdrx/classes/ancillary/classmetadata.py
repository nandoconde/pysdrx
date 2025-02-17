class ClassMetadata:
    """A class to represent metadata for a specific class.

    Attributes:
    ----------
    id : str | None
        Unique identifier.
    artifact : list[str]
        Zero or more link specifications to information pertaining
        to the class instance. Can be any URI formatted information.
    comments : list[str]
        Zero or more text/html comments providing additional detail
        regarding the class instance.
    """

    id: str | None
    artifact: list[str]
    comment: list[str]

    def __init__(
        self,
        id: str | None = None,
        artifact: list[str] = [],
        comment: list[str] = [],
    ):
        self.id = id
        self.artifact = artifact
        self.comment = comment
