# What is ClientUser?
`<ClientUser>`  is the current session user object with some extra metadata. Also `<ClientUser>` has some functions for help us.

# Functions
## get_guild_channel
Get a channel. (from cache.)
- Returns `<Channel>` object.
```py
session.client.get_guild_channel(channel_id: str)
# channel_id -> The channel id
```
## fetch_channel
Fetch a channel.
- Returns `<Channel>` object.
```py
await session.client.fetch_channel(channel_id: str)
# channel_id -> The channel id
```
## bulk_delete
Bulk delete a channel.
- Returns the list of the filtered message ids.
```py
await session.client.bulk_delete(channel_id: str, limit: int = 10)
# channel_id -> The channel id will bulk-deleted
# limit -> Message limit for bulk-delete
```
## say
Send message to a channel with API params
- Returns the `<Message>` object that sent
```py
await session.client.say(channel_id: str, params: dict = None)
# channel_id -> The channel id.
# params -> https://discord.com/developers/docs/resources/channel#create-message-jsonform-params
```
## fetch_invite
Fetch invite details with code. (Supports API params.)
- Returns `<Invite>` object
```py
await session.client.fetch_invite(code: str, params: dict = None)
# code -> Invite code.
# params -> https://discord.com/developers/docs/resources/invite#get-invite-query-string-params
```
## remove_invite
Remove invite with code.
- Returns `<Invite>` object
```py
await session.client.remove_invite(code: str)
# code -> Invite code.
```
## fetch_client_user
Fetch information about client user.
- Returns `<User>` object
```py
await session.client.fetch_client_user()
```
## fetch_user
Fetch information about an user.
- Returns `<User>` object
```py
await session.client.fetch_user(user_id: str)
# user_id -> User id
```
## get_message
Get message from cache.
- Returns `<Message>` object
```py
session.client.get_message(message_id: str)
# message_id -> Message id
```
## get_guild
Get guild from cache.
- Returns `<Guild>` object
```py
session.client.get_guild(guild_id: str)
# guild_id -> Guild id
```
## fetch_guild
Fetch guild with API params.
- Returns `<Guild>` object
```py
await session.client.fetch_guild(guild_id: str, params: dict = None)
# guild_id -> Guild id
# params -> https://discord.com/developers/docs/resources/guild#get-guild-query-string-params
```
## edit_user
Edit client user with API params.
- Returns updated `<User>` object
```py
await session.client.edit_user(params: dict = None)
# params -> https://discord.com/developers/docs/resources/user#modify-current-user-json-params
```
## create_guild
Create a new guild. (only works if your bot's server count is less than 10.)
- Returns `Guild` object.
```py
await session.client.create_guild(params: dict)
# params -> https://discord.com/developers/docs/resources/guild#create-guild-json-params
```
## leave_guild
Leave a guild with id.
- Returns `True`
```py
await session.client.leave_guild(guild_id: str)
# guild_id -> Guild id.
```
## fetch_guild_preview
Fetch guild preview with id.
- Returns `<GuildPreview>` object
```py
await session.client.fetch_guild_preview(guild_id: str)
# guild_id -> Guild id.
```