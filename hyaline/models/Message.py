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

        self.id: str = json['id']
        self.channel_id: str = json['channel_id']
        self.guild_id: Union[str,
                             None] = json['guild_id'] if 'guild_id' in json else None
        self.author: Union[User, None] = User(
            json['author'], self.__token) if 'author' in json else None
        self.member: Union[Member, None] = Member(
            json['member'], self.__token) if 'member' in json else None
        self.content: str = json['content']
        self.timestamp: datetime = parse(json['timestamp'])
        self.edited_timestamp: Union[datetime, None] = parse(
            json['edited_timestamp']) if 'edited_timestamp' in json and json['edited_timestamp'] else None
        self.tts: bool = json['tts']

        self.mention_everyone: bool = json['mention_everyone']
        self.mentions: list = [User(i, self.__token) for i in json['mentions']]
        self.mention_roles: bool = json['mention_everyone']
        self.mention_channels: Union[list,
                                     None] = json['mention_channels'] if 'mention_channels' in json else None
        self.attachments: list = [Attachment(i) for i in json['attachments']]
        self.embeds: list = [Embed(i) for i in json['embeds']]
        self.reactions: Union[list, None] = [Reaction(
            i, self.__token) for i in json['reactions']] if 'reactions' in json else None
        self.nonce: Union[str, int,
                          None] = json['nonce'] if 'nonce' in json else None
        self.pinned: bool = json['pinned']
        self.webhook_id: Union[str,
                               None] = json['webhook_id'] if 'webhook_id' in json else None
        self.type: int = json['type']

        self.activity: Union[MessageActivity, None] = MessageActivity(
            json['activity']) if 'activity' in json else None
        self.application: Union[Application, None] = Application(
            json['application'], self.__token) if 'application' in json else None
        self.application_id: Union[str,
                                   None] = json['application_id'] if 'application_id' in json else None

        self.message_reference: Union[MessageReference, None] = MessageReference(
            json['message_reference']) if 'message_reference' in json else None
        self.flags: Union[int,
                          None] = json['flags'] if 'flags' in json else None
        self.stickers: Union[Sticker, None] = Sticker(
            json['stickers']) if 'stickers' in json else None
        self.referenced_message: Union[Message, None] = Message(
            json['referenced_message'], self.__token) if 'referenced_message' in json and json['referenced_message'] else None
        self.thread: Union[Channel, None] = Channel(
            json['thread'], self.__token) if 'thread' in json else None

        self.components: Union[dict,
                               None] = json['components'] if 'components' in json else None

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
