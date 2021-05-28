from dataclasses import dataclass
from .Emoji import Emoji


@dataclass
class Reaction:
    # Attrs
    def __init__(self, json) -> None:
        self.count: int = json['count']
        self.reacted: bool = json['me']
        self.emoji: Emoji = Emoji(json['emoji'])
