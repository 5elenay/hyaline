from dataclasses import dataclass
from datetime import datetime
from typing import Union
from dateutil.parser import parse


@dataclass
class VoiceState:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        from .Member import Member

        for key in json:
            if key == "member":
                setattr(self, key, Member(json[key], self.__token))
            elif key == "request_to_speak_timestamp":
                setattr(self, key, parse(json[key]) if json[key] else None)
            else:
                setattr(self, key, json[key])
