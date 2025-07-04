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
    ImageStatus,
    ImageVisibility,
    ListImagesRequestOrderBy,
    ListNamespacesRequestOrderBy,
    ListTagsRequestOrderBy,
    NamespaceStatus,
    TagStatus,
    Image,
    Namespace,
    Tag,
    ListImagesResponse,
    ListNamespacesResponse,
    ListTagsResponse,
    CreateNamespaceRequest,
    UpdateImageRequest,
    UpdateNamespaceRequest,
)

def unmarshal_Image(data: Any) -> Image:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Image' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("namespace_id", str())
    args["namespace_id"] = field

    field = data.get("status", getattr(ImageStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("visibility", getattr(ImageVisibility, "VISIBILITY_UNKNOWN"))
    args["visibility"] = field

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("status_message", None)
    args["status_message"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Image(**args)

def unmarshal_Namespace(data: Any) -> Namespace:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Namespace' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("status", getattr(NamespaceStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("status_message", str())
    args["status_message"] = field

    field = data.get("endpoint", str())
    args["endpoint"] = field

    field = data.get("is_public", False)
    args["is_public"] = field

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("image_count", 0)
    args["image_count"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Namespace(**args)

def unmarshal_Tag(data: Any) -> Tag:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Tag' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("image_id", str())
    args["image_id"] = field

    field = data.get("status", getattr(TagStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("digest", str())
    args["digest"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Tag(**args)

def unmarshal_ListImagesResponse(data: Any) -> ListImagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("images", [])
    args["images"] = [unmarshal_Image(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListImagesResponse(**args)

def unmarshal_ListNamespacesResponse(data: Any) -> ListNamespacesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNamespacesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("namespaces", [])
    args["namespaces"] = [unmarshal_Namespace(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListNamespacesResponse(**args)

def unmarshal_ListTagsResponse(data: Any) -> ListTagsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTagsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tags", [])
    args["tags"] = [unmarshal_Tag(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListTagsResponse(**args)

def marshal_CreateNamespaceRequest(
    request: CreateNamespaceRequest,
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

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.is_public is not None:
        output["is_public"] = request.is_public
    else:
        output["is_public"] = False

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_UpdateImageRequest(
    request: UpdateImageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.visibility is not None:
        output["visibility"] = str(request.visibility)
    else:
        output["visibility"] = None


    return output

def marshal_UpdateNamespaceRequest(
    request: UpdateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.is_public is not None:
        output["is_public"] = request.is_public
    else:
        output["is_public"] = None


    return output
