# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from dateutil import parser
from .types import (
    ImageVisibility,
    Image,
    ListImagesResponse,
    ListNamespacesResponse,
    ListTagsResponse,
    Namespace,
    Tag,
    CreateNamespaceRequest,
    UpdateNamespaceRequest,
    UpdateImageRequest,
)


def unmarshal_Image(data: Any) -> Image:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Image' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("namespace_id")
    args["namespace_id"] = field

    field = data.get("size")
    args["size"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("status_message")
    args["status_message"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("visibility")
    args["visibility"] = field

    return Image(**args)


def unmarshal_Namespace(data: Any) -> Namespace:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Namespace' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description")
    args["description"] = field

    field = data.get("endpoint")
    args["endpoint"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("image_count")
    args["image_count"] = field

    field = data.get("is_public")
    args["is_public"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("region")
    args["region"] = field

    field = data.get("size")
    args["size"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("status_message")
    args["status_message"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Namespace(**args)


def unmarshal_Tag(data: Any) -> Tag:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Tag' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("digest")
    args["digest"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("image_id")
    args["image_id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Tag(**args)


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


def unmarshal_ListNamespacesResponse(data: Any) -> ListNamespacesResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListNamespacesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("namespaces")
    args["namespaces"] = [unmarshal_Namespace(v) for v in data["namespaces"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListNamespacesResponse(**args)


def unmarshal_ListTagsResponse(data: Any) -> ListTagsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTagsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tags")
    args["tags"] = [unmarshal_Tag(v) for v in data["tags"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListTagsResponse(**args)


def marshal_CreateNamespaceRequest(
    request: CreateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        **resolve_one_of(
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
        "description": request.description,
        "is_public": request.is_public,
        "name": request.name,
    }


def marshal_UpdateImageRequest(
    request: UpdateImageRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "visibility": ImageVisibility(request.visibility),
    }


def marshal_UpdateNamespaceRequest(
    request: UpdateNamespaceRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "is_public": request.is_public,
    }
