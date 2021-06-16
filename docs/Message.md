# What is Message?

`<Message>` is a message object that contains informations about message. [Click Here](https://discord.com/developers/docs/resources/channel#message-object) for more information.

# Functions

## reply

Reply to the message.

- Returns `<Message>` object.

```py
await message.reply(params: dict = None)
# params -> https://discord.com/developers/docs/resources/channel#create-message-jsonform-params
```

## edit

Edit your message.

- Returns `<Message>` object.

```py
await message.edit(params: dict = None)
# params -> https://discord.com/developers/docs/resources/channel#edit-message-jsonform-params
```

## delete

Delete a message.

- Returns self.

```py
await message.delete()
```

## add_reaction

Add reaction to message.

- Returns self.

```py
await message.add_reaction(emoji: str)
# emoji -> discord custom emoji or normal emoji. (Check Emoji.md)
```

## remove_reaction

Remove reaction from message.

- Returns self.

```py
await message.remove_reaction(emoji: str, user_id: str = None)
# emoji -> discord custom emoji or normal emoji. (Check Emoji.md)
# user_id -> Used id for reaction remove. if None, bot's reaction will removed.
```

## fetch_reactions

Fetch all users for message reaction.

- Returns list of `<User>` object.

```py
await message.fetch_reactions(emoji: str, params: dict = None)
# emoji -> discord custom emoji or normal emoji. (Check Emoji.md)
# params -> https://discord.com/developers/docs/resources/channel#get-reactions-query-string-params
```

## remove_reactions

Remove all reactions for a emoji.

- Returns `True`

```py
await message.remove_reactions(emoji: str)
# emoji -> discord custom emoji or normal emoji. (Check Emoji.md)
```

## crosspost

[Cross-post](https://discord.com/developers/docs/resources/channel#crosspost-message) the message.

- Returns `<Message>` object.

```py
await message.crosspost()
```
