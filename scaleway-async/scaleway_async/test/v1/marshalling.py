# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
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

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("height", None)
    if field is not None:
        args["height"] = field
    else:
        args["height"] = None

    field = data.get("shoe_size", None)
    if field is not None:
        args["shoe_size"] = field
    else:
        args["shoe_size"] = None

    field = data.get("altitude_in_meter", None)
    if field is not None:
        args["altitude_in_meter"] = field
    else:
        args["altitude_in_meter"] = None

    field = data.get("altitude_in_millimeter", None)
    if field is not None:
        args["altitude_in_millimeter"] = field
    else:
        args["altitude_in_millimeter"] = None

    field = data.get("fingers_count", None)
    if field is not None:
        args["fingers_count"] = field
    else:
        args["fingers_count"] = None

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
    else:
        args["hair_count"] = None

    field = data.get("is_happy", None)
    if field is not None:
        args["is_happy"] = field
    else:
        args["is_happy"] = None

    field = data.get("eyes_color", None)
    if field is not None:
        args["eyes_color"] = field
    else:
        args["eyes_color"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    return Human(**args)


def unmarshal_ListHumansResponse(data: Any) -> ListHumansResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHumansResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("humans", None)
    if field is not None:
        args["humans"] = (
            [unmarshal_Human(v) for v in field] if field is not None else None
        )
    else:
        args["humans"] = None

    return ListHumansResponse(**args)


def unmarshal_RegisterResponse(data: Any) -> RegisterResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RegisterResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("secret_key", None)
    if field is not None:
        args["secret_key"] = field
    else:
        args["secret_key"] = None

    field = data.get("access_key", None)
    if field is not None:
        args["access_key"] = field
    else:
        args["access_key"] = None

    return RegisterResponse(**args)


def marshal_CreateHumanRequest(
    request: CreateHumanRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project_id",
                    value=request.project_id,
                    default=defaults.default_project_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="organization_id",
                    value=request.organization_id,
                    default=defaults.default_organization_id,
                    marshal_func=None,
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
        output["eyes_color"] = request.eyes_color

    return output


def marshal_RegisterRequest(
    request: RegisterRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    return output


def marshal_UpdateHumanRequest(
    request: UpdateHumanRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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
        output["eyes_color"] = request.eyes_color

    if request.name is not None:
        output["name"] = request.name

    return output
