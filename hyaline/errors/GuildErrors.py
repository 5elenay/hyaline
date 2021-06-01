class EditGuildFailed(Exception):
    """Raises when editing the guild is failed."""

    pass


class FetchGuildChannelsFailed(Exception):
    """Raises when fetching the guild channels is failed."""

    pass


class CreateGuildChannelFailed(Exception):
    """Raises when creating new guild channel is failed."""

    pass


class ChangeChannelPositionFailed(Exception):
    """Raises when changing a channel position is failed."""

    pass


class FetchGuildMemberFailed(Exception):
    """Raises when fetching a guild member is failed."""

    pass


class FetchGuildMembersFailed(Exception):
    """Raises when fetching guild member list is failed."""

    pass


class SearchGuildMemberFailed(Exception):
    """Raises when searching the guild members is failed."""

    pass


class EditGuildMemberFailed(Exception):
    """Raises when editing the guild member is failed."""

    pass
