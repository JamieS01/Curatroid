# models/server.py
from typing import Dict, Any
from dataclasses import dataclass, field

@dataclass
class Server:

    cpu_1_load: int                     # 'cpu1'
    cpu_2_load: int                     # 'cpu2'
    cpu_3_load: int                     # 'cpu3'
    cpu_4_load: int                     # 'cpu4'
    threads_per_minute: int             # 'threadsmin'
    active_scrapers: int                # 'nbscrapeurs'
    total_api_calls_today: int          # 'apiacces'
    closed_to_non_members: bool         # 'closefornomember'
    closed_to_leechers: bool            # 'closeforleecher'
    max_threads_non_member: int         # 'maxthreadfornonmember'
    current_threads_non_member: int     # 'threadfornonmember'
    max_threads_member: int             # 'maxthreadformember'
    current_threads_member: int         # 'threadformember'

    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'Server':

        """
        Factory method to create a Server instance from a dict.
        """

        known_keys = {
            "cpu1", "cpu2", "cpu3", "cpu4", "threadsmin", "nbscrapeurs", "apiacces",
            "closefornomember", "closeforleecher", "maxthreadfornonmember",
            "threadfornonmember", "maxthreadformember", "threadformember"
        }

        return cls(
            cpu_1_load=int(data["cpu1"]),
            cpu_2_load=int(data["cpu2"]),
            cpu_3_load=int(data["cpu3"]),
            cpu_4_load=int(data["cpu4"]),
            threads_per_minute=int(data["threadsmin"]),
            active_scrapers=int(data["nbscrapeurs"]),
            total_api_calls_today=int(data["apiacces"]),
            closed_to_non_members=bool(int(data["closefornomember"])),
            closed_to_leechers=bool(int(data["closeforleecher"])),
            max_threads_non_member=int(data["maxthreadfornonmember"]),
            current_threads_non_member=int(data["threadfornonmember"]),
            max_threads_member=int(data["maxthreadformember"]),
            current_threads_member=int(data["threadformember"]),
            extra_fields={
                k: v for k, v in data.items() if k not in known_keys
            }
        )