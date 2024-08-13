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
    KeyRotationPolicy,
    KeyUsage,
    Key,
    DataKey,
    DecryptResponse,
    EncryptResponse,
    ListKeysResponse,
    CreateKeyRequest,
    DecryptRequest,
    EncryptRequest,
    GenerateDataKeyRequest,
    ImportKeyMaterialRequest,
    UpdateKeyRequest,
)


def unmarshal_KeyRotationPolicy(data: Any) -> KeyRotationPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KeyRotationPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rotation_period", None)
    if field is not None:
        args["rotation_period"] = field
    else:
        args["rotation_period"] = None

    field = data.get("next_rotation_at", None)
    if field is not None:
        args["next_rotation_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["next_rotation_at"] = None

    return KeyRotationPolicy(**args)


def unmarshal_KeyUsage(data: Any) -> KeyUsage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KeyUsage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("symmetric_encryption", None)
    if field is not None:
        args["symmetric_encryption"] = field
    else:
        args["symmetric_encryption"] = None

    return KeyUsage(**args)


def unmarshal_Key(data: Any) -> Key:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Key' failed as data isn't a dictionary."
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

    field = data.get("state", None)
    if field is not None:
        args["state"] = field

    field = data.get("rotation_count", None)
    if field is not None:
        args["rotation_count"] = field

    field = data.get("usage", None)
    if field is not None:
        args["usage"] = unmarshal_KeyUsage(field)
    else:
        args["usage"] = None

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

    field = data.get("protected", None)
    if field is not None:
        args["protected"] = field

    field = data.get("locked", None)
    if field is not None:
        args["locked"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("origin", None)
    if field is not None:
        args["origin"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("rotated_at", None)
    if field is not None:
        args["rotated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["rotated_at"] = None

    field = data.get("rotation_policy", None)
    if field is not None:
        args["rotation_policy"] = unmarshal_KeyRotationPolicy(field)
    else:
        args["rotation_policy"] = None

    return Key(**args)


def unmarshal_DataKey(data: Any) -> DataKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DataKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field

    field = data.get("algorithm", None)
    if field is not None:
        args["algorithm"] = field

    field = data.get("ciphertext", None)
    if field is not None:
        args["ciphertext"] = field

    field = data.get("plaintext", None)
    if field is not None:
        args["plaintext"] = field
    else:
        args["plaintext"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return DataKey(**args)


def unmarshal_DecryptResponse(data: Any) -> DecryptResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DecryptResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field

    field = data.get("plaintext", None)
    if field is not None:
        args["plaintext"] = field

    field = data.get("ciphertext", None)
    if field is not None:
        args["ciphertext"] = field
    else:
        args["ciphertext"] = None

    return DecryptResponse(**args)


def unmarshal_EncryptResponse(data: Any) -> EncryptResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EncryptResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field

    field = data.get("ciphertext", None)
    if field is not None:
        args["ciphertext"] = field

    return EncryptResponse(**args)


def unmarshal_ListKeysResponse(data: Any) -> ListKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListKeysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("keys", None)
    if field is not None:
        args["keys"] = [unmarshal_Key(v) for v in field] if field is not None else None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    return ListKeysResponse(**args)


def marshal_KeyRotationPolicy(
    request: KeyRotationPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.rotation_period is not None:
        output["rotation_period"] = request.rotation_period

    if request.next_rotation_at is not None:
        output["next_rotation_at"] = request.next_rotation_at.isoformat()

    return output


def marshal_KeyUsage(
    request: KeyUsage,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("symmetric_encryption", request.symmetric_encryption),
            ]
        ),
    )

    return output


def marshal_CreateKeyRequest(
    request: CreateKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.unprotected is not None:
        output["unprotected"] = request.unprotected

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.name is not None:
        output["name"] = request.name

    if request.usage is not None:
        output["usage"] = marshal_KeyUsage(request.usage, defaults)

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    if request.rotation_policy is not None:
        output["rotation_policy"] = marshal_KeyRotationPolicy(
            request.rotation_policy, defaults
        )

    if request.origin is not None:
        output["origin"] = str(request.origin)

    return output


def marshal_DecryptRequest(
    request: DecryptRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ciphertext is not None:
        output["ciphertext"] = request.ciphertext

    if request.associated_data is not None:
        output["associated_data"] = request.associated_data

    return output


def marshal_EncryptRequest(
    request: EncryptRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.plaintext is not None:
        output["plaintext"] = request.plaintext

    if request.associated_data is not None:
        output["associated_data"] = request.associated_data

    return output


def marshal_GenerateDataKeyRequest(
    request: GenerateDataKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.without_plaintext is not None:
        output["without_plaintext"] = request.without_plaintext

    if request.algorithm is not None:
        output["algorithm"] = str(request.algorithm)

    return output


def marshal_ImportKeyMaterialRequest(
    request: ImportKeyMaterialRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.key_material is not None:
        output["key_material"] = request.key_material

    if request.salt is not None:
        output["salt"] = request.salt

    return output


def marshal_UpdateKeyRequest(
    request: UpdateKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    if request.rotation_policy is not None:
        output["rotation_policy"] = marshal_KeyRotationPolicy(
            request.rotation_policy, defaults
        )

    return output
