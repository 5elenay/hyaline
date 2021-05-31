from dataclasses import dataclass
from typing import Union
from datetime import datetime
from dateutil.parser import parse


@dataclass
class Invite:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token = token

        from .Channel import Channel
        from .User import User
        from .Guild import Guild
        from .Application import Application

        for key in json:
            if key == "guild":
                setattr(self, key, Guild(json[key], self.__token))
            elif key == "channel":
                setattr(self, key, Channel(json[key], self.__token))
            elif key in ("inviter", "target_user", ):
                setattr(self, key, User(json[key], self.__token))
            elif key == "target_application":
                setattr(self, key, Application(json[key], self.__token))
            elif key == "expires_at":
                setattr(self, key, parse(json[key]) if json[key] else None)
            else:
                setattr(self, key, json[key])
