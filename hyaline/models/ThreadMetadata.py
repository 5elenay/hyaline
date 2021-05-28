from dataclasses import dataclass
from datetime import datetime
from typing import Union
from dateutil.parser import parse


@dataclass
class ThreadMetadata:
    # Attrs
    def __init__(self, json) -> None:
        self.archived: bool = json['archived']
        self.archiver_id: Union[str,
                                None] = json['archiver_id'] if 'archiver_id' in json else None
        self.auto_archive_duration: int = json['auto_archive_duration']
        self.archive_timestamp: datetime = parse(json['archive_timestamp'])
        self.locked: Union[bool,
                           None] = json['locked'] if 'locked' in json else None
