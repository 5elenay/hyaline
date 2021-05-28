from dataclasses import dataclass
from typing import Union


@dataclass
class MessageReference:
    # Attrs
    def __init__(self, json) -> None:
        self.message_id: Union[str,
                               None] = json['message_id'] if 'message_id' in json else None
        self.channel_id: Union[str,
                               None] = json['channel_id'] if 'channel_id' in json else None
        self.guild_id: Union[str,
                             None] = json['guild_id'] if 'guild_id' in json else None
        self.fail_if_not_exists: Union[bool,
                                       None] = json['fail_if_not_exists'] if 'fail_if_not_exists' in json else None
