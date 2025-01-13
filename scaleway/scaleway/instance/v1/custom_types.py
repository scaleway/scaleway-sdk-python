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
