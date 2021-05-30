from dataclasses import dataclass


@dataclass
class PresenceUpdate:
    # Attrs
    def __init__(self, json) -> None:
        from .User import User

        self.user: User = User(json['user'])
        self.guild_id: str = json['guild_id']
        self.status: str = json['status']
        self.activities: list = json['activities']
        self.client_status: dict = json['client_status']
