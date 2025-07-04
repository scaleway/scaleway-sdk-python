# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ListNatsAccountsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListNatsCredentialsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSnsCredentialsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSqsCredentialsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class SnsInfoStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ENABLED = "enabled"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)


class SqsInfoStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    ENABLED = "enabled"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class File:
    name: str
    """
    File name.
    """

    content: str
    """
    File content.
    """


@dataclass
class SnsPermissions:
    can_publish: Optional[bool]
    """
    Defines whether the credentials bearer can publish messages to the service (publish to Topics and Events topics).
    """

    can_receive: Optional[bool]
    """
    Defines whether the credentials bearer can receive messages from the service (configure subscriptions).
    """

    can_manage: Optional[bool]
    """
    Defines whether the credentials bearer can manage the associated Topics and Events topics or subscriptions.
    """


@dataclass
class SqsPermissions:
    can_publish: Optional[bool]
    """
    Defines whether the credentials bearer can publish messages to the service (send messages to Queues queues).
    """

    can_receive: Optional[bool]
    """
    Defines whether the credentials bearer can receive messages from Queues queues.
    """

    can_manage: Optional[bool]
    """
    Defines whether the credentials bearer can manage the associated Queues queues.
    """


@dataclass
class NatsAccount:
    id: str
    """
    NATS account ID.
    """

    name: str
    """
    NATS account name.
    """

    endpoint: str
    """
    Endpoint of the NATS service for this account.
    """

    project_id: str
    """
    Project ID of the Project containing the NATS account.
    """

    region: ScwRegion
    """
    Region where the NATS account is deployed.
    """

    created_at: Optional[datetime]
    """
    NATS account creation date.
    """

    updated_at: Optional[datetime]
    """
    NATS account last modification date.
    """


@dataclass
class NatsCredentials:
    id: str
    """
    ID of the credentials.
    """

    name: str
    """
    Name of the credentials.
    """

    nats_account_id: str
    """
    NATS account containing the credentials.
    """

    checksum: str
    """
    Checksum of the credentials file.
    """

    created_at: Optional[datetime]
    """
    NATS credentials creation date.
    """

    updated_at: Optional[datetime]
    """
    NATS credentials last modification date.
    """

    credentials: Optional[File]
    """
    Object containing the credentials file (Only returned by **Create Nats Credentials** call).
    """


