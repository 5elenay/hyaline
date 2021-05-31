from dataclasses import dataclass
from typing import Union


@dataclass
class Application:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        from .User import User
        from .Team import Team

        self.id: str = json['id']
        self.name: str = json['name']
        self.icon: Union[str,
                         None] = None if 'icon' in json and json['icon'] is None else json['icon']
        self.description: str = json['description']
        self.rpc_origins: Union[str,
                                None] = json['rpc_origins'] if 'rpc_origins' in json else None
        self.bot_public: Union[bool,
                               None] = json['bot_public'] if 'bot_public' in json else None
        self.bot_require_code_grant: Union[bool,
                                           None] = json['bot_require_code_grant'] if 'bot_require_code_grant' in json else None
        self.terms_of_service_url: Union[str,
                                         None] = json['terms_of_service_url'] if 'terms_of_service_url' in json else None
        self.privacy_policy_url: Union[str,
                                       None] = json['privacy_policy_url'] if 'privacy_policy_url' in json else None
        self.owner: User = User(json['owner'], self.__token)
        self.summary: str = json['summary']
        self.verify_key: str = json['verify_key']
        self.team: Union[Team, None] = json['team']
        self.guild_id: Union[str,
                             None] = json['guild_id'] if 'guild_id' in json else None
        self.primary_sku_id: Union[str,
                                   None] = json['primary_sku_id'] if 'primary_sku_id' in json else None
        self.slug: Union[str, None] = json['slug'] if 'slug' in json else None
        self.cover_image: Union[str,
                                None] = json['cover_image'] if 'cover_image' in json else None
        self.flags: int = json['flags']
