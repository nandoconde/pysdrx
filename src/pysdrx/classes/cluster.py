class Cluster:
    "Grouping of Sources."
    id: str
    "Unique identifier."
    origin: str | None
    "Origin of cluster frame w.r.t. platform frame."
    orientation: str | None
    "Orientation of cluster frame w.r.t. platform frame."
    vendor: str | None
    "Vendor name."
    model: str | None
    "Model number."
    serial: str | None
    "Serial number."

    def __init__(self, id: str, origin: str | None = None, orientation: str | None = None, vendor: str | None = None, model: str | None = None, serial: str | None = None):
        self.id = id
        self.origin = origin
        self.orientation = orientation
        self.vendor = vendor
        self.model = model
        self.serial = serial
