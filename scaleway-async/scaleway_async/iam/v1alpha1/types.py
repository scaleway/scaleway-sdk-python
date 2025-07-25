# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class BearerType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_BEARER_TYPE = "unknown_bearer_type"
    USER = "user"
    APPLICATION = "application"

    def __str__(self) -> str:
        return str(self.value)


class GracePeriodType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_GRACE_PERIOD_TYPE = "unknown_grace_period_type"
    UPDATE_PASSWORD = "update_password"
    SET_MFA = "set_mfa"

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
    USERNAME_ASC = "username_asc"
    USERNAME_DESC = "username_desc"

    def __str__(self) -> str:
        return str(self.value)


class LocalityType(str, Enum, metaclass=StrEnumMeta):
    GLOBAL = "global"
    REGION = "region"
    ZONE = "zone"

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


class SamlCertificateOrigin(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_CERTIFICATE_ORIGIN = "unknown_certificate_origin"
    SCALEWAY = "scaleway"
    IDENTITY_PROVIDER = "identity_provider"

    def __str__(self) -> str:
        return str(self.value)


class SamlCertificateType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_CERTIFICATE_TYPE = "unknown_certificate_type"
    SIGNING = "signing"
    ENCRYPTION = "encryption"

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
class ConnectionConnectedOrganization:
    id: str

    name: str

    locked: bool


@dataclass
class ConnectionConnectedUser:
    id: str

    username: str

    type_: UserType


@dataclass
class QuotumLimit:
    global_: Optional[bool]

    region: Optional[ScwRegion]

    zone: Optional[ScwZone]

    limit: Optional[int]

    unlimited: Optional[bool]


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

    send_welcome_email: bool
    """
    Whether or not to send a welcome email that includes onboarding information.
    """

    username: str
    """
    The member's username.
    """

    password: str
    """
    The member's password.
    """

    first_name: str
    """
    The member's first name.
    """

    last_name: str
    """
    The member's last name.
    """

    phone_number: str
    """
    The member's phone number.
    """

    locale: str
    """
    The member's locale.
    """


@dataclass
class Connection:
    organization: Optional[ConnectionConnectedOrganization]
    """
    Information about the connected organization.
    """

    user: Optional[ConnectionConnectedUser]
    """
    Information about the connected user.
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

    deletable: bool
    """
    Defines whether or not the API key is deletable.
    """

    managed: bool
    """
    Defines whether or not the API key is managed.
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

    deletable: bool
    """
    Defines whether or not the application is deletable.
    """

    managed: bool
    """
    Defines whether or not the application is managed.
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
class GracePeriod:
    type_: GracePeriodType
    """
    Type of grace period.
    """

    created_at: Optional[datetime]
    """
    Date and time the grace period was created.
    """

    expires_at: Optional[datetime]
    """
    Date and time the grace period expires.
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

    editable: bool
    """
    Defines whether or not the group is editable.
    """

    deletable: bool
    """
    Defines whether or not the group is deletable.
    """

    managed: bool
    """
    Defines whether or not the group is managed.
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

    created_at: Optional[datetime]
    """
    Date and time of policy creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of last policy update.
    """

    editable: bool
    """
    Defines whether or not a policy is editable.
    """

    deletable: bool
    """
    Defines whether or not a policy is deletable.
    """

    managed: bool
    """
    Defines whether or not a policy is managed.
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

    locality_type: LocalityType
    """
    Whether this quotum is applied on at the zone level, region level, or globally.
    """

    limits: List[QuotumLimit]
    """
    Limits per locality.
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
class SamlCertificate:
    id: str
    """
    ID of the SAML certificate.
    """

    type_: SamlCertificateType
    """
    Type of the SAML certificate.
    """

    origin: SamlCertificateOrigin
    """
    Origin of the SAML certificate.
    """

    content: str
    """
    Content of the SAML certificate.
    """

    expires_at: Optional[datetime]
    """
    Date and time of the SAML certificate expiration.
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

    first_name: str
    """
    First name of the user.
    """

    last_name: str
    """
    Last name of the user.
    """

    phone_number: str
    """
    Phone number of the user.
    """

    locale: str
    """
    Locale of the user.
    """

    organization_id: str
    """
    ID of the Organization.
    """

    deletable: bool
    """
    Deletion status of user. Owners cannot be deleted.
    """

    created_at: Optional[datetime]
    """
    Date user was created.
    """

    updated_at: Optional[datetime]
    """
    Date of last user update.
    """

    last_login_at: Optional[datetime]
    """
    Date of the last login.
    """

    type_: UserType
    """
    Type of user.
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

    two_factor_enabled: Optional[bool]
    """
    Deprecated, use "mfa" instead.
    """

    status: Optional[UserStatus]
    """
    Status of user invitation.
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
class AddSamlCertificateRequest:
    saml_id: str
    """
    ID of the SAML configuration.
    """

    type_: SamlCertificateType
    """
    Type of the SAML certificate.
    """

    content: str
    """
    Content of the SAML certificate.
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
class CreateOrganizationSamlRequest:
    entity_id: str
    """
    Entity ID of the SAML Identity Provider.
    """

    single_sign_on_url: str
    """
    Single Sign-On URL of the SAML Identity Provider.
    """

    organization_id: Optional[str]
    """
    ID of the Organization.
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
class CreateUserMFAOTPRequest:
    user_id: str
    """
    User ID of the MFA OTP.
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
class DeleteOrganizationSamlRequest:
    organization_id: Optional[str]
    """
    ID of the Organization.
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
class DeleteSamlCertificateRequest:
    certificate_id: str
    """
    ID of the certificate to delete.
    """


@dataclass
class DeleteUserMFAOTPRequest:
    user_id: str
    """
    User ID of the MFA OTP.
    """


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
class GetOrganizationRequest:
    organization_id: Optional[str]
    """
    ID of the Organization.
    """


@dataclass
class GetOrganizationSamlRequest:
    organization_id: Optional[str]
    """
    ID of the Organization.
    """


@dataclass
class GetOrganizationSecuritySettingsRequest:
    organization_id: Optional[str]
    """
    ID of the Organization.
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
class GetUserConnectionsRequest:
    user_id: str
    """
    ID of the user to list connections for.
    """


@dataclass
class GetUserConnectionsResponse:
    connections: List[Connection]
    """
    List of connections.
    """


@dataclass
class GetUserRequest:
    user_id: str
    """
    ID of the user to find.
    """


@dataclass
class InitiateUserConnectionRequest:
    user_id: str
    """
    ID of the user that will be added to your connection.
    """


@dataclass
class InitiateUserConnectionResponse:
    token: str
    """
    Token to be used in JoinUserConnection.
    """


@dataclass
class JoinUserConnectionRequest:
    user_id: str
    """
    User ID.
    """

    token: str
    """
    A token returned by InitiateUserConnection.
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
class ListGracePeriodsRequest:
    user_id: Optional[str]
    """
    ID of the user to list grace periods for.
    """


@dataclass
class ListGracePeriodsResponse:
    grace_periods: List[GracePeriod]
    """
    List of grace periods.
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
    audience_id: str
    """
    ID of the user to search.
    """

    order_by: Optional[ListJWTsRequestOrderBy]
    """
    Criteria for sorting results.
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
class ListSamlCertificatesRequest:
    saml_id: str
    """
    ID of the SAML configuration.
    """


@dataclass
class ListSamlCertificatesResponse:
    certificates: List[SamlCertificate]
    """
    List of SAML certificates.
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

    type_: Optional[UserType]
    """
    Filter by user type.
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
class LockUserRequest:
    user_id: str
    """
    ID of the user to lock.
    """


@dataclass
class MFAOTP:
    secret: str


@dataclass
class MigrateOrganizationGuestsRequest:
    organization_id: Optional[str]
    """
    ID of the Organization.
    """


@dataclass
class Organization:
    id: str
    """
    ID of the Organization.
    """

    name: str
    """
    Name of the Organization.
    """

    alias: str
    """
    Alias of the Organization.
    """


@dataclass
class OrganizationSecuritySettings:
    enforce_password_renewal: bool
    """
    Defines whether password renewal is enforced during first login.
    """

    login_attempts_before_locked: int
    """
    Number of login attempts before the account is locked.
    """

    grace_period_duration: Optional[str]
    """
    Duration of the grace period to renew password or enable MFA.
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
class RemoveUserConnectionRequest:
    user_id: str
    """
    ID of the user you want to manage the connection for.
    """

    target_user_id: str
    """
    ID of the user you want to remove from your connection.
    """


@dataclass
class Saml:
    id: str
    """
    ID of the SAML configuration.
    """

    entity_id: str
    """
    Entity ID of the SAML Identity Provider.
    """

    single_sign_on_url: str
    """
    Single Sign-On URL of the SAML Identity Provider.
    """


@dataclass
class SetGroupMembersRequest:
    group_id: str

    user_ids: List[str]

    application_ids: List[str]


@dataclass
class SetOrganizationAliasRequest:
    alias: str
    """
    Alias of the Organization.
    """

    organization_id: Optional[str]
    """
    ID of the Organization.
    """


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
class UnlockUserRequest:
    user_id: str
    """
    ID of the user to unlock.
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
class UpdateOrganizationSamlRequest:
    organization_id: Optional[str]
    """
    ID of the Organization.
    """

    entity_id: Optional[str]
    """
    Entity ID of the SAML Identity Provider.
    """

    single_sign_on_url: Optional[str]
    """
    Single Sign-On URL of the SAML Identity Provider.
    """


@dataclass
class UpdateOrganizationSecuritySettingsRequest:
    organization_id: Optional[str]
    """
    ID of the Organization.
    """

    enforce_password_renewal: Optional[bool]
    """
    Defines whether password renewal is enforced during first login.
    """

    grace_period_duration: Optional[str]
    """
    Duration of the grace period to renew password or enable MFA.
    """

    login_attempts_before_locked: Optional[int]
    """
    Number of login attempts before the account is locked.
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
class UpdateUserPasswordRequest:
    user_id: str
    """
    ID of the user to update.
    """

    password: str
    """
    The new password.
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

    email: Optional[str]
    """
    IAM member email.
    """

    first_name: Optional[str]
    """
    IAM member first name.
    """

    last_name: Optional[str]
    """
    IAM member last name.
    """

    phone_number: Optional[str]
    """
    IAM member phone number.
    """

    locale: Optional[str]
    """
    IAM member locale.
    """


@dataclass
class UpdateUserUsernameRequest:
    user_id: str
    """
    ID of the user to update.
    """

    username: str
    """
    The new username.
    """


@dataclass
class ValidateUserMFAOTPRequest:
    user_id: str
    """
    User ID of the MFA OTP.
    """

    one_time_password: str
    """
    A password generated using the OTP.
    """


@dataclass
class ValidateUserMFAOTPResponse:
    recovery_codes: List[str]
    """
    List of recovery codes usable for this OTP method.
    """
