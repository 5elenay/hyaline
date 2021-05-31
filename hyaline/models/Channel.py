from dataclasses import dataclass
from typing import Union
from ..utils.Request import Request
from ..errors.ChannelErrors import *
from datetime import datetime
from dateutil.parser import parse
from ..utils.WrongType import raise_error
from ..utils.Dict2Query import convert as d2q_converter


@dataclass
class Channel:
    # Attrs
    def __init__(self, json: dict, token: str) -> None:
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

    async def send(self, options: dict = {}):
        """Send message to the channel."""
        raise_error(options, "options", dict)

        from .Message import Message

        atom, result = await Request().send_async_request(f"/channels/{self.id}/messages", "POST", self.__token, options)

        if atom == 0:
            return Message(result, self.__token)
        else:
            raise SendMessageToChannelFailed(result)

    async def edit(self, options: dict = {}):
        """Edit channel with API params."""
        raise_error(options, "options", dict)

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
        raise_error(options, "options", dict)

        from .Message import Message

        atom, result = await Request().send_async_request(f"/channels/{self.id}/messages{d2q_converter(options)}", "GET", self.__token)

        if atom == 0:
            return [Message(i, self.__token) for i in result]
        else:
            raise FetchChannelHistoryFailed(result)

    async def fetch_message(self, id: str):
        """Fetch channel message with id."""
        raise_error(id, "id", str)

        from .Message import Message

        atom, result = await Request().send_async_request(f"/channels/{self.id}/messages/{id}", "GET", self.__token)

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

    async def create_invite(self, params: dict = {}):
        """Create new invite with API params."""
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

        atom, result = await Request().send_async_request(f"/channels/{self.id}/pins/{message_id}", "DELETE", self.__token)

        if atom == 0:
            return True
        else:
            raise PinMessageFailed(result)
