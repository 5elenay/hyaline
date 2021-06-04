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


class FetchGuildEmojiListFailed(Exception):
    """Raises when fetching the emoji list is failed."""

    pass


class FetchGuildEmojiFailed(Exception):
    """Raises when fetching the guild emoji is failed."""

    pass


class CreateGuildEmojiFailed(Exception):
    """Raises when creating a guild emoji is failed."""

    pass


class EditGuildEmojiFailed(Exception):
    """Raises when editing a guild emoji is failed."""

    pass


class DeleteGuildEmojiFailed(Exception):
    """Raises when delete a guild emoji is failed."""

    pass


class AddRoleToGuildMemberFailed(Exception):
    """Raises when adding a role to guild member is failed."""

    pass


class RemoveRoleFromGuildMemberFailed(Exception):
    """Raises when removing a role from guild member is failed."""

    pass

class KickMemberFromGuildFailed(Exception):
    """Raises when kicking a member from guild is failed."""

    pass
