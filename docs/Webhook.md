# Webhooks

"Webhooks are a low-effort way to post messages to channels in Discord. They do not require a bot user or authentication to use."

Webhook functions for hyaline, learn more information from [here](https://discord.com/developers/docs/resources/webhook)

# Functions

## edit

Modify the webhook with API params.

- Returns `<Webhook>` object.

```py
await webhook.edit(params: dict)
# params -> https://discord.com/developers/docs/resources/webhook#modify-webhook-json-params
```

## delete

Delete the webhook.

- Returns `self`.

```py
await webhook.delete()
```

## execute

Execute the webhook.

- Returns `self`.

```py
await webhook.execute(params: dict, **kwargs)
# params -> https://discord.com/developers/docs/resources/webhook#execute-webhook-jsonform-params
# keyword args -> https://discord.com/developers/docs/resources/webhook#execute-webhook-query-string-params
```
