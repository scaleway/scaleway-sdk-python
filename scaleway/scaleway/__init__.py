"""Scaleway SDK for Python"""

import importlib.metadata

__version__ = importlib.metadata.version(__name__)

# import internal dependencies
from ._dependancies import *

# optional: explicitly define __all__ for public API
# __all__ = _dependancies.__all__
