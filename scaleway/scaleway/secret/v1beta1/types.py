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


class BrowseSecretsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class EphemeralPolicyAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
    DELETE = "delete"
    DISABLE = "disable"

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
    UNKNOWN_PRODUCT = "unknown_product"
    EDGE_SERVICES = "edge_services"

    def __str__(self) -> str:
        return str(self.value)


class SecretStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class SecretType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    OPAQUE = "opaque"
    CERTIFICATE = "certificate"
    KEY_VALUE = "key_value"
    BASIC_CREDENTIALS = "basic_credentials"
    DATABASE_CREDENTIALS = "database_credentials"
    SSH_KEY = "ssh_key"

    def __str__(self) -> str:
        return str(self.value)


class SecretVersionStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ENABLED = "enabled"
    DISABLED = "disabled"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class EphemeralPolicy:
    action: EphemeralPolicyAction
    """
    See the `EphemeralPolicy.Action` enum for a description of values.
    """

    time_to_live: Optional[str]
    """
    Time frame, from one second and up to one year, during which the secret's versions are valid.
    """

    expires_once_accessed: Optional[bool]
    """
    Returns `true` if the version expires after a single user access.
    """


@dataclass
class BrowseSecretsResponseItemFolderDetails:
    pass


@dataclass
class BrowseSecretsResponseItemSecretDetails:
    id: str

    tags: List[str]

    version_count: int

    protected: bool

    type_: SecretType

    ephemeral_policy: Optional[EphemeralPolicy]


@dataclass
class EphemeralProperties:
    action: EphemeralPolicyAction
    """
    See `EphemeralPolicy.Action` enum for a description of values.
    """

    expires_at: Optional[datetime]
    """
    (Optional.) If not specified, the version does not have an expiration date.
    """

    expires_once_accessed: Optional[bool]
    """
    (Optional.) If not specified, the version can be accessed an unlimited amount of times.
    """


@dataclass
class BrowseSecretsResponseItem:
    name: str

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    secret: Optional[BrowseSecretsResponseItemSecretDetails]

    folder: Optional[BrowseSecretsResponseItemFolderDetails]


@dataclass
class SecretVersion:
    revision: int
    """
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1.
    """

    secret_id: str
    """
    ID of the secret.
    """

    status: SecretVersionStatus
    """
    * `unknown_status`: the version is in an invalid state.
* `enabled`: the version is accessible.
* `disabled`: the version is not accessible but can be enabled.
* `deleted`: the version is permanently deleted. It is not possible to recover it.
    """

    latest: bool
    """
    Returns `true` if the version is the latest.
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

    ephemeral_properties: Optional[EphemeralProperties]
    """
    Returns the version's expiration date, whether it expires after being accessed once, and the action to perform (disable or delete) once the version expires.
    """


@dataclass
class Secret:
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
    * `ready`: the secret can be read, modified and deleted.
* `locked`: no action can be performed on the secret. This status can only be applied and removed by Scaleway.
    """

    tags: List[str]
    """
    List of the secret's tags.
    """

    version_count: int
    """
    Number of versions for this secret.
    """

    managed: bool
    """
    Returns `true` for secrets that are managed by another product.
    """

    protected: bool
    """
    Returns `true` for protected secrets that cannot be deleted.
    """

    type_: SecretType
    """
    See the `Secret.Type` enum for a description of values.
    """

    path: str
    """
    Location of the secret in the directory structure.
    """

    used_by: List[Product]
    """
    List of Scaleway resources that can access and manage the secret.
    """

    region: Region
    """
    Region of the secret.
    """

    created_at: Optional[datetime]
    """
    Date and time of the secret's creation.
    """

    updated_at: Optional[datetime]
    """
    Last update of the secret.
    """

    description: Optional[str]
    """
    Updated description of the secret.
    """

    ephemeral_policy: Optional[EphemeralPolicy]
    """
    (Optional.) Policy that defines whether/when a secret's versions expire. By default, the policy is applied to all the secret's versions.
    """


@dataclass
class AccessSecretVersionByPathRequest:
    secret_path: str
    """
    Secret's path.
    """

    secret_name: str
    """
    Secret's name.
    """

    revision: str
    """
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
- an integer (the revision number)
- "latest" (the latest revision)
- "latest_enabled" (the latest enabled revision).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    """


@dataclass
class AccessSecretVersionRequest:
    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
- a number (the revision number)
- "latest" (the latest revision)
- "latest_enabled" (the latest enabled revision).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class AccessSecretVersionResponse:
    secret_id: str
    """
    ID of the secret.
    """

    revision: int
    """
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1.
    """

    data: str
    """
    The base64-encoded secret payload of the version.
    """

    type_: SecretType
    """
    See the `Secret.Type` enum for a description of values.
    """

    data_crc32: Optional[int]
    """
    This field is only available if a CRC32 was supplied during the creation of the version.
    """


