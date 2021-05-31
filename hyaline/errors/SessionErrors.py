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
