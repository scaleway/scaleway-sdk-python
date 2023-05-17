# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from scaleway_core.bridge import (
    Region,
)


@dataclass
class _GetClusterKubeConfigRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cluster_id: str
    """
    Cluster ID for which to download the kubeconfig.
    """
