# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from dateutil import parser
from .types import (
    GetImageResponse,
    GetVersionResponse,
    Image,
    ListImagesResponse,
    ListVersionsResponse,
    LocalImage,
    Organization,
    Version,
)


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

    field = data.get("zone", None)
    args["zone"] = field

    return LocalImage(**args)


def unmarshal_Organization(data: Any) -> Organization:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Organization' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    return Organization(**args)


def unmarshal_Version(data: Any) -> Version:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("local_images", None)
    args["local_images"] = (
        [unmarshal_LocalImage(v) for v in field] if field is not None else None
    )

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name", None)
    args["name"] = field

    return Version(**args)


def unmarshal_Image(data: Any) -> Image:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Image' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("categories", None)
    args["categories"] = field

    field = data.get("creation_date", None)
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("current_public_version", None)
    args["current_public_version"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("label", None)
    args["label"] = field

    field = data.get("logo", None)
    args["logo"] = field

    field = data.get("modification_date", None)
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("organization", None)
    args["organization"] = unmarshal_Organization(field) if field is not None else None

    field = data.get("valid_until", None)
    args["valid_until"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("versions", None)
    args["versions"] = (
        [unmarshal_Version(v) for v in field] if field is not None else None
    )

    return Image(**args)


def unmarshal_GetImageResponse(data: Any) -> GetImageResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image", None)
    args["image"] = unmarshal_Image(field) if field is not None else None

    return GetImageResponse(**args)


def unmarshal_GetVersionResponse(data: Any) -> GetVersionResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("version", None)
    args["version"] = unmarshal_Version(field) if field is not None else None

    return GetVersionResponse(**args)


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
