from dataclasses import dataclass


@dataclass
class Application:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        from .User import User
        from .Team import Team

        for key in json:
            if key == "owner":
                setattr(self, key, User(json[key], self.__token))
            elif key == "team":
                setattr(self, key, Team(json[key], self.__token))
            else:
                setattr(self, key, json[key])
