from typing import Dict, Any
from dataclasses import dataclass, field

@dataclass
class Server:

    cpu1: int # CPU usage on server 1
    cpu2: int # CPU usage on server 2
    cpu3: int # CPU usage on server 3
    cpu4: int # CPU usage on server 4
    threadsmin: int # total number of API accesses in the last minute
    nbscrapeurs: int # number of active API users
    apiacces: int # total number of API accesses made today (midnight to current, Fr)
    closefornomember: bool # 1 if API is closed to non members
    closeforleecher: bool # 1 if API is closed to users with no contributions
    maxthreadfornonmember: int # Max concurrent threads for non members
    threadfornonmember: int # Currently open threads for non members
    maxthreadformember: int # Max concurrent threads for members
    threadformember: int # Currently open threads for members

    # Catch-all for any extra fields returned by the API
    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'Server':

        """
        Factory method to create a Server instance from a dict,
        converting strings to appropriate types and capturing unknown fields.
        """

        known_keys = {
            "cpu1", "cpu2", "cpu3", "cpu4", "threadsmin", "nbscrapeurs", "apiacces",
            "closefornomember", "closeforleecher", "maxthreadfornonmember",
            "threadfornonmember", "maxthreadformember", "threadformember"
        }

        return cls(
            cpu1=int(data["cpu1"]),
            cpu2=int(data["cpu2"]),
            cpu3=int(data["cpu3"]),
            cpu4=int(data["cpu4"]),
            threadsmin=int(data["threadsmin"]),
            nbscrapeurs=int(data["nbscrapeurs"]),
            apiacces=int(data["apiacces"]),
            closefornomember=bool(int(data["closefornomember"])),
            closeforleecher=bool(int(data["closeforleecher"])),
            maxthreadfornonmember=int(data["maxthreadfornonmember"]),
            threadfornonmember=int(data["threadfornonmember"]),
            maxthreadformember=int(data["maxthreadformember"]),
            threadformember=int(data["threadformember"]),
            extra_fields={
                k: v for k, v in data.items() if k not in known_keys
            }
        )