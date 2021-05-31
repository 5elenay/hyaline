from dataclasses import dataclass
from typing import Union


@dataclass
class User:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        self.id: str = json.get('id')
        self.username: str = json.get('username')
        self.avatar: Union[str, None] = json.get('avatar')
        self.discriminator: str = json.get('discriminator')

        self.tag: str = f"{self.username}#{self.discriminator}"
        self.mention: str = f"<@{self.id}>"

        self.public_flags: int = json.get('public_flags')
