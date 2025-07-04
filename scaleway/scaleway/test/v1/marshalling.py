# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    Human,
    ListHumansResponse,
    RegisterResponse,
    CreateHumanRequest,
    RegisterRequest,
    UpdateHumanRequest,
)


def unmarshal_Human(data: Any) -> Human:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Human' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("height", None)
    if field is not None:
        args["height"] = field

    field = data.get("shoe_size", None)
    if field is not None:
        args["shoe_size"] = field

    field = data.get("altitude_in_meter", None)
    if field is not None:
        args["altitude_in_meter"] = field

    field = data.get("altitude_in_millimeter", None)
    if field is not None:
        args["altitude_in_millimeter"] = field

    field = data.get("fingers_count", None)
    if field is not None:
        args["fingers_count"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("hair_count", None)
    if field is not None:
        args["hair_count"] = field

    field = data.get("is_happy", None)
    if field is not None:
        args["is_happy"] = field

    field = data.get("eyes_color", None)
    if field is not None:
        args["eyes_color"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    return Human(**args)


def unmarshal_ListHumansResponse(data: Any) -> ListHumansResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHumansResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("humans", None)
    if field is not None:
        args["humans"] = (
            [unmarshal_Human(v) for v in field] if field is not None else None
        )

    return ListHumansResponse(**args)


def unmarshal_RegisterResponse(data: Any) -> RegisterResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RegisterResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secret_key", None)
    if field is not None:
        args["secret_key"] = field

    field = data.get("access_key", None)
    if field is not None:
        args["access_key"] = field

    return RegisterResponse(**args)


def marshal_CreateHumanRequest(
    request: CreateHumanRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
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
    )

    if request.height is not None:
        output["height"] = request.height

    if request.shoe_size is not None:
        output["shoe_size"] = request.shoe_size

    if request.altitude_in_meter is not None:
        output["altitude_in_meter"] = request.altitude_in_meter

    if request.altitude_in_millimeter is not None:
        output["altitude_in_millimeter"] = request.altitude_in_millimeter

    if request.fingers_count is not None:
        output["fingers_count"] = request.fingers_count

    if request.hair_count is not None:
        output["hair_count"] = request.hair_count

    if request.is_happy is not None:
        output["is_happy"] = request.is_happy

    if request.name is not None:
        output["name"] = request.name

    if request.eyes_color is not None:
        output["eyes_color"] = str(request.eyes_color)

    return output


def marshal_RegisterRequest(
    request: RegisterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    return output


def marshal_UpdateHumanRequest(
    request: UpdateHumanRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.height is not None:
        output["height"] = request.height

    if request.shoe_size is not None:
        output["shoe_size"] = request.shoe_size

    if request.altitude_in_meter is not None:
        output["altitude_in_meter"] = request.altitude_in_meter

    if request.altitude_in_millimeter is not None:
        output["altitude_in_millimeter"] = request.altitude_in_millimeter

    if request.fingers_count is not None:
        output["fingers_count"] = request.fingers_count

    if request.hair_count is not None:
        output["hair_count"] = request.hair_count

    if request.is_happy is not None:
        output["is_happy"] = request.is_happy

    if request.eyes_color is not None:
        output["eyes_color"] = str(request.eyes_color)

    if request.name is not None:
        output["name"] = request.name

    return output
