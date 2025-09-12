# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    AttachmentResourceType,
    FileSystemStatus,
    FileSystem,
    Attachment,
    ListAttachmentsResponse,
    ListFileSystemsResponse,
    CreateFileSystemRequest,
    UpdateFileSystemRequest,
)


def unmarshal_FileSystem(data: Any) -> FileSystem:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'FileSystem' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = FileSystemStatus.UNKNOWN_STATUS

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("number_of_attachments", None)
    if field is not None:
        args["number_of_attachments"] = field
    else:
        args["number_of_attachments"] = 0

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    return FileSystem(**args)


def unmarshal_Attachment(data: Any) -> Attachment:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Attachment' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("filesystem_id", None)
    if field is not None:
        args["filesystem_id"] = field
    else:
        args["filesystem_id"] = None

    field = data.get("resource_id", None)
    if field is not None:
        args["resource_id"] = field
    else:
        args["resource_id"] = None

    field = data.get("resource_type", None)
    if field is not None:
        args["resource_type"] = field
    else:
        args["resource_type"] = AttachmentResourceType.UNKNOWN_RESOURCE_TYPE

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    return Attachment(**args)


def unmarshal_ListAttachmentsResponse(data: Any) -> ListAttachmentsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAttachmentsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("attachments", None)
    if field is not None:
        args["attachments"] = (
            [unmarshal_Attachment(v) for v in field] if field is not None else None
        )
    else:
        args["attachments"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListAttachmentsResponse(**args)


def unmarshal_ListFileSystemsResponse(data: Any) -> ListFileSystemsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFileSystemsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("filesystems", None)
    if field is not None:
        args["filesystems"] = (
            [unmarshal_FileSystem(v) for v in field] if field is not None else None
        )
    else:
        args["filesystems"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListFileSystemsResponse(**args)


def marshal_CreateFileSystemRequest(
    request: CreateFileSystemRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.size is not None:
        output["size"] = request.size

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateFileSystemRequest(
    request: UpdateFileSystemRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.size is not None:
        output["size"] = request.size

    if request.tags is not None:
        output["tags"] = request.tags

    return output
