from dataclasses import dataclass
from typing import Optional

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
class GetServerUserDataResponse:
    server_id: str

    key: str
    """
    Key of the user data
    """

    content: str


@dataclass
class SetServerUserDataRequest:
    zone: Optional[Zone]
    """
    Zone of the user data to set
    """

    server_id: str

    key: str
    """
    Key defines the user data key to set
    """

    content: bytes
    """
    Content defines the data to set as bytes
    """
