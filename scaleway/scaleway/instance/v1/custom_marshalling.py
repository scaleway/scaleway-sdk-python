from typing import Dict, Any

from scaleway.instance.v1.custom_types import GetServerUserDataRequest, GetServerUserDataResponse, \
    SetServerUserDataRequest
from scaleway_core.profile import ProfileDefaults


def marshal_GetServerUserDataRequest(request: GetServerUserDataRequest, defaults: ProfileDefaults) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_id is not None:
        output["server_id"] = request.server_id
    if request.key is not None:
        output["key"] = request.key
    if request.zone is not None:
        output["zone"] = request.zone

    return output


def unmarshal_GetServerUserDataResponse(data: Any) -> GetServerUserDataResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetServerUserDataResponse' failed as data isn't a dictionary."
        )
    args: Dict[str, Any] = {}

    field = data.get("server_id", None)
    if field is not None:
        args["server_id"] = field

    field = data.get("key", None)
    if field is not None:
        args["key"] = field

    field = data.get("content", None)
    if field is not None:
        args["content"] = field

    return GetServerUserDataResponse(**args)


def marshal_SetServerUserDataRequest(request: SetServerUserDataRequest, defaults: ProfileDefaults) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_id is not None:
        output["server_id"] = request.server_id
    if request.key is not None:
        output["key"] = request.key
    if request.zone is not None:
        output["zone"] = request.zone
    if request.content is not None:
        output["content"] = request.content.getvalue()

    return output
