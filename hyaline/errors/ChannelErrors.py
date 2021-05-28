class GetChannelError(Exception):
    """Raises when fetch channel is failed."""

    pass

class SendMessageToChannelFailed(Exception):
    """Raises when send message to channel is failed."""

    pass

class EditChannelFailed(Exception):
    """Raises when editing the channel is failed."""

    pass

class DeleteChannelFailed(Exception):
    """Raises when deleting the channel is failed."""

    pass

class FetchChannelHistoryFailed(Exception):
    """Raises when fetching the channel history is failed."""

    pass

class FetchChannelMessageFailed(Exception):
    """Raises when fetching the channel message is failed."""

    pass