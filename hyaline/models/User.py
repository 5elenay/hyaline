from dataclasses import dataclass
from typing import Union


@dataclass
class User:
    # Attrs
    def __init__(self, json) -> None:
        self.id: str = json['id']
        self.username: str = json['username']
        self.avatar: Union[str, None] = json['avatar']
        self.discriminator: str = json['discriminator']

        self.tag: str = f"{self.username}#{self.discriminator}"
        self.mention: str = f"<@{self.id}>"

        self.public_flags: int = json['public_flags']
