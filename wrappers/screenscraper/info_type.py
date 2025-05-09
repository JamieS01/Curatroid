# models/info_type.py

from dataclasses import dataclass, field
from typing import Optional, Dict, Any

@dataclass
class InfoType:

    id: int                             # 'id'
    code: str                           # 'nomcourt'
    name: str                           # 'nom'
    category: str                       # 'categorie'
    platform_types: Optional[str]       # 'plateformtypes'
    platforms: Optional[str]            # 'plateforms'
    info_type: str                      # 'type'
    file_format: Optional[str]          # 'fileformat'
    file_format2: Optional[str]         # 'fileformat2'
    autogen: bool                       # 'autogen'
    multi_regions: bool                 # 'multiregions'
    multi_supports: Optional[bool]      # 'multisupports'
    multi_versions: Optional[bool]      # 'multiversions'
    multi_choice: bool                  # 'multichoix'

    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'InfoType':

        """
        Factory method to create an InfoType instance from a dict.
        """

        known_keys = {
            "id", "nomcourt", "nom", "categorie", "plateformtypes", "plateforms",
            "type", "fileformat", "fileformat2", "autogen", "multiregions",
            "multisupports", "multiversions", "multichoix"
        }

        return cls(
            id=int(data["id"]),
            code=data["nomcourt"],
            name=data["nom"],
            category=data["categorie"],
            platform_types=data.get("plateformtypes") or None,
            platforms=data.get("plateforms") or None,
            info_type=data["type"],
            file_format=data.get("fileformat") or None,
            file_format2=data.get("fileformat2") or None,
            autogen=bool(int(data["autogen"])),
            multi_regions=bool(int(data["multiregions"])),
            multi_supports=bool(int(data.get("multisupports", "0") or "0")),
            multi_versions=bool(int(data.get("multiversions", "0") or "0")),
            multi_choice=bool(int(data["multichoix"])),
            extra_fields={k: v for k, v in data.items() if k not in known_keys}
        )
