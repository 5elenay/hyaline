from dataclasses import dataclass
from typing import Union


@dataclass
class MessageActivity:
    # Attrs
    def __init__(self, json) -> None:
        self.type: int = json['type']
        self.party_id: Union[str,
                             None] = json['party_id'] if 'party_id' in json else None
