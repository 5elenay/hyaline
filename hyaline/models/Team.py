from dataclasses import dataclass
from typing import Union


@dataclass
class Team:
    # Attrs
    def __init__(self, json) -> None:
        self.id: str = json['id']
        self.icon: Union[str, None] = json['icon']
        self.members: list = json['members']
        self.name: str = json['name']
        self.owner_user_id: str = json['owner_user_id']
