from dataclasses import dataclass
from ..utils.Request import Request
from ..errors.WebhookErrors import *
from ..utils.WrongType import raise_error


@dataclass
class Webhook:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token
        self.request_handler = Request()

        from .User import User
        from .Guild import Guild
        from .Channel import Channel

        for key in json:
            if key == "user":
                setattr(self, key, User(json[key], self.__token))
            elif key == "source_guild":
                setattr(self, key, Guild(json[key], self.__token))
            elif key == "source_channel":
                setattr(self, key, Channel(json[key], self.__token))
            else:
                setattr(self, key, json[key])

    async def edit(self, params: dict):
        """Modify the webhook with API params."""
        raise_error(params, "params", dict)

        from .Webhook import Webhook

        atom, result = await self.request_handler.send_async_request(f"/webhooks/{self.id}", "PATCH", self.__token, params)

        if atom == 0:
            return Webhook(result, self.__token)
        else:
            raise ModifyWebhookFailed(result)

    async def delete(self):
        """Delete the webhook."""

        atom, result = await self.request_handler.send_async_request(f"/webhooks/{self.id}", "DELETE", self.__token, {})

        if atom == 0:
            return self
        else:
            raise DeleteWebhookFailed(result)

    async def execute(self, params: dict, **kwargs):
        """Execute the webhook with API params."""
        raise_error(params, "params", dict)

        from ..utils.Dict2Query import convert as d2q

        atom, result = await self.request_handler.send_async_request(f"/webhooks/{self.id}/{self.token}{d2q(kwargs)}", "POST", self.__token, params)

        if atom == 0:
            return self
        else:
            raise ExecuteWebhookFailed(result)
