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

    field = data.get("arch")
    args["arch"] = field

    field = data.get("compatible_commercial_types")
    args["compatible_commercial_types"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("zone")
    args["zone"] = field

    return LocalImage(**args)


def unmarshal_Organization(data: Any) -> Organization:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Organization' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    return Organization(**args)


def unmarshal_Version(data: Any) -> Version:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Version' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("creation_date")
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id")
    args["id"] = field

    field = data.get("local_images")
    args["local_images"] = [unmarshal_LocalImage(v) for v in data["local_images"]]

    field = data.get("modification_date")
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name")
    args["name"] = field

    return Version(**args)


def unmarshal_Image(data: Any) -> Image:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Image' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("categories")
    args["categories"] = field

    field = data.get("creation_date")
    args["creation_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("current_public_version")
    args["current_public_version"] = field

    field = data.get("description")
    args["description"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("label")
    args["label"] = field

    field = data.get("logo")
    args["logo"] = field

    field = data.get("modification_date")
    args["modification_date"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization")
    args["organization"] = unmarshal_Organization(field) if field is not None else None

    field = data.get("valid_until")
    args["valid_until"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("versions")
    args["versions"] = [unmarshal_Version(v) for v in data["versions"]]

    return Image(**args)


def unmarshal_GetImageResponse(data: Any) -> GetImageResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image")
    args["image"] = unmarshal_Image(field) if field is not None else None

    return GetImageResponse(**args)


def unmarshal_GetVersionResponse(data: Any) -> GetVersionResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'GetVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("version")
    args["version"] = unmarshal_Version(field) if field is not None else None

    return GetVersionResponse(**args)


def unmarshal_ListImagesResponse(data: Any) -> ListImagesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListImagesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("images")
    args["images"] = [unmarshal_Image(v) for v in data["images"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListImagesResponse(**args)


def unmarshal_ListVersionsResponse(data: Any) -> ListVersionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count")
    args["total_count"] = field

    field = data.get("versions")
    args["versions"] = [unmarshal_Version(v) for v in data["versions"]]

    return ListVersionsResponse(**args)
