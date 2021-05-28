from dataclasses import dataclass
from datetime import datetime
from dateutil.parser import parse


@dataclass
class ThreadMember:
    # Attrs
    def __init__(self, json) -> None:
        self.id: str = json['id']
        self.user_id: str = json['user_id']
        self.join_timestamp: datetime = parse(json['join_timestamp'])
        self.flags: int = json['flags']
