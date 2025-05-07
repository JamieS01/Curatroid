from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class Result:

    status_code: int
    message: str = ''
    data: List[Dict] = field(default_factory=list) # List of Dicts initalised as empty immutable List