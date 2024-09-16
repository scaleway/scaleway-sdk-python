# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.utils import (
    StrEnumMeta,
)


class BearerType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_BEARER_TYPE = "unknown_bearer_type"
    USER = "user"
    APPLICATION = "application"

    def __str__(self) -> str:
        return str(self.value)


class ListAPIKeysRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    EXPIRES_AT_ASC = "expires_at_asc"
    EXPIRES_AT_DESC = "expires_at_desc"
    ACCESS_KEY_ASC = "access_key_asc"
    ACCESS_KEY_DESC = "access_key_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListApplicationsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListGroupsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListJWTsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListLogsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPermissionSetsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListPoliciesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    POLICY_NAME_ASC = "policy_name_asc"
    POLICY_NAME_DESC = "policy_name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListQuotaRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListSSHKeysRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListUsersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    EMAIL_ASC = "email_asc"
    EMAIL_DESC = "email_desc"
    LAST_LOGIN_ASC = "last_login_asc"
    LAST_LOGIN_DESC = "last_login_desc"

    def __str__(self) -> str:
        return str(self.value)


class LogAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
    CREATED = "created"
    UPDATED = "updated"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)


class LogResourceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RESOURCE_TYPE = "unknown_resource_type"
    API_KEY = "api_key"
    USER = "user"
    APPLICATION = "application"
    GROUP = "group"
    POLICY = "policy"

    def __str__(self) -> str:
        return str(self.value)


class PermissionSetScopeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SCOPE_TYPE = "unknown_scope_type"
    PROJECTS = "projects"
    ORGANIZATION = "organization"
    ACCOUNT_ROOT_USER = "account_root_user"

    def __str__(self) -> str:
        return str(self.value)


class UserStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    INVITATION_PENDING = "invitation_pending"
    ACTIVATED = "activated"

    def __str__(self) -> str:
        return str(self.value)


class UserType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    GUEST = "guest"
    OWNER = "owner"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class RuleSpecs:
    condition: str
    """
    Condition expression to evaluate.
    """

    permission_set_names: Optional[List[str]]
    """
    Names of permission sets bound to the rule.
    """

    project_ids: Optional[List[str]]

    organization_id: Optional[str]


@dataclass
class CreateUserRequestMember:
    email: str
    """
    Email of the user to create.
    """

    send_password_email: bool
    """
    Whether or not to send an email containing the member's password.
    """

    username: str
    """
    The member's username.
    """

    password: str
    """
    The member's password.
    """


@dataclass
class JWT:
    jti: str
    """
    JWT ID.
    """

    issuer_id: str
    """
    ID of the user who issued the JWT.
    """

    audience_id: str
    """
    ID of the user targeted by the JWT.
    """

    ip: str
    """
    IP address used during the creation of the JWT.
    """

    user_agent: str
    """
    User-agent used during the creation of the JWT.
    """

    created_at: Optional[datetime]
    """
    Creation date of the JWT.
    """

    updated_at: Optional[datetime]
    """
    Last update date of the JWT.
    """

    expires_at: Optional[datetime]
    """
    Expiration date of the JWT.
    """


@dataclass
class APIKey:
    access_key: str
    """
    Access key of the API key.
    """

    description: str
    """
    Description of API key.
    """

    default_project_id: str
    """
    Default Project ID specified for this API key.
    """

    editable: bool
    """
    Defines whether or not the API key is editable.
    """

    creation_ip: str
    """
    IP address of the device that created the API key.
    """

    secret_key: Optional[str]
    """
    Secret key of the API Key.
    """

    created_at: Optional[datetime]
    """
    Date and time of API key creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of last API key update.
    """

    expires_at: Optional[datetime]
    """
    Date and time of API key expiration.
    """

    application_id: Optional[str]

    user_id: Optional[str]


@dataclass
class Application:
    id: str
    """
    ID of the application.
    """

    name: str
    """
    Name of the application.
    """

    description: str
    """
    Description of the application.
    """

    organization_id: str
    """
    ID of the Organization.
    """

    editable: bool
    """
    Defines whether or not the application is editable.
    """

    nb_api_keys: int
    """
    Number of API keys attributed to the application.
    """

    tags: List[str]
    """
    Tags associated with the user.
    """

    created_at: Optional[datetime]
    """
    Date and time application was created.
    """

    updated_at: Optional[datetime]
    """
    Date and time of last application update.
    """


