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
    ListImagesRequestOrderBy,
    ListLocalImagesRequestOrderBy,
    ListVersionsRequestOrderBy,
    LocalImageType,
    Category,
    Image,
    LocalImage,
    Version,
    ListCategoriesResponse,
    ListImagesResponse,
    ListLocalImagesResponse,
    ListVersionsResponse,
)

def unmarshal_Category(data: Any) -> Category:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Category' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    return Category(**args)

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

    field = data.get("description", str())
    args["description"] = field

    field = data.get("logo", str())
    args["logo"] = field

    field = data.get("categories", [])
    args["categories"] = field

    field = data.get("label", str())
    args["label"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("valid_until", None)
    args["valid_until"] = parser.isoparse(field) if isinstance(field, str) else field

    return Image(**args)

def unmarshal_LocalImage(data: Any) -> LocalImage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LocalImage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("compatible_commercial_types", [])
    args["compatible_commercial_types"] = field

    field = data.get("arch", str())
    args["arch"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("label", str())
    args["label"] = field

    field = data.get("type", getattr(LocalImageType, "UNKNOWN_TYPE"))
    args["type_"] = field

    return LocalImage(**args)

def unmarshal_Version(data: Any) -> Version:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("published_at", None)
    args["published_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Version(**args)

def unmarshal_ListCategoriesResponse(data: Any) -> ListCategoriesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCategoriesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("categories", str())
    args["categories"] = [unmarshal_Category(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListCategoriesResponse(**args)

def unmarshal_ListImagesResponse(data: Any) -> ListImagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("images", str())
    args["images"] = [unmarshal_Image(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListImagesResponse(**args)

def unmarshal_ListLocalImagesResponse(data: Any) -> ListLocalImagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLocalImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("local_images", str())
    args["local_images"] = [unmarshal_LocalImage(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListLocalImagesResponse(**args)

def unmarshal_ListVersionsResponse(data: Any) -> ListVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("versions", str())
    args["versions"] = [unmarshal_Version(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListVersionsResponse(**args)
