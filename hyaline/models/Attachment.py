from dataclasses import dataclass


@dataclass
class Attachment:
    # Attrs
    def __init__(self, json) -> None:
        self.id: str = json['id']

        self.width: int = json['width']
        self.height: int = json['height']
        self.size: int = json['size']

        self.url: str = json['url']
        self.proxy_url: str = json['proxy_url']
        self.filename: str = json['filename']
        self.content_type: str = json['content_type']
