import asyncio
import json
import sys
import traceback
from typing import Callable

import aiohttp

from ..errors.SessionErrors import TokenNotFoundError, InvalidTokenError, IntentNotFoundError
from ..models.Channel import Channel
from ..models.ClientUser import ClientUser
from ..models.Guild import Guild
from ..models.Member import Member
from ..models.Message import Message
from ..models.User import User
from ..utils.Request import Request
from ..utils.WrongType import raise_error
from ..meta import __version__, __author__

async_request = Request().send_async_request


class Session:
    """Session class for connection and etc.."""
    DISPATCH = 0
    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE = 3
    VOICE_STATE = 4
    VOICE_PING = 5
    RESUME = 6
    RECONNECT = 7
    REQUEST_MEMBERS = 8
    INVALID_SESSION = 9
    HELLO = 10
    HEARTBEAT_ACK = 11
    GUILD_SYNC = 12

    def __init__(self, options: dict, will_loaded_events: list = None) -> None:
        if not isinstance(options, dict):
            raise TypeError("Options argument must be a dictionary.")

        self.options = options

        if "TOKEN" not in self.options:
            raise TokenNotFoundError("Please pass a token in session option.")

        if "INTENTS" not in self.options:
            raise IntentNotFoundError(
                "Please pass a intent.")

        raise_error(self.options['TOKEN'], "TOKEN", str)
        raise_error(self.options['INTENTS'], "INTENTS", int)

        self.shard_count = 0

        if 'MAX_MESSAGES' in self.options:
            raise_error(self.options['MAX_MESSAGES'], "MAX_MESSAGES", int)
            self.max_messages = options['MAX_MESSAGES']
        else:
            self.max_messages = 100

        self.token = self.options['TOKEN']
        self.intents = self.options['INTENTS']
        self.gateway = "wss://gateway.discord.gg/?v=9&encoding=json"
        self.ws = None
        self.client = None
        self.session_id = None
        self.event_loop = asyncio.get_event_loop()
        self.session = None
        self.shards = []

        self.events = []

        if will_loaded_events is None:
            self.__will_loaded_events = []
        else:
            self.__will_loaded_events = will_loaded_events

    def event(self, event_name: str, fn: Callable) -> True:
        """Create new event."""

        raise_error(event_name, "event_name", str)
        raise_error(fn, "function", type(lambda: True))

        self.__will_loaded_events.append({
            "EVENT": event_name,
            "FUNCTION": fn
        })

        return True

    async def __check_token(self):
        atom, result = await async_request("/users/@me", "GET", self.token)

        # Atom Check:
        if atom == 1:
            raise InvalidTokenError(
                "Token is invalid. Please check your token!")
        else:
            self.client = ClientUser(result, self.token, self.max_messages)

    def __load_events(self):
        cache_events = (
            {
                "EVENT": "MESSAGE_CREATE",
                "FUNCTION": self.client.add_message_cache
            },
            {
                "EVENT": "MESSAGE_DELETE",
                "FUNCTION": self.client.remove_message_cache
            },
            {
                "EVENT": "MESSAGE_UPDATE",
                "FUNCTION": self.client.update_message_cache
            },
            {
                "EVENT": "MESSAGE_DELETE_BULK",
                "FUNCTION": self.client.bulk_delete_message_cache
            },
            {
                "EVENT": "GUILD_CREATE",
                "FUNCTION": self.client.add_guild_cache
            },
            {
                "EVENT": "GUILD_UPDATE",
                "FUNCTION": self.client.update_guild_cache
            },
            {
                "EVENT": "GUILD_DELETE",
                "FUNCTION": self.client.remove_guild_cache
            },
            {
                "EVENT": "GUILD_MEMBER_ADD",
                "FUNCTION": self.client.add_guild_member
            },
            {
                "EVENT": "GUILD_MEMBER_REMOVE",
                "FUNCTION": self.client.remove_guild_member
            },
            {
                "EVENT": "GUILD_MEMBER_UPDATE",
                "FUNCTION": self.client.update_guild_member
            },
            {
                "EVENT": "CHANNEL_CREATE",
                "FUNCTION": self.client.add_guild_channel
            },
            {
                "EVENT": "CHANNEL_UPDATE",
                "FUNCTION": self.client.update_guild_channel
            },
            {
                "EVENT": "CHANNEL_DELETE",
                "FUNCTION": self.client.remove_guild_channel
            },
            {
                "EVENT": "READY",
                "FUNCTION": self.__get_session_id
            }
        )

        # Load Cache System
        self.events.extend([
            *cache_events,
            *self.__will_loaded_events
        ])

    async def __connect_to_gateway(self):
        self.session = aiohttp.ClientSession()
        self.ws = await self.session.ws_connect(self.gateway)

    async def __get_session_id(self, packet):
        self.session_id = packet.get('session_id')

    async def __identify(self, packet, shard_id: int = 0):
        heartbeat = packet['d']['heartbeat_interval']

        if self.session_id is None:
            payload = {
                "op": self.IDENTIFY,
                "d": {
                    "token": self.token,
                    "intents": self.intents,
                    "properties": {
                        "$os": "linux",
                        "$browser": f"@{__author__}/hyaline",
                        "$device": f"@{__author__}/hyaline"
                    }
                }
            }

            if self.shard_count > 0:
                payload['d']['shard'] = [shard_id, self.shard_count]

            await self.ws.send_json(payload)
        else:
            await self.ws.send_json({
                "op": self.RESUME,
                "d": {
                    "token": self.token,
                    "session_id": self.session_id
                }
            })

        # Keep Connection Alive:
        async def _keep_alive():
            while True:
                await self.ws.send_json({
                    "op": self.HEARTBEAT,
                    "d": None
                })

                await asyncio.sleep(heartbeat / 1000)

        asyncio.run_coroutine_threadsafe(_keep_alive(), self.event_loop)

    def __filter_events(self, events: tuple = (), *args):
        return [
            event['FUNCTION'](*args) for event in self.events if event['EVENT'] in events
        ]

    def __return_filtered_events(self, event_type, event_data):
        if event_type in ("MESSAGE_CREATE", "MESSAGE_UPDATE"):
            filtered = self.__filter_events(
                (event_type,), Message(event_data, self.token))
        elif event_type in ("GUILD_CREATE", "GUILD_UPDATE"):
            filtered = self.__filter_events(
                (event_type,), Guild(event_data, self.token))
        elif event_type in ("GUILD_MEMBER_ADD", "GUILD_MEMBER_UPDATE"):
            filtered = self.__filter_events(
                (event_type,), event_data['guild_id'], Member(event_data, self.token))
        elif event_type == "GUILD_MEMBER_REMOVE":
            filtered = self.__filter_events((event_type,), event_data['guild_id'],
                                            User(event_data['user'], self.token))
        elif event_type in ("GUILD_BAN_ADD", "GUILD_BAN_REMOVE"):
            guild_id = event_data['guild_id']
            del event_data['guild_id']

            filtered = self.__filter_events(
                (event_type,), guild_id, User(event_data, self.token))
        elif event_type in ("CHANNEL_CREATE", "CHANNEL_UPDATE", "CHANNEL_DELETE"):
            filtered = self.__filter_events(
                (event_type,), Channel(event_data, self.token))
        else:
            filtered = self.__filter_events((event_type,), event_data)

        return filtered

    async def __handle_event(self, packet):
        event_type = packet['t']
        event_data = packet['d']

        if event_type in (event['EVENT'] for event in self.events):
            filtered = self.__return_filtered_events(event_type, event_data)

            await asyncio.gather(*filtered)

    async def __receive(self, shard_id: int = None):
        while True:
            packet = await self.ws.receive()

            # WebSocket Error
            if isinstance(packet.data, int) and len(str(packet.data)) == 4:
                print("WebSocket Exception Found: {0} ({1})".format(
                    packet.data, packet.extra))
                continue
            elif isinstance(packet.data, type(None)):
                # WebSocket Closed
                if packet.type == 0x101:
                    return 0x0

            packet = json.loads(packet.data)
            # print(packet)

            if packet['op'] == self.HELLO:
                await self.__identify(packet, shard_id)
            elif packet['op'] == self.RECONNECT:
                return 0x1
            elif packet['op'] == self.DISPATCH:
                try:
                    self.event_loop.create_task(self.__handle_event(packet))
                except Exception as error:
                    error = getattr(error, 'original', error)
                    print('Exception Found In Event {0}:'.format(
                        packet['t']), file=sys.stderr)
                    traceback.print_exception(
                        type(error), error, error.__traceback__, file=sys.stderr)

    async def __start_client(self, shard_id: int = None):
        await self.__check_token()
        self.__load_events()
        await self.__connect_to_gateway()

        if shard_id is None:
            result = await self.__receive()
        else:
            result = await self.__receive(shard_id)

        self.session = None

        # Reconnect
        if result == 0x1:
            await self.__start_client()

    async def change_presence(self, params: dict = None):
        if params is None:
            params = {}

        raise_error(params, "params", dict)

        await self.ws.send_json({
            "op": self.PRESENCE,
            "d": params
        })

    def start(self, shard_count: int = None):
        """Start the session."""
        if shard_count is not None:
            raise_error(shard_count, "shard_count", int)
            self.shard_count = shard_count

            tasks = []
            for shard in range(self.shard_count):
                shard_client = Session(self.options, self.__will_loaded_events)
                self.shards.append(shard_client)

                tasks.append(shard_client.__start_client(shard))

            async def __host_shards(shards):
                return await asyncio.gather(*shards)

            self.event_loop.run_until_complete(__host_shards(tasks))
        else:
            self.event_loop.run_until_complete(self.__start_client())
