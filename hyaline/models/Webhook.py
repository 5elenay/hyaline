from dataclasses import dataclass


@dataclass
class Webhook:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        from .User import User
        from .Guild import Guild
        from .Channel import Channel

        for key in json:
            if key == "user":
                setattr(self, key, User(json[key], self.__token))
            elif key == "source_guild":
                setattr(self, key, Guild(json[key], self.__token))
            elif key == "source_channel":
                setattr(self, key, Channel(json[key], self.__token))
            else:
                setattr(self, key, json[key])
