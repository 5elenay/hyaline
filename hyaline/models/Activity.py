from dataclasses import dataclass
from typing import Union
from datetime import datetime


@dataclass
class Activity:
    # Attrs
    def __init__(self, json) -> None:
        # TODO: Burayı Bitir.
        self.name: str = json['name']
        self.type: int = json['type']
        self.url: Union[str, None] = json['url'] if 'url' in json else None
        self.created_at: datetime = datetime.fromtimestamp(json['created_at'])
        # self.created_at: datetime = datetime.fromtimestamp(json['created_at'])
