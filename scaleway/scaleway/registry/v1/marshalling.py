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

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("namespace_id", None)
    if field is not None:
        args["namespace_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("visibility", None)
    if field is not None:
        args["visibility"] = field

    field = data.get("size", None)
    if field is not None:
        args["size"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("status_message", None)
    if field is not None:
        args["status_message"] = field
    else:
        args["status_message"] = None

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

    return Image(**args)


def unmarshal_Namespace(data: Any) -> Namespace:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Namespace' failed as data isn't a dictionary."
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

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("status_message", None)
    if field is not None:
        args["status_message"] = field

    field = data.get("endpoint", None)
    if field is not None:
        args["endpoint"] = field

    field = data.get("is_public", None)
    if field is not None:
        args["is_public"] = field

    field = data.get("size", None)
    if field is not None:
        args["size"] = field

    field = data.get("image_count", None)
    if field is not None:
        args["image_count"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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

    return Namespace(**args)


def unmarshal_Tag(data: Any) -> Tag:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Tag' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("image_id", None)
    if field is not None:
        args["image_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("digest", None)
    if field is not None:
        args["digest"] = field

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

    return Tag(**args)


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


def unmarshal_ListNamespacesResponse(data: Any) -> ListNamespacesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListNamespacesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("namespaces", None)
    if field is not None:
        args["namespaces"] = (
            [unmarshal_Namespace(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListNamespacesResponse(**args)


def unmarshal_ListTagsResponse(data: Any) -> ListTagsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTagsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = [unmarshal_Tag(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListTagsResponse(**args)


def marshal_CreateNamespaceRequest(
    request: CreateNamespaceRequest,
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

    if request.description is not None:
        output["description"] = request.description

    if request.is_public is not None:
        output["is_public"] = request.is_public

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_UpdateImageRequest(
    request: UpdateImageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.visibility is not None:
        output["visibility"] = str(request.visibility)

    return output


def marshal_UpdateNamespaceRequest(
    request: UpdateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.is_public is not None:
        output["is_public"] = request.is_public

    return output
