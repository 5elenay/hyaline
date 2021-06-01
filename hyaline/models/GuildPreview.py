from dataclasses import dataclass


@dataclass
class GuildPreview:
    # Attrs
    def __init__(self, json, token) -> None:
        self.__token = token

        from .Emoji import Emoji

        for key in json:
            if key == "emojis":
                setattr(self, key, [Emoji(i, self.__token) for i in json[key]])
            else:
                setattr(self, key, json[key])
