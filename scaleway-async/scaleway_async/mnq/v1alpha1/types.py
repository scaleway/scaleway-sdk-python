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


class ListCredentialsRequestOrderBy(str, Enum):
    ID_ASC = "id_asc"
    ID_DESC = "id_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListNamespacesRequestOrderBy(str, Enum):
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


class NamespaceProtocol(str, Enum):
    UNKNOWN = "unknown"
    NATS = "nats"
    SQS_SNS = "sqs_sns"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Credential:
    """
    Credential.
    """

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
    """
    Object containing the credentials, if the credentials are for a NATS namespace.
    
    One-of ('credential_type'): at most one of 'nats_credentials', 'sqs_sns_credentials' could be set.
    """

    sqs_sns_credentials: Optional[CredentialSQSSNSCreds]
    """
    Object containing the credentials and their metadata, if the credentials are for an SQS/SNS namespace.
    
    One-of ('credential_type'): at most one of 'nats_credentials', 'sqs_sns_credentials' could be set.
    """


@dataclass
class CredentialNATSCredsFile:
    """
    Credential.nats creds file.
    """

    content: str
    """
    Raw content of the NATS credentials file.
    """


@dataclass
class CredentialSQSSNSCreds:
    """
    Credential.sqssns creds.
    """

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
    """
    Credential summary.
    """

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
    """
    Object containing the credentials and their metadata, if the credentials are for an SQS/SNS namespace.
    
    One-of ('credential_type'): at most one of 'sqs_sns_credentials' could be set.
    """


@dataclass
class CredentialSummarySQSSNSCreds:
    """
    Credential summary.sqssns creds.
    """

    access_key: str
    """
    Access key ID.
    """

    permissions: Optional[Permissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class ListCredentialsResponse:
    """
    List credentials response.
    """

    total_count: int
    """
    Total count of existing credentials (matching any filters specified).
    """

    credentials: List[CredentialSummary]
    """
    Credentials on this page.
    """


@dataclass
class ListNamespacesResponse:
    """
    List namespaces response.
    """

    total_count: int
    """
    Total count of existing namespaces (matching any filters specified).
    """

    namespaces: List[Namespace]
    """
    Namespaces on this page.
    """


@dataclass
class Namespace:
    """
    Namespace.
    """

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
class Permissions:
    """
    Permissions.
    """

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
class CreateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Namespace name.
    """

    protocol: Optional[NamespaceProtocol]
    """
    Namespace protocol. You must specify a valid protocol (and not `unknown`) to avoid an error.
    """

    project_id: Optional[str]
    """
    Project containing the Namespace.
    """


@dataclass
class UpdateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    ID of the Namespace to update.
    """

    name: Optional[str]
    """
    Namespace name.
    """


@dataclass
class GetNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    ID of the Namespace to get.
    """


@dataclass
class DeleteNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    ID of the namespace to delete.
    """


@dataclass
class CreateCredentialRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str
    """
    Namespace containing the credentials.
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
class DeleteCredentialRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    credential_id: str
    """
    ID of the credentials to delete.
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
class UpdateCredentialRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    credential_id: str
    """
    ID of the credentials to update.
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
class GetCredentialRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    credential_id: str
    """
    ID of the credentials to get.
    """
