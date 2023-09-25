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
    SecretType,
    AccessSecretVersionResponse,
    Folder,
    ListFoldersResponse,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    ListTagsResponse,
    PasswordGenerationParams,
    Secret,
    SecretVersion,
    CreateSecretRequest,
    CreateFolderRequest,
    UpdateSecretRequest,
    AddSecretOwnerRequest,
    CreateSecretVersionRequest,
    GeneratePasswordRequest,
    UpdateSecretVersionRequest,
)


def unmarshal_Folder(data: Any) -> Folder:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Folder' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id", None)
    args["id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("path", None)
    args["path"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    return Folder(**args)


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

    field = data.get("is_protected", None)
    args["is_protected"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("path", None)
    args["path"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("type", None)
    args["type_"] = field

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


def unmarshal_ListFoldersResponse(data: Any) -> ListFoldersResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListFoldersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("folders", None)
    args["folders"] = (
        [unmarshal_Folder(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListFoldersResponse(**args)


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


def unmarshal_ListTagsResponse(data: Any) -> ListTagsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListTagsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListTagsResponse(**args)


def marshal_PasswordGenerationParams(
    request: PasswordGenerationParams,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.additional_chars is not None:
        output["additional_chars"] = request.additional_chars

    if request.length is not None:
        output["length"] = request.length

    if request.no_digits is not None:
        output["no_digits"] = request.no_digits

    if request.no_lowercase_letters is not None:
        output["no_lowercase_letters"] = request.no_lowercase_letters

    if request.no_uppercase_letters is not None:
        output["no_uppercase_letters"] = request.no_uppercase_letters

    return output


def marshal_AddSecretOwnerRequest(
    request: AddSecretOwnerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.product is not None:
        output["product"] = Product(request.product)

    if request.product_name is not None:
        output["product_name"] = request.product_name

    return output


def marshal_CreateFolderRequest(
    request: CreateFolderRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.path is not None:
        output["path"] = request.path

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_CreateSecretRequest(
    request: CreateSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.path is not None:
        output["path"] = request.path

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.type_ is not None:
        output["type"] = SecretType(request.type_)

    return output


def marshal_CreateSecretVersionRequest(
    request: CreateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
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
    )

    if request.data is not None:
        output["data"] = request.data

    if request.data_crc32 is not None:
        output["data_crc32"] = request.data_crc32

    if request.description is not None:
        output["description"] = request.description

    if request.disable_previous is not None:
        output["disable_previous"] = request.disable_previous

    return output


def marshal_GeneratePasswordRequest(
    request: GeneratePasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.additional_chars is not None:
        output["additional_chars"] = request.additional_chars

    if request.description is not None:
        output["description"] = request.description

    if request.disable_previous is not None:
        output["disable_previous"] = request.disable_previous

    if request.length is not None:
        output["length"] = request.length

    if request.no_digits is not None:
        output["no_digits"] = request.no_digits

    if request.no_lowercase_letters is not None:
        output["no_lowercase_letters"] = request.no_lowercase_letters

    if request.no_uppercase_letters is not None:
        output["no_uppercase_letters"] = request.no_uppercase_letters

    return output


def marshal_UpdateSecretRequest(
    request: UpdateSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.path is not None:
        output["path"] = request.path

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateSecretVersionRequest(
    request: UpdateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    return output
