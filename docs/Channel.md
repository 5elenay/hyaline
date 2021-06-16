# What is Channel?

`<Channel>` is a channel object that contains text, voice, state channel and more!
[Click Here](https://discord.com/developers/docs/resources/channel) for channel object.

# Functions

## send

Send message to channel.

- Returns `<Message>` object.

```py
await channel.send(params: dict = None)
# params -> https://discord.com/developers/docs/resources/channel#create-message-jsonform-params
```

## edit

Edit current channel.

- Returns `<Channel>` object.

```py
await channel.edit(params: dict = None)
# params -> https://discord.com/developers/docs/resources/channel#modify-channel-json-params-guild-channel
```

## delete

Delete current channel.

- Returns `<Channel>` object.

```py
await channel.delete()
```

## fetch_history

Fetch channel message history.

- Returns list of `<Message>` objects.

```py
await channel.fetch_history(options: dict = None)
# options -> https://discord.com/developers/docs/resources/channel#get-channel-messages
```

## fetch_message

Fetch a message from channel.

- Returns `<Message>` object.

```py
await channel.fetch_message(message_id: str)
# message_id -> Message id.
```

## fetch_invites

Fetch channel invites.

- Returns list of `<Invite>` objects.

```py
await channel.fetch_invites()
```

## create_invite

Create channel invite.

- Returns `<Invite>` object.

```py
await channel.create_invite(params: dict = None)
# params -> https://discord.com/developers/docs/resources/channel#create-channel-invite-json-params
```

## pinned_messages

Fetch all pinned messages.

- Returns list of `<Message>` objects.

```py
await channel.pinned_messages()
```

## delete_message

Delete channel message.

- Returns self.

```py
await channel.delete_message(message_id: str)
# message_id -> Message id.
```

## pin_message

Pin a message.

- Returns `True`.

```py
await channel.pin_message(message_id: str)
# message_id -> Message id.
```

## unpin_message

Unpin a message.

- Returns `True`.

```py
await channel.unpin_message(message_id: str)
# message_id -> Message id.
```

## edit_permissions

Edit channel permissions for user/role.

- Returns `self`.

```py
await channel.edit_permissions(user_or_role_id: str, params: dict = None)
# user_or_role_id -> User or role id for channel.
# params -> https://discord.com/developers/docs/resources/channel#edit-channel-permissions-json-params.

# NOTE: you can use helpers/Permissions for bitwise values.
```

## delete_permissions

Delete channel permissions for user/role.

- Returns `self`.

```py
await channel.delete_permissions(user_or_role_id: str)
# user_or_role_id -> User or role id for channel.
```

## trigger_typing

Trigger typing event.

- Returns `self`.

```py
await channel.delete_permissions()
```

## create_webhook

Create a webhook.

- Returns `<Webhook>` object.

```py
await channel.create_webhook(params: dict)
# params -> https://discord.com/developers/docs/resources/webhook#create-webhook-json-params
```

## fetch_webhooks

Fetch all webhooks in the channel.

- Returns list of `<Webhook>` objects.

```py
await channel.fetch_webhooks()
```