@dataclass
class Group:
    id: str
    """
    ID of the group.
    """

    organization_id: str
    """
    ID of Organization linked to the group.
    """

    name: str
    """
    Name of the group.
    """

    description: str
    """
    Description of the group.
    """

    user_ids: List[str]
    """
    IDs of users attached to this group.
    """

    application_ids: List[str]
    """
    IDs of applications attached to this group.
    """

    tags: List[str]
    """
    Tags associated to the group.
    """

    created_at: Optional[datetime]
    """
    Date and time of group creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of last group update.
    """


@dataclass
class Log:
    id: str
    """
    Log ID.
    """

    ip: str
    """
    IP address of the HTTP request linked to the log.
    """

    user_agent: str
    """
    User-Agent of the HTTP request linked to the log.
    """

    action: LogAction
    """
    Action linked to the log.
    """

    bearer_id: str
    """
    ID of the principal at the origin of the log.
    """

    organization_id: str
    """
    ID of Organization linked to the log.
    """

    resource_type: LogResourceType
    """
    Type of the resource linked to the log.
    """

    resource_id: str
    """
    ID of the resource linked  to the log.
    """

    created_at: Optional[datetime]
    """
    Creation date of the log.
    """


@dataclass
class PermissionSet:
    id: str
    """
    Id of the permission set.
    """

    name: str
    """
    Name of the permission set.
    """

    scope_type: PermissionSetScopeType
    """
    Scope of the permission set.
    """

    description: str
    """
    Description of the permission set.
    """

    categories: Optional[List[str]]
    """
    Categories of the permission set.
    """


@dataclass
class Policy:
    id: str
    """
    Id of the policy.
    """

    name: str
    """
    Name of the policy.
    """

    description: str
    """
    Description of the policy.
    """

    organization_id: str
    """
    Organization ID of the policy.
    """

    editable: bool
    """
    Defines whether or not a policy is editable.
    """

    nb_rules: int
    """
    Number of rules of the policy.
    """

    nb_scopes: int
    """
    Number of policy scopes.
    """

    nb_permission_sets: int
    """
    Number of permission sets of the policy.
    """

    tags: List[str]
    """
    Tags associated with the policy.
    """

    created_at: Optional[datetime]
    """
    Date and time of policy creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of last policy update.
    """

    user_id: Optional[str]

    group_id: Optional[str]

    application_id: Optional[str]

    no_principal: Optional[bool]


@dataclass
class Quotum:
    name: str
    """
    Name of the quota.
    """

    pretty_name: str
    """
    A human-readable name for the quota.
    """

    unit: str
    """
    The unit in which the quota is expressed.
    """

    description: str
    """
    Details about the quota.
    """

    limit: Optional[int]

    unlimited: Optional[bool]


@dataclass
class Rule:
    id: str
    """
    Id of rule.
    """

    permission_sets_scope_type: PermissionSetScopeType
    """
    Permission_set_names have the same scope_type.
    """

    condition: str
    """
    Condition expression to evaluate.
    """

    permission_set_names: Optional[List[str]]
    """
    Names of permission sets bound to the rule.
    """

    project_ids: Optional[List[str]]

    organization_id: Optional[str]

    account_root_user_id: Optional[str]


@dataclass
class SSHKey:
    id: str
    """
    ID of SSH key.
    """

    name: str
    """
    Name of SSH key.
    """

    public_key: str
    """
    Public key of SSH key.
    """

    fingerprint: str
    """
    Fingerprint of the SSH key.
    """

    organization_id: str
    """
    ID of Organization linked to the SSH key.
    """

    project_id: str
    """
    ID of Project linked to the SSH key.
    """

    disabled: bool
    """
    SSH key status.
    """

    created_at: Optional[datetime]
    """
    Creation date of SSH key.
    """

    updated_at: Optional[datetime]
    """
    Last update date of SSH key.
    """


