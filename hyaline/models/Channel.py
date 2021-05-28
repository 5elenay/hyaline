from dataclasses import dataclass
from typing import Union
from ..utils.Request import Request
from ..errors.ChannelErrors import *
from datetime import datetime
from dateutil.parser import parse
from .Overwrite import Overwrite
from .User import User
from .ThreadMetadata import ThreadMetadata
from .ThreadMember import ThreadMember


@dataclass
class Channel:
    # Attrs
    def __init__(self, json: dict, token: str) -> None:
        self.__token: str = token

        self.id: str = json['id']
        self.type: int = json['type']
        self.guild_id: Union[str,
                             None] = json['guild_id'] if 'guild_id' in json else None
        self.position: Union[int,
                             None] = json['position'] if 'position' in json else None
        self.permission_overwrites: Union[list, None] = [Overwrite(
            i) for i in json['permission_overwrites']] if 'permission_overwrites' in json else None
        self.name: Union[str, None] = json['name'] if 'name' in json else None
        self.topic: Union[str,
                          None] = json['topic'] if 'topic' in json else None
        self.nsfw: Union[bool, None] = json['nsfw'] if 'nsfw' in json else None
        self.last_message_id: Union[str,
                                    None] = json['last_message_id'] if 'last_message_id' in json else None
        self.bitrate: Union[int,
                            None] = json['bitrate'] if 'bitrate' in json else None
        self.user_limit: Union[int,
                               None] = json['user_limit'] if 'user_limit' in json else None
        self.rate_limit_per_user: Union[int,
                                        None] = json['rate_limit_per_user'] if 'rate_limit_per_user' in json else None
        self.recipients: Union[User, None] = [
            User(i) for i in json['recipients']] if 'recipients' in json else None
        self.icon: Union[str, None] = json['icon'] if 'icon' in json else None
        self.owner_id: Union[str,
                             None] = json['owner_id'] if 'owner_id' in json else None
        self.application_id: Union[str,
                                   None] = json['application_id'] if 'application_id' in json else None
        self.parent_id: Union[str,
                              None] = json['parent_id'] if 'parent_id' in json else None
        self.last_pin_timestamp: Union[datetime, None] = parse(
            json['last_pin_timestamp']) if 'last_pin_timestamp' in json and json['last_pin_timestamp'] else None
        self.rtc_region: Union[str,
                               None] = json['rtc_region'] if 'rtc_region' in json else None
        self.video_quality_mode: Union[int,
                                       None] = json['video_quality_mode'] if 'video_quality_mode' in json else None
        self.message_count: Union[int,
                                  None] = json['message_count'] if 'message_count' in json else None
        self.member_count: Union[int,
                                 None] = json['member_count'] if 'member_count' in json else None
        self.thread_metadata: Union[ThreadMetadata, None] = ThreadMetadata(
            json['thread_metadata']) if 'thread_metadata' in json else None
        self.member: Union[ThreadMember, None] = ThreadMetadata(
            json['member']) if 'member' in json else None

    async def send(self, options: dict = {}):
        """Send message to the channel."""

        from .Message import Message

        atom, result = await Request().send_async_request(f"/channels/{self.id}/messages", "POST", self.__token, options)

        if atom == 0:
            return Message(result, self.__token)
        else:
            raise SendMessageToChannelFailed(result)

    async def edit(self, options: dict = {}):
        """Edit channel with API params."""

        atom, result = await Request().send_async_request(f"/channels/{self.id}", "PATCH", self.__token, options)

        if atom == 0:
            return Channel(result, self.__token)
        else:
            raise EditChannelFailed(result)

    async def delete(self):
        """Delete channel with API params."""

        atom, result = await Request().send_async_request(f"/channels/{self.id}", "DELETE", self.__token)

        if atom == 0:
            return Channel(result, self.__token)
        else:
            raise DeleteChannelFailed(result)

    async def fetch_history(self, options: dict = {}):
        """Fetch channel history with API params."""

        from .Message import Message

        query_format = f"/channels/{self.id}/messages?{'&'.join(f'{i}={options.get(i)}' for i in options)}"
        print(query_format)

        atom, result = await Request().send_async_request(query_format, "GET", self.__token)

        if atom == 0:
            return [Message(i, self.__token) for i in result]
        else:
            raise FetchChannelHistoryFailed(result)

    async def fetch_message(self, id: str):
        """Fetch channel message with id."""

        from .Message import Message

        atom, result = await Request().send_async_request(f"/channels/{self.id}/messages/{id}", "GET", self.__token)

        if atom == 0:
            return Message(result, self.__token)
        else:
            raise FetchChannelMessageFailed(result)
