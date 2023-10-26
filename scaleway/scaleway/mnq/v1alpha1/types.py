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


class ListCredentialsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    ID_ASC = "id_asc"
    ID_DESC = "id_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListNamespacesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    ID_ASC = "id_asc"
    ID_DESC = "id_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    PROJECT_ID_ASC = "project_id_asc"
    PROJECT_ID_DESC = "project_id_desc"

    def __str__(self) -> str:
        return str(self.value)


class NamespaceProtocol(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    NATS = "nats"
    SQS_SNS = "sqs_sns"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Permissions:
    can_publish: Optional[bool]
    """
    Defines whether the credentials bearer can publish messages to the service (send messages to SQS queues or publish to SNS topics).
    """

    can_receive: Optional[bool]
    """
    Defines whether the credentials bearer can receive messages from the service.
    """

    can_manage: Optional[bool]
    """
    Defines whether the credentials bearer can manage the associated resources (SQS queues or SNS topics or subscriptions).
    """


@dataclass
class CredentialSummarySQSSNSCreds:
    access_key: str
    """
    Access key ID.
    """

    permissions: Optional[Permissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class CredentialNATSCredsFile:
    content: str
    """
    Raw content of the NATS credentials file.
    """


@dataclass
class CredentialSQSSNSCreds:
    access_key: str
    """
    Access key ID.
    """

    secret_key: Optional[str]
    """
    Secret key ID.
    """

    permissions: Optional[Permissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class CredentialSummary:
    id: str
    """
    ID of the credentials.
    """

    name: str
    """
    Name of the credentials.
    """

    namespace_id: str
    """
    Namespace containing the credentials.
    """

    protocol: NamespaceProtocol
    """
    Protocol associated with the credentials.
    """

    sqs_sns_credentials: Optional[CredentialSummarySQSSNSCreds]


@dataclass
class Namespace:
    id: str
    """
    Namespace ID.
    """

    name: str
    """
    Namespace name.
    """

    endpoint: str
    """
    Endpoint of the service matching the namespace's protocol.
    """

    protocol: NamespaceProtocol
    """
    Namespace protocol.
    """

    project_id: str
    """
    Project ID of the Project containing the namespace.
    """

    region: Region
    """
    Region where the namespace is deployed.
    """

    created_at: Optional[datetime]
    """
    Namespace creation date.
    """

    updated_at: Optional[datetime]
    """
    Namespace last modification date.
    """


@dataclass
class CreateCredentialRequest:
    namespace_id: str
    """
    Namespace containing the credentials.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the credentials.
    """

    permissions: Optional[Permissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class CreateNamespaceRequest:
    protocol: NamespaceProtocol
    """
    Namespace protocol. You must specify a valid protocol (and not `unknown`) to avoid an error.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Namespace name.
    """

    project_id: Optional[str]
    """
    Project containing the Namespace.
    """


@dataclass
class Credential:
    id: str
    """
    ID of the credentials.
    """

    name: str
    """
    Name of the credentials.
    """

    namespace_id: str
    """
    Namespace containing the credentials.
    """

    protocol: NamespaceProtocol
    """
    Protocol associated with the credentials.
    """

    nats_credentials: Optional[CredentialNATSCredsFile]

    sqs_sns_credentials: Optional[CredentialSQSSNSCreds]


@dataclass
class DeleteCredentialRequest:
    credential_id: str
    """
    ID of the credentials to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteNamespaceRequest:
    namespace_id: str
    """
    ID of the namespace to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetCredentialRequest:
    credential_id: str
    """
    ID of the credentials to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetNamespaceRequest:
    namespace_id: str
    """
    ID of the Namespace to get.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListCredentialsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: Optional[str]
    """
    Namespace containing the credentials.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of credentials to return per page.
    """

    order_by: Optional[ListCredentialsRequestOrderBy]
    """
    Order in which to return results.
    """


@dataclass
class ListCredentialsResponse:
    total_count: int
    """
    Total count of existing credentials (matching any filters specified).
    """

    credentials: List[CredentialSummary]
    """
    Credentials on this page.
    """


@dataclass
class ListNamespacesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    organization_id: Optional[str]
    """
    Include only namespaces in this Organization.
    """

    project_id: Optional[str]
    """
    Include only namespaces in this Project.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of namespaces to return per page.
    """

    order_by: Optional[ListNamespacesRequestOrderBy]
    """
    Order in which to return results.
    """


@dataclass
class ListNamespacesResponse:
    total_count: int
    """
    Total count of existing namespaces (matching any filters specified).
    """

    namespaces: List[Namespace]
    """
    Namespaces on this page.
    """


@dataclass
class UpdateCredentialRequest:
    credential_id: str
    """
    ID of the credentials to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the credentials.
    """

    permissions: Optional[Permissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class UpdateNamespaceRequest:
    namespace_id: str
    """
    ID of the Namespace to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Namespace name.
    """
