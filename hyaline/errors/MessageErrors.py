class EditMessageFailed(Exception):
    """Raises when editing the message is failed."""

    pass

class DeleteMessageFailed(Exception):
    """Raises when deleting the message is failed."""

    pass

class BulkDeleteMessageFailed(Exception):
    """Raises when bulk-delete the messages is failed."""

    pass