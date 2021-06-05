from dataclasses import dataclass


@dataclass
class Ban:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token
        from .User import User

        for key in json:
            if key == "user":
                setattr(self, key, User(json[key], self.__token))
            else:
                setattr(self, key, json[key])
