from dataclasses import dataclass
from typing import Union


@dataclass
class Role:
    # Attrs
    def __init__(self, json) -> None:
        from .RoleTags import RoleTags

        for key in json:
            if key == "tags":
                setattr(self, key, RoleTags(json[key]))
            else:
                setattr(self, key, json[key])
