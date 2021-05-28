from dataclasses import dataclass
from typing import Union


@dataclass
class Sticker:
    # Attrs
    def __init__(self, json) -> None:
        self.id: str = json['id']
        self.pack_id: str = json['pack_id']
        self.name: str = json['name']
        self.description: str = json['description']
        self.tags: Union[str, None] = json['tags'] if 'tags' in json else None
        self.asset: Union[str,
                          None] = json['asset'] if 'asset' in json else None
        self.format_type: int = json['format_type']
