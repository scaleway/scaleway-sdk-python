# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    Project,
    ListProjectsResponse,
    ProjectApiCreateProjectRequest,
    ProjectApiUpdateProjectRequest,
)


def unmarshal_Project(data: Any) -> Project:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Project' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field

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

    return Project(**args)


def unmarshal_ListProjectsResponse(data: Any) -> ListProjectsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProjectsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("projects", None)
    if field is not None:
        args["projects"] = (
            [unmarshal_Project(v) for v in field] if field is not None else None
        )

    return ListProjectsResponse(**args)


def marshal_ProjectApiCreateProjectRequest(
    request: ProjectApiCreateProjectRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.organization_id is not None:
        output["organization_id"] = (
            request.organization_id or defaults.default_organization_id
        )

    return output


def marshal_ProjectApiUpdateProjectRequest(
    request: ProjectApiUpdateProjectRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    return output
