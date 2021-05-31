from dataclasses import dataclass
from typing import Union
from datetime import datetime
from dateutil.parser import parse


@dataclass
class Invite:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token = token

        from .Channel import Channel
        from .User import User
        from .Application import Application

        self.code: str = json['code']
        self.guild: Union[dict,
                          None] = json['guild'] if 'guild' in json else None
        self.channel: Channel = Channel(json['channel'], self.__token)
        self.inviter: Union[User, None] = User(
            json['inviter'], self.__token) if 'inviter' in json else None
        self.target_type: Union[int,
                                None] = json['target_type'] if 'target_type' in json else None
        self.target_user: Union[User, None] = User(
            json['target_user'], self.__token) if 'target_user' in json else None
        self.target_application: Union[Application, None] = Application(
            json['target_application'], self.__token) if 'target_application' in json else None
        self.approximate_presence_count: Union[int,
                                               None] = json['approximate_presence_count'] if 'approximate_presence_count' in json else None
        self.approximate_member_count: Union[int,
                                             None] = json['approximate_member_count'] if 'approximate_member_count' in json else None
        self.expires_at: Union[datetime, None] = parse(
            json['expires_at']) if 'expires_at' in json and json['expires_at'] else None

        self.uses: Union[int, None] = json['uses'] if 'uses' in json else None
        self.max_uses: Union[int,
                             None] = json['max_uses'] if 'max_uses' in json else None
        self.max_age: Union[int,
                            None] = json['max_age'] if 'max_age' in json else None
        self.temporary: Union[bool,
                              None] = json['temporary'] if 'temporary' in json else None
        self.created_at: Union[datetime, None] = parse(
            json['created_at']) if 'created_at' in json and json['created_at'] else None