@dataclass
class User:
    id: str
    """
    ID of user.
    """

    email: str
    """
    Email of user.
    """

    username: str
    """
    User identifier unique to the Organization.
    """

    organization_id: str
    """
    ID of the Organization.
    """

    created_at: Optional[datetime]
    """
    Date user was created.
    """

    updated_at: Optional[datetime]
    """
    Date of last user update.
    """

    deletable: bool
    """
    Deletion status of user. Owners cannot be deleted.
    """

    type_: UserType
    """
    Type of user.
    """

    status: UserStatus
    """
    Status of user invitation.
    """

    mfa: bool
    """
    Defines whether MFA is enabled.
    """

    account_root_user_id: str
    """
    ID of the account root user associated with the user.
    """

    tags: List[str]
    """
    Tags associated with the user.
    """

    locked: bool
    """
    Defines whether the user is locked.
    """

    last_login_at: Optional[datetime]
    """
    Date of the last login.
    """

    two_factor_enabled: Optional[bool]
    """
    Deprecated, use "mfa" instead.
    """


@dataclass
class AddGroupMemberRequest:
    group_id: str
    """
    ID of the group.
    """

    user_id: Optional[str]

    application_id: Optional[str]


@dataclass
class AddGroupMembersRequest:
    group_id: str
    """
    ID of the group.
    """

    user_ids: Optional[List[str]]
    """
    IDs of the users to add.
    """

    application_ids: Optional[List[str]]
    """
    IDs of the applications to add.
    """


@dataclass
class ClonePolicyRequest:
    policy_id: str


@dataclass
class CreateAPIKeyRequest:
    description: str
    """
    Description of the API key (max length is 200 characters).
    """

    expires_at: Optional[datetime]
    """
    Expiration date of the API key.
    """

    default_project_id: Optional[str]
    """
    Default Project ID to use with Object Storage.
    """

    application_id: Optional[str]

    user_id: Optional[str]


@dataclass
class CreateApplicationRequest:
    description: str
    """
    Description of the application (max length is 200 characters).
    """

    name: Optional[str]
    """
    Name of the application to create (max length is 64 characters).
    """

    organization_id: Optional[str]
    """
    ID of the Organization.
    """

    tags: Optional[List[str]]
    """
    Tags associated with the application (maximum of 10 tags).
    """


@dataclass
class CreateGroupRequest:
    description: str
    """
    Description of the group to create (max length is 200 chars).
    """

    organization_id: Optional[str]
    """
    ID of Organization linked to the group.
    """

    name: Optional[str]
    """
    Name of the group to create (max length is 64 chars). MUST be unique inside an Organization.
    """

    tags: Optional[List[str]]
    """
    Tags associated with the group (maximum of 10 tags).
    """


@dataclass
class CreateJWTRequest:
    user_id: str
    """
    ID of the user the JWT will be created for.
    """

    referrer: str
    """
    Referrer of the JWT.
    """


@dataclass
class CreatePolicyRequest:
    description: str
    """
    Description of the policy to create (max length is 200 characters).
    """

    name: Optional[str]
    """
    Name of the policy to create (max length is 64 characters).
    """

    organization_id: Optional[str]
    """
    ID of the Organization.
    """

    rules: Optional[List[RuleSpecs]]
    """
    Rules of the policy to create.
    """

    tags: Optional[List[str]]
    """
    Tags associated with the policy (maximum of 10 tags).
    """

    user_id: Optional[str]

    group_id: Optional[str]

    application_id: Optional[str]

    no_principal: Optional[bool]


@dataclass
class CreateSSHKeyRequest:
    public_key: str
    """
    SSH public key. Currently only the ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST curves are supported. Max length is 65000.
    """

    name: Optional[str]
    """
    Name of the SSH key. Max length is 1000.
    """

    project_id: Optional[str]
    """
    Project the resource is attributed to.
    """


@dataclass
class CreateUserRequest:
    organization_id: Optional[str]
    """
    ID of the Organization.
    """

    tags: Optional[List[str]]
    """
    Tags associated with the user.
    """

    email: Optional[str]

    member: Optional[CreateUserRequestMember]


@dataclass
class DeleteAPIKeyRequest:
    access_key: str
    """
    Access key to delete.
    """


