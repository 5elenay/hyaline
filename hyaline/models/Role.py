from dataclasses import dataclass
from typing import Union


@dataclass
class Role:
    # Attrs
    def __init__(self, json) -> None:
        from .RoleTags import RoleTags

        self.id: str = json['id']
        self.name: str = json['name']
        self.color: int = json['color']
        self.hoist: bool = json['hoist']
        self.position: int = json['position']
        self.permissions: str = json['permissions']
        self.managed: bool = json['managed']
        self.mentionable: bool = json['mentionable']
        self.tags: Union[RoleTags, None] = RoleTags(
            json['tags']) if 'tags' in json else None