@dataclass
class SnsCredentials:
    id: str
    """
    ID of the credentials.
    """

    name: str
    """
    Name of the credentials.
    """

    project_id: str
    """
    Project ID of the Project containing the credentials.
    """

    region: ScwRegion
    """
    Region where the credentials exists.
    """

    access_key: str
    """
    Access key ID.
    """

    secret_key: str
    """
    Secret key ID (Only returned by **Create Topics and Events Credentials** call).
    """

    secret_checksum: str
    """
    Checksum of the Secret key.
    """

    created_at: Optional[datetime]
    """
    Credentials creation date.
    """

    updated_at: Optional[datetime]
    """
    Credentials last modification date.
    """

    permissions: Optional[SnsPermissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class SqsCredentials:
    id: str
    """
    ID of the credentials.
    """

    name: str
    """
    Name of the credentials.
    """

    project_id: str
    """
    Project ID of the Project containing the credentials.
    """

    region: ScwRegion
    """
    Region where the credentials exists.
    """

    access_key: str
    """
    Access key ID.
    """

    secret_key: str
    """
    Secret key ID (Only returned by **Create Queues Credentials** call).
    """

    secret_checksum: str
    """
    Checksum of the Secret key.
    """

    created_at: Optional[datetime]
    """
    Credentials creation date.
    """

    updated_at: Optional[datetime]
    """
    Credentials last modification date.
    """

    permissions: Optional[SqsPermissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class ListNatsAccountsResponse:
    total_count: int
    """
    Total count of existing NATS accounts (matching any filters specified).
    """

    nats_accounts: List[NatsAccount]
    """
    NATS accounts on this page.
    """


@dataclass
class ListNatsCredentialsResponse:
    total_count: int
    """
    Total count of existing credentials (matching any filters specified).
    """

    nats_credentials: List[NatsCredentials]
    """
    Credentials on this page.
    """


@dataclass
class ListSnsCredentialsResponse:
    total_count: int
    """
    Total count of existing credentials (matching any filters specified).
    """

    sns_credentials: List[SnsCredentials]
    """
    Topics and Events credentials on this page.
    """


@dataclass
class ListSqsCredentialsResponse:
    total_count: int
    """
    Total count of existing credentials (matching any filters specified).
    """

    sqs_credentials: List[SqsCredentials]
    """
    Queues credentials on this page.
    """


@dataclass
class NatsApiCreateNatsAccountRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    NATS account name.
    """

    project_id: Optional[str]
    """
    Project containing the NATS account.
    """


@dataclass
class NatsApiCreateNatsCredentialsRequest:
    nats_account_id: str
    """
    NATS account containing the credentials.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the credentials.
    """


@dataclass
class NatsApiDeleteNatsAccountRequest:
    nats_account_id: str
    """
    ID of the NATS account to delete.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class NatsApiDeleteNatsCredentialsRequest:
    nats_credentials_id: str
    """
    ID of the credentials to delete.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class NatsApiGetNatsAccountRequest:
    nats_account_id: str
    """
    ID of the NATS account to get.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class NatsApiGetNatsCredentialsRequest:
    nats_credentials_id: str
    """
    ID of the credentials to get.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class NatsApiListNatsAccountsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Include only NATS accounts in this Project.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of NATS accounts to return per page.
    """

    order_by: Optional[ListNatsAccountsRequestOrderBy]
    """
    Order in which to return results.
    """


@dataclass
class NatsApiListNatsCredentialsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Include only NATS accounts in this Project.
    """

    nats_account_id: Optional[str]
    """
    Include only credentials for this NATS account.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of credentials to return per page.
    """

    order_by: Optional[ListNatsCredentialsRequestOrderBy]
    """
    Order in which to return results.
    """


@dataclass
class NatsApiUpdateNatsAccountRequest:
    nats_account_id: str
    """
    ID of the NATS account to update.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    NATS account name.
    """


@dataclass
class SnsApiActivateSnsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project on which to activate the Topics and Events service.
    """


@dataclass
class SnsApiCreateSnsCredentialsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project containing the Topics and Events credentials.
    """

    name: Optional[str]
    """
    Name of the credentials.
    """

    permissions: Optional[SnsPermissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class SnsApiDeactivateSnsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project on which to deactivate the Topics and Events service.
    """


@dataclass
class SnsApiDeleteSnsCredentialsRequest:
    sns_credentials_id: str
    """
    ID of the credentials to delete.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class SnsApiGetSnsCredentialsRequest:
    sns_credentials_id: str
    """
    ID of the Topics and Events credentials to get.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class SnsApiGetSnsInfoRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project to retrieve Topics and Events info from.
    """


@dataclass
class SnsApiListSnsCredentialsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Include only Topics and Events credentials in this Project.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of credentials to return per page.
    """

    order_by: Optional[ListSnsCredentialsRequestOrderBy]
    """
    Order in which to return results.
    """


@dataclass
class SnsApiUpdateSnsCredentialsRequest:
    sns_credentials_id: str
    """
    ID of the Topics and Events credentials to update.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the credentials.
    """

    permissions: Optional[SnsPermissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class SnsInfo:
    project_id: str
    """
    Project ID of the Project containing the service.
    """

    region: ScwRegion
    """
    Region of the service.
    """

    status: SnsInfoStatus
    """
    Topics and Events activation status.
    """

    sns_endpoint_url: str
    """
    Endpoint of the Topics and Events service for this region and project.
    """

    created_at: Optional[datetime]
    """
    Topics and Events creation date.
    """

    updated_at: Optional[datetime]
    """
    Topics and Events last modification date.
    """


@dataclass
class SqsApiActivateSqsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project on which to activate the Queues service.
    """


@dataclass
class SqsApiCreateSqsCredentialsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project containing the Queues credentials.
    """

    name: Optional[str]
    """
    Name of the credentials.
    """

    permissions: Optional[SqsPermissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class SqsApiDeactivateSqsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project on which to deactivate the Queues service.
    """


@dataclass
class SqsApiDeleteSqsCredentialsRequest:
    sqs_credentials_id: str
    """
    ID of the credentials to delete.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class SqsApiGetSqsCredentialsRequest:
    sqs_credentials_id: str
    """
    ID of the Queues credentials to get.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class SqsApiGetSqsInfoRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Project to retrieve Queues info from.
    """


@dataclass
class SqsApiListSqsCredentialsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    Include only Queues credentials in this Project.
    """

    page: Optional[int]
    """
    Page number to return.
    """

    page_size: Optional[int]
    """
    Maximum number of credentials to return per page.
    """

    order_by: Optional[ListSqsCredentialsRequestOrderBy]
    """
    Order in which to return results.
    """


@dataclass
class SqsApiUpdateSqsCredentialsRequest:
    sqs_credentials_id: str
    """
    ID of the Queues credentials to update.
    """

    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the credentials.
    """

    permissions: Optional[SqsPermissions]
    """
    Permissions associated with these credentials.
    """


@dataclass
class SqsInfo:
    project_id: str
    """
    Project ID of the Project containing the service.
    """

    region: ScwRegion
    """
    Region of the service.
    """

    status: SqsInfoStatus
    """
    Queues activation status.
    """

    sqs_endpoint_url: str
    """
    Endpoint of the Queues service for this region and project.
    """

    created_at: Optional[datetime]
    """
    Queues creation date.
    """

    updated_at: Optional[datetime]
    """
    Queues last modification date.
    """
