from dataclasses import dataclass
from typing import Union
from asyncio import sleep

from aiohttp import ClientSession, client_exceptions


@dataclass
class Request:
    api: str = "https://discord.com/api/v9"
    ratelimit = {
        "left": None,
        "reset_after": None
    }

    async def send_async_request(self, endpoint: str, method: str, token: str, body: Union[dict, list] = None) -> tuple:
        """Send an async request to discord API."""

        if self.ratelimit["left"] in (0, 1):
            await sleep(self.ratelimit["reset_after"] + 0.1)

        result: tuple = ()
        # Atom 0: When Request Success (atom, json)
        # Atom 1: When Request Got Error (atom, error_message)

        url: str = f"{self.api}{endpoint}"

        async with ClientSession(trust_env=True) as session:
            async with session.request(method, url,
                                       headers={"Authorization": f"Bot {token}",
                                                'Content-Type': 'application/json'},
                                       json=body) as response:
                try:
                    json_data = await response.json()
                except client_exceptions.ContentTypeError:
                    body_text = await response.text()

                    if str(response.status).startswith("2"):
                        return (0, "")
                    else:
                        return (1, body_text)

                self.ratelimit["left"] = int(
                    response.headers.get("x-ratelimit-remaining") or 5)
                self.ratelimit["reset_after"] = float(
                    response.headers.get("x-ratelimit-reset-after") or 0.0)

                if not str(response.status).startswith("2"):
                    result = (
                        1,
                        f"Error ({response.status}): {json_data['message']}\nRetry After? {json_data['retry_after'] if 'retry_after' in json_data else 'Not Found'}",
                    )
                else:

                    result = (0, json_data,)

                return result
