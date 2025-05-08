# models/media_type.py

from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class MediaType:

    id: int                           # 'id'
    short_name: str                   # 'nomcourt'
    name: str                         # 'nom'
    category: str                     # 'categorie'
    platform_types: Optional[str]     # 'plateformtypes' (pipe-separated string of type IDs)
    platforms: Optional[str]          # 'plateforms' (typically empty)
    media_type: str                   # 'type' (e.g. 'image', 'video', 'zip', 'vectoriel')
    file_format: str                  # 'fileformat' (e.g. 'png', 'mp4', etc.)
    file_format2: str                 # 'fileformat2'
    autogen: bool                     # 'autogen' (0 or 1)
    multi_regions: bool               # 'multiregions' (0 or 1)
    multi_supports: bool              # 'multisupports' (0 or 1)
    multi_versions: bool              # 'multiversions' (0 or 1)
    extra_info_text: Optional[str]    # 'extrainfostxt'

    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'MediaType':

        """
        Factory method to create a MediaType instance from a dict.
        """

        known_keys = {
            "id", "nomcourt", "nom", "categorie", "plateformtypes", "plateforms",
            "type", "fileformat", "fileformat2", "autogen", "multiregions",
            "multisupports", "multiversions", "extrainfostxt"
        }

        return cls(
            id=int(data["id"]),
            short_name=data["nomcourt"],
            name=data["nom"],
            category=data["categorie"],
            platform_types=data.get("plateformtypes") or None,
            platforms=data.get("plateforms") or None,
            media_type=data["type"],
            file_format=data["fileformat"],
            file_format2=data["fileformat2"],
            autogen=bool(int(data["autogen"])),
            multi_regions=bool(int(data["multiregions"])),
            multi_supports=bool(int(data["multisupports"])),
            multi_versions=bool(int(data["multiversions"])),
            extra_info_text=data.get("extrainfostxt") or None,
            extra_fields={k: v for k, v in data.items() if k not in known_keys}
        )
