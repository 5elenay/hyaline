# Hyaline Discord API Wrapper.

[![Version](https://badge.fury.io/py/hyaline.svg)](https://pypi.python.org/pypi/hyaline)
[![Downloads](https://img.shields.io/pypi/dm/hyaline.svg)](https://pypi.python.org/pypi/hyaline)
![Stars](https://img.shields.io/github/stars/5elenay/hyaline)
![Commits](https://img.shields.io/github/commit-activity/w/5elenay/hyaline)

**WARNING**: Hyaline is not easy to use library.

Hyaline is a discord api wrapper for python. hyaline is created for discord developers and hyaline makes everything harder. _Hyaline is in alpha-release and still not finished._

Check `./docs` folder for documentation and more informations about hyaline. Documentation is not finished. You can use python `dir()` function for get all functions, attrs in the object. Also use `help()` for get help about a function / class.

## Installation

Just type `pip install hyaline` and you are ready to go!

- **Current Version** - 0.1.2

## Change Log:

- Added `bot` attribute for `User`.
- Added `fetch_user_profile` function.

## Example Ping-Pong Discord Bot

```py
# Import the library and intent helper.
import hyaline
from hyaline.helpers.Intents import ALL

# Setup session configurations.
# NOTE: If you want to limit message cache add MAX_MESSAGES
session = hyaline.Session({
    "TOKEN": "token",
    "INTENTS": ALL
})


async def on_ready(_packet):
    print(f"Bot Started with name: {session.client.username}.")


async def on_message(msg):
    if not msg.author.bot and msg.content.lower() == "ping":
        await msg.reply({
            "content": ":ping_pong: Pong!"
        })

# Configure the events.
# Also you can configure multiple event.
session.event("MESSAGE_CREATE", on_message)
session.event("READY", on_ready)

# Start the session.
session.start()
```
