from dataclasses import dataclass
from datetime import datetime


@dataclass
class Embed:
    # Attrs
    def __init__(self, data=None) -> None:
        if data is None:
            data = {}
        self.color = None
        self.title = None
        self.description = None
        self.url = None
        self.author = None
        self.image = None
        self.thumbnail = None
        self.timestamp = None
        self.fields = None
        self.footer = None

        for key in data:
            setattr(self, key, data[key])

    def __call__(self):
        self.embed = {}

        if self.title:
            self.embed['title'] = self.title

        if self.url:
            self.embed['url'] = self.url

        if self.color:
            self.embed['color'] = self.color

        if self.description:
            self.embed['description'] = self.description

        if self.author:
            self.embed['author'] = self.author

        if self.thumbnail:
            self.embed['thumbnail'] = self.thumbnail

        if self.image:
            self.embed['image'] = self.image

        if self.timestamp:
            self.embed['timestamp'] = self.timestamp

        if self.footer:
            self.embed['footer'] = self.footer

        if self.footer:
            self.embed['footer'] = self.footer

        if self.fields:
            self.embed['fields'] = self.fields

        return self.embed

    def set_author(self, **kwargs):
        """Set author to the embed."""

        self.author = {}

        if 'text' in kwargs:
            self.author['text'] = kwargs['name']

        if 'icon_url' in kwargs:
            self.author['icon_url'] = kwargs['icon_url']

        if 'url' in kwargs:
            self.author['url'] = kwargs['url']

    def set_footer(self, **kwargs):
        """Set footer to the embed."""

        self.footer = {}

        if 'text' in kwargs:
            self.footer['text'] = kwargs['text']

        if 'icon_url' in kwargs:
            self.footer['icon_url'] = kwargs['icon_url']

    def set_image(self, url: str):
        """Set image to the embed."""

        self.image = {"url": url}

    def set_thumbnail(self, url: str):
        """Set thumbnail to the embed."""

        self.thumbnail = {"url": url}

    def set_timestamp(self):
        """Add current timestamp to the embed."""

        self.timestamp = datetime.utcnow().isoformat()

    def add_field(self, name: str, value: str, inline: bool = True):
        """Add new field to the embed."""

        if not self.fields:
            self.fields = []

        self.fields.append({
            "name": name,
            "value": value,
            "inline": inline
        })
