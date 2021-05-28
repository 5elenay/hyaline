from dataclasses import dataclass
from datetime import datetime


@dataclass
class Embed:
    # Attrs
    def __init__(self, data: dict = {}) -> None:
        self.color = None
        self.title = None
        self.description = None
        self.url = None
        self.__author = None
        self.__image = None
        self.__thumbnail = None
        self.__timestamp = None
        self.__fields = None
        self.__footer = None

        if data:
            if 'color' in data:
                self.color = data['color']

            if 'title' in data:
                self.title = data['title']

            if 'description' in data:
                self.description = data['description']

            if 'url' in data:
                self.url = data['url']

            if 'author' in data:
                self.__author = data['author']

            if 'image' in data:
                self.__image = data['image']

            if 'thumbnail' in data:
                self.__thumbnail = data['thumbnail']

            if 'timestamp' in data:
                self.__timestamp = data['timestamp']

            if 'fields' in data:
                self.__fields = data['fields']

            if 'footer' in data:
                self.__footer = data['footer']

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

        if self.__author:
            self.embed['author'] = self.__author

        if self.__thumbnail:
            self.embed['thumbnail'] = self.__thumbnail

        if self.__image:
            self.embed['image'] = self.__image

        if self.__timestamp:
            self.embed['timestamp'] = self.__timestamp

        if self.__footer:
            self.embed['footer'] = self.__footer

        if self.__footer:
            self.embed['footer'] = self.__footer

        if self.__fields:
            self.embed['fields'] = self.__fields

        return self.embed

    def set_author(self, **kwargs):
        """Set author to the embed."""

        self.__author = {}

        if 'text' in kwargs:
            self.__author['text'] = kwargs['name']

        if 'icon_url' in kwargs:
            self.__author['icon_url'] = kwargs['icon_url']

        if 'url' in kwargs:
            self.__author['url'] = kwargs['url']

    def set_footer(self, **kwargs):
        """Set footer to the embed."""

        self.__footer = {}

        if 'text' in kwargs:
            self.__footer['text'] = kwargs['text']

        if 'icon_url' in kwargs:
            self.__footer['icon_url'] = kwargs['icon_url']

    def set_image(self, url: str):
        """Set image to the embed."""

        self.__image = {"url": url}

    def set_thumbnail(self, url: str):
        """Set thumbnail to the embed."""

        self.__thumbnail = {"url": url}

    def set_timestamp(self):
        """Add current timestamp to the embed."""

        self.__timestamp = datetime.utcnow().isoformat()

    def add_field(self, name: str, value: str, inline: bool = True):
        """Add new field to the embed."""

        if not self.__fields:
            self.__fields = []

        self.__fields.append({
            "name": name,
            "value": value,
            "inline": inline
        })
