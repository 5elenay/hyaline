from dataclasses import dataclass


@dataclass
class Button:
    # Attrs
    def __init__(self, json) -> None:
        from .Message import Message
        from .Member import Member

        # TODO: Burayı Bitir.
        self.message: Message = Message(json['message'])
        self.member: Member = Member(json['member'])
