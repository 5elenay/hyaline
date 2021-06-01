from dataclasses import dataclass


@dataclass
class Team:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token: str = token

        from .TeamMember import TeamMember

        for key in json:
            if key == "members":
                setattr(self, key, [TeamMember(i, self.__token)
                        for i in json[key]])
            else:
                setattr(self, key, json[key])
