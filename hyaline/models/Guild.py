from dataclasses import dataclass

from dateutil.parser import parse

from ..errors.GuildErrors import *
from ..utils.Dict2Query import convert as d2q_converter
from ..utils.Request import Request
from ..utils.WrongType import raise_error


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
        """Fetch member list with API params."""
        if options is None:
            options = {}

        raise_error(options, "options", dict)

        from .Member import Member

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/members{d2q_converter(options)}", "GET",
                                                          self.__token)

        if atom == 0:
            return [Member(i, self.__token) for i in result]
        else:
            raise FetchGuildMembersFailed(result)

    async def search_members(self, options: dict = None):
        """Search members with API params (https://discord.com/developers/docs/resources/guild#search-guild-members-query-string-params)."""
        if options is None:
            options = {}

        raise_error(options, "options", dict)

        from .Member import Member

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/members/search{d2q_converter(options)}",
                                                          "GET", self.__token)

        if atom == 0:
            return [Member(i, self.__token) for i in result]
        else:
            raise SearchGuildMemberFailed(result)

    async def edit_member(self, member_id: str, options: dict = None):
        """Edit guild member with API params."""
        if options is None:
            options = {}

        raise_error(member_id, "member_id", str)
        raise_error(options, "options", dict)

        from .Member import Member

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/members/{member_id}", "PATCH",
                                                          self.__token, options)

        if atom == 0:
            return Member(result, self.__token)
        else:
            raise EditGuildMemberFailed(result)

    async def fetch_emoji_list(self):
        """Fetch all emojis in the guild."""

        from .Emoji import Emoji

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/emojis", "GET", self.__token)

        if atom == 0:
            return [Emoji(i, self.__token) for i in result]
        else:
            raise FetchGuildEmojiListFailed(result)

    async def fetch_emoji(self, emoji_id: str):
        """Fetch guild emoji with id."""

        from .Emoji import Emoji

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/emojis/{emoji_id}", "GET", self.__token)

        if atom == 0:
            return Emoji(result, self.__token)
        else:
            raise FetchGuildEmojiFailed(result)

    async def create_emoji(self, options=None):
        """Create guild emoji with API params."""

        if options is None:
            options = {}

        raise_error(options, "options", dict)

        from .Emoji import Emoji

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/emojis", "POST", self.__token, options)

        if atom == 0:
            return Emoji(result, self.__token)
        else:
            raise CreateGuildEmojiFailed(result)

    async def edit_emoji(self, emoji_id: str, options=None):
        """Edit guild emoji with API params."""
        if options is None:
            options = {}

        raise_error(emoji_id, "emoji_id", str)
        raise_error(options, "options", dict)

        from .Emoji import Emoji

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/emojis/{emoji_id}", "PATCH", self.__token,
                                                          options)

        if atom == 0:
            return Emoji(result, self.__token)
        else:
            raise EditGuildEmojiFailed(result)

    async def remove_emoji(self, emoji_id: str):
        """Remove guild emoji with id."""

        raise_error(emoji_id, "emoji_id", str)

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/emojis/{emoji_id}", "DELETE",
                                                          self.__token)

        if atom == 0:
            return True
        else:
            raise DeleteGuildEmojiFailed(result)

    async def add_role(self, member_id: str, role_id: str):
        """Add a role to guild member."""

        raise_error(member_id, "member_id", str)
        raise_error(role_id, "role_id", str)

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/members/{member_id}/roles/{role_id}",
                                                          "PUT", self.__token)

        if atom == 0:
            return self, member_id, role_id
        else:
            raise AddRoleToGuildMemberFailed(result)

    async def remove_role(self, member_id: str, role_id: str):
        """Remove a role from guild member."""

        raise_error(member_id, "member_id", str)
        raise_error(role_id, "role_id", str)

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/members/{member_id}/roles/{role_id}",
                                                          "DELETE", self.__token)

        if atom == 0:
            return self, member_id, role_id
        else:
            raise RemoveRoleFromGuildMemberFailed(result)

    async def kick(self, member_id: str):
        """Kick a member from guild."""

        raise_error(member_id, "member_id", str)

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/members/{member_id}", "DELETE",
                                                          self.__token)

        if atom == 0:
            return self, member_id
        else:
            raise KickMemberFromGuildFailed(result)

    async def ban(self, member_id: str, params: dict = None):
        """Ban a member from guild."""

        if params is None:
            params = {}

        raise_error(member_id, "member_id", str)
        raise_error(params, "params", dict)

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/bans/{member_id}", "PUT", self.__token,
                                                          params)

        if atom == 0:
            return self, member_id
        else:
            raise BanMemberFromGuildFailed(result)

    async def unban(self, member_id: str):
        """Unban a member from guild."""

        raise_error(member_id, "member_id", str)

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/bans/{member_id}", "DELETE", self.__token,
                                                          {})

        if atom == 0:
            return self, member_id
        else:
            raise UnbanGuildMemberFailed(result)

    async def fetch_bans(self):
        """Fetch all guild bans."""

        from .Ban import Ban

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/bans", "GET", self.__token)

        if atom == 0:
            return [Ban(i, self.__token) for i in result]
        else:
            raise FetchGuildBansFailed(result)

    async def fetch_member_ban(self, member_id: str):
        """Fetch an user guild ban."""

        from .Ban import Ban

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/bans/{member_id}", "GET", self.__token)

        if atom == 0:
            return Ban(result, self.__token)
        else:
            raise FetchGuildBanFailed(result)

    async def is_banned(self, member_id: str) -> bool:
        """Check is guild member banned from guild."""

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/bans/{member_id}", "GET", self.__token)

        if atom == 0:
            return True
        else:
            return False

    async def fetch_roles(self):
        """Fetch all roles from guild."""

        from .Role import Role

        atom, result = await Request().send_async_request(f"/guilds/{self.id}/roles", "GET", self.__token)

        if atom == 0:
            return [Role(i) for i in result]
        else:
            return FetchGuildRolesFailed(result)
