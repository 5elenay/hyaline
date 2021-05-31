from dataclasses import dataclass
from datetime import datetime
from dateutil.parser import parse
from typing import Union


@dataclass
class Guild:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token = token

        from .Role import Role
        from .Emoji import Emoji
        from .VoiceState import VoiceState
        from .Member import Member
        from .Channel import Channel

        for key in json:
            if key == "roles":
                setattr(self, key, [Role(i) for i in json[key]])
            elif key == "emojis":
                setattr(self, key, [Emoji(i, self.__token) for i in json[key]])
            elif key == "joined_at":
                setattr(self, key, parse(json[key]) if json[key] else None)
            elif key == "voice_states":
                setattr(self, key, [VoiceState(i, self.__token)
                        for i in json[key]])
            elif key == "members":
                setattr(self, key, [Member(i, self.__token)
                        for i in json[key]])
            elif key == "channels":
                setattr(self, key, [Channel(i, self.__token)
                        for i in json[key]])
            elif key == "threads":
                setattr(self, key, [Channel(i, self.__token)
                        for i in json[key]])
            else:
                setattr(self, key, json[key])
