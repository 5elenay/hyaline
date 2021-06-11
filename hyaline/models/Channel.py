from dataclasses import dataclass

from dateutil.parser import parse

from ..errors.ChannelErrors import *
from ..utils.Dict2Query import convert as d2q_converter
from ..utils.Request import Request
from ..utils.WrongType import raise_error


@dataclass
class Channel:
    # Attrs
    def __init__(self, json: dict, token: str) -> None:
        self.id = None

        from .Overwrite import Overwrite
        from .User import User
        from .ThreadMetadata import ThreadMetadata
        from .ThreadMember import ThreadMember

        self.__token: str = token

        for key in json:
            if key == "permission_overwrites":
                setattr(self, key, [Overwrite(i) for i in json[key]])
            elif key == "recipients":
                setattr(self, key, [User(i, self.__token) for i in json[key]])
            elif key == "last_pin_timestamp":
                setattr(self, key, parse(json[key]) if json[key] else None)
            elif key == "thread_metadata":
                setattr(self, key, ThreadMetadata(json[key]))
            elif key == "member":
                setattr(self, key, ThreadMember(json[key]))
            else:
                setattr(self, key, json[key])

    async def send(self, options=None):
        """Send message to the channel."""
        if options is None:
            options = {}

        raise_error(options, "options", dict)

        from .Message import Message

        atom, result = await Request().send_async_request(f"/channels/{self.id}/messages", "POST", self.__token,
                                                          options)

        if atom == 0:
            return Message(result, self.__token)
        else:
            raise SendMessageToChannelFailed(result)

    async def edit(self, options=None):
        """Edit channel with API params."""
        if options is None:
            options = {}
        raise_error(options, "options", dict)

        atom, result = await Request().send_async_request(f"/channels/{self.id}", "PATCH", self.__token, options)

        if atom == 0:
            return Channel(result, self.__token)
        else:
            raise EditChannelFailed(result)

    async def delete(self):
        """Delete current channel."""

        atom, result = await Request().send_async_request(f"/channels/{self.id}", "DELETE", self.__token, {})

        if atom == 0:
            return Channel(result, self.__token)
        else:
            raise DeleteChannelFailed(result)

    async def delete_message(self, message_id: str):
        """Delete a message from channel."""

        atom, result = await Request().send_async_request(f"/channels/{self.id}/messages/{message_id}", "DELETE", self.__token, {})

        if atom == 0:
            return self
        else:
            raise DeleteChannelMessageFailed(result)

    async def fetch_history(self, options=None):
        """Fetch channel history with API params."""
        if options is None:
            options = {}
        raise_error(options, "options", dict)

        from .Message import Message

        atom, result = await Request().send_async_request(f"/channels/{self.id}/messages{d2q_converter(options)}",
                                                          "GET", self.__token)

        if atom == 0:
            return [Message(i, self.__token) for i in result]
        else:
            raise FetchChannelHistoryFailed(result)

    async def fetch_message(self, message_id: str):
        """Fetch channel message with id."""
        raise_error(message_id, "id", str)

        from .Message import Message

        atom, result = await Request().send_async_request(f"/channels/{self.id}/messages/{message_id}", "GET",
                                                          self.__token)

        if atom == 0:
            return Message(result, self.__token)
        else:
            raise FetchChannelMessageFailed(result)

    async def fetch_invites(self):
        """Fetch channel invites."""
        from .Invite import Invite

        atom, result = await Request().send_async_request(f"/channels/{self.id}/invites", "GET", self.__token)

        if atom == 0:
            return [Invite(i, self.__token) for i in result]
        else:
            raise FetchChannelInvitesFailed(result)

    async def create_invite(self, params=None):
        """Create new invite with API params."""
        if params is None:
            params = {}
        raise_error(params, "params", dict)

        from .Invite import Invite

        atom, result = await Request().send_async_request(f"/channels/{self.id}/invites", "POST", self.__token, params)

        if atom == 0:
            return Invite(result, self.__token)
        else:
            raise CreateInviteFailed(result)

    async def pinned_messages(self):
        """Fetch pinned messages."""
        from .Message import Message

        atom, result = await Request().send_async_request(f"/channels/{self.id}/pins", "GET", self.__token)

        if atom == 0:
            return [Message(i, self.__token) for i in result]
        else:
            raise FetchPinnedMessagesFailed(result)

    async def pin_message(self, message_id: str):
        """Pin a message with id."""
        raise_error(message_id, "message_id", str)

        atom, result = await Request().send_async_request(f"/channels/{self.id}/pins/{message_id}", "PUT", self.__token)

        if atom == 0:
            return True
        else:
            raise PinMessageFailed(result)

    async def unpin_message(self, message_id: str):
        """Unpin a message with id."""
        raise_error(message_id, "message_id", str)

        atom, result = await Request().send_async_request(f"/channels/{self.id}/pins/{message_id}", "DELETE",
                                                          self.__token, {})

        if atom == 0:
            return True
        else:
            raise UnpinMessageFailed(result)

    async def edit_permissions(self, user_or_role_id: str, params: dict):
        """Edit channel permission. (bitwise must be string.)"""
        raise_error(user_or_role_id, "user_or_role_id", str)
        raise_error(params, "params", dict)

        atom, result = await Request().send_async_request(f"/channels/{self.id}/permissions/{user_or_role_id}", "PUT",
                                                          self.__token, params)

        if atom == 0:
            return self
        else:
            raise EditChannelPermissionsFailed(result)

    async def delete_permissions(self, user_or_role_id: str):
        """Delete permissions from role/user"""
        raise_error(user_or_role_id, "user_or_role_id", str)

        atom, result = await Request().send_async_request(f"/channels/{self.id}/permissions/{user_or_role_id}",
                                                          "DELETE", self.__token, {})

        if atom == 0:
            return self
        else:
            raise DeleteChannelPermissionsFailed(result)

    async def trigger_typing(self):
        """Start typing in this channel."""

        atom, result = await Request().send_async_request(f"/channels/{self.id}/typing", "POST", self.__token)

        if atom == 0:
            return self
        else:
            raise TriggerTypingFailed(result)
