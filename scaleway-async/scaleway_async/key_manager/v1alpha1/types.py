# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class DataKeyAlgorithmSymmetricEncryption(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SYMMETRIC_ENCRYPTION = "unknown_symmetric_encryption"
    AES_256_GCM = "aes_256_gcm"

    def __str__(self) -> str:
        return str(self.value)


class KeyAlgorithmSymmetricEncryption(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SYMMETRIC_ENCRYPTION = "unknown_symmetric_encryption"
    AES_256_GCM = "aes_256_gcm"

    def __str__(self) -> str:
        return str(self.value)


class KeyOrigin(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ORIGIN = "unknown_origin"
    SCALEWAY_KMS = "scaleway_kms"
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)


class KeyState(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATE = "unknown_state"
    ENABLED = "enabled"
    DISABLED = "disabled"
    PENDING_KEY_MATERIAL = "pending_key_material"

    def __str__(self) -> str:
        return str(self.value)


class ListKeysRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class KeyRotationPolicy:
    rotation_period: Optional[str]
    """
    Duration between two key rotations. The minimum duration is 24 hours and the maximum duration is 876000 hours (1 year).
    """

    next_rotation_at: Optional[datetime]
    """
    Date at which the key will be rotated next.
    """


@dataclass
class KeyUsage:
    symmetric_encryption: Optional[KeyAlgorithmSymmetricEncryption]


@dataclass
class Key:
    id: str
    """
    ID of the key.
    """

    project_id: str
    """
    ID of the Project containing the key.
    """

    name: str
    """
    Name of the key.
    """

    state: KeyState
    """
    See the `Key.State` enum for a description of values.
    """

    rotation_count: int
    """
    The rotation count tracks the amount of times that the key was rotated.
    """

    usage: Optional[KeyUsage]
    """
    Keys with a usage set to `symmetric_encryption` are used to encrypt and decrypt data. The only key algorithm currently supported by Key Manager is AES-256-GCM.
    """

    created_at: Optional[datetime]
    """
    Key creation date.
    """

    updated_at: Optional[datetime]
    """
    Key last modification date.
    """

    protected: bool
    """
    Returns `true` if key protection is applied to the key.
    """

    locked: bool
    """
    Returns `true` if the key is locked.
    """

    tags: List[str]
    """
    List of the key's tags.
    """

    origin: KeyOrigin
    """
    Refer to the `Key.Origin` enum for a description of values.
    """

    region: Region
    """
    Region of the key.
    """

    description: Optional[str]
    """
    Description of the key.
    """

    rotated_at: Optional[datetime]
    """
    Key last rotation date.
    """

    rotation_policy: Optional[KeyRotationPolicy]
    """
    Key rotation policy.
    """


@dataclass
class CreateKeyRequest:
    unprotected: bool
    """
    Default value is `false`.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project containing the key.
    """

    name: Optional[str]
    """
    (Optional) Name of the key.
    """

    usage: Optional[KeyUsage]
    """
    See the `Key.Algorithm.SymmetricEncryption` enum for a description of values.
    """

    description: Optional[str]
    """
    (Optional) Description of the key.
    """

    tags: Optional[List[str]]
    """
    (Optional) List of the key's tags.
    """

    rotation_policy: Optional[KeyRotationPolicy]
    """
    If not specified, no rotation policy will be applied to the key.
    """

    origin: Optional[KeyOrigin]
    """
    Refer to the `Key.Origin` enum for a description of values.
    """


@dataclass
class DataKey:
    key_id: str
    """
    ID of the data encryption key.
    """

    algorithm: DataKeyAlgorithmSymmetricEncryption
    """
    Symmetric encryption algorithm of the data encryption key.
    """

    ciphertext: str
    """
    Your data encryption key's ciphertext can be stored safely. It can only be decrypted through the keys you create in Key Manager, using the relevant key ID.
    """

    plaintext: Optional[str]
    """
    (Optional) Your data encryption key's plaintext allows you to use the key immediately upon creation. It must neither be stored or shared.
    """

    created_at: Optional[datetime]
    """
    Data encryption key creation date.
    """


@dataclass
class DecryptRequest:
    key_id: str
    """
    ID of the key to decrypt.
    """

    ciphertext: str
    """
    Data size must be between 1 and 131071 bytes.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    associated_data: Optional[str]
    """
    The additional data must match the value passed in the encryption request.
    """


@dataclass
class DecryptResponse:
    key_id: str
    """
    ID of the key used for decryption.
    """

    plaintext: str
    """
    Key's decrypted data.
    """

    ciphertext: Optional[str]
    """
    If the data was already encrypted with the latest key rotation, no output will be returned in the response object.
    """


@dataclass
class DeleteKeyMaterialRequest:
    key_id: str
    """
    ID of the key of which to delete the key material.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteKeyRequest:
    key_id: str
    """
    ID of the key to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DisableKeyRequest:
    key_id: str
    """
    ID of the key to disable.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EnableKeyRequest:
    key_id: str
    """
    ID of the key to enable.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EncryptRequest:
    key_id: str
    """
    ID of the key to encrypt.
    """

    plaintext: str
    """
    Data size must be between 1 and 65535 bytes.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    associated_data: Optional[str]
    """
    Additional data which will not be encrypted, but authenticated and appended to the encrypted payload.
    """


@dataclass
class EncryptResponse:
    key_id: str
    """
    ID of the key used for encryption.
    """

    ciphertext: str
    """
    Key's encrypted data.
    """


@dataclass
class GenerateDataKeyRequest:
    key_id: str
    """
    ID of the key.
    """

    without_plaintext: bool
    """
    Default value is `false`, meaning that the plaintext is returned.
Set it to `true` if you do not wish the plaintext to be returned in the response object.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    algorithm: Optional[DataKeyAlgorithmSymmetricEncryption]
    """
    See the `DataKey.Algorithm.SymmetricEncryption` enum for a description of values.
    """


@dataclass
class GetKeyRequest:
    key_id: str
    """
    ID of the key to target.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ImportKeyMaterialRequest:
    key_id: str
    """
    The key's origin must be 'external'.
    """

    key_material: str
    """
    The key material The key material is a random sequence of bytes used to derive a cryptographic key.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    salt: Optional[str]
    """
    A salt can be used to improve the quality of randomness when the key material is generated from a low entropy source.
    """


@dataclass
class ListKeysRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    (Optional) Filter by Organization ID.
    """

    project_id: Optional[str]
    """
    (Optional) Filter by Project ID.
    """

    order_by: Optional[ListKeysRequestOrderBy]

    page: Optional[int]

    page_size: Optional[int]

    tags: Optional[List[str]]
    """
    (Optional) List of tags to filter on.
    """

    name: Optional[str]
    """
    (Optional) Filter by key name.
    """


@dataclass
class ListKeysResponse:
    keys: List[Key]
    """
    Single page of keys matching the requested criteria.
    """

    total_count: int
    """
    Total count of keys matching the requested criteria.
    """


@dataclass
class ProtectKeyRequest:
    key_id: str
    """
    ID of the key to apply key protection to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RotateKeyRequest:
    key_id: str
    """
    ID of the key to rotate.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UnprotectKeyRequest:
    key_id: str
    """
    ID of the key to remove key protection from.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateKeyRequest:
    key_id: str
    """
    ID of the key to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    (Optional) Updated name of the key.
    """

    description: Optional[str]
    """
    (Optional) Updated description of the key.
    """

    tags: Optional[List[str]]
    """
    (Optional) Updated list of the key's tags.
    """

    rotation_policy: Optional[KeyRotationPolicy]
    """
    If not specified, the key's existing rotation policy applies.
    """
