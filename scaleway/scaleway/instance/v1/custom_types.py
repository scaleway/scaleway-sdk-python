from dataclasses import dataclass
from typing import Optional, Dict

from scaleway_core.bridge import Zone


@dataclass
class GetServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone of the user data to get
    """

    server_id: str

    key: str
    """
    Key defines the user data key to get
    """

@dataclass
class ListServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone of the user data to get
    """

    server_id: str

@dataclass
class GetAllServerUserDataResponse:
    user_data: Dict[str, bytes]
