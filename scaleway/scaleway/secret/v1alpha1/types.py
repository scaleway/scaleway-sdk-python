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


class EphemeralPolicyAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
    DELETE = "delete"
    DISABLE = "disable"

    def __str__(self) -> str:
        return str(self.value)


class ListFoldersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSecretsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class Product(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    EDGE_SERVICES = "edge_services"

    def __str__(self) -> str:
        return str(self.value)


class SecretStatus(str, Enum, metaclass=StrEnumMeta):
    READY = "ready"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class SecretType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SECRET_TYPE = "unknown_secret_type"
    OPAQUE = "opaque"
    CERTIFICATE = "certificate"
    KEY_VALUE = "key_value"

    def __str__(self) -> str:
        return str(self.value)


class SecretVersionStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    ENABLED = "enabled"
    DISABLED = "disabled"
    DESTROYED = "destroyed"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class AccessSecretVersionResponse:
    """
    Access secret version response.
    """

    secret_id: str
    """
    ID of the secret.
    """

    revision: int
    """
    Version number.
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1.
    """

    data: str
    """
    The base64-encoded secret payload of the version.
    """

    data_crc32: Optional[int]
    """
    The CRC32 checksum of the data as a base-10 integer.
    This field is only available if a CRC32 was supplied during the creation of the version.
    """


@dataclass
class EphemeralPolicy:
    """
    Ephemeral policy.
    """

    time_to_live: Optional[str]
    """
    Time frame, from one second and up to one year, during which the secret's versions are valid.
    """

    expires_once_accessed: Optional[bool]
    """
    Returns `true` if the version expires after a single user access.
    """

    action: EphemeralPolicyAction
    """
    Action to perform when the version of a secret expires.
    See the `EphemeralPolicy.Action` enum for a description of values.
    """


@dataclass
class EphemeralProperties:
    """
    Ephemeral properties.
    """

    expires_at: Optional[datetime]
    """
    The version's expiration date.
    (Optional.) If not specified, the version does not have an expiration date.
    """

    expires_once_accessed: Optional[bool]
    """
    Returns `true` if the version expires after a single user access.
    (Optional.) If not specified, the version can be accessed an unlimited amount of times.
    """

    action: EphemeralPolicyAction
    """
    Action to perform when the version of a secret expires.
    See `EphemeralPolicy.Action` enum for a description of values.
    """


@dataclass
class Folder:
    """
    Folder.
    """

    id: str
    """
    ID of the folder.
    """

    project_id: str
    """
    ID of the Project containing the folder.
    """

    name: str
    """
    Name of the folder.
    """

    path: str
    """
    Path of the folder.
    Location of the folder in the directory structure.
    """

    created_at: Optional[datetime]
    """
    Date and time of the folder's creation.
    """

    region: Region
    """
    Region of the folder.
    """


@dataclass
class ListFoldersResponse:
    """
    List folders response.
    """

    folders: List[Folder]
    """
    List of folders.
    """

    total_count: int
    """
    Count of all folders matching the requested criteria.
    """


@dataclass
class ListSecretVersionsResponse:
    """
    List secret versions response.
    """

    versions: List[SecretVersion]
    """
    Single page of versions.
    """

    total_count: int
    """
    Number of versions.
    """


@dataclass
class ListSecretsResponse:
    """
    List secrets response.
    """

    secrets: List[Secret]
    """
    Single page of secrets matching the requested criteria.
    """

    total_count: int
    """
    Count of all secrets matching the requested criteria.
    """


@dataclass
class ListTagsResponse:
    """
    List tags response.
    """

    tags: List[str]
    """
    List of tags.
    """

    total_count: int
    """
    Count of all tags matching the requested criteria.
    """


@dataclass
class PasswordGenerationParams:
    """
    Password generation params.
    """

    length: int
    """
    Length of the password to generate (between 1 and 1024).
    """

    no_lowercase_letters: bool
    """
    Do not include lower case letters by default in the alphabet.
    """

    no_uppercase_letters: bool
    """
    Do not include upper case letters by default in the alphabet.
    """

    no_digits: bool
    """
    Do not include digits by default in the alphabet.
    """

    additional_chars: str
    """
    Additional ascii characters to be included in the alphabet.
    """


@dataclass
class Secret:
    """
    Secret.
    """

    id: str
    """
    ID of the secret.
    """

    project_id: str
    """
    ID of the Project containing the secret.
    """

    name: str
    """
    Name of the secret.
    """

    status: SecretStatus
    """
    Current status of the secret.
    * `ready`: the secret can be read, modified and deleted.
    * `locked`: no action can be performed on the secret. This status can only be applied and removed by Scaleway.
    """

    created_at: Optional[datetime]
    """
    Date and time of the secret's creation.
    """

    updated_at: Optional[datetime]
    """
    Last update of the secret.
    """

    tags: List[str]
    """
    List of the secret's tags.
    """

    version_count: int
    """
    Number of versions for this secret.
    """

    description: Optional[str]
    """
    Updated description of the secret.
    """

    is_managed: bool
    """
    Returns `true` for secrets that are managed by another product.
    """

    is_protected: bool
    """
    Returns `true` for protected secrets that cannot be deleted.
    """

    type_: SecretType
    """
    Type of the secret.
    See `Secret.Type` enum for description of values.
    """

    path: str
    """
    Path of the secret.
    Location of the secret in the directory structure.
    """

    ephemeral_policy: Optional[EphemeralPolicy]
    """
    Ephemeral policy of the secret.
    (Optional.) Policy that defines whether/when a secret's versions expire. By default, the policy is applied to all the secret's versions.
    """

    region: Region
    """
    Region of the secret.
    """


@dataclass
class SecretVersion:
    """
    Secret version.
    """

    revision: int
    """
    Version number.
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1.
    """

    secret_id: str
    """
    ID of the secret.
    """

    status: SecretVersionStatus
    """
    Current status of the version.
    * `unknown`: the version is in an invalid state.
    * `enabled`: the version is accessible.
    * `disabled`: the version is not accessible but can be enabled.
    * `destroyed`: the version is permanently deleted. It is not possible to recover it.
    """

    created_at: Optional[datetime]
    """
    Date and time of the version's creation.
    """

    updated_at: Optional[datetime]
    """
    Last update of the version.
    """

    description: Optional[str]
    """
    Description of the version.
    """

    is_latest: bool
    """
    Returns `true` if the version is the latest.
    """

    ephemeral_properties: Optional[EphemeralProperties]
    """
    Properties of the ephemeral version.
    Returns the version's expiration date, whether it expires after being accessed once, and the action to perform (disable or delete) once the version expires.
    """


@dataclass
class CreateSecretRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project containing the secret.
    """

    name: str
    """
    Name of the secret.
    """

    tags: Optional[List[str]]
    """
    List of the secret's tags.
    """

    description: Optional[str]
    """
    Description of the secret.
    """

    type_: SecretType
    """
    Type of the secret.
    (Optional.) See `Secret.Type` enum for description of values. If not specified, the type is `Opaque`.
    """

    path: Optional[str]
    """
    Path of the secret.
    (Optional.) Location of the secret in the directory structure. If not specified, the path is `/`.
    """

    ephemeral_policy: Optional[EphemeralPolicy]
    """
    Ephemeral policy of the secret.
    (Optional.) Policy that defines whether/when a secret's versions expire. By default, the policy is applied to all the secret's versions.
    """

    is_protected: bool
    """
    Returns `true` if secret protection is enabled on a given secret.
    A protected secret cannot be deleted.
    """


@dataclass
class CreateFolderRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project containing the folder.
    """

    name: str
    """
    Name of the folder.
    """

    path: Optional[str]
    """
    Path of the folder.
    (Optional.) Location of the folder in the directory structure. If not specified, the path is `/`.
    """


@dataclass
class GetSecretRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """


@dataclass
class GetSecretByNameRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_name: str
    """
    Name of the secret.
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    (Optional.) If not specified, Secret Manager will look for the secret in all Projects.
    """


@dataclass
class UpdateSecretRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    name: Optional[str]
    """
    Secret's updated name (optional).
    """

    tags: Optional[List[str]]
    """
    Secret's updated list of tags (optional).
    """

    description: Optional[str]
    """
    Description of the secret.
    """

    path: Optional[str]
    """
    Path of the folder.
    (Optional.) Location of the folder in the directory structure. If not specified, the path is `/`.
    """

    ephemeral_policy: Optional[EphemeralPolicy]
    """
    Ephemeral policy of the secret.
    (Optional.) Policy that defines whether/when a secret's versions expire.
    """


@dataclass
class ListSecretsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID (optional).
    """

    project_id: Optional[str]
    """
    Filter by Project ID (optional).
    """

    order_by: Optional[ListSecretsRequestOrderBy]

    page: Optional[int]

    page_size: Optional[int]

    tags: Optional[List[str]]
    """
    List of tags to filter on (optional).
    """

    name: Optional[str]
    """
    Filter by secret name (optional).
    """

    is_managed: Optional[bool]
    """
    Filter by managed / not managed (optional).
    """

    path: Optional[str]
    """
    Filter by path (optional).
    """

    is_ephemeral: Optional[bool]
    """
    Filter by ephemeral / not ephemeral (optional).
    """


@dataclass
class ListFoldersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Filter by Project ID (optional).
    """

    path: Optional[str]
    """
    Filter by path (optional).
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListFoldersRequestOrderBy]


@dataclass
class DeleteSecretRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """


@dataclass
class DeleteFolderRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    folder_id: str
    """
    ID of the folder.
    """


@dataclass
class ProtectSecretRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret to protect.
    """


@dataclass
class UnprotectSecretRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret to unprotect.
    """


@dataclass
class AddSecretOwnerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    product_name: Optional[str]
    """
    (Deprecated: use `product` field) Name of the product to add.
    :deprecated
    """

    product: Product
    """
    ID of the product to add.
    See `Product` enum for description of values.
    """


@dataclass
class CreateSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    data: str
    """
    The base64-encoded secret payload of the version.
    """

    description: Optional[str]
    """
    Description of the version.
    """

    disable_previous: Optional[bool]
    """
    Disable the previous secret version.
    (Optional.) If there is no previous version or if the previous version was already disabled, does nothing.
    """

    password_generation: Optional[PasswordGenerationParams]
    """
    Options to generate a password.
    (Optional.) If specified, a random password will be generated. The `data` and `data_crc32` fields must be empty. By default, the generator will use upper and lower case letters, and digits. This behavior can be tuned using the generation parameters.
    
    One-of ('_password_generation'): at most one of 'password_generation' could be set.
    :deprecated
    """

    data_crc32: Optional[int]
    """
    (Optional.) The CRC32 checksum of the data as a base-10 integer.
    If specified, Secret Manager will verify the integrity of the data received against the given CRC32 checksum. An error is returned if the CRC32 does not match. If, however, the CRC32 matches, it will be stored and returned along with the SecretVersion on future access requests.
    """


@dataclass
class GeneratePasswordRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    description: Optional[str]
    """
    Description of the version.
    """

    disable_previous: Optional[bool]
    """
    (Optional.) Disable the previous secret version.
    This has no effect if there is no previous version or if the previous version was already disabled.
    """

    length: int
    """
    Length of the password to generate (between 1 and 1024 characters).
    """

    no_lowercase_letters: Optional[bool]
    """
    (Optional.) Exclude lower case letters by default in the password character set.
    """

    no_uppercase_letters: Optional[bool]
    """
    (Optional.) Exclude upper case letters by default in the password character set.
    """

    no_digits: Optional[bool]
    """
    (Optional.) Exclude digits by default in the password character set.
    """

    additional_chars: Optional[str]
    """
    (Optional.) Additional ASCII characters to be included in the password character set.
    """


@dataclass
class GetSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    Version number.
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
    - a number (the revision number)
    - "latest" (the latest revision)
    - "latest_enabled" (the latest enabled revision).
    """


