import re
import uuid
from urllib.parse import urlparse

_is_access_key_regex = re.compile(r"^SCW[A-Z0-9]{17}$", re.IGNORECASE)


def is_access_key(s: str) -> bool:
    return _is_access_key_regex.match(s) is not None


def _is_uuid(s: str) -> bool:
    try:
        uuid.UUID(s)
        return True
    except ValueError:
        return False


def is_secret_key(s: str) -> bool:
    return _is_uuid(s)


def is_organization_id(s: str) -> bool:
    return _is_uuid(s)


def is_project_id(s: str) -> bool:
    return _is_uuid(s)


_is_region_regex = re.compile(r"^[a-z]{2}-[a-z]{3}$", re.IGNORECASE)


def is_region(s: str) -> bool:
    return _is_region_regex.match(s) is not None


_is_zone_regex = re.compile(r"^[a-z]{2}-[a-z]{3}-[1-9]$", re.IGNORECASE)


def is_zone(s: str) -> bool:
    return _is_zone_regex.match(s) is not None


def is_url(s: str) -> bool:
    try:
        result = urlparse(s)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
