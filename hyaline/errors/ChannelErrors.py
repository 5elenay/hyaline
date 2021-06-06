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


class FetchChannelInvitesFailed(Exception):
    """Raises when fetching the channel invites is failed."""

    pass


class CreateInviteFailed(Exception):
    """Raises when creating new invite is failed."""

    pass


class FetchPinnedMessagesFailed(Exception):
    """Raises when fetching the pinned messages is failed."""

    pass


class PinMessageFailed(Exception):
    """Raises when pinning a message is failed."""

    pass


class UnpinMessageFailed(Exception):
    """Raises when unpinning a message is failed."""

    pass


class EditChannelPermissionsFailed(Exception):
    """Raises when editing the channel permissions is failed."""

    pass


class DeleteChannelPermissionsFailed(Exception):
    """Raises when deleting the channel permissions is failed."""

    pass


class TriggerTypingFailed(Exception):
    """Raises when trigger the typing is failed."""

    pass
