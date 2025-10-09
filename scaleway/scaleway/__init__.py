"""Scaleway SDK for Python"""

import importlib.metadata

__version__: str = importlib.metadata.version(__name__)

from scaleway_core.api import (
    API,
    ScalewayException,
)

from scaleway_core.client import Client

from scaleway_core.profile import (
    Profile,
    ProfileConfig,
    ProfileDefaults,
)

from scaleway_core.utils.waiter import (
    WaitForOptions,
    WaitForStopCondition,
)

from . import _bridge

__all__ = [
    "API",
    "ScalewayException",
    "Client",
    "Profile",
    "ProfileConfig",
    "ProfileDefaults",
    "WaitForOptions",
    "WaitForStopCondition",
]
