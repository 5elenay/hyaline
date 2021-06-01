from dataclasses import dataclass

from dateutil.parser import parse


@dataclass
class Member:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        from .User import User

        for key in json:
            if key == "user":
                setattr(self, key, User(json[key], self.__token))
            elif key in ("joined_at", "premium_since"):
                setattr(self, key, parse(json[key]) if json[key] else None)
            else:
                setattr(self, key, json[key])
