from dataclasses import dataclass
from datetime import datetime
from dateutil.parser import parse
from typing import Union


@dataclass
class Member:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        from .User import User

        self.user: Union[User, None] = User(
            json['user'], self.__token) if 'user' in json else None

        self.nick: Union[str, None] = json['nick'] if 'nick' in json else None
        self.roles: list = json['roles']
        self.joined_at: datetime = json['joined_at']
        self.premium_since: Union[datetime, None] = parse(
            json['premium_since']) if 'premium_since' in json and json['premium_since'] else None
        self.deaf: bool = json['deaf']
        self.mute: bool = json['mute']
        self.pending: Union[bool,
                            None] = json['pending'] if 'pending' in json else None
        self.permissions: Union[str,
                                None] = json['permissions'] if 'permissions' in json else None
