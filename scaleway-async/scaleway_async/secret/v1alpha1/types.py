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


class ListSecretsRequestOrderBy(str, Enum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class Product(str, Enum):
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)


class SecretStatus(str, Enum):
    READY = "ready"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)


class SecretVersionStatus(str, Enum):
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
    * `ready`: the secret is ready.
    * `locked`: the secret is locked.
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
    True for secrets that are managed by another product.
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
    (Deprecated: use product field) ID of the product to add (see product enum).
    :deprecated
    """

    product: Product
    """
    ID of the product to add (see product enum).
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
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
    """

    description: Optional[str]
    """
    Description of the version.
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
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
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
    The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be a number or "latest".
    """
