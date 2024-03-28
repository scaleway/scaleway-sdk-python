# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass

from scaleway_core.bridge import (
    Region,
)


@dataclass
class _GetRegionResponse:
    region: Region
    """
    Region to target. If none is passed will use default region from the config.
    """
