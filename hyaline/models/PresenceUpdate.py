from dataclasses import dataclass


@dataclass
class PresenceUpdate:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        from .User import User

        self.user: User = User(json['user'], self.__token)
        self.guild_id: str = json['guild_id']
        self.status: str = json['status']
        self.activities: list = json['activities']
        self.client_status: dict = json['client_status']
