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
    Credential
    """

    id: str
    """
    Credential ID
    """

    name: str
    """
    Credential name
    """

    namespace_id: str
    """
    Namespace containing the Credential
    """

    protocol: NamespaceProtocol
    """
    Protocol associated to the Credential
    """

    nats_credentials: Optional[CredentialNATSCredsFile]
    """
    Credentials file used to connect to the NATS service.
    
    One-of ('credential_type'): at most one of 'nats_credentials', 'sqs_sns_credentials' could be set.
    """

    sqs_sns_credentials: Optional[CredentialSQSSNSCreds]
    """
    Credential used to connect to the SQS/SNS service.
    
    One-of ('credential_type'): at most one of 'nats_credentials', 'sqs_sns_credentials' could be set.
    """


@dataclass
class CredentialNATSCredsFile:
    """
    Credential.nats creds file
    """

    content: str
    """
    Raw content of the NATS credentials file
    """


@dataclass
class CredentialSQSSNSCreds:
    """
    Credential.sqssns creds
    """

    access_key: str
    """
    ID of the key
    """

    secret_key: Optional[str]
    """
    Secret value of the key
    """

    permissions: Optional[Permissions]
    """
    List of permissions associated to this Credential
    """


@dataclass
class CredentialSummary:
    """
    Credential summary
    """

    id: str
    """
    Credential ID
    """

    name: str
    """
    Credential name
    """

    namespace_id: str
    """
    Namespace containing the Credential
    """

    protocol: NamespaceProtocol
    """
    Protocol associated to the Credential
    """

    sqs_sns_credentials: Optional[CredentialSummarySQSSNSCreds]
    """
    Credential used to connect to the SQS/SNS service.
    
    One-of ('credential_type'): at most one of 'sqs_sns_credentials' could be set.
    """


@dataclass
class CredentialSummarySQSSNSCreds:
    """
    Credential summary.sqssns creds
    """

    access_key: str
    """
    ID of the key
    """

    permissions: Optional[Permissions]
    """
    List of permissions associated to this Credential
    """


@dataclass
class ListCredentialsResponse:
    """
    List credentials response
    """

    total_count: int
    """
    Total number of existing Credentials
    """

    credentials: List[CredentialSummary]
    """
    A page of Credentials
    """


@dataclass
class ListNamespacesResponse:
    """
    List namespaces response
    """

    total_count: int
    """
    Total number of existing Namespaces
    """

    namespaces: List[Namespace]
    """
    A page of Namespaces
    """


@dataclass
class Namespace:
    """
    Namespace
    """

    id: str
    """
    Namespace ID
    """

    name: str
    """
    Namespace name
    """

    endpoint: str
    """
    Endpoint of the service matching the Namespace protocol
    """

    protocol: NamespaceProtocol
    """
    Namespace protocol
    """

    project_id: str
    """
    Project containing the Namespace
    """

    region: Region
    """
    Region where the Namespace is deployed
    """

    created_at: Optional[datetime]
    """
    Namespace creation date
    """

    updated_at: Optional[datetime]
    """
    Namespace last modification date
    """


@dataclass
class Permissions:
    """
    Permissions
    """

    can_publish: Optional[bool]
    """
    Defines if user can publish messages to the service
    """

    can_receive: Optional[bool]
    """
    Defines if user can receive messages from the service
    """

    can_manage: Optional[bool]
    """
    Defines if user can manage the associated resource(s)
    """


@dataclass
class ListNamespacesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    organization_id: Optional[str]
    """
    Will list only the Namespaces owned by the specified organization
    """

    project_id: Optional[str]
    """
    Will list only the Namespaces contained into the specified project
    """

    page: Optional[int]
    """
    Indicate the page number of results to be returned
    """

    page_size: Optional[int]
    """
    Maximum number of results returned by page
    """

    order_by: Optional[ListNamespacesRequestOrderBy]
    """
    Field used for sorting results
    """


@dataclass
class CreateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    name: Optional[str]
    """
    Namespace name
    """

    protocol: Optional[NamespaceProtocol]
    """
    Namespace protocol
    """

    project_id: Optional[str]
    """
    Project containing the Namespace
    """


@dataclass
class UpdateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str
    """
    ID of the Namespace to update
    """

    name: Optional[str]
    """
    Namespace name
    """


@dataclass
class GetNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str
    """
    ID of the Namespace to get
    """


@dataclass
class DeleteNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str
    """
    ID of the Namespace to delete
    """


@dataclass
class CreateCredentialRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: str
    """
    Namespace containing the Credential
    """

    name: Optional[str]
    """
    Credential name
    """

    permissions: Optional[Permissions]
    """
    List of permissions associated to this Credential.
    
    One-of ('optional_permissions'): at most one of 'permissions' could be set.
    """


@dataclass
class DeleteCredentialRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    credential_id: str
    """
    ID of the Credential to delete
    """


@dataclass
class ListCredentialsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    namespace_id: Optional[str]
    """
    Namespace containing the Credential
    """

    page: Optional[int]
    """
    Indicate the page number of results to be returned
    """

    page_size: Optional[int]
    """
    Maximum number of results returned by page
    """

    order_by: Optional[ListCredentialsRequestOrderBy]
    """
    Field used for sorting results
    """


@dataclass
class UpdateCredentialRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    credential_id: str
    """
    ID of the Credential to update
    """

    name: Optional[str]
    """
    Credential name
    """

    permissions: Optional[Permissions]
    """
    List of permissions associated to this Credential.
    
    One-of ('optional_permissions'): at most one of 'permissions' could be set.
    """


@dataclass
class GetCredentialRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    credential_id: str
    """
    ID of the Credential to get
    """
