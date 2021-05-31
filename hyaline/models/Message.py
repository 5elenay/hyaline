from dataclasses import dataclass
from datetime import datetime
from dateutil.parser import parse
from typing import Union
from ..utils.Request import Request
from ..errors.ChannelErrors import *
from ..errors.MessageErrors import *
from ..utils.WrongType import raise_error
from ..utils.Dict2Query import convert as d2q_converter
from urllib.parse import quote


@dataclass
class Message:
    # Attrs
    def __init__(self, json, token) -> None:
        from .Reaction import Reaction
        from .MessageActivity import MessageActivity
        from .Application import Application
        from .MessageReference import MessageReference
        from .Sticker import Sticker
        from .Channel import Channel
        from .Member import Member
        from .User import User
        from .Embed import Embed
        from .Attachment import Attachment

        self.__token: str = token

        for key in json:
            if key in ("mentions", "author"):
                setattr(
                    self,
                    key,
                    User(
                        json[key],
                        self.__token) if key == "author" else [
                        User(
                            i,
                            self.__token) for i in json[key]])
            elif key == "member":
                setattr(self, key, Member(json[key], self.__token))
            elif key in ("timestamp", "edited_timestamp"):
                setattr(self, key, parse(json[key]) if json[key] else None)
            elif key == "mentions":
                setattr(self, key, [User(i, self.__token) for i in json[key]])
            elif key == "attachments":
                setattr(self, key, [Attachment(i) for i in json[key]])
            elif key == "embeds":
                setattr(self, key, [Embed(i) for i in json[key]])
            elif key == "reactions":
                setattr(self, key, [Reaction(i, self.__token)
                        for i in json[key]])
            elif key == "activity":
                setattr(self, key, MessageActivity(json[key]))
            elif key == "application":
                setattr(self, key, Application(json[key], self.__token))
            elif key == "message_reference":
                setattr(self, key, MessageReference(json[key]))
            elif key == "stickers":
                setattr(self, key, [Sticker(i) for i in json[key]])
            elif key == "referenced_message":
                setattr(
                    self,
                    key,
                    Message(
                        json[key],
                        self.__token) if json[key] else None)
            elif key == "thread":
                setattr(self, key, Channel(json[key], self.__token))
            else:
                setattr(self, key, json[key])

    async def reply(self, options: dict = {}):
        """Reply to the message with API params."""
        raise_error(options, "options", dict)

        atom, result = await Request().send_async_request(f"/channels/{self.channel_id}/messages", "POST", self.__token, {
            **options,
            "message_reference": {
                "message_id": self.id
            }
        })

        if atom == 0:
            return Message(result, self.__token)
        else:
            raise SendMessageToChannelFailed(result)

    async def edit(self, options: dict = {}):
        """Edit your message with API params."""
        raise_error(options, "options", dict)

        atom, result = await Request().send_async_request(f"/channels/{self.channel_id}/messages/{self.id}", "PATCH", self.__token, options)

        if atom == 0:
            return Message(result, self.__token)
        else:
            raise EditMessageFailed(result)

    async def delete(self):
        """Delete the message."""

        atom, result = await Request().send_async_request(f"/channels/{self.channel_id}/messages/{self.id}", "DELETE", self.__token)

        if atom == 0:
            return self
        else:
            raise DeleteMessageFailed(result)

    async def add_reaction(self, emoji: str):
        """Add reaction to message."""
        raise_error(emoji, "emoji", str)

        atom, result = await Request().send_async_request(f"/channels/{self.channel_id}/messages/{self.id}/reactions/{quote(emoji)}/@me", "PUT", self.__token)

        if atom == 0:
            return self
        else:
            raise AddReactionToMessageFailed(result)

    async def remove_reaction(self, emoji: str, user: str = None):
        """Remove an user reaction from message."""
        raise_error(emoji, "emoji", str)

        if user is not None:
            raise_error(user, "user", str)

        atom, result = await Request().send_async_request(f"/channels/{self.channel_id}/messages/{self.id}/reactions/{quote(emoji)}/{'@me' if user is None else user}", "DELETE", self.__token)

        if atom == 0:
            return self
        else:
            raise RemoveReactionToMessageFailed(result)

    async def fetch_reactions(self, emoji: str, options: dict = {"limit": 25}):
        """Fetch message reactions with API params."""

        from .User import User

        raise_error(emoji, "emoji", str)
        raise_error(options, "options", dict)

        query_param = f"/channels/{self.channel_id}/messages/{self.id}/reactions/{emoji}{d2q_converter(options)}"

        atom, result = await Request().send_async_request(query_param, "GET", self.__token)

        if atom == 0:
            return [User(i, self.__token) for i in result]
        else:
            raise FetchReactionsFromMessageFailed(result)

    async def remove_reactions(self, emoji: str = None):
        """Fetch message reactions with API params."""
        if emoji is not None:
            raise_error(emoji, "emoji", str)

        atom, result = await Request().send_async_request(f"/channels/{self.channel_id}/messages/{self.id}/reactions{'/' + quote(emoji) if emoji is not None else ''}", "DELETE", self.__token)

        if atom == 0:
            return True
        else:
            raise RemoveReactionsFromMessageFailed(result)

    async def crosspost(self):
        """Cross post the message (https://discord.com/developers/docs/resources/channel#crosspost-message)"""

        atom, result = await Request().send_async_request(f"/channels/{self.channel_id}/messages/{self.id}/crosspost", "POST", self.__token)

        if atom == 0:
            return Message(result, self.__token)
        else:
            raise CrossPostMessageFailed(result)