@dataclass
class DeleteApplicationRequest:
    application_id: str
    """
    ID of the application to delete.
    """


@dataclass
class DeleteGroupRequest:
    group_id: str
    """
    ID of the group to delete.
    """


@dataclass
class DeleteJWTRequest:
    jti: str
    """
    JWT ID of the JWT to delete.
    """


@dataclass
class DeletePolicyRequest:
    policy_id: str
    """
    Id of policy to delete.
    """


@dataclass
class DeleteSSHKeyRequest:
    ssh_key_id: str


@dataclass
class DeleteUserRequest:
    user_id: str
    """
    ID of the user to delete.
    """


@dataclass
class EncodedJWT:
    token: str
    """
    The encoded token of the renewed JWT.
    """

    renew_token: str
    """
    The encoded renew token. This token is necessary to renew the JWT.
    """

    jwt: Optional[JWT]
    """
    The renewed JWT.
    """


@dataclass
class GetAPIKeyRequest:
    access_key: str
    """
    Access key to search for.
    """


@dataclass
class GetApplicationRequest:
    application_id: str
    """
    ID of the application to find.
    """


@dataclass
class GetGroupRequest:
    group_id: str
    """
    ID of the group.
    """


@dataclass
class GetJWTRequest:
    jti: str
    """
    JWT ID of the JWT to get.
    """


@dataclass
class GetLogRequest:
    log_id: str
    """
    ID of the log.
    """


@dataclass
class GetPolicyRequest:
    policy_id: str
    """
    Id of policy to search.
    """


@dataclass
class GetQuotumRequest:
    quotum_name: str
    """
    Name of the quota to get.
    """

    organization_id: Optional[str]
    """
    ID of the Organization.
    """


@dataclass
class GetSSHKeyRequest:
    ssh_key_id: str
    """
    ID of the SSH key.
    """


@dataclass
class GetUserRequest:
    user_id: str
    """
    ID of the user to find.
    """


@dataclass
class ListAPIKeysRequest:
    order_by: Optional[ListAPIKeysRequestOrderBy]
    """
    Criteria for sorting results.
    """

    page: Optional[int]
    """
    Page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100.
    """

    organization_id: Optional[str]
    """
    ID of Organization.
    """

    editable: Optional[bool]
    """
    Defines whether to filter out editable API keys or not.
    """

    expired: Optional[bool]
    """
    Defines whether to filter out expired API keys or not.
    """

    access_key: Optional[str]
    """
    Filter by access key (deprecated in favor of `access_keys`).
    """

    description: Optional[str]
    """
    Filter by description.
    """

    bearer_id: Optional[str]
    """
    Filter by bearer ID.
    """

    bearer_type: Optional[BearerType]
    """
    Filter by type of bearer.
    """

    access_keys: Optional[List[str]]
    """
    Filter by a list of access keys.
    """

    application_id: Optional[str]

    user_id: Optional[str]


@dataclass
class ListAPIKeysResponse:
    api_keys: List[APIKey]
    """
    List of API keys.
    """

    total_count: int
    """
    Total count of API Keys.
    """


@dataclass
class ListApplicationsRequest:
    order_by: Optional[ListApplicationsRequestOrderBy]
    """
    Criteria for sorting results.
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int]
    """
    Page number. Value must be greater than 1.
    """

    name: Optional[str]
    """
    Name of the application to filter.
    """

    organization_id: Optional[str]
    """
    ID of the Organization to filter.
    """

    editable: Optional[bool]
    """
    Defines whether to filter out editable applications or not.
    """

    application_ids: Optional[List[str]]
    """
    Filter by list of IDs.
    """

    tag: Optional[str]
    """
    Filter by tags containing a given string.
    """


@dataclass
class ListApplicationsResponse:
    applications: List[Application]
    """
    List of applications.
    """

    total_count: int
    """
    Total count of applications.
    """


@dataclass
class ListGroupsRequest:
    order_by: Optional[ListGroupsRequestOrderBy]
    """
    Sort order of groups.
    """

    page: Optional[int]
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int]
    """
    Number of items per page. Value must be between 1 and 100.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    name: Optional[str]
    """
    Name of group to find.
    """

    application_ids: Optional[List[str]]
    """
    Filter by a list of application IDs.
    """

    user_ids: Optional[List[str]]
    """
    Filter by a list of user IDs.
    """

    group_ids: Optional[List[str]]
    """
    Filter by a list of group IDs.
    """

    tag: Optional[str]
    """
    Filter by tags containing a given string.
    """


