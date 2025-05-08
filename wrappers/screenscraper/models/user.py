# models/user.py
from typing import Dict, Any
from dataclasses import dataclass, field

@dataclass
class User:

    username: str                        # 'id' in API
    user_id: int                         # 'numid'
    level: int                           # 'niveau'
    contribution_points: int             # 'contribution'
    system_uploads: int                  # 'uploadsysteme'
    info_uploads: int                    # 'uploadinfos'
    rom_associations: int                # 'romasso'
    media_uploads: int                   # 'uploadmedia'
    accepted_proposals: int              # 'propositionok'
    rejected_proposals: int              # 'propositionko'
    quota_refused: int                   # 'quotarefu'
    max_threads: int                     # 'maxthreads'
    max_download_speed_kbps: int         # 'maxdownloadspeed'
    requests_today: int                  # 'requeststoday'
    requests_ko_today: int               # 'requestskotoday'
    max_requests_per_minute: int         # 'maxrequestspermin'
    max_requests_per_day: int            # 'maxrequestsperday'
    max_failed_requests_per_day: int     # 'maxrequestskoperday'
    total_visits: int                    # 'visites'
    last_visit: str                      # 'datedernierevisite'
    preferred_region: str                # 'favregion'

    extra_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'User':

        """
        Factory method to create a User instance from a dict.
        """

        known_keys = {
            "id", "numid", "niveau", "contribution", "uploadsysteme", "uploadinfos",
            "romasso", "uploadmedia", "propositionok", "propositionko", "quotarefu",
            "maxthreads", "maxdownloadspeed", "requeststoday", "maxrequestspermin",
            "maxrequestsperday", "maxrequestskoperday", "visites", "datedernierevisite",
            "favregion"
        }

        return cls(
            username=data["id"],
            user_id=int(data["numid"]),
            level=int(data["niveau"]),
            contribution_points=int(data["contribution"]),
            system_uploads=int(data["uploadsysteme"]),
            info_uploads=int(data["uploadinfos"]),
            rom_associations=int(data["romasso"]),
            media_uploads=int(data["uploadmedia"]),
            accepted_proposals=int(data["propositionok"]),
            rejected_proposals=int(data["propositionko"]),
            quota_refused=int(data["quotarefu"]),
            max_threads=int(data["maxthreads"]),
            max_download_speed_kbps=int(data["maxdownloadspeed"]),
            requests_today=int(data["requeststoday"]),
            requests_ko_today=int(data["requestskotoday"]),
            max_requests_per_minute=int(data["maxrequestspermin"]),
            max_requests_per_day=int(data["maxrequestsperday"]),
            max_failed_requests_per_day=int(data["maxrequestskoperday"]),
            total_visits=int(data["visites"]),
            last_visit=data["datedernierevisite"],
            preferred_region=data["favregion"],
            extra_fields={
                k: v for k, v in data.items() if k not in known_keys
            }
        )
