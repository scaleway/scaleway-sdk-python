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
    DataKeyAlgorithmSymmetricEncryption,
    KeyAlgorithmAsymmetricEncryption,
    KeyAlgorithmAsymmetricSigning,
    KeyAlgorithmSymmetricEncryption,
    KeyOrigin,
    KeyState,
    ListKeysRequestOrderBy,
    ListKeysRequestUsage,
    KeyRotationPolicy,
    KeyUsage,
    Key,
    DataKey,
    DecryptResponse,
    EncryptResponse,
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

    args: Dict[str, Any] = {}

    field = data.get("rotation_period", None)
    args["rotation_period"] = field

    field = data.get("next_rotation_at", None)
    args["next_rotation_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return KeyRotationPolicy(**args)

def unmarshal_KeyUsage(data: Any) -> KeyUsage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KeyUsage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("symmetric_encryption", None)
    args["symmetric_encryption"] = field

    field = data.get("asymmetric_encryption", None)
    args["asymmetric_encryption"] = field

    field = data.get("asymmetric_signing", None)
    args["asymmetric_signing"] = field

    return KeyUsage(**args)

def unmarshal_Key(data: Any) -> Key:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Key' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("state", getattr(KeyState, "UNKNOWN_STATE"))
    args["state"] = field

    field = data.get("rotation_count", 0)
    args["rotation_count"] = field

    field = data.get("usage", None)
    args["usage"] = unmarshal_KeyUsage(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("protected", False)
    args["protected"] = field

    field = data.get("locked", False)
    args["locked"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("origin", getattr(KeyOrigin, "UNKNOWN_ORIGIN"))
    args["origin"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("rotated_at", None)
    args["rotated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("rotation_policy", None)
    args["rotation_policy"] = unmarshal_KeyRotationPolicy(field) if field is not None else None

    field = data.get("deletion_requested_at", None)
    args["deletion_requested_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Key(**args)

def unmarshal_DataKey(data: Any) -> DataKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DataKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key_id", str())
    args["key_id"] = field

    field = data.get("algorithm", getattr(DataKeyAlgorithmSymmetricEncryption, "UNKNOWN_SYMMETRIC_ENCRYPTION"))
    args["algorithm"] = field

    field = data.get("ciphertext", str())
    args["ciphertext"] = field

    field = data.get("plaintext", None)
    args["plaintext"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DataKey(**args)

def unmarshal_DecryptResponse(data: Any) -> DecryptResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DecryptResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key_id", str())
    args["key_id"] = field

    field = data.get("plaintext", str())
    args["plaintext"] = field

    field = data.get("ciphertext", None)
    args["ciphertext"] = field

    return DecryptResponse(**args)

def unmarshal_EncryptResponse(data: Any) -> EncryptResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EncryptResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key_id", str())
    args["key_id"] = field

    field = data.get("ciphertext", str())
    args["ciphertext"] = field

    return EncryptResponse(**args)

def unmarshal_ListKeysResponse(data: Any) -> ListKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListKeysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("keys", [])
    args["keys"] = [unmarshal_Key(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListKeysResponse(**args)

def unmarshal_PublicKey(data: Any) -> PublicKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("pem", str())
    args["pem"] = field

    return PublicKey(**args)

def unmarshal_SignResponse(data: Any) -> SignResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SignResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key_id", str())
    args["key_id"] = field

    field = data.get("signature", str())
    args["signature"] = field

    return SignResponse(**args)

def unmarshal_VerifyResponse(data: Any) -> VerifyResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VerifyResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("key_id", str())
    args["key_id"] = field

    field = data.get("valid", False)
    args["valid"] = field

    return VerifyResponse(**args)

def marshal_KeyRotationPolicy(
    request: KeyRotationPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.rotation_period is not None:
        output["rotation_period"] = request.rotation_period
    else:
        output["rotation_period"] = None

    if request.next_rotation_at is not None:
        output["next_rotation_at"] = request.next_rotation_at.isoformat()
    else:
        output["next_rotation_at"] = None


    return output

def marshal_KeyUsage(
    request: KeyUsage,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="symmetric_encryption", value=request.symmetric_encryption,marshal_func=marshal_KeyAlgorithmSymmetricEncryption
            ),
            OneOfPossibility(param="asymmetric_encryption", value=request.asymmetric_encryption,marshal_func=marshal_KeyAlgorithmAsymmetricEncryption
            ),
            OneOfPossibility(param="asymmetric_signing", value=request.asymmetric_signing,marshal_func=marshal_KeyAlgorithmAsymmetricSigning
            ),
        ]),
    )


    return output

def marshal_CreateKeyRequest(
    request: CreateKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.unprotected is not None:
        output["unprotected"] = request.unprotected
    else:
        output["unprotected"] = False

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.usage is not None:
        output["usage"] = marshal_KeyUsage(request.usage, defaults)
    else:
        output["usage"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.rotation_policy is not None:
        output["rotation_policy"] = marshal_KeyRotationPolicy(request.rotation_policy, defaults)
    else:
        output["rotation_policy"] = None

    if request.origin is not None:
        output["origin"] = str(request.origin)
    else:
        output["origin"] = None


    return output

def marshal_DecryptRequest(
    request: DecryptRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ciphertext is not None:
        output["ciphertext"] = request.ciphertext
    else:
        output["ciphertext"] = str()

    if request.associated_data is not None:
        output["associated_data"] = request.associated_data
    else:
        output["associated_data"] = None


    return output

def marshal_EncryptRequest(
    request: EncryptRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.plaintext is not None:
        output["plaintext"] = request.plaintext
    else:
        output["plaintext"] = str()

    if request.associated_data is not None:
        output["associated_data"] = request.associated_data
    else:
        output["associated_data"] = None


    return output

def marshal_GenerateDataKeyRequest(
    request: GenerateDataKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.without_plaintext is not None:
        output["without_plaintext"] = request.without_plaintext
    else:
        output["without_plaintext"] = False

    if request.algorithm is not None:
        output["algorithm"] = str(request.algorithm)
    else:
        output["algorithm"] = None


    return output

def marshal_ImportKeyMaterialRequest(
    request: ImportKeyMaterialRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.key_material is not None:
        output["key_material"] = request.key_material
    else:
        output["key_material"] = str()

    if request.salt is not None:
        output["salt"] = request.salt
    else:
        output["salt"] = None


    return output

def marshal_SignRequest(
    request: SignRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.digest is not None:
        output["digest"] = request.digest
    else:
        output["digest"] = str()


    return output

def marshal_UpdateKeyRequest(
    request: UpdateKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.rotation_policy is not None:
        output["rotation_policy"] = marshal_KeyRotationPolicy(request.rotation_policy, defaults)
    else:
        output["rotation_policy"] = None


    return output

def marshal_VerifyRequest(
    request: VerifyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.digest is not None:
        output["digest"] = request.digest
    else:
        output["digest"] = str()

    if request.signature is not None:
        output["signature"] = request.signature
    else:
        output["signature"] = str()


    return output
