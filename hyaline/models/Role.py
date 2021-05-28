from dataclasses import dataclass


@dataclass
class Roles:
    # Attrs
    def __init__(self, json) -> None:
        # TODO: Burayı Yenile
        self.position: int = json['role']['position']
        self.permissions: str = json['role']['permissions']
        self.name: str = json['role']['name']
        self.mentionable: bool = json['role']['mentionable']
        self.managed: bool = json['role']['managed']
        self.id: str = json['role']['id']
