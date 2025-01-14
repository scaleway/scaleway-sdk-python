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
class GetAllServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone of the user data to get
    """

    server_id: str

@dataclass
class GetAllServerUserDataResponse:
    user_data: Dict[str, bytes]

@dataclass
class SetAllServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone of the user data to set
    """

    server_id: str

    user_data: Dict[str, bytes]
