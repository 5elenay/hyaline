from dataclasses import dataclass


@dataclass
class Overwrite:
    # Attrs
    def __init__(self, json) -> None:
        self.id: str = json['id']
        self.type: int = json['type']
        self.allow: str = json['allow']
        self.deny: str = json['deny']
