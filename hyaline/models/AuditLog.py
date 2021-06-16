from dataclasses import dataclass


@dataclass
class AuditLog:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        from .Webhook import Webhook
        from .User import User

        for key in json:
            if key == "webhooks":
                setattr(self, key, [Webhook(i, self.__token)
                        for i in json[key]])
            elif key == "users":
                setattr(self, key, [User(i, self.__token) for i in json[key]])
            else:
                setattr(self, key, json[key])
