# models/genre.py
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from models.media import Media

@dataclass
class Genre:
    
    id: int                                # 'id'
    name_en: str                           # 'nom_en'
    name_fr: Optional[str] = None          # 'nom_fr'
    name_de: Optional[str] = None          # 'nom_de'
    name_es: Optional[str] = None          # 'nom_es'
    name_it: Optional[str] = None          # 'nom_it'
    name_pt: Optional[str] = None          # 'nom_pt'
    parent_id: Optional[int] = None        # 'parent'
    media: List[Media] = field(default_factory=list)

    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> "Genre":
        """
        Factory method to create a Genre instance from a dict.
        Extracts media URLs from the 'medias' sub-dictionary and
        creates a list of Media objects.
        """
        known_keys = {
            "id", "nom_en", "nom_fr", "nom_de", "nom_es", "nom_it",
            "nom_pt", "parent", "medias"
        }

        media_entries = data.get("medias", {})
        media_list = [Media.from_url(url) for url in media_entries.values()]

        return cls(
            id=int(data["id"]),
            name_en=data["nom_en"],
            name_fr=data.get("nom_fr"),
            name_de=data.get("nom_de"),
            name_es=data.get("nom_es"),
            name_it=data.get("nom_it"),
            name_pt=data.get("nom_pt"),
            parent_id=int(data["parent"]) if data.get("parent") else None,
            media=media_list,
            extra_fields={k: v for k, v in data.items() if k not in known_keys}
        )
