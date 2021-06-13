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


class BanMemberFromGuildFailed(Exception):
    """Raises when banning a member from guild is failed."""

    pass


class UnbanGuildMemberFailed(Exception):
    """Raises when unbanning a user from guild is failed."""

    pass


class FetchGuildBansFailed(Exception):
    """Raises when fetching the guild bans is failed."""

    pass


class FetchGuildBanFailed(Exception):
    """Raises when fetching the member guild ban is failed."""

    pass


class FetchGuildRolesFailed(Exception):
    """Raises when fetching the guild roles is failed."""

    pass


class CreateGuildRoleFailed(Exception):
    """Raises when creating new guild role is failed."""

    pass


class EditGuildRoleFailed(Exception):
    """Raises when editing the guild role is failed."""

    pass


class DeleteGuildRoleFailed(Exception):
    """Raises when deleting the guild role is failed."""

    pass


class ChangeClientUserNicknameFailed(Exception):
    """Raises when changing the client-user guild nickname is failed."""

    pass


class FetchGuildVanityUrlFailed(Exception):
    """Raises when fetching the vanity url is failed."""

    pass


class FetchAuditLogFailed(Exception):
    """Raises when fetching the guild audit log is failed."""

    pass
