# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from .types import (
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

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    return Category(**args)


def unmarshal_Image(data: Any) -> Image:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Image' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

    field = data.get("logo", None)
    if field is not None:
        args["logo"] = field

    field = data.get("categories", None)
    if field is not None:
        args["categories"] = field

    field = data.get("label", None)
    if field is not None:
        args["label"] = field

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

    field = data.get("valid_until", None)
    if field is not None:
        args["valid_until"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["valid_until"] = None

    return Image(**args)


def unmarshal_LocalImage(data: Any) -> LocalImage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LocalImage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("compatible_commercial_types", None)
    if field is not None:
        args["compatible_commercial_types"] = field

    field = data.get("arch", None)
    if field is not None:
        args["arch"] = field

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field

    field = data.get("label", None)
    if field is not None:
        args["label"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    return LocalImage(**args)


def unmarshal_Version(data: Any) -> Version:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

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

    field = data.get("published_at", None)
    if field is not None:
        args["published_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["published_at"] = None

    return Version(**args)


def unmarshal_ListCategoriesResponse(data: Any) -> ListCategoriesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCategoriesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("categories", None)
    if field is not None:
        args["categories"] = (
            [unmarshal_Category(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListCategoriesResponse(**args)


def unmarshal_ListImagesResponse(data: Any) -> ListImagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("images", None)
    if field is not None:
        args["images"] = (
            [unmarshal_Image(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListImagesResponse(**args)


def unmarshal_ListLocalImagesResponse(data: Any) -> ListLocalImagesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLocalImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("local_images", None)
    if field is not None:
        args["local_images"] = (
            [unmarshal_LocalImage(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListLocalImagesResponse(**args)


def unmarshal_ListVersionsResponse(data: Any) -> ListVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_Version(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListVersionsResponse(**args)
