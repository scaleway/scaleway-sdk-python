from dataclasses import dataclass
from typing import Optional, Dict

from scaleway_core.bridge import Zone as ScwZone


@dataclass
class GetServerUserDataRequest:
    server_id: str

    """
    Key defines the user data key to get
    """
    key: str

    """
    Zone of the user data to get
    """
    zone: Optional[ScwZone]


@dataclass
class GetAllServerUserDataRequest:
    server_id: str

    """
    Zone of the user data to get
    """
    zone: Optional[ScwZone]


@dataclass
class GetAllServerUserDataResponse:
    user_data: Dict[str, bytes]


@dataclass
class SetAllServerUserDataRequest:
    server_id: str

    user_data: Dict[str, bytes]

    """
    Zone of the user data to set
    """
    zone: Optional[ScwZone]
