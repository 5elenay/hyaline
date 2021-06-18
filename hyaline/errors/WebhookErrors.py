class ModifyWebhookFailed(Exception):
    """Raises when modifying the webhook is failed."""

    pass


class DeleteWebhookFailed(Exception):
    """Raises when deleting the webhook is failed."""

    pass


class ExecuteWebhookFailed(Exception):
    """Raises when executing the webhook is failed."""

    pass
