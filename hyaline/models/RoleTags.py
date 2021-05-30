from dataclasses import dataclass
from typing import Union


@dataclass
class RoleTags:
    # Attrs
    def __init__(self, json) -> None:
        self.bot_id: Union[str,
                           None] = json['bot_id'] if 'bot_id' in json else None
        self.integration_id: Union[str,
                                   None] = json['integration_id'] if 'integration_id' in json else None
        self.premium_subscriber: None = json['premium_subscriber'] if 'premium_subscriber' in json else None
