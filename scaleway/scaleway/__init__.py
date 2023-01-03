"""Scaleway SDK for Python"""

import pkg_resources

__version__: str = pkg_resources.get_distribution(__name__).version

from scaleway_core.api import API as API  # noqa

from scaleway_core.client import Client as Client  # noqa

from scaleway_core.profile import Profile as Profile  # noqa
from scaleway_core.profile import ProfileConfig as ProfileConfig  # noqa
from scaleway_core.profile import ProfileDefaults as ProfileDefaults  # noqa
