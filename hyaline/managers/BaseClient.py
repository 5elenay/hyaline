import asyncio
import json
import sys
import time
import traceback
from typing import Callable

import aiohttp

from ..errors.SessionErrors import TokenNotFoundError, InvalidTokenError, IntentNotFoundError
from ..models.ClientUser import ClientUser
from ..models.Guild import Guild
from ..models.Member import Member
from ..models.Message import Message
from ..models.User import User
from ..utils.Request import Request
from ..utils.WrongType import raise_error

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

    def __init__(self, options: dict) -> None:
        if not isinstance(options, dict):
            raise TypeError("Options argument must be a dictionary.")

        if "TOKEN" not in options:
            raise TokenNotFoundError("Please pass a token in session option.")

        if "INTENTS" not in options:
            raise IntentNotFoundError(
                "Please pass a intent.")

        raise_error(options['TOKEN'], "TOKEN", str)
        raise_error(options['INTENTS'], "INTENTS", int)

        self.token = options['TOKEN']
        self.intents = options['INTENTS']
        self.gateway = "wss://gateway.discord.gg/?v=9&encoding=json"
        self.ws = None
        self.client = None
        self.event_loop = asyncio.get_event_loop()

        self.events = []
        self.__will_loaded_events = []

    def event(self, event_name: str, fn: Callable) -> True:
        """Create new event."""

        raise_error(event_name, "Event Name", str)
        raise_error(fn, "Function", type(lambda: True))

        self.__will_loaded_events.append({
            "EVENT": event_name,
            "FUNCTION": fn
        })

        return True

    async def __check_token(self):
        atom, result = await async_request("/users/@me", "GET", self.token)

        # Atom Check:
        if atom == 1:
            raise InvalidTokenError("Token is invalid. Please check your token!")
        else:
            self.client = ClientUser(result, self.token)

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
        )

        # Load Cache System
        self.events.extend([
            *cache_events,
            *self.__will_loaded_events
        ])

    async def __connect_to_gateway(self):
        self.ws = await aiohttp.ClientSession().ws_connect(self.gateway)

    async def __identify(self, packet):
        heartbeat = packet['d']['heartbeat_interval']

        await self.ws.send_str(json.dumps({
            "op": 2,
            "d": {
                "token": self.token,
                "intents": self.intents,
                "properties": {
                    "$os": "linux",
                    "$browser": "5elenay/hyaline",
                    "$device": "5elenay/hyaline"
                }
            }
        }))

        # Keep Connection Alive:
        async def _keep_alive():
            while True:
                started = time.time()

                await self.ws.send_str(json.dumps({
                    "op": 1,
                    "d": None
                }))

                await asyncio.sleep(heartbeat / 1000)

        asyncio.run_coroutine_threadsafe(_keep_alive(), self.event_loop)

    def __filter_events(self, events: tuple = (), *args):
        return [
            event['FUNCTION'](*args) for event in self.events if event['EVENT'] in events
        ]

    async def __handle_event(self, packet):
        event_type = packet['t']
        event_data = packet['d']

        if event_type in [event['EVENT'] for event in self.events]:
            if event_type in ("MESSAGE_CREATE", "MESSAGE_UPDATE"):
                filtered = self.__filter_events((event_type,), Message(event_data, self.token))
            elif event_type in ("GUILD_CREATE", "GUILD_UPDATE"):
                filtered = self.__filter_events((event_type,), Guild(event_data, self.token))
            elif event_type in ("GUILD_MEMBER_ADD", "GUILD_MEMBER_UPDATE"):
                filtered = self.__filter_events((event_type,), event_data['guild_id'], Member(event_data, self.token))
            elif event_type == "GUILD_MEMBER_REMOVE":
                filtered = self.__filter_events((event_type,), event_data['guild_id'],
                                                User(event_data['user'], self.token))
            else:
                filtered = self.__filter_events((event_type,), event_data)

            await asyncio.gather(*filtered)
        else:
            return None

    async def __receive(self):
        while True:
            packet = await self.ws.receive()
            packet = json.loads(packet.data)

            print(packet)

            if packet['op'] == self.HELLO:
                await self.__identify(packet)
            elif packet['op'] == self.DISPATCH:
                try:
                    self.event_loop.create_task(self.__handle_event(packet))
                except Exception as error:
                    error = getattr(error, 'original', error)
                    print('Exception Found In Event {0}:'.format(packet['t']), file=sys.stderr)
                    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    async def __start_client(self):
        await self.__check_token()
        self.__load_events()
        await self.__connect_to_gateway()
        await self.__receive()

    def start(self):
        """Start the session."""
        
        self.event_loop.run_until_complete(self.__start_client())
