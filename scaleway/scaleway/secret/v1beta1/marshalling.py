# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    EphemeralPolicyAction,
    Product,
    SecretStatus,
    SecretType,
    SecretVersionStatus,
    EphemeralProperties,
    SecretVersion,
    EphemeralPolicy,
    Secret,
    AccessSecretVersionResponse,
    BrowseSecretsResponseItemFolderDetails,
    BrowseSecretsResponseItemSecretDetails,
    BrowseSecretsResponseItem,
    BrowseSecretsResponse,
    ListSecretTypesResponse,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    ListTagsResponse,
    AddSecretOwnerRequest,
    CreateSecretRequest,
    CreateSecretVersionRequest,
    UpdateSecretRequest,
    UpdateSecretVersionRequest,
)


def unmarshal_EphemeralProperties(data: Any) -> EphemeralProperties:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EphemeralProperties' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("action", None)
    if field is not None:
        args["action"] = field
    else:
        args["action"] = EphemeralPolicyAction.UNKNOWN_ACTION

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    field = data.get("expires_once_accessed", None)
    if field is not None:
        args["expires_once_accessed"] = field
    else:
        args["expires_once_accessed"] = False

    return EphemeralProperties(**args)


def unmarshal_SecretVersion(data: Any) -> SecretVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretVersion' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("revision", None)
    if field is not None:
        args["revision"] = field
    else:
        args["revision"] = 0

    field = data.get("secret_id", None)
    if field is not None:
        args["secret_id"] = field
    else:
        args["secret_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = SecretVersionStatus.UNKNOWN_STATUS

    field = data.get("latest", None)
    if field is not None:
        args["latest"] = field
    else:
        args["latest"] = False

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

    field = data.get("deleted_at", None)
    if field is not None:
        args["deleted_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["deleted_at"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("ephemeral_properties", None)
    if field is not None:
        args["ephemeral_properties"] = unmarshal_EphemeralProperties(field)
    else:
        args["ephemeral_properties"] = None

    field = data.get("deletion_requested_at", None)
    if field is not None:
        args["deletion_requested_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["deletion_requested_at"] = None

    return SecretVersion(**args)


def unmarshal_EphemeralPolicy(data: Any) -> EphemeralPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EphemeralPolicy' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("action", None)
    if field is not None:
        args["action"] = field
    else:
        args["action"] = EphemeralPolicyAction.UNKNOWN_ACTION

    field = data.get("time_to_live", None)
    if field is not None:
        args["time_to_live"] = field
    else:
        args["time_to_live"] = None

    field = data.get("expires_once_accessed", None)
    if field is not None:
        args["expires_once_accessed"] = field
    else:
        args["expires_once_accessed"] = False

    return EphemeralPolicy(**args)


def unmarshal_Secret(data: Any) -> Secret:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Secret' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = SecretStatus.UNKNOWN_STATUS

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("version_count", None)
    if field is not None:
        args["version_count"] = field
    else:
        args["version_count"] = 0

    field = data.get("managed", None)
    if field is not None:
        args["managed"] = field
    else:
        args["managed"] = False

    field = data.get("protected", None)
    if field is not None:
        args["protected"] = field
    else:
        args["protected"] = False

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = SecretType.UNKNOWN_TYPE

    field = data.get("path", None)
    if field is not None:
        args["path"] = field
    else:
        args["path"] = None

    field = data.get("used_by", None)
    if field is not None:
        args["used_by"] = [Product(v) for v in field] if field is not None else None
    else:
        args["used_by"] = []

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

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("ephemeral_policy", None)
    if field is not None:
        args["ephemeral_policy"] = unmarshal_EphemeralPolicy(field)
    else:
        args["ephemeral_policy"] = None

    field = data.get("deletion_requested_at", None)
    if field is not None:
        args["deletion_requested_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["deletion_requested_at"] = None

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field
    else:
        args["key_id"] = None

    return Secret(**args)


def unmarshal_AccessSecretVersionResponse(data: Any) -> AccessSecretVersionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccessSecretVersionResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("secret_id", None)
    if field is not None:
        args["secret_id"] = field
    else:
        args["secret_id"] = None

    field = data.get("revision", None)
    if field is not None:
        args["revision"] = field
    else:
        args["revision"] = 0

    field = data.get("data", None)
    if field is not None:
        args["data"] = field
    else:
        args["data"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = SecretType.UNKNOWN_TYPE

    field = data.get("data_crc32", None)
    if field is not None:
        args["data_crc32"] = field
    else:
        args["data_crc32"] = 0

    return AccessSecretVersionResponse(**args)


def unmarshal_BrowseSecretsResponseItemFolderDetails(
    data: Any,
) -> BrowseSecretsResponseItemFolderDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BrowseSecretsResponseItemFolderDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return BrowseSecretsResponseItemFolderDetails(**args)


def unmarshal_BrowseSecretsResponseItemSecretDetails(
    data: Any,
) -> BrowseSecretsResponseItemSecretDetails:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BrowseSecretsResponseItemSecretDetails' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    field = data.get("version_count", None)
    if field is not None:
        args["version_count"] = field
    else:
        args["version_count"] = None

    field = data.get("protected", None)
    if field is not None:
        args["protected"] = field
    else:
        args["protected"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("ephemeral_policy", None)
    if field is not None:
        args["ephemeral_policy"] = unmarshal_EphemeralPolicy(field)
    else:
        args["ephemeral_policy"] = None

    return BrowseSecretsResponseItemSecretDetails(**args)


def unmarshal_BrowseSecretsResponseItem(data: Any) -> BrowseSecretsResponseItem:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BrowseSecretsResponseItem' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

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

    field = data.get("secret", None)
    if field is not None:
        args["secret"] = unmarshal_BrowseSecretsResponseItemSecretDetails(field)
    else:
        args["secret"] = None

    field = data.get("folder", None)
    if field is not None:
        args["folder"] = unmarshal_BrowseSecretsResponseItemFolderDetails(field)
    else:
        args["folder"] = None

    return BrowseSecretsResponseItem(**args)


def unmarshal_BrowseSecretsResponse(data: Any) -> BrowseSecretsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BrowseSecretsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("items", None)
    if field is not None:
        args["items"] = (
            [unmarshal_BrowseSecretsResponseItem(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["items"] = []

    field = data.get("current_path", None)
    if field is not None:
        args["current_path"] = field
    else:
        args["current_path"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return BrowseSecretsResponse(**args)


def unmarshal_ListSecretTypesResponse(data: Any) -> ListSecretTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecretTypesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("types", None)
    if field is not None:
        args["types"] = [SecretType(v) for v in field] if field is not None else None
    else:
        args["types"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListSecretTypesResponse(**args)


def unmarshal_ListSecretVersionsResponse(data: Any) -> ListSecretVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecretVersionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_SecretVersion(v) for v in field] if field is not None else None
        )
    else:
        args["versions"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListSecretVersionsResponse(**args)


def unmarshal_ListSecretsResponse(data: Any) -> ListSecretsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecretsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("secrets", None)
    if field is not None:
        args["secrets"] = (
            [unmarshal_Secret(v) for v in field] if field is not None else None
        )
    else:
        args["secrets"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListSecretsResponse(**args)


def unmarshal_ListTagsResponse(data: Any) -> ListTagsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTagsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListTagsResponse(**args)


def marshal_AddSecretOwnerRequest(
    request: AddSecretOwnerRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.product is not None:
        output["product"] = request.product

    return output


def marshal_EphemeralPolicy(
    request: EphemeralPolicy,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.action is not None:
        output["action"] = request.action

    if request.time_to_live is not None:
        output["time_to_live"] = request.time_to_live

    if request.expires_once_accessed is not None:
        output["expires_once_accessed"] = request.expires_once_accessed

    return output


def marshal_CreateSecretRequest(
    request: CreateSecretRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.protected is not None:
        output["protected"] = request.protected

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.description is not None:
        output["description"] = request.description

    if request.type_ is not None:
        output["type"] = request.type_

    if request.path is not None:
        output["path"] = request.path

    if request.ephemeral_policy is not None:
        output["ephemeral_policy"] = marshal_EphemeralPolicy(
            request.ephemeral_policy, defaults
        )

    if request.key_id is not None:
        output["key_id"] = request.key_id

    return output


def marshal_CreateSecretVersionRequest(
    request: CreateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.data is not None:
        output["data"] = request.data

    if request.description is not None:
        output["description"] = request.description

    if request.disable_previous is not None:
        output["disable_previous"] = request.disable_previous

    if request.data_crc32 is not None:
        output["data_crc32"] = request.data_crc32

    return output


def marshal_UpdateSecretRequest(
    request: UpdateSecretRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    if request.description is not None:
        output["description"] = request.description

    if request.path is not None:
        output["path"] = request.path

    if request.ephemeral_policy is not None:
        output["ephemeral_policy"] = marshal_EphemeralPolicy(
            request.ephemeral_policy, defaults
        )

    return output


def marshal_EphemeralProperties(
    request: EphemeralProperties,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.action is not None:
        output["action"] = request.action

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    if request.expires_once_accessed is not None:
        output["expires_once_accessed"] = request.expires_once_accessed

    return output


def marshal_UpdateSecretVersionRequest(
    request: UpdateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.ephemeral_properties is not None:
        output["ephemeral_properties"] = marshal_EphemeralProperties(
            request.ephemeral_properties, defaults
        )

    return output
