from dataclasses import dataclass


@dataclass
class Attachment:
    # Attrs
    def __init__(self, json) -> None:

        for key in json:
            setattr(self, key, json[key])
