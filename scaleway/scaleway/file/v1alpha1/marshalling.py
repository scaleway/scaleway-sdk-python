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
    AttachmentResourceType,
    FileSystemStatus,
    ListFileSystemsRequestOrderBy,
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

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("status", getattr(FileSystemStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("number_of_attachments", 0)
    args["number_of_attachments"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return FileSystem(**args)

def unmarshal_Attachment(data: Any) -> Attachment:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Attachment' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("filesystem_id", str())
    args["filesystem_id"] = field

    field = data.get("resource_id", str())
    args["resource_id"] = field

    field = data.get("resource_type", getattr(AttachmentResourceType, "UNKNOWN_RESOURCE_TYPE"))
    args["resource_type"] = field

    field = data.get("zone", None)
    args["zone"] = field

    return Attachment(**args)

def unmarshal_ListAttachmentsResponse(data: Any) -> ListAttachmentsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAttachmentsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("attachments", [])
    args["attachments"] = [unmarshal_Attachment(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListAttachmentsResponse(**args)

def unmarshal_ListFileSystemsResponse(data: Any) -> ListFileSystemsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFileSystemsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("filesystems", [])
    args["filesystems"] = [unmarshal_FileSystem(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListFileSystemsResponse(**args)

def marshal_CreateFileSystemRequest(
    request: CreateFileSystemRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateFileSystemRequest(
    request: UpdateFileSystemRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.size is not None:
        output["size"] = request.size
    else:
        output["size"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output
