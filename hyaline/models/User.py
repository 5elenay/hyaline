from dataclasses import dataclass
from typing import Union


@dataclass
class User:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        for key in json:
            setattr(self, key, json[key])

    @property
    def tag(self) -> str:
        return f"{self.username}#{self.discriminator}"

    @property
    def mention(self) -> str:
        return f"<@{self.id}>"
