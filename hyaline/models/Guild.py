from dataclasses import dataclass
from datetime import datetime
from dateutil.parser import parse
from typing import Union


@dataclass
class Guild:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token = token

        from .Role import Role
        from .Emoji import Emoji
        from .VoiceState import VoiceState
        from .Member import Member
        from .Channel import Channel

        self.id: str = json['id']
        self.name: str = json['name']
        self.icon: Union[str, None] = json['icon']
        self.icon_hash: Union[str,
                              None] = json['icon_hash'] if 'icon_hash' in json else None
        self.splash: Union[str, None] = json['splash']
        self.discovery_splash: Union[str,
                                     None] = json['discovery_splash'] if 'discovery_splash' in json else None
        self.owner: Union[bool,
                          None] = json['owner'] if 'owner' in json else None
        self.owner_id: Union[str,
                             None] = json['owner_id'] if 'owner_id' in json else None
        self.permissions: Union[str,
                                None] = json['permissions'] if 'permissions' in json else None
        self.region: Union[str,
                           None] = json['region'] if 'region' in json else None
        self.afk_channel_id: Union[str,
                                   None] = json['afk_channel_id'] if 'afk_channel_id' in json else None
        self.afk_timeout: int = json['afk_timeout']
        self.widget_enabled: Union[bool,
                                   None] = json['widget_enabled'] if 'widget_enabled' in json else None
        self.widget_channel_id: Union[str,
                                      None] = json['widget_channel_id'] if 'widget_channel_id' in json else None
        self.verification_level: int = json['verification_level']
        self.default_message_notifications: int = json['default_message_notifications']
        self.explicit_content_filter: int = json['explicit_content_filter']
        self.roles: list = [Role(i) for i in json['roles']]
        self.emojis: list = [Emoji(i) for i in json['emojis']]
        self.features: list = json['features']
        self.mfa_level: int = json['mfa_level']
        self.application_id: Union[str, None] = json['application_id']
        self.system_channel_id: Union[str, None] = json['system_channel_id']
        self.system_channel_flags: int = json['system_channel_flags']
        self.rules_channel_id: Union[str, None] = json['rules_channel_id']
        self.joined_at: Union[datetime, None] = parse(
            json['joined_at']) if 'joined_at' in json and json['joined_at'] else None
        self.large: Union[bool,
                          None] = json['large'] if 'large' in json else None
        self.unavailable: Union[bool,
                                None] = json['unavailable'] if 'unavailable' in json else None
        self.member_count: Union[int,
                                 None] = json['member_count'] if 'member_count' in json else None
        self.voice_states: Union[VoiceState, None] = [VoiceState(
            i) for i in json['voice_states']] if 'voice_states' in json else None
        self.members: Union[Member, None] = [
            Member(i) for i in json['members']] if 'members' in json else None
        self.channels: Union[Channel, None] = [Channel(
            i, self.__token) for i in json['channels']] if 'channels' in json else None
        self.threads: Union[Channel, None] = [Channel(
            i, self.__token) for i in json['threads']] if 'threads' in json else None
        self.presences: Union[list,
                              None] = json['presences'] if 'presences' in json else None
        self.max_presences: Union[int,
                                  None] = json['max_presences'] if 'max_presences' in json else None
        self.max_members: Union[int,
                                None] = json['max_members'] if 'max_members' in json else None
        self.vanity_url_code: Union[str,
                                    None] = json['vanity_url_code'] if 'vanity_url_code' in json else None
        self.description: Union[str,
                                None] = json['description'] if 'description' in json else None
        self.banner: Union[str,
                           None] = json['banner'] if 'banner' in json else None
        self.premium_tier: int = json['premium_tier']
        self.premium_subscription_count: Union[int,
                                               None] = json['premium_subscription_count'] if 'premium_subscription_count' in json else None
        self.preferred_locale: str = json['preferred_locale']
        self.public_updates_channel_id: Union[str,
                                              None] = json['public_updates_channel_id'] if 'public_updates_channel_id' in json else None
        self.max_video_channel_users: Union[int,
                                            None] = json['max_video_channel_users'] if 'max_video_channel_users' in json else None
        self.approximate_member_count: Union[int,
                                             None] = json['approximate_member_count'] if 'approximate_member_count' in json else None
        self.welcome_screen: Union[dict,
                                   None] = json['welcome_screen'] if 'welcome_screen' in json else None
        self.nsfw_level: int = json['nsfw_level']
        self.stage_instances: Union[dict,
                                    None] = json['stage_instances'] if 'stage_instances' in json else None