@dataclass
class ListGroupsResponse:
    groups: List[Group]
    """
    List of groups.
    """

    total_count: int
    """
    Total count of groups.
    """


@dataclass
class ListJWTsRequest:
    order_by: Optional[ListJWTsRequestOrderBy]
    """
    Criteria for sorting results.
    """

    audience_id: Optional[str]
    """
    ID of the user to search.
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int]
    """
    Page number. Value must be greater to 1.
    """

    expired: Optional[bool]
    """
    Filter out expired JWTs or not.
    """


@dataclass
class ListJWTsResponse:
    jwts: List[JWT]

    total_count: int


@dataclass
class ListLogsRequest:
    order_by: Optional[ListLogsRequestOrderBy]
    """
    Criteria for sorting results.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int]
    """
    Page number. Value must be greater to 1.
    """

    created_after: Optional[datetime]
    """
    Defined whether or not to filter out logs created after this timestamp.
    """

    created_before: Optional[datetime]
    """
    Defined whether or not to filter out logs created before this timestamp.
    """

    action: Optional[LogAction]
    """
    Defined whether or not to filter out by a specific action.
    """

    resource_type: Optional[LogResourceType]
    """
    Defined whether or not to filter out by a specific type of resource.
    """

    search: Optional[str]
    """
    Defined whether or not to filter out log by bearer ID or resource ID.
    """


@dataclass
class ListLogsResponse:
    logs: List[Log]
    """
    List of logs.
    """

    total_count: int
    """
    Total count of logs.
    """


@dataclass
class ListPermissionSetsRequest:
    order_by: Optional[ListPermissionSetsRequestOrderBy]
    """
    Criteria for sorting results.
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int]
    """
    Page number. Value must be greater than 1.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """


@dataclass
class ListPermissionSetsResponse:
    permission_sets: List[PermissionSet]
    """
    List of permission sets.
    """

    total_count: int
    """
    Total count of permission sets.
    """


@dataclass
class ListPoliciesRequest:
    order_by: Optional[ListPoliciesRequestOrderBy]
    """
    Criteria for sorting results.
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int]
    """
    Page number. Value must be greater than 1.
    """

    organization_id: Optional[str]
    """
    ID of the Organization to filter.
    """

    editable: Optional[bool]
    """
    Defines whether or not filter out editable policies.
    """

    user_ids: Optional[List[str]]
    """
    Defines whether or not to filter by list of user IDs.
    """

    group_ids: Optional[List[str]]
    """
    Defines whether or not to filter by list of group IDs.
    """

    application_ids: Optional[List[str]]
    """
    Filter by a list of application IDs.
    """

    no_principal: Optional[bool]
    """
    Defines whether or not the policy is attributed to a principal.
    """

    policy_name: Optional[str]
    """
    Name of the policy to fetch.
    """

    tag: Optional[str]
    """
    Filter by tags containing a given string.
    """

    policy_ids: Optional[List[str]]
    """
    Filter by a list of IDs.
    """


@dataclass
class ListPoliciesResponse:
    policies: List[Policy]
    """
    List of policies.
    """

    total_count: int
    """
    Total count of policies.
    """


@dataclass
class ListQuotaRequest:
    order_by: Optional[ListQuotaRequestOrderBy]
    """
    Criteria for sorting results.
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int]
    """
    Page number. Value must be greater than 1.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    quotum_names: Optional[List[str]]
    """
    List of quotum names to filter from.
    """


@dataclass
class ListQuotaResponse:
    quota: List[Quotum]
    """
    List of quota.
    """

    total_count: int
    """
    Total count of quota.
    """


