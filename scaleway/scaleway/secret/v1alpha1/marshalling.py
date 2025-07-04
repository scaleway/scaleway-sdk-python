# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    Folder,
    EphemeralProperties,
    SecretVersion,
    EphemeralPolicy,
    Secret,
    AccessSecretVersionResponse,
    ListFoldersResponse,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    ListTagsResponse,
    AddSecretOwnerRequest,
    CreateFolderRequest,
    CreateSecretRequest,
    PasswordGenerationParams,
    CreateSecretVersionRequest,
    GeneratePasswordRequest,
    UpdateSecretRequest,
    UpdateSecretVersionRequest,
)


def unmarshal_Folder(data: Any) -> Folder:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Folder' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("path", None)
    if field is not None:
        args["path"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return Folder(**args)


def unmarshal_EphemeralProperties(data: Any) -> EphemeralProperties:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EphemeralProperties' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", None)
    if field is not None:
        args["action"] = field

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    field = data.get("expires_once_accessed", None)
    if field is not None:
        args["expires_once_accessed"] = field
    else:
        args["expires_once_accessed"] = None

    return EphemeralProperties(**args)


def unmarshal_SecretVersion(data: Any) -> SecretVersion:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("revision", None)
    if field is not None:
        args["revision"] = field

    field = data.get("secret_id", None)
    if field is not None:
        args["secret_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("is_latest", None)
    if field is not None:
        args["is_latest"] = field

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

    field = data.get("ephemeral_properties", None)
    if field is not None:
        args["ephemeral_properties"] = unmarshal_EphemeralProperties(field)
    else:
        args["ephemeral_properties"] = None

    return SecretVersion(**args)


def unmarshal_EphemeralPolicy(data: Any) -> EphemeralPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EphemeralPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", None)
    if field is not None:
        args["action"] = field

    field = data.get("time_to_live", None)
    if field is not None:
        args["time_to_live"] = field
    else:
        args["time_to_live"] = None

    field = data.get("expires_once_accessed", None)
    if field is not None:
        args["expires_once_accessed"] = field
    else:
        args["expires_once_accessed"] = None

    return EphemeralPolicy(**args)


def unmarshal_Secret(data: Any) -> Secret:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Secret' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

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

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("version_count", None)
    if field is not None:
        args["version_count"] = field

    field = data.get("is_managed", None)
    if field is not None:
        args["is_managed"] = field

    field = data.get("is_protected", None)
    if field is not None:
        args["is_protected"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("path", None)
    if field is not None:
        args["path"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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

    return Secret(**args)


def unmarshal_AccessSecretVersionResponse(data: Any) -> AccessSecretVersionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccessSecretVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secret_id", None)
    if field is not None:
        args["secret_id"] = field

    field = data.get("revision", None)
    if field is not None:
        args["revision"] = field

    field = data.get("data", None)
    if field is not None:
        args["data"] = field

    field = data.get("data_crc32", None)
    if field is not None:
        args["data_crc32"] = field
    else:
        args["data_crc32"] = None

    return AccessSecretVersionResponse(**args)


def unmarshal_ListFoldersResponse(data: Any) -> ListFoldersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFoldersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("folders", None)
    if field is not None:
        args["folders"] = (
            [unmarshal_Folder(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListFoldersResponse(**args)


def unmarshal_ListSecretVersionsResponse(data: Any) -> ListSecretVersionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecretVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("versions", None)
    if field is not None:
        args["versions"] = (
            [unmarshal_SecretVersion(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListSecretVersionsResponse(**args)


def unmarshal_ListSecretsResponse(data: Any) -> ListSecretsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSecretsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secrets", None)
    if field is not None:
        args["secrets"] = (
            [unmarshal_Secret(v) for v in field] if field is not None else None
        )

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListSecretsResponse(**args)


def unmarshal_ListTagsResponse(data: Any) -> ListTagsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListTagsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListTagsResponse(**args)


def marshal_AddSecretOwnerRequest(
    request: AddSecretOwnerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.product_name is not None:
        output["product_name"] = request.product_name

    if request.product is not None:
        output["product"] = str(request.product)

    return output


def marshal_CreateFolderRequest(
    request: CreateFolderRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.path is not None:
        output["path"] = request.path

    return output


def marshal_EphemeralPolicy(
    request: EphemeralPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = str(request.action)

    if request.time_to_live is not None:
        output["time_to_live"] = request.time_to_live

    if request.expires_once_accessed is not None:
        output["expires_once_accessed"] = request.expires_once_accessed

    return output


def marshal_CreateSecretRequest(
    request: CreateSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.is_protected is not None:
        output["is_protected"] = request.is_protected

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.description is not None:
        output["description"] = request.description

    if request.type_ is not None:
        output["type"] = str(request.type_)

    if request.path is not None:
        output["path"] = request.path

    if request.ephemeral_policy is not None:
        output["ephemeral_policy"] = marshal_EphemeralPolicy(
            request.ephemeral_policy, defaults
        )

    return output


def marshal_PasswordGenerationParams(
    request: PasswordGenerationParams,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.length is not None:
        output["length"] = request.length

    if request.no_lowercase_letters is not None:
        output["no_lowercase_letters"] = request.no_lowercase_letters

    if request.no_uppercase_letters is not None:
        output["no_uppercase_letters"] = request.no_uppercase_letters

    if request.no_digits is not None:
        output["no_digits"] = request.no_digits

    if request.additional_chars is not None:
        output["additional_chars"] = request.additional_chars

    return output


def marshal_CreateSecretVersionRequest(
    request: CreateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.data is not None:
        output["data"] = request.data

    if request.description is not None:
        output["description"] = request.description

    if request.disable_previous is not None:
        output["disable_previous"] = request.disable_previous

    if request.password_generation is not None:
        output["password_generation"] = marshal_PasswordGenerationParams(
            request.password_generation, defaults
        )

    if request.data_crc32 is not None:
        output["data_crc32"] = request.data_crc32

    return output


def marshal_GeneratePasswordRequest(
    request: GeneratePasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.length is not None:
        output["length"] = request.length

    if request.description is not None:
        output["description"] = request.description

    if request.disable_previous is not None:
        output["disable_previous"] = request.disable_previous

    if request.no_lowercase_letters is not None:
        output["no_lowercase_letters"] = request.no_lowercase_letters

    if request.no_uppercase_letters is not None:
        output["no_uppercase_letters"] = request.no_uppercase_letters

    if request.no_digits is not None:
        output["no_digits"] = request.no_digits

    if request.additional_chars is not None:
        output["additional_chars"] = request.additional_chars

    return output


def marshal_UpdateSecretRequest(
    request: UpdateSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = str(request.action)

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    if request.expires_once_accessed is not None:
        output["expires_once_accessed"] = request.expires_once_accessed

    return output


def marshal_UpdateSecretVersionRequest(
    request: UpdateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.ephemeral_properties is not None:
        output["ephemeral_properties"] = marshal_EphemeralProperties(
            request.ephemeral_properties, defaults
        )

    return output
