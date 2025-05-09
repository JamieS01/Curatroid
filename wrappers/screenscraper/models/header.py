# models/header.py
from typing import Dict, Any
from dataclasses import dataclass, field

@dataclass
class Header:

    api_version: str        # 'APIversion'
    date_time: str          # 'dateTime'
    request: str            # 'commandRequested'
    success: str            # 'success'
    error: str              # 'error'

    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'Header':

        """
        Factory method to create a Header instance from a dict.
        """

        known_keys = {
            "APIversion", "dateTime", "commandRequested", "success", "error"
        }

        return cls(
            api_version=data["APIversion"],
            date_time=data["dateTime"],
            request=data["commandRequested"],
            success=data["success"],
            error=data["error"],
            extra_fields={k: v for k, v in data.items() if k not in known_keys}
        )