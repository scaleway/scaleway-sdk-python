from typing import Dict, Any

from scaleway.instance.v1.custom_types import (
    GetServerUserDataRequest,
    GetAllServerUserDataRequest,
)
from scaleway_core.profile import ProfileDefaults


def marshal_GetServerUserDataRequest(
    request: GetServerUserDataRequest, defaults: ProfileDefaults
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_id is not None:
        output["server_id"] = request.server_id
    if request.key is not None:
        output["key"] = request.key
    if request.zone is not None:
        output["zone"] = request.zone

    return output


def marshal_ListServerUserDataRequest(
    request: GetAllServerUserDataRequest, defaults: ProfileDefaults
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_id is not None:
        output["server_id"] = request.server_id
    if request.zone is not None:
        output["zone"] = request.zone

    return output
