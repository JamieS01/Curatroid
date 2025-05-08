# models/rom_type.py
from typing import Dict, Any
from dataclasses import dataclass, field

@dataclass
class RomType:
    
    name: str                          # ROM type name
    
    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_value(cls, value: str) -> 'RomType':

        """
        Factory method to create a RomType instance from a string value.
        """

        return cls(name=value)
