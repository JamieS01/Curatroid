# models/user_level.py
from typing import Dict, Any
from dataclasses import dataclass, field

@dataclass
class UserLevel:

    id: int                             # 'id'
    name: str                           # 'nom_fr'

    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'UserLevel':

        """
        Factory method to create a UserLevel instance from a dict.
        """

        known_keys = {"id", "nom_fr"}
        return cls(
            id=int(data["id"]),
            name=data["nom_fr"],
            extra_fields={k: v for k, v in data.items() if k not in known_keys}
        )
