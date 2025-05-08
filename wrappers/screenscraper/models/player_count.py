# models/player_count.py
from typing import Dict, Any
from dataclasses import dataclass, field

@dataclass
class PlayerCount:
    
    id: int               # 'id'
    label: str            # 'nom'
    parent_id: int        # 'parent'

    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'PlayerCount':

        """
        Factory method to create a PlayerCount instance from a dict.
        """

        known_keys = {"id", "nom", "parent"}
        return cls(
            id=int(data["id"]),
            label=data["nom"],
            parent_id=int(data["parent"]),
            extra_fields={k: v for k, v in data.items() if k not in known_keys}
        )