from dataclasses import dataclass
from datetime import datetime
from typing import Union


@dataclass
class Activity:
    # Attrs
    def __init__(self, json) -> None:
        self.name: str = json['name']
        self.type: int = json['type']
        self.url: Union[str, None] = json['url'] if 'url' in json else None
        self.created_at: datetime = datetime.fromtimestamp(json['created_at'])
