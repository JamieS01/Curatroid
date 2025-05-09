# models/media.py
from typing import Optional
from dataclasses import dataclass
from media_type import MediaType

@dataclass
class Media:

    url: str
    media_type: Optional[MediaType] = None
    path: Optional[str] = None

    @classmethod
    def from_url(cls, url: str, media_type: Optional[MediaType] = None) -> 'Media':

        """
        Factory method to create a Media instance from a url.
        """

        return cls(
            url=url,
            media_type=media_type
        )