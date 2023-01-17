# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    AccessSecretVersionResponse,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    Secret,
    SecretVersion,
    CreateSecretRequest,
    UpdateSecretRequest,
    CreateSecretVersionRequest,
    UpdateSecretVersionRequest,
)


def unmarshal_Secret(data: Any) -> Secret:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Secret' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description")
    args["description"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("name")
    args["name"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("region")
    args["region"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("tags")
    args["tags"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("version_count")
    args["version_count"] = field

    return Secret(**args)


def unmarshal_SecretVersion(data: Any) -> SecretVersion:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecretVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description")
    args["description"] = field

    field = data.get("revision")
    args["revision"] = field

    field = data.get("secret_id")
    args["secret_id"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return SecretVersion(**args)


def unmarshal_AccessSecretVersionResponse(data: Any) -> AccessSecretVersionResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AccessSecretVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("data")
    args["data"] = field

    field = data.get("revision")
    args["revision"] = field

    field = data.get("secret_id")
    args["secret_id"] = field

    return AccessSecretVersionResponse(**args)


def unmarshal_ListSecretVersionsResponse(data: Any) -> ListSecretVersionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSecretVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count")
    args["total_count"] = field

    field = data.get("versions")
    args["versions"] = [unmarshal_SecretVersion(v) for v in data["versions"]]

    return ListSecretVersionsResponse(**args)


def unmarshal_ListSecretsResponse(data: Any) -> ListSecretsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSecretsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secrets")
    args["secrets"] = [unmarshal_Secret(v) for v in data["secrets"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListSecretsResponse(**args)


def marshal_CreateSecretRequest(
    request: CreateSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "name": request.name,
        "project_id": request.project_id or defaults.default_project_id,
        "tags": request.tags,
    }


def marshal_CreateSecretVersionRequest(
    request: CreateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "data": request.data,
        "description": request.description,
    }


def marshal_UpdateSecretRequest(
    request: UpdateSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
        "name": request.name,
        "tags": request.tags,
    }


def marshal_UpdateSecretVersionRequest(
    request: UpdateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "description": request.description,
    }
