# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from .types import (
    LocalImage,
    Organization,
    Version,
    Image,
    GetImageResponse,
    GetVersionResponse,
    ListImagesResponse,
    ListVersionsResponse,
)


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

    return LocalImage(**args)


def unmarshal_Organization(data: Any) -> Organization:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Organization' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    return Organization(**args)


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

    field = data.get("local_images", None)
    if field is not None:
        args["local_images"] = (
            [unmarshal_LocalImage(v) for v in field] if field is not None else None
        )

    field = data.get("creation_date", None)
    if field is not None:
        args["creation_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )

    field = data.get("modification_date", None)
    if field is not None:
        args["modification_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )

    return Version(**args)


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

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_Version(v) for v in field] if field is not None else None
        )

    field = data.get("current_public_version", None)
    if field is not None:
        args["current_public_version"] = field

    field = data.get("creation_date", None)
    if field is not None:
        args["creation_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )

    field = data.get("modification_date", None)
    if field is not None:
        args["modification_date"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )

    field = data.get("valid_until", None)
    if field is not None:
        args["valid_until"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = unmarshal_Organization(field)

    return Image(**args)


def unmarshal_GetImageResponse(data: Any) -> GetImageResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetImageResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("image", None)
    if field is not None:
        args["image"] = unmarshal_Image(field)

    return GetImageResponse(**args)


def unmarshal_GetVersionResponse(data: Any) -> GetVersionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("version", None)
    if field is not None:
        args["version"] = unmarshal_Version(field)

    return GetVersionResponse(**args)


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
