from dataclasses import dataclass


@dataclass
class Reaction:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        from .Emoji import Emoji

        self.count: int = json['count']
        self.reacted: bool = json['me']
        self.emoji: Emoji = Emoji(json['emoji'], self.__token)