@dataclass
class GetSecretVersionByNameRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_name: str
    """
    Name of the secret.
    """

    revision: str
    """
    Version number.
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
    - a number (the revision number)
    - "latest" (the latest revision)
    - "latest_enabled" (the latest enabled revision).
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    (Optional.) If not specified, Secret Manager will look for the secret version in all Projects.
    """


@dataclass
class UpdateSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    Version number.
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
    - a number (the revision number)
    - "latest" (the latest revision)
    - "latest_enabled" (the latest enabled revision).
    """

    description: Optional[str]
    """
    Description of the version.
    """

    ephemeral_properties: Optional[EphemeralProperties]
    """
    Ephemeral properties of the version.
    (Optional.) Properties that defines the version's expiration date, whether it expires after being accessed once, and the action to perform (disable or delete) once the version expires.
    """


@dataclass
class ListSecretVersionsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    page: Optional[int]

    page_size: Optional[int]

    status: Optional[List[SecretVersionStatus]]
    """
    Filter results by status.
    """


@dataclass
class ListSecretVersionsByNameRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_name: str
    """
    Name of the secret.
    """

    page: Optional[int]

    page_size: Optional[int]

    status: Optional[List[SecretVersionStatus]]
    """
    Filter results by status.
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    (Optional.) If not specified, Secret Manager will look for the secret in all Projects.
    """


@dataclass
class EnableSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    Version number.
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
    - a number (the revision number)
    - "latest" (the latest revision)
    - "latest_enabled" (the latest enabled revision).
    """


@dataclass
class DisableSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    Version number.
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
    - a number (the revision number)
    - "latest" (the latest revision)
    - "latest_enabled" (the latest enabled revision).
    """


@dataclass
class AccessSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    Version number.
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
    - a number (the revision number)
    - "latest" (the latest revision)
    - "latest_enabled" (the latest enabled revision).
    """


@dataclass
class AccessSecretVersionByNameRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_name: str
    """
    Name of the secret.
    """

    revision: str
    """
    Version number.
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
    - a number (the revision number)
    - "latest" (the latest revision)
    - "latest_enabled" (the latest enabled revision).
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    (Optional.) If not specified, Secret Manager will look for the secret version in all Projects.
    """


@dataclass
class DestroySecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    Version number.
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
    - a number (the revision number)
    - "latest" (the latest revision)
    - "latest_enabled" (the latest enabled revision).
    """


@dataclass
class ListTagsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    (Optional.) If not specified, Secret Manager will look for tags in all Projects.
    """

    page: Optional[int]

    page_size: Optional[int]
