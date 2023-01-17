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
    Access secret version response
    """

    secret_id: str
    """
    ID of the Secret
    """

    revision: int
    """
    Revision of the SecretVersion
    """

    data: str
    """
    The base64-encoded secret payload of the SecretVersion
    """


@dataclass
class ListSecretVersionsResponse:
    """
    List secret versions response
    """

    total_count: int
    """
    Count of all SecretVersions
    """

    versions: List[SecretVersion]
    """
    Single page of SecretVersions
    """


@dataclass
class ListSecretsResponse:
    """
    List secrets response
    """

    total_count: int
    """
    Count of all Secrets matching the requested criteria
    """

    secrets: List[Secret]
    """
    Single page of Secrets matching the requested criteria
    """


@dataclass
class Secret:
    """
    Secret
    """

    id: str
    """
    ID of the Secret
    """

    project_id: str
    """
    ID of the project containing the Secret
    """

    name: str
    """
    Name of the Secret
    """

    status: SecretStatus
    """
    * `ready`: the Secret is ready.
    * `locked`: the Secret is locked.
    
    """

    created_at: Optional[datetime]
    """
    The time at which the Secret was created
    """

    updated_at: Optional[datetime]
    """
    The time at which the Secret was updated
    """

    tags: List[str]
    """
    List of tags associated to this Secret
    """

    region: Region
    """
    Region of the Secret
    """

    version_count: int
    """
    The number of versions for this Secret
    """

    description: Optional[str]
    """
    Description of the Secret
    """


@dataclass
class SecretVersion:
    """
    Secret version
    """

    secret_id: str
    """
    ID of the Secret
    """

    revision: int
    """
    Revision of the SecretVersion
    """

    status: SecretVersionStatus
    """
    * `unknown`: the SecretVersion is in an invalid state.
    * `enabled`: the SecretVersion is accessible.
    * `disabled`: the SecretVersion is not accessible but can be enabled.
    * `destroyed`: the SecretVersion is permanently destroyed.
    
    """

    created_at: Optional[datetime]
    """
    The time at which the SecretVersion was created
    """

    updated_at: Optional[datetime]
    """
    The time at which the SecretVersion was updated
    """

    description: Optional[str]
    """
    Description of the SecretVersion
    """


@dataclass
class CreateSecretRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    project_id: Optional[str]
    """
    ID of the project containing the Secret
    """

    name: str
    """
    Name of the Secret
    """

    tags: Optional[List[str]]
    """
    List of tags associated to this Secret
    """

    description: Optional[str]
    """
    Description of the Secret
    """


@dataclass
class GetSecretRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """


@dataclass
class UpdateSecretRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """

    name: Optional[str]
    """
    New name of the Secret (optional)
    """

    tags: Optional[List[str]]
    """
    New list of tags associated to this Secret (optional)
    """

    description: Optional[str]
    """
    Description of the Secret
    """


@dataclass
class ListSecretsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    organization_id: Optional[str]
    """
    ID of an organization to filter on (optional)
    """

    project_id: Optional[str]
    """
    ID of a project to filter on (optional)
    """

    tags: Optional[List[str]]
    """
    List of tags to filter on (optional)
    """

    order_by: Optional[ListSecretsRequestOrderBy]

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class DeleteSecretRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """


@dataclass
class CreateSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """

    data: str
    """
    The base64-encoded secret payload of the SecretVersion
    """

    description: Optional[str]
    """
    Description of the SecretVersion
    """


@dataclass
class GetSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """

    revision: str
    """
    Revision of the SecretVersion (may be a number or "latest")
    """


@dataclass
class UpdateSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """

    revision: str
    """
    Revision of the SecretVersion (may be a number or "latest")
    """

    description: Optional[str]
    """
    Description of the SecretVersion
    """


@dataclass
class ListSecretVersionsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """

    page: Optional[int]

    page_size: Optional[int]


@dataclass
class DestroySecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """

    revision: str
    """
    Revision of the SecretVersion (may be a number or "latest")
    """


@dataclass
class EnableSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """

    revision: str
    """
    Revision of the SecretVersion (may be a number or "latest")
    """


@dataclass
class DisableSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """

    revision: str
    """
    Revision of the SecretVersion (may be a number or "latest")
    """


@dataclass
class AccessSecretVersionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    secret_id: str
    """
    ID of the Secret
    """

    revision: str
    """
    Revision of the SecretVersion (may be a number or "latest")
    """
