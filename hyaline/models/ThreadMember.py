from dataclasses import dataclass
from datetime import datetime
from dateutil.parser import parse


@dataclass
class ThreadMember:
    # Attrs
    def __init__(self, json) -> None:
        for key in json:
            if key == "join_timestamp":
                setattr(self, key, parse(json[key]) if json[key] else None)
            else:
                setattr(self, key, json[key])
