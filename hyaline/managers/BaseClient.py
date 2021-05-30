from typing import Callable
from ..models.ClientUser import ClientUser
from ..errors.SessionErrors import TokenNotFoundError, InvalidTokenError, IntentNotFoundError
from ..utils.Request import Request
from ..utils.WrongType import raise_error
from ..models.Message import Message
from gc import collect as collect_garbage

from websockets import connect as wconnect
import json
import asyncio
import sys
import traceback

async_request = Request().send_async_request

# Session Class


class Session:
    def __init__(self, options: dict) -> None:
        if not isinstance(options, dict):
            raise TypeError("Options argument must be a dictionary.")

        if "TOKEN" not in options:
            raise TokenNotFoundError("Please pass a token in session option.")

        if "INTENTS" not in options:
            raise IntentNotFoundError(
                "Please pass a intent number (https://discord.com/developers/docs/topics/gateway#gateway-intents) in session option. For calculation: https://ziad87.net/intents/")

        raise_error(options['TOKEN'], "TOKEN", str)
        raise_error(options['INTENTS'], "INTENTS", int)

        self.token = options['TOKEN']
        self.intents = options['INTENTS']
        self.ws = "wss://gateway.discord.gg/?v=9&encoding=json"

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

    def start(self) -> None:
        loop = asyncio.get_event_loop()

        async def _connect() -> None:
            """Start the session."""
            atom, result = await async_request("/users/@me", "GET", self.token)

            # Atom Check:
            if atom == 1:
                raise InvalidTokenError(
                    "Token is invalid. Please check your token!")
            else:
                self.client = ClientUser(result, self.token)

                # Load Cache System
                self.events.extend([
                    {
                        "EVENT": "MESSAGE_CREATE",
                        "FUNCTION": self.client._add_message_cache
                    },
                    {
                        "EVENT": "MESSAGE_DELETE",
                        "FUNCTION": self.client._remove_message_cache
                    },
                    {
                        "EVENT": "MESSAGE_UPDATE",
                        "FUNCTION": self.client._update_message_cache
                    },
                    {
                        "EVENT": "MESSAGE_DELETE_BULK",
                        "FUNCTION": self.client._bulk_delete_message_cache
                    },
                    *self.__will_loaded_events
                ])

                # Websocket Connection:
                async with wconnect(self.ws) as websocket:
                    while True:
                        collect_garbage()
                        websocket_result = json.loads(await websocket.recv())
                        print(
                            json.dumps(
                                websocket_result,
                                indent=4),
                            end="\n\n")

                        try:
                            # Async Event Run Function
                            async def _run_async_event(class_optional: Callable = None, token: str = None, events: tuple = ()):
                                if class_optional is None:
                                    if token is None:
                                        await asyncio.gather(*(
                                            k['FUNCTION'](websocket_result['d']) for k in self.events if k['EVENT'] in events
                                        ))
                                    else:
                                        await asyncio.gather(*(
                                            k['FUNCTION'](websocket_result['d'], token) for k in self.events if k['EVENT'] in events
                                        ))
                                else:
                                    if token is None:
                                        await asyncio.gather(*(
                                            k['FUNCTION'](class_optional(websocket_result['d'])) for k in self.events if k['EVENT'] in events
                                        ))
                                    else:
                                        await asyncio.gather(*(
                                            k['FUNCTION'](class_optional(websocket_result['d'], token)) for k in self.events if k['EVENT'] in events
                                        ))

                            if websocket_result['t'] in (
                                    k['EVENT'] for k in self.events):
                                if websocket_result['t'] in (
                                        "MESSAGE_CREATE", "MESSAGE_UPDATE", ):
                                    loop.create_task(
                                        _run_async_event(
                                            Message, self.token, ("MESSAGE_CREATE", "MESSAGE_UPDATE", )))
                                else:
                                    loop.create_task(_run_async_event())

                        except Exception as error:
                            error = getattr(error, 'original', error)
                            print('Exception Found, Ignored:', file=sys.stderr)
                            traceback.print_exception(
                                type(error), error, error.__traceback__, file=sys.stderr)

                        if websocket_result['op'] == 10:
                            heartbeat = websocket_result['d']['heartbeat_interval']
                            await websocket.send(json.dumps({
                                "op": 2,
                                "d": {
                                    "token": self.token,
                                    "intents": self.intents,
                                    "properties": {
                                        "$os": "linux",
                                        "$browser": "hyaline",
                                        "$device": "hyaline"
                                    }
                                }
                            }))

                            # Keep Connection Alive:
                            async def keep_alive():
                                while True:
                                    await websocket.send(json.dumps({
                                        "op": 1,
                                        "d": None
                                    }))

                                    await asyncio.sleep(heartbeat / 1000)

                            loop.create_task(keep_alive())

        loop.run_until_complete(_connect())
