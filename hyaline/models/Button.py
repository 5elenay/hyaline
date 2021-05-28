from dataclasses import dataclass
from .Message import Message
from .Member import Member


@dataclass
class Button:
    # Attrs
    def __init__(self, json) -> None:
        self.message: Message = Message(json['message'])
        self.member: Member = Member(json['member'])
