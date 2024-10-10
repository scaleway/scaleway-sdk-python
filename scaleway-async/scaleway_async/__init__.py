"""Scaleway SDK for Python - Async"""

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

from scaleway_core.bridge import (
    Money,
    Region,
    ALL_REGIONS,
    Zone,
    ALL_ZONES,
    ScwFile,
    ServiceInfo,
    TimeSeriesPoint,
    TimeSeries,
)

__all__ = [
    "API",
    "ScalewayException",
    "Client",
    "Profile",
    "ProfileConfig",
    "ProfileDefaults",
    "WaitForOptions",
    "WaitForStopCondition",
    "Money",
    "Region",
    "ALL_REGIONS",
    "Zone",
    "ALL_ZONES",
    "ScwFile",
    "ServiceInfo",
    "TimeSeriesPoint",
    "TimeSeries",
]
