class TokenNotFoundError(Exception):
    """Raises when token not found in session object."""

    pass


class IntentNotFoundError(Exception):
    """Raises when token not found in session object."""

    pass


class InvalidTokenError(Exception):
    """Raises when token is invalid in session object."""

    pass


class FetchInviteFailedError(Exception):
    """Raises when fetcing the invite is failed."""

    pass


class RemoveInviteFailedError(Exception):
    """Raises when removing the invite is failed."""

    pass


class FetchUserFailedError(Exception):
    """Raises when fetching the user is failed."""

    pass


class FetchGuildFailedError(Exception):
    """Raises when fetching the guild is failed."""

    pass


class EditClientUserFailed(Exception):
    """Raises when editing the current user is failed."""

    pass


class LeaveGuildFailed(Exception):
    """Raises when leaving the guild is failed."""

    pass


class FetchGuildPreviewFailed(Exception):
    """Raises when fetching the guild preview is failed."""

    pass
