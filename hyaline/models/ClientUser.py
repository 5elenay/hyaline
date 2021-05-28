from dataclasses import dataclass
from typing import Union
from .Channel import Channel
from ..utils.Request import Request
from ..errors.ChannelErrors import GetChannelError


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
