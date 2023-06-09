# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from dateutil import parser
from .types import (
    Category,
    Image,
    ListCategoriesResponse,
    ListImagesResponse,
    ListLocalImagesResponse,
    ListVersionsResponse,
    LocalImage,
    Version,
)


def unmarshal_Category(data: Any) -> Category:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Category' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", None)
    args["description"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    return Category(**args)


def unmarshal_Image(data: Any) -> Image:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Image' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("categories", None)
    args["categories"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("label", None)
    args["label"] = field

    field = data.get("logo", None)
    args["logo"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("valid_until", None)
    args["valid_until"] = parser.isoparse(field) if type(field) is str else field

    return Image(**args)


def unmarshal_LocalImage(data: Any) -> LocalImage:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'LocalImage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("arch", None)
    args["arch"] = field

    field = data.get("compatible_commercial_types", None)
    args["compatible_commercial_types"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("label", None)
    args["label"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return LocalImage(**args)


def unmarshal_Version(data: Any) -> Version:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("published_at", None)
    args["published_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Version(**args)


def unmarshal_ListCategoriesResponse(data: Any) -> ListCategoriesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListCategoriesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("categories", None)
    args["categories"] = (
        [unmarshal_Category(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListCategoriesResponse(**args)


def unmarshal_ListImagesResponse(data: Any) -> ListImagesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("images", None)
    args["images"] = [unmarshal_Image(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListImagesResponse(**args)


def unmarshal_ListLocalImagesResponse(data: Any) -> ListLocalImagesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListLocalImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("local_images", None)
    args["local_images"] = (
        [unmarshal_LocalImage(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListLocalImagesResponse(**args)


def unmarshal_ListVersionsResponse(data: Any) -> ListVersionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("versions", None)
    args["versions"] = (
        [unmarshal_Version(v) for v in field] if field is not None else None
    )

    return ListVersionsResponse(**args)
