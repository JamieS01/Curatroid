# models/classification.py
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from models.media import Media

@dataclass
class Classification:
    
    id: int                                 # 'id'
    code: str                               # 'nomcourt'
    parent_id: Optional[int] = None         # 'parent'
    media: List[Media] = field(default_factory=list)

    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> "Classification":

        """
        Factory method to create a Classification instance from a dict.
        Extracts media URLs from the 'medias' sub-dictionary and
        creates a list of Media objects.
        """

        known_keys = {"id", "nomcourt", "parent", "medias"}

        media_entries = data.get("medias", {})
        media_list = [Media.from_url(url) for url in media_entries.values()]

        return cls(
            id=int(data["id"]),
            code=data["nomcourt"],
            parent_id=int(data["parent"]) if data.get("parent") else None,
            media=media_list,
            extra_fields={k: v for k, v in data.items() if k not in known_keys}
        )
