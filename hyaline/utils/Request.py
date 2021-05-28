from typing import Tuple
from aiohttp import ClientSession, client_exceptions
from dataclasses import dataclass


@dataclass
class Request(object):
    api: str = "https://discord.com/api/v9"

    async def send_async_request(self, endpoint: str, method: str, token: str, body: dict = None) -> Tuple:
        """Send an async request to discord API."""

        result: tuple = ()
        # Atom 0: When Request Success (atom, json)
        # Atom 1: When Request Got Error (atom, error_message)

        url: str = f"{self.api}{endpoint}"

        async with ClientSession(trust_env=True) as session:
            async with session.request(method, url, headers={"Authorization": f"Bot {token}", 'Content-Type': 'application/json'}, json=body) as response:
                try:
                    json_data = await response.json()
                except client_exceptions.ContentTypeError:
                    body_text = await response.text()
                    return (1, body_text)

                if response.status != 200:
                    result = (
                        1,
                        f"Error ({response.status}): {json_data['message']}\nRetry After? {json_data['retry_after'] if 'retry_after' in json_data else 'Not Found'}",
                    )
                else:
                    result = (0, json_data, )

                return result
