# models/support_type.py
from typing import Dict, Any
from dataclasses import dataclass, field

@dataclass
class SupportType:
    
    name: str                          # support type name
    
    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_value(cls, value: str) -> 'SupportType':

        """
        Factory method to create a SupportType instance from a string value.
        """

        return cls(name=value)
