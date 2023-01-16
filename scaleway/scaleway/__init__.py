"""Scaleway SDK for Python"""

import pkg_resources

__version__: str = pkg_resources.get_distribution(__name__).version

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
    Zone,
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
    "Zone",
    "ScwFile",
    "ServiceInfo",
    "TimeSeriesPoint",
    "TimeSeries",
]
