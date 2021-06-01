from dataclasses import dataclass

from dateutil.parser import parse

from ..errors.GuildErrors import *
from ..utils.Request import Request
from ..utils.WrongType import raise_error
from ..utils.Dict2Query import convert as d2q_converter


@dataclass
class Guild:
    # Attrs
    def __init__(self, json, token) -> None:
        self.id = None
        self.__token = token

        from .Role import Role
        from .Emoji import Emoji
        from .VoiceState import VoiceState
        from .Member import Member
        from .Channel import Channel

        for key in json:
            if key == "roles":
                setattr(self, key, [Role(i) for i in json[key]])
            elif key == "emojis":
                setattr(self, key, [Emoji(i, self.__token) for i in json[key]])
            elif key == "joined_at":
                setattr(self, key, parse(json[key]) if json[key] else None)
            elif key == "voice_states":
                setattr(self, key, [VoiceState(i, self.__token)
                                    for i in json[key]])
            elif key == "members":
                setattr(self, key, [Member(i, self.__token)
                                    for i in json[key]])
            elif key == "channels":
                setattr(self, key, [Channel(i, self.__token)
                                    for i in json[key]])
            elif key == "threads":
                setattr(self, key, [Channel(i, self.__token)
                                    for i in json[key]])
            else:
                setattr(self, key, json[key])

    async def edit(self, params=None):
        """Edit a guild with API params."""
        if params is None:
            params = {}
        raise_error(params, "params", dict)

        atom, result = await Request().send_async_request(f"/guilds/{self.id}", "PATCH", self.__token, params)

        if atom == 0:
            return Guild(result, self.__token)
        else:
            raise EditGuildFailed(result)

    async def fetch_channels(self):
        """Fetch all channels in the guild and returns."""

        from .Channel import Channel

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/channels", "GET", self.__token)

        if atom == 0:
            return [Channel(i, self.__token) for i in result]
        else:
            raise FetchGuildChannelsFailed(result)

    async def create_channel(self, params=None):
        """Create new channel with API params."""
        if params is None:
            params = {}
        raise_error(params, "params", dict)

        from .Channel import Channel

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/channels", "POST", self.__token, params)

        if atom == 0:
            return Channel(result, self.__token)
        else:
            raise CreateGuildChannelFailed(result)

    async def edit_channel_position(self, *args):
        """Edit multiple channel position with API params."""

        for arg in args:
            raise_error(arg, "arg", dict)

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/channels", "PATCH", self.__token, [*args])

        if atom == 0:
            return True
        else:
            raise ChangeChannelPositionFailed(result)

    async def fetch_member(self, user_id: str):
        """Fetch a member from guild with id."""
        raise_error(user_id, "user_id", str)

        from .Member import Member

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/members/{user_id}", "GET", self.__token)

        if atom == 0:
            return Member(result, self.__token)
        else:
            raise FetchGuildMemberFailed(result)

    async def fetch_member_list(self, options: dict = None):
        """Fetch a member from guild with id."""
        if options is None:
            options = {}

        raise_error(options, "options", dict)

        from .Member import Member

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/members{d2q_converter(options)}", "GET", self.__token)

        if atom == 0:
            return [Member(i, self.__token) for i in result]
        else:
            raise FetchGuildMembersFailed(result)
