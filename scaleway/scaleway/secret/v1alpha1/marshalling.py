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
    Product,
    AccessSecretVersionResponse,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    PasswordGenerationParams,
    Secret,
    SecretVersion,
    CreateSecretRequest,
    UpdateSecretRequest,
    AddSecretOwnerRequest,
    CreateSecretVersionRequest,
    GeneratePasswordRequest,
    UpdateSecretVersionRequest,
)


def unmarshal_Secret(data: Any) -> Secret:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Secret' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("is_managed", None)
    args["is_managed"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("version_count", None)
    args["version_count"] = field

    return Secret(**args)


def unmarshal_SecretVersion(data: Any) -> SecretVersion:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecretVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("is_latest", None)
    args["is_latest"] = field

    field = data.get("revision", None)
    args["revision"] = field

    field = data.get("secret_id", None)
    args["secret_id"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return SecretVersion(**args)


def unmarshal_AccessSecretVersionResponse(data: Any) -> AccessSecretVersionResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AccessSecretVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("data", None)
    args["data"] = field

    field = data.get("data_crc32", None)
    args["data_crc32"] = field

    field = data.get("revision", None)
    args["revision"] = field

    field = data.get("secret_id", None)
    args["secret_id"] = field

    return AccessSecretVersionResponse(**args)


def unmarshal_ListSecretVersionsResponse(data: Any) -> ListSecretVersionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSecretVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("versions", None)
    args["versions"] = (
        [unmarshal_SecretVersion(v) for v in field] if field is not None else None
    )

    return ListSecretVersionsResponse(**args)


def unmarshal_ListSecretsResponse(data: Any) -> ListSecretsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSecretsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secrets", None)
    args["secrets"] = (
        [unmarshal_Secret(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSecretsResponse(**args)


def marshal_PasswordGenerationParams(
    request: PasswordGenerationParams,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "additional_chars": request.additional_chars,
        "length": request.length,
        "no_digits": request.no_digits,
        "no_lowercase_letters": request.no_lowercase_letters,
        "no_uppercase_letters": request.no_uppercase_letters,
    }


def marshal_AddSecretOwnerRequest(
    request: AddSecretOwnerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "product": Product(request.product),
        "product_name": request.product_name,
    }


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
        **resolve_one_of(
            [
                OneOfPossibility(
                    "password_generation",
                    marshal_PasswordGenerationParams(
                        request.password_generation, defaults
                    )
                    if request.password_generation is not None
                    else None,
                ),
            ]
        ),
        "data": request.data,
        "data_crc32": request.data_crc32,
        "description": request.description,
        "disable_previous": request.disable_previous,
    }


def marshal_GeneratePasswordRequest(
    request: GeneratePasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "additional_chars": request.additional_chars,
        "description": request.description,
        "disable_previous": request.disable_previous,
        "length": request.length,
        "no_digits": request.no_digits,
        "no_lowercase_letters": request.no_lowercase_letters,
        "no_uppercase_letters": request.no_uppercase_letters,
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
