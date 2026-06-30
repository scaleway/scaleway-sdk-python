# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    DataKeyAlgorithmSymmetricEncryption,
    KeyAlgorithmAsymmetricEncryption,
    KeyAlgorithmAsymmetricSigning,
    KeyAlgorithmSymmetricEncryption,
    KeyOrigin,
    KeyState,
    KeyRotationPolicy,
    KeyUsage,
    Key,
    DataKey,
    DecryptResponse,
    EncryptResponse,
    ListAlgorithmsResponseAlgorithm,
    ListAlgorithmsResponse,
    ListKeysResponse,
    PublicKey,
    SignResponse,
    VerifyResponse,
    CreateKeyRequest,
    DecryptRequest,
    EncryptRequest,
    GenerateDataKeyRequest,
    ImportKeyMaterialRequest,
    SignRequest,
    UpdateKeyRequest,
    VerifyRequest,
)


def unmarshal_KeyRotationPolicy(data: Any) -> KeyRotationPolicy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KeyRotationPolicy' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

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

    args: dict[str, Any] = {}

    field = data.get("symmetric_encryption", None)
    if field is not None:
        args["symmetric_encryption"] = field
    else:
        args["symmetric_encryption"] = (
            KeyAlgorithmSymmetricEncryption.UNKNOWN_SYMMETRIC_ENCRYPTION
        )

    field = data.get("asymmetric_encryption", None)
    if field is not None:
        args["asymmetric_encryption"] = field
    else:
        args["asymmetric_encryption"] = (
            KeyAlgorithmAsymmetricEncryption.UNKNOWN_ASYMMETRIC_ENCRYPTION
        )

    field = data.get("asymmetric_signing", None)
    if field is not None:
        args["asymmetric_signing"] = field
    else:
        args["asymmetric_signing"] = (
            KeyAlgorithmAsymmetricSigning.UNKNOWN_ASYMMETRIC_SIGNING
        )

    return KeyUsage(**args)


def unmarshal_Key(data: Any) -> Key:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Key' failed as data isn't a dictionary."
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

    field = data.get("state", None)
    if field is not None:
        args["state"] = field
    else:
        args["state"] = KeyState.UNKNOWN_STATE

    field = data.get("rotation_count", None)
    if field is not None:
        args["rotation_count"] = field
    else:
        args["rotation_count"] = 0

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
    else:
        args["protected"] = False

    field = data.get("locked", None)
    if field is not None:
        args["locked"] = field
    else:
        args["locked"] = False

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("origin", None)
    if field is not None:
        args["origin"] = field
    else:
        args["origin"] = KeyOrigin.UNKNOWN_ORIGIN

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    field = data.get("deletion_requested_at", None)
    if field is not None:
        args["deletion_requested_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["deletion_requested_at"] = None

    return Key(**args)


def unmarshal_DataKey(data: Any) -> DataKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DataKey' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field
    else:
        args["key_id"] = None

    field = data.get("algorithm", None)
    if field is not None:
        args["algorithm"] = field
    else:
        args["algorithm"] = (
            DataKeyAlgorithmSymmetricEncryption.UNKNOWN_SYMMETRIC_ENCRYPTION
        )

    field = data.get("ciphertext", None)
    if field is not None:
        args["ciphertext"] = field
    else:
        args["ciphertext"] = None

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

    args: dict[str, Any] = {}

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field
    else:
        args["key_id"] = None

    field = data.get("plaintext", None)
    if field is not None:
        args["plaintext"] = field
    else:
        args["plaintext"] = None

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

    args: dict[str, Any] = {}

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field
    else:
        args["key_id"] = None

    field = data.get("ciphertext", None)
    if field is not None:
        args["ciphertext"] = field
    else:
        args["ciphertext"] = None

    return EncryptResponse(**args)


def unmarshal_ListAlgorithmsResponseAlgorithm(
    data: Any,
) -> ListAlgorithmsResponseAlgorithm:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAlgorithmsResponseAlgorithm' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("usage", None)
    if field is not None:
        args["usage"] = field
    else:
        args["usage"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("recommended", None)
    if field is not None:
        args["recommended"] = field
    else:
        args["recommended"] = None

    return ListAlgorithmsResponseAlgorithm(**args)


def unmarshal_ListAlgorithmsResponse(data: Any) -> ListAlgorithmsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAlgorithmsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("algorithms", None)
    if field is not None:
        args["algorithms"] = (
            [unmarshal_ListAlgorithmsResponseAlgorithm(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["algorithms"] = []

    return ListAlgorithmsResponse(**args)


def unmarshal_ListKeysResponse(data: Any) -> ListKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListKeysResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("keys", None)
    if field is not None:
        args["keys"] = [unmarshal_Key(v) for v in field] if field is not None else None
    else:
        args["keys"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListKeysResponse(**args)


def unmarshal_PublicKey(data: Any) -> PublicKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicKey' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pem", None)
    if field is not None:
        args["pem"] = field
    else:
        args["pem"] = None

    return PublicKey(**args)


def unmarshal_SignResponse(data: Any) -> SignResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SignResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field
    else:
        args["key_id"] = None

    field = data.get("signature", None)
    if field is not None:
        args["signature"] = field
    else:
        args["signature"] = None

    return SignResponse(**args)


def unmarshal_VerifyResponse(data: Any) -> VerifyResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VerifyResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field
    else:
        args["key_id"] = None

    field = data.get("valid", None)
    if field is not None:
        args["valid"] = field
    else:
        args["valid"] = False

    return VerifyResponse(**args)


def marshal_KeyRotationPolicy(
    request: KeyRotationPolicy,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.rotation_period is not None:
        output["rotation_period"] = request.rotation_period

    if request.next_rotation_at is not None:
        output["next_rotation_at"] = request.next_rotation_at.isoformat()

    return output


def marshal_KeyUsage(
    request: KeyUsage,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="symmetric_encryption",
                    value=request.symmetric_encryption,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="asymmetric_encryption",
                    value=request.asymmetric_encryption,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="asymmetric_signing",
                    value=request.asymmetric_signing,
                    marshal_func=None,
                ),
            ]
        ),
    )

    return output


def marshal_CreateKeyRequest(
    request: CreateKeyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.unprotected is not None:
        output["unprotected"] = request.unprotected

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

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
        output["origin"] = request.origin

    return output


def marshal_DecryptRequest(
    request: DecryptRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ciphertext is not None:
        output["ciphertext"] = request.ciphertext

    if request.associated_data is not None:
        output["associated_data"] = request.associated_data

    return output


def marshal_EncryptRequest(
    request: EncryptRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.plaintext is not None:
        output["plaintext"] = request.plaintext

    if request.associated_data is not None:
        output["associated_data"] = request.associated_data

    return output


def marshal_GenerateDataKeyRequest(
    request: GenerateDataKeyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.without_plaintext is not None:
        output["without_plaintext"] = request.without_plaintext

    if request.algorithm is not None:
        output["algorithm"] = request.algorithm

    return output


def marshal_ImportKeyMaterialRequest(
    request: ImportKeyMaterialRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.key_material is not None:
        output["key_material"] = request.key_material

    if request.salt is not None:
        output["salt"] = request.salt

    return output


def marshal_SignRequest(
    request: SignRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.digest is not None:
        output["digest"] = request.digest

    return output


def marshal_UpdateKeyRequest(
    request: UpdateKeyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

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


def marshal_VerifyRequest(
    request: VerifyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.digest is not None:
        output["digest"] = request.digest

    if request.signature is not None:
        output["signature"] = request.signature

    return output
