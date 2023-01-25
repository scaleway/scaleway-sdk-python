# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    EyeColors,
    Human,
    ListHumansResponse,
    RegisterResponse,
    RegisterRequest,
    CreateHumanRequest,
    UpdateHumanRequest,
)


def unmarshal_Human(data: Any) -> Human:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Human' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("altitude_in_meter")
    args["altitude_in_meter"] = field

    field = data.get("altitude_in_millimeter")
    args["altitude_in_millimeter"] = field

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("eyes_color")
    args["eyes_color"] = field

    field = data.get("fingers_count")
    args["fingers_count"] = field

    field = data.get("hair_count")
    args["hair_count"] = field

    field = data.get("height")
    args["height"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("is_happy")
    args["is_happy"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("shoe_size")
    args["shoe_size"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Human(**args)


def unmarshal_ListHumansResponse(data: Any) -> ListHumansResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListHumansResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("humans")
    args["humans"] = [unmarshal_Human(v) for v in data["humans"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListHumansResponse(**args)


def unmarshal_RegisterResponse(data: Any) -> RegisterResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'RegisterResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key")
    args["access_key"] = field

    field = data.get("secret_key")
    args["secret_key"] = field

    return RegisterResponse(**args)


def marshal_CreateHumanRequest(
    request: CreateHumanRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
            [
                OneOfPossibility(
                    "project_id", request.project_id, defaults.default_project_id
                ),
                OneOfPossibility(
                    "organization_id",
                    request.organization_id,
                    defaults.default_organization_id,
                ),
            ]
        ),
        "altitude_in_meter": request.altitude_in_meter,
        "altitude_in_millimeter": request.altitude_in_millimeter,
        "eyes_color": EyeColors(request.eyes_color),
        "fingers_count": request.fingers_count,
        "hair_count": request.hair_count,
        "height": request.height,
        "is_happy": request.is_happy,
        "name": request.name,
        "shoe_size": request.shoe_size,
    }


def marshal_RegisterRequest(
    request: RegisterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "username": request.username,
    }


def marshal_UpdateHumanRequest(
    request: UpdateHumanRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "altitude_in_meter": request.altitude_in_meter,
        "altitude_in_millimeter": request.altitude_in_millimeter,
        "eyes_color": EyeColors(request.eyes_color),
        "fingers_count": request.fingers_count,
        "hair_count": request.hair_count,
        "height": request.height,
        "is_happy": request.is_happy,
        "name": request.name,
        "shoe_size": request.shoe_size,
    }
