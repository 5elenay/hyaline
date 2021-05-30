class EditMessageFailed(Exception):
    """Raises when editing the message is failed."""

    pass


class DeleteMessageFailed(Exception):
    """Raises when deleting the message is failed."""

    pass


class BulkDeleteMessageFailed(Exception):
    """Raises when bulk-delete the messages is failed."""

    pass


class AddReactionToMessageFailed(Exception):
    """Raises when adding a reaction to message is failed."""

    pass


class RemoveReactionToMessageFailed(Exception):
    """Raises when removing a reaction to message is failed."""

    pass


class FetchReactionsFromMessageFailed(Exception):
    """Raises when fetching reactions from message is failed."""

    pass


class RemoveReactionsFromMessageFailed(Exception):
    """Raises when removing reactions from message is failed."""

    pass


class CrossPostMessageFailed(Exception):
    """Raises when cross posting a message is failed."""

    pass