@dataclass
class AddSecretOwnerRequest:
    secret_id: str
    """
    ID of the secret.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    product: Optional[Product]
    """
    See `Product` enum for description of values.
    """


@dataclass
class BasicCredentials:
    username: str
    """
    The username or identifier associated with the credentials.
    """

    password: str
    """
    The password associated with the credentials.
    """


@dataclass
class BrowseSecretsRequest:
    prefix: str
    """
    Filter secrets and folders for a given prefix (default /).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Filter by Project ID (optional).
    """

    order_by: Optional[BrowseSecretsRequestOrderBy]

    page: Optional[int]

    page_size: Optional[int]

    tags: Optional[List[str]]
    """
    Filter secrets by tags.
    """

    type_: Optional[SecretType]
    """
    Filter by secret type (optional).
    """


@dataclass
class BrowseSecretsResponse:
    items: List[BrowseSecretsResponseItem]
    """
    Repeated item of type secret or folder, sorted by the request parameter.
    """

    current_path: str
    """
    Current path for the given prefix.
    """

    total_count: int
    """
    Count of all secrets and folders matching the requested criteria.
    """


@dataclass
class CreateSecretRequest:
    name: str
    """
    Name of the secret.
    """

    protected: bool
    """
    A protected secret cannot be deleted.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project containing the secret.
    """

    tags: Optional[List[str]]
    """
    List of the secret's tags.
    """

    description: Optional[str]
    """
    Description of the secret.
    """

    type_: Optional[SecretType]
    """
    (Optional.) See the `Secret.Type` enum for a description of values. If not specified, the type is `Opaque`.
    """

    path: Optional[str]
    """
    (Optional.) Location of the secret in the directory structure. If not specified, the path is `/`.
    """

    ephemeral_policy: Optional[EphemeralPolicy]
    """
    (Optional.) Policy that defines whether/when a secret's versions expire. By default, the policy is applied to all the secret's versions.
    """


@dataclass
class CreateSecretVersionRequest:
    secret_id: str
    """
    ID of the secret.
    """

    data: str
    """
    The base64-encoded secret payload of the version.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str]
    """
    Description of the version.
    """

    disable_previous: Optional[bool]
    """
    (Optional.) If there is no previous version or if the previous version was already disabled, does nothing.
    """

    data_crc32: Optional[int]
    """
    If specified, Secret Manager will verify the integrity of the data received against the given CRC32 checksum. An error is returned if the CRC32 does not match. If, however, the CRC32 matches, it will be stored and returned along with the SecretVersion on future access requests.
    """


@dataclass
class DatabaseCredentials:
    engine: str
    """
    Supported database engines are: 'postgres', 'mysql', 'other'.
    """

    username: str
    """
    The username used to authenticate to the database server.
    """

    password: str
    """
    The password used to authenticate to the database server.
    """

    host: str
    """
    The hostname or resolvable DNS name of the database server.
    """

    dbname: str
    """
    The name of the database to connect to.
    """

    port: str
    """
    The port must be an integer ranging from 0 to 65535.
    """


@dataclass
class DeleteSecretRequest:
    secret_id: str
    """
    ID of the secret.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteSecretVersionRequest:
    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
- a number (the revision number)
- "latest" (the latest revision)
- "latest_enabled" (the latest enabled revision).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DisableSecretVersionRequest:
    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
- a number (the revision number)
- "latest" (the latest revision)
- "latest_enabled" (the latest enabled revision).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class EnableSecretVersionRequest:
    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
- a number (the revision number)
- "latest" (the latest revision)
- "latest_enabled" (the latest enabled revision).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetSecretRequest:
    secret_id: str
    """
    ID of the secret.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetSecretVersionRequest:
    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
- a number (the revision number)
- "latest" (the latest revision)
- "latest_enabled" (the latest enabled revision).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListSecretTypesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the Project to target.
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListSecretTypesResponse:
    types: List[SecretType]
    """
    List of secret types.
    """

    total_count: int
    """
    Count of all secret types matching the requested criteria.
    """


@dataclass
class ListSecretVersionsRequest:
    secret_id: str
    """
    ID of the secret.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    status: Optional[List[SecretVersionStatus]]
    """
    Filter results by status.
    """


@dataclass
class ListSecretVersionsResponse:
    versions: List[SecretVersion]
    """
    Single page of versions.
    """

    total_count: int
    """
    Number of versions.
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

    path: Optional[str]
    """
    Filter by exact path (optional).
    """

    ephemeral: Optional[bool]
    """
    Filter by ephemeral / not ephemeral (optional).
    """

    type_: Optional[SecretType]
    """
    Filter by secret type (optional).
    """


@dataclass
class ListSecretsResponse:
    secrets: List[Secret]
    """
    Single page of secrets matching the requested criteria.
    """

    total_count: int
    """
    Count of all secrets matching the requested criteria.
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
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class ListTagsResponse:
    tags: List[str]
    """
    List of tags.
    """

    total_count: int
    """
    Count of all tags matching the requested criteria.
    """


@dataclass
class ProtectSecretRequest:
    secret_id: str
    """
    ID of the secret to enable secret protection for.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class SSHKey:
    ssh_private_key: str
    """
    The private SSH key.
    """


@dataclass
class UnprotectSecretRequest:
    secret_id: str
    """
    ID of the secret to disable secret protection for.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class UpdateSecretRequest:
    secret_id: str
    """
    ID of the secret.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
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
    (Optional.) Location of the folder in the directory structure. If not specified, the path is `/`.
    """

    ephemeral_policy: Optional[EphemeralPolicy]
    """
    (Optional.) Policy that defines whether/when a secret's versions expire.
    """


@dataclass
class UpdateSecretVersionRequest:
    secret_id: str
    """
    ID of the secret.
    """

    revision: str
    """
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
- a number (the revision number)
- "latest" (the latest revision)
- "latest_enabled" (the latest enabled revision).
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    description: Optional[str]
    """
    Description of the version.
    """

    ephemeral_properties: Optional[EphemeralProperties]
    """
    (Optional.) Properties that defines the version's expiration date, whether it expires after being accessed once, and the action to perform (disable or delete) once the version expires.
    """
