# models/region.py
from typing import Dict, Any
from dataclasses import dataclass, field

@dataclass
class Region:
    
    id: int                        # 'id'
    code: str                      # 'nomcourt'
    name_en: str                   # 'nom_en'
    name_fr: str                   # 'nom_fr'
    name_de: str                   # 'nom_de'
    name_es: str                   # 'nom_es'
    name_it: str = ''              # 'nom_it' (optional in some cases)
    name_pt: str = ''              # 'nom_pt' (optional in some cases)
    parent_id: int                 # 'parent'
    
    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'Region':

        """
        Factory method to create a Region instance from a dict.
        """

        known_keys = {
            "id", "nomcourt", "nom_en", "nom_fr", "nom_de", "nom_es", "nom_it", "nom_pt", "parent"
        }

        return cls(
            id=int(data["id"]),
            code=data["nomcourt"],
            name_en=data["nom_en"],
            name_fr=data["nom_fr"],
            name_de=data["nom_de"],
            name_es=data["nom_es"],
            name_it=data.get("nom_it", ''),
            name_pt=data.get("nom_pt", ''),
            parent_id=int(data["parent"]),
            extra_fields={k: v for k, v in data.items() if k not in known_keys}
        )
