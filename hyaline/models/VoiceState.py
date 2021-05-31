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

        self.guild_id: Union[str,
                             None] = json['guild_id'] if 'guild_id' in json else None
        self.channel_id: Union[str,
                               None] = json['channel_id'] if 'channel_id' in json else None
        self.user_id: str = json['user_id']
        self.member: Union[Member, None] = Member(
            json['member'], self.__token) if 'member' in json else None
        self.session_id: str = json['session_id']
        self.deaf: bool = json['deaf']
        self.mute: bool = json['mute']
        self.self_deaf: bool = json['self_deaf']
        self.self_mute: bool = json['self_mute']
        self.self_stream: Union[bool,
                                None] = json['self_stream'] if 'self_stream' in json else None
        self.self_video: bool = json['self_video']
        self.suppress: bool = json['suppress']
        self.request_to_speak_timestamp: Union[datetime, None] = parse(
            json['request_to_speak_timestamp']) if 'request_to_speak_timestamp' in json and json['request_to_speak_timestamp'] else None
