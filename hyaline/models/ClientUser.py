from dataclasses import dataclass
from typing import Union
from ..utils.Request import Request
from .Channel import Channel
from ..errors.ChannelErrors import GetChannelError
from ..errors.MessageErrors import BulkDeleteMessageFailed
from ..errors.ChannelErrors import FetchChannelHistoryFailed


@dataclass
class ClientUser:
    # Attrs
    def __init__(self, json: dict, token: str) -> None:
        self.__token: str = token

        self.id: str = json['id']

        self.username: str = json['username']
        self.avatar: Union[str, None] = json['avatar']
        self.discriminator: str = json['discriminator']

        self.public_flags: int = json['public_flags']
        self.flags: int = json['flags']

        self.bot: bool = json['bot']
        self.locale: str = json['locale']
        self.mfa_enabled: bool = json['mfa_enabled']
        self.email: Union[str, None] = json['email']
        self.verified: bool = json['verified']

        self.channels: list = []
        
        self.cache: dict = {
            "message": []
        }

    async def add_message_cache(self, message):
        """Add message to cache"""

        self.cache['message'].append(message)

    async def remove_message_cache(self, packet):
        """Remove deleted message from cache"""

        for index, cache in enumerate(self.cache['message']):
            if cache.id == packet['id'] and cache.channel_id == packet['channel_id']:
                del self.cache['message'][index]
                break

    async def bulk_delete_message_cache(self, packet):
        """Remove Bulk-deleted message from cache"""

        shift = 0
        for index, cache in enumerate(self.cache['message'][:]):
            if cache.id in packet['ids'] and cache.channel_id == packet['channel_id']:
                del self.cache['message'][index - shift]
                shift += 1

    async def update_message_cache(self, message):
        """Update message from cache"""

        for index, cache in enumerate(self.cache['message']):
            if cache.id == message.id and cache.channel_id == message.channel_id:
                self.cache['message'][index] = message
                break

    async def get_channel(self, id: str, fetch: bool = False) -> Channel:
        """Get channel with id."""

        for channel in self.channels:
            if id == channel.id and not fetch:
                return channel

        atom, result = await Request().send_async_request(f"/channels/{id}", "GET", self.__token)

        if atom == 0:
            channel_object = Channel(result, self.__token)
            self.channels.append(channel_object)

            return channel_object
        else:
            raise GetChannelError(f"ATOM #{atom}: #{result}")

    async def bulk_delete(self, channel_id: str, limit: int = 10):
        """Bulk-delete channel messages with channel id."""

        from .Message import Message

        # filtered = [i.id for i in self.cache["message"] if i.channel_id == channel_id][::-1][:limit]

        # if len(filtered) < 2:
        query_format = f"/channels/{channel_id}/messages?limit={limit}"
        atom, result = await Request().send_async_request(query_format, "GET", self.__token)

        if atom == 0:
            filtered = [Message(i, self.__token).id for i in result][::-1][:limit]
        else:
            raise FetchChannelHistoryFailed(result)

        atom, result = await Request().send_async_request(f"/channels/{channel_id}/messages/bulk-delete", "POST", self.__token, {"messages": filtered})

        if atom == 0:
            return filtered
        else:
            raise BulkDeleteMessageFailed(result)