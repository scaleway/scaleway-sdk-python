# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    EyeColors,
    HumanStatus,
    ListHumansRequestOrderBy,
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

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("height", str())
    args["height"] = field

    field = data.get("shoe_size", str())
    args["shoe_size"] = field

    field = data.get("altitude_in_meter", str())
    args["altitude_in_meter"] = field

    field = data.get("altitude_in_millimeter", str())
    args["altitude_in_millimeter"] = field

    field = data.get("fingers_count", str())
    args["fingers_count"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("hair_count", str())
    args["hair_count"] = field

    field = data.get("is_happy", str())
    args["is_happy"] = field

    field = data.get("eyes_color", str())
    args["eyes_color"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    return Human(**args)

def unmarshal_ListHumansResponse(data: Any) -> ListHumansResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHumansResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("humans", str())
    args["humans"] = [unmarshal_Human(v) for v in field] if field is not None else None

    return ListHumansResponse(**args)

def unmarshal_RegisterResponse(data: Any) -> RegisterResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RegisterResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secret_key", str())
    args["secret_key"] = field

    field = data.get("access_key", str())
    args["access_key"] = field

    return RegisterResponse(**args)

def marshal_CreateHumanRequest(
    request: CreateHumanRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project_id", value=request.project_id, default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization_id", value=request.organization_id,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.height is not None:
        output["height"] = request.height
    else:
        output["height"] = str()

    if request.shoe_size is not None:
        output["shoe_size"] = request.shoe_size
    else:
        output["shoe_size"] = str()

    if request.altitude_in_meter is not None:
        output["altitude_in_meter"] = request.altitude_in_meter
    else:
        output["altitude_in_meter"] = str()

    if request.altitude_in_millimeter is not None:
        output["altitude_in_millimeter"] = request.altitude_in_millimeter
    else:
        output["altitude_in_millimeter"] = str()

    if request.fingers_count is not None:
        output["fingers_count"] = request.fingers_count
    else:
        output["fingers_count"] = str()

    if request.hair_count is not None:
        output["hair_count"] = request.hair_count
    else:
        output["hair_count"] = str()

    if request.is_happy is not None:
        output["is_happy"] = request.is_happy
    else:
        output["is_happy"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.eyes_color is not None:
        output["eyes_color"] = str(request.eyes_color)
    else:
        output["eyes_color"] = None


    return output

def marshal_RegisterRequest(
    request: RegisterRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()


    return output

def marshal_UpdateHumanRequest(
    request: UpdateHumanRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.height is not None:
        output["height"] = request.height
    else:
        output["height"] = None

    if request.shoe_size is not None:
        output["shoe_size"] = request.shoe_size
    else:
        output["shoe_size"] = None

    if request.altitude_in_meter is not None:
        output["altitude_in_meter"] = request.altitude_in_meter
    else:
        output["altitude_in_meter"] = None

    if request.altitude_in_millimeter is not None:
        output["altitude_in_millimeter"] = request.altitude_in_millimeter
    else:
        output["altitude_in_millimeter"] = None

    if request.fingers_count is not None:
        output["fingers_count"] = request.fingers_count
    else:
        output["fingers_count"] = None

    if request.hair_count is not None:
        output["hair_count"] = request.hair_count
    else:
        output["hair_count"] = None

    if request.is_happy is not None:
        output["is_happy"] = request.is_happy
    else:
        output["is_happy"] = None

    if request.eyes_color is not None:
        output["eyes_color"] = str(request.eyes_color)
    else:
        output["eyes_color"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output
