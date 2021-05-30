from dataclasses import dataclass
from typing import Union


@dataclass
class Emoji:
    # Attrs
    def __init__(self, json) -> None:
        from .User import User

        self.id: Union[str, None] = json['id']
        self.name: Union[str, None] = json['name']
        self.roles: Union[list,
                          None] = json['roles'] if 'roles' in json else None
        self.user: Union[User, None] = User(
            json['user']) if 'user' in json else None

        self.require_colons: Union[bool,
                                   None] = json['require_colons'] if 'require_colons' in json else None
        self.managed: Union[bool,
                            None] = json['managed'] if 'managed' in json else None
        self.animated: Union[bool,
                             None] = json['animated'] if 'animated' in json else None
        self.available: Union[bool,
                              None] = json['available'] if 'available' in json else None
