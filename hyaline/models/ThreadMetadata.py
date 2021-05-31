from dataclasses import dataclass
from dateutil.parser import parse


@dataclass
class ThreadMetadata:
    # Attrs
    def __init__(self, json) -> None:
        for key in json:
            if key == "archive_timestamp":
                setattr(self, key, parse(json[key]) if json[key] else None)
            else:
                setattr(self, key, json[key])
