import random
import uuid
from datetime import datetime
from typing import Union

from scaleway_core.profile import ProfileDefaults

system_random = random.SystemRandom()


def random_name() -> str:
    return "test-{}".format(uuid.uuid4().hex)


def random_access_key() -> str:
    return "SCW" + "".join(
        system_random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=16)
    )


def string_to_datetime(date: str) -> datetime:
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")


def random_date(min: Union[str, datetime], max: Union[str, datetime]) -> datetime:
    min_time = min if isinstance(min, datetime) else string_to_datetime(min)
    max_time = max if isinstance(max, datetime) else string_to_datetime(max)

    random_time = min_time + system_random.random() * (max_time - min_time)
    return random_time


def datetime_to_string(date: datetime) -> str:
    return date.strftime("%Y-%m-%dT%H:%M:%SZ")


def random_date_string(min: str, max: str) -> str:
    return datetime_to_string(random_date(min, max))


def random_profile_defaults() -> ProfileDefaults:
    return ProfileDefaults(
        default_organization_id=uuid.uuid4().hex,
        default_project_id=uuid.uuid4().hex,
    )