@dataclass
class ListRulesRequest:
    policy_id: str
    """
    Id of policy to search.
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int]
    """
    Page number. Value must be greater than 1.
    """


@dataclass
class ListRulesResponse:
    rules: List[Rule]
    """
    Rules of the policy.
    """

    total_count: int
    """
    Total count of rules.
    """


@dataclass
class ListSSHKeysRequest:
    order_by: Optional[ListSSHKeysRequestOrderBy]
    """
    Sort order of the SSH keys.
    """

    page: Optional[int]
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int]
    """
    Number of items per page. Value must be between 1 and 100.
    """

    organization_id: Optional[str]
    """
    Filter by Organization ID.
    """

    name: Optional[str]
    """
    Name of group to find.
    """

    project_id: Optional[str]
    """
    Filter by Project ID.
    """

    disabled: Optional[bool]
    """
    Defines whether to include disabled SSH keys or not.
    """


@dataclass
class ListSSHKeysResponse:
    ssh_keys: List[SSHKey]
    """
    List of SSH keys.
    """

    total_count: int
    """
    Total count of SSH keys.
    """


@dataclass
class ListUsersRequest:
    order_by: Optional[ListUsersRequestOrderBy]
    """
    Criteria for sorting results.
    """

    page_size: Optional[int]
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int]
    """
    Page number. Value must be greater or equal to 1.
    """

    organization_id: Optional[str]
    """
    ID of the Organization to filter.
    """

    user_ids: Optional[List[str]]
    """
    Filter by list of IDs.
    """

    mfa: Optional[bool]
    """
    Filter by MFA status.
    """

    tag: Optional[str]
    """
    Filter by tags containing a given string.
    """


@dataclass
class ListUsersResponse:
    users: List[User]
    """
    List of users.
    """

    total_count: int
    """
    Total count of users.
    """


@dataclass
class RemoveGroupMemberRequest:
    group_id: str
    """
    ID of the group.
    """

    user_id: Optional[str]

    application_id: Optional[str]


@dataclass
class SetGroupMembersRequest:
    group_id: str

    user_ids: List[str]

    application_ids: List[str]


@dataclass
class SetRulesRequest:
    policy_id: str
    """
    Id of policy to update.
    """

    rules: List[RuleSpecs]
    """
    Rules of the policy to set.
    """


@dataclass
class SetRulesResponse:
    rules: List[Rule]
    """
    Rules of the policy.
    """


@dataclass
class UpdateAPIKeyRequest:
    access_key: str
    """
    Access key to update.
    """

    default_project_id: Optional[str]
    """
    New default Project ID to set.
    """

    description: Optional[str]
    """
    New description to update.
    """


@dataclass
class UpdateApplicationRequest:
    application_id: str
    """
    ID of the application to update.
    """

    name: Optional[str]
    """
    New name for the application (max length is 64 chars).
    """

    description: Optional[str]
    """
    New description for the application (max length is 200 chars).
    """

    tags: Optional[List[str]]
    """
    New tags for the application (maximum of 10 tags).
    """


@dataclass
class UpdateGroupRequest:
    group_id: str
    """
    ID of the group to update.
    """

    name: Optional[str]
    """
    New name for the group (max length is 64 chars). MUST be unique inside an Organization.
    """

    description: Optional[str]
    """
    New description for the group (max length is 200 chars).
    """

    tags: Optional[List[str]]
    """
    New tags for the group (maximum of 10 tags).
    """


@dataclass
class UpdatePolicyRequest:
    policy_id: str
    """
    Id of policy to update.
    """

    name: Optional[str]
    """
    New name for the policy (max length is 64 characters).
    """

    description: Optional[str]
    """
    New description of policy (max length is 200 characters).
    """

    tags: Optional[List[str]]
    """
    New tags for the policy (maximum of 10 tags).
    """

    user_id: Optional[str]

    group_id: Optional[str]

    application_id: Optional[str]

    no_principal: Optional[bool]


@dataclass
class UpdateSSHKeyRequest:
    ssh_key_id: str

    name: Optional[str]
    """
    Name of the SSH key. Max length is 1000.
    """

    disabled: Optional[bool]
    """
    Enable or disable the SSH key.
    """


@dataclass
class UpdateUserRequest:
    user_id: str
    """
    ID of the user to update.
    """

    tags: Optional[List[str]]
    """
    New tags for the user (maximum of 10 tags).
    """
