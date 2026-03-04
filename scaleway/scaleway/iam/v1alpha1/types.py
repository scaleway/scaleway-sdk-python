# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
    ScwFile,
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


class ListScimTokensRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListUserWebAuthnAuthenticatorsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

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


class SamlStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SAML_STATUS = "unknown_saml_status"
    VALID = "valid"
    MISSING_CERTIFICATE = "missing_certificate"
    MISSING_ENTITY_ID = "missing_entity_id"
    MISSING_SINGLE_SIGN_ON_URL = "missing_single_sign_on_url"

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
    global_: Optional[bool] = False

    region: Optional[ScwRegion] = None

    zone: Optional[ScwZone] = None

    limit: Optional[int] = 0

    unlimited: Optional[bool] = False


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

    created_at: Optional[datetime] = None
    """
    Creation date of the JWT.
    """

    updated_at: Optional[datetime] = None
    """
    Last update date of the JWT.
    """

    expires_at: Optional[datetime] = None
    """
    Expiration date of the JWT.
    """


@dataclass
class RuleSpecs:
    condition: str
    """
    Condition expression to evaluate.
    """

    permission_set_names: Optional[list[str]] = field(default_factory=list)
    """
    Names of permission sets bound to the rule.
    """

    project_ids: Optional[list[str]] = field(default_factory=list)

    organization_id: Optional[str] = None


@dataclass
class ScimToken:
    id: str
    scim_id: str
    created_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None


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
    organization: Optional[ConnectionConnectedOrganization] = None
    """
    Information about the connected organization.
    """

    user: Optional[ConnectionConnectedUser] = None
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

    secret_key: Optional[str] = None
    """
    Secret key of the API Key.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of API key creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of last API key update.
    """

    expires_at: Optional[datetime] = None
    """
    Date and time of API key expiration.
    """

    application_id: Optional[str] = None

    user_id: Optional[str] = None


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

    tags: list[str]
    """
    Tags associated with the user.
    """

    created_at: Optional[datetime] = None
    """
    Date and time application was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of last application update.
    """


@dataclass
class GracePeriod:
    type_: GracePeriodType
    """
    Type of grace period.
    """

    created_at: Optional[datetime] = None
    """
    Date and time the grace period was created.
    """

    expires_at: Optional[datetime] = None
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

    user_ids: list[str]
    """
    IDs of users attached to this group.
    """

    application_ids: list[str]
    """
    IDs of applications attached to this group.
    """

    tags: list[str]
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

    created_at: Optional[datetime] = None
    """
    Date and time of group creation.
    """

    updated_at: Optional[datetime] = None
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

    created_at: Optional[datetime] = None
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

    categories: Optional[list[str]] = field(default_factory=list)
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

    tags: list[str]
    """
    Tags associated with the policy.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of policy creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of last policy update.
    """

    user_id: Optional[str] = None

    group_id: Optional[str] = None

    application_id: Optional[str] = None

    no_principal: Optional[bool] = False


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

    limits: list[QuotumLimit]
    """
    Limits per locality.
    """

    limit: Optional[int] = 0

    unlimited: Optional[bool] = False


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

    permission_set_names: Optional[list[str]] = field(default_factory=list)
    """
    Names of permission sets bound to the rule.
    """

    project_ids: Optional[list[str]] = field(default_factory=list)

    organization_id: Optional[str] = None

    account_root_user_id: Optional[str] = None


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

    created_at: Optional[datetime] = None
    """
    Creation date of SSH key.
    """

    updated_at: Optional[datetime] = None
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

    expires_at: Optional[datetime] = None
    """
    Date and time of the SAML certificate expiration.
    """


@dataclass
class WebAuthnAuthenticator:
    id: str
    """
    The ID of the authenticator.
    """

    name: str
    """
    The name of the authenticator.
    """

    created_at: Optional[datetime] = None
    """
    The creation date.
    """

    last_login_at: Optional[datetime] = None
    """
    The timestamp of the last successful login using the authenticator.
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

    type_: UserType
    """
    Type of user.
    """

    two_factor_enabled: bool
    """
    Deprecated, use "mfa" instead.
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

    tags: list[str]
    """
    Tags associated with the user.
    """

    locked: bool
    """
    Defines whether the user is locked.
    """

    created_at: Optional[datetime] = None
    """
    Date user was created.
    """

    updated_at: Optional[datetime] = None
    """
    Date of last user update.
    """

    last_login_at: Optional[datetime] = None
    """
    Date of the last login.
    """


@dataclass
class SamlServiceProvider:
    entity_id: str
    assertion_consumer_service_url: str


@dataclass
class AddGroupMemberRequest:
    group_id: str
    """
    ID of the group.
    """

    user_id: Optional[str] = None

    application_id: Optional[str] = None


@dataclass
class AddGroupMembersRequest:
    group_id: str
    """
    ID of the group.
    """

    user_ids: Optional[list[str]] = field(default_factory=list)
    """
    IDs of the users to add.
    """

    application_ids: Optional[list[str]] = field(default_factory=list)
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

    expires_at: Optional[datetime] = None
    """
    Expiration date of the API key.
    """

    default_project_id: Optional[str] = None
    """
    Default Project ID to use with Object Storage.
    """

    application_id: Optional[str] = None

    user_id: Optional[str] = None


@dataclass
class CreateApplicationRequest:
    description: str
    """
    Description of the application (max length is 200 characters).
    """

    name: Optional[str] = None
    """
    Name of the application to create (max length is 64 characters).
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags associated with the application (maximum of 10 tags).
    """


@dataclass
class CreateGroupRequest:
    description: str
    """
    Description of the group to create (max length is 200 chars).
    """

    organization_id: Optional[str] = None
    """
    ID of Organization linked to the group.
    """

    name: Optional[str] = None
    """
    Name of the group to create (max length is 64 chars). MUST be unique inside an Organization.
    """

    tags: Optional[list[str]] = field(default_factory=list)
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

    name: Optional[str] = None
    """
    Name of the policy to create (max length is 64 characters).
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization.
    """

    rules: Optional[list[RuleSpecs]] = field(default_factory=list)
    """
    Rules of the policy to create.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags associated with the policy (maximum of 10 tags).
    """

    user_id: Optional[str] = None

    group_id: Optional[str] = None

    application_id: Optional[str] = None

    no_principal: Optional[bool] = False


@dataclass
class CreateSSHKeyRequest:
    public_key: str
    """
    SSH public key. Currently only the ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST curves are supported. Max length is 65000.
    """

    name: Optional[str] = None
    """
    Name of the SSH key. Max length is 1000.
    """

    project_id: Optional[str] = None
    """
    Project the resource is attributed to.
    """


@dataclass
class CreateScimTokenRequest:
    scim_id: str
    """
    ID of the SCIM configuration.
    """


@dataclass
class CreateScimTokenResponse:
    bearer_token: str
    """
    The Bearer Token to use to authenticate to SCIM endpoints.
    """

    token: Optional[ScimToken] = None
    """
    The SCIM token metadata.
    """


@dataclass
class CreateUserMFAOTPRequest:
    user_id: str
    """
    User ID of the MFA OTP.
    """


@dataclass
class CreateUserRequest:
    organization_id: Optional[str] = None
    """
    ID of the Organization.
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    Tags associated with the user.
    """

    email: Optional[str] = None

    member: Optional[CreateUserRequestMember] = None


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
class DeleteSamlCertificateRequest:
    certificate_id: str
    """
    ID of the certificate to delete.
    """


@dataclass
class DeleteSamlRequest:
    saml_id: str
    """
    ID of the SAML configuration.
    """


@dataclass
class DeleteScimRequest:
    scim_id: str
    """
    ID of the SCIM configuration.
    """


@dataclass
class DeleteScimTokenRequest:
    token_id: str
    """
    The SCIM token ID.
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
class DeleteWebAuthnAuthenticatorRequest:
    authenticator_id: str


@dataclass
class EnableOrganizationSamlRequest:
    organization_id: Optional[str] = None
    """
    ID of the Organization.
    """


@dataclass
class EnableOrganizationScimRequest:
    organization_id: Optional[str] = None
    """
    ID of the Organization.
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

    jwt: Optional[JWT] = None
    """
    The renewed JWT.
    """


@dataclass
class FinishUserWebAuthnRegistrationRequest:
    user_id: str
    """
    The ID of the user on which to finish a webauthn registration.
    """

    ceremony_id: str
    """
    The ceremony ID returned by StartUserWebAuthnRegistration.
    """

    authenticator_name: str
    """
    Name of the WebAuthn Authenticator to create.
    """

    origin: str
    """
    The domain on which the registration is occurring.
    """

    raw_id: str
    """
    Unique identifier of the key used by the authenticator.
    """

    client_data_json: str
    """
    JSON representation of the client data.
    """

    authenticator_data: str
    """
    Data about the authenticator that performed the authentication.
    """

    attestation_object: str
    """
    Attestation Object.
    """

    public_key: str
    """
    Public key that allows to verify signature.
    """

    public_key_algorithm: int
    """
    Algorithm used for the signature (see https://www.iana.org/assignments/cose/cose.xhtml#algorithms).
    """


@dataclass
class FinishUserWebAuthnRegistrationResponse:
    authenticator_id: str
    """
    The ID of the new authenticator created.
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
    organization_id: Optional[str] = None
    """
    ID of the Organization.
    """


@dataclass
class GetOrganizationSamlRequest:
    organization_id: Optional[str] = None
    """
    ID of the Organization.
    """


@dataclass
class GetOrganizationScimRequest:
    organization_id: Optional[str] = None


@dataclass
class GetOrganizationSecuritySettingsRequest:
    organization_id: Optional[str] = None
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

    organization_id: Optional[str] = None
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
    connections: list[Connection]
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
    order_by: Optional[ListAPIKeysRequestOrderBy] = (
        ListAPIKeysRequestOrderBy.CREATED_AT_ASC
    )
    """
    Criteria for sorting results.
    """

    page: Optional[int] = 0
    """
    Page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    Number of results per page. Value must be between 1 and 100.
    """

    organization_id: Optional[str] = None
    """
    ID of Organization.
    """

    editable: Optional[bool] = False
    """
    Defines whether to filter out editable API keys or not.
    """

    expired: Optional[bool] = False
    """
    Defines whether to filter out expired API keys or not.
    """

    access_key: Optional[str] = None
    """
    Filter by access key (deprecated in favor of `access_keys`).
    """

    description: Optional[str] = None
    """
    Filter by description.
    """

    bearer_id: Optional[str] = None
    """
    Filter by bearer ID.
    """

    bearer_type: Optional[BearerType] = BearerType.UNKNOWN_BEARER_TYPE
    """
    Filter by type of bearer.
    """

    access_keys: Optional[list[str]] = field(default_factory=list)
    """
    Filter by a list of access keys.
    """

    application_id: Optional[str] = None

    user_id: Optional[str] = None


@dataclass
class ListAPIKeysResponse:
    api_keys: list[APIKey]
    """
    List of API keys.
    """

    total_count: int
    """
    Total count of API Keys.
    """


@dataclass
class ListApplicationsRequest:
    order_by: Optional[ListApplicationsRequestOrderBy] = (
        ListApplicationsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Criteria for sorting results.
    """

    page_size: Optional[int] = 0
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int] = 0
    """
    Page number. Value must be greater than 1.
    """

    name: Optional[str] = None
    """
    Name of the application to filter.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization to filter.
    """

    editable: Optional[bool] = False
    """
    Defines whether to filter out editable applications or not.
    """

    application_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by list of IDs.
    """

    tag: Optional[str] = None
    """
    Filter by tags containing a given string.
    """


@dataclass
class ListApplicationsResponse:
    applications: list[Application]
    """
    List of applications.
    """

    total_count: int
    """
    Total count of applications.
    """


@dataclass
class ListGracePeriodsRequest:
    user_id: Optional[str] = None
    """
    ID of the user to list grace periods for.
    """


@dataclass
class ListGracePeriodsResponse:
    grace_periods: list[GracePeriod]
    """
    List of grace periods.
    """


@dataclass
class ListGroupsRequest:
    order_by: Optional[ListGroupsRequestOrderBy] = (
        ListGroupsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of groups.
    """

    page: Optional[int] = 0
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    Number of items per page. Value must be between 1 and 100.
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID.
    """

    name: Optional[str] = None
    """
    Name of group to find.
    """

    application_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by a list of application IDs.
    """

    user_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by a list of user IDs.
    """

    group_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by a list of group IDs.
    """

    tag: Optional[str] = None
    """
    Filter by tags containing a given string.
    """


@dataclass
class ListGroupsResponse:
    groups: list[Group]
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

    order_by: Optional[ListJWTsRequestOrderBy] = ListJWTsRequestOrderBy.CREATED_AT_ASC
    """
    Criteria for sorting results.
    """

    page_size: Optional[int] = 0
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int] = 0
    """
    Page number. Value must be greater to 1.
    """

    expired: Optional[bool] = False
    """
    Filter out expired JWTs or not.
    """


@dataclass
class ListJWTsResponse:
    jwts: list[JWT]
    total_count: int


@dataclass
class ListLogsRequest:
    order_by: Optional[ListLogsRequestOrderBy] = ListLogsRequestOrderBy.CREATED_AT_ASC
    """
    Criteria for sorting results.
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID.
    """

    page_size: Optional[int] = 0
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int] = 0
    """
    Page number. Value must be greater to 1.
    """

    created_after: Optional[datetime] = None
    """
    Defined whether or not to filter out logs created after this timestamp.
    """

    created_before: Optional[datetime] = None
    """
    Defined whether or not to filter out logs created before this timestamp.
    """

    action: Optional[LogAction] = LogAction.UNKNOWN_ACTION
    """
    Defined whether or not to filter out by a specific action.
    """

    resource_type: Optional[LogResourceType] = LogResourceType.UNKNOWN_RESOURCE_TYPE
    """
    Defined whether or not to filter out by a specific type of resource.
    """

    search: Optional[str] = None
    """
    Defined whether or not to filter out log by bearer ID or resource ID.
    """


@dataclass
class ListLogsResponse:
    logs: list[Log]
    """
    List of logs.
    """

    total_count: int
    """
    Total count of logs.
    """


@dataclass
class ListPermissionSetsRequest:
    order_by: Optional[ListPermissionSetsRequestOrderBy] = (
        ListPermissionSetsRequestOrderBy.NAME_ASC
    )
    """
    Criteria for sorting results.
    """

    page_size: Optional[int] = 0
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int] = 0
    """
    Page number. Value must be greater than 1.
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID.
    """


@dataclass
class ListPermissionSetsResponse:
    permission_sets: list[PermissionSet]
    """
    List of permission sets.
    """

    total_count: int
    """
    Total count of permission sets.
    """


@dataclass
class ListPoliciesRequest:
    order_by: Optional[ListPoliciesRequestOrderBy] = (
        ListPoliciesRequestOrderBy.POLICY_NAME_ASC
    )
    """
    Criteria for sorting results.
    """

    page_size: Optional[int] = 0
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int] = 0
    """
    Page number. Value must be greater than 1.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization to filter.
    """

    editable: Optional[bool] = False
    """
    Defines whether or not filter out editable policies.
    """

    user_ids: Optional[list[str]] = field(default_factory=list)
    """
    Defines whether or not to filter by list of user IDs.
    """

    group_ids: Optional[list[str]] = field(default_factory=list)
    """
    Defines whether or not to filter by list of group IDs.
    """

    application_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by a list of application IDs.
    """

    no_principal: Optional[bool] = False
    """
    Defines whether or not the policy is attributed to a principal.
    """

    policy_name: Optional[str] = None
    """
    Name of the policy to fetch.
    """

    tag: Optional[str] = None
    """
    Filter by tags containing a given string.
    """

    policy_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by a list of IDs.
    """


@dataclass
class ListPoliciesResponse:
    policies: list[Policy]
    """
    List of policies.
    """

    total_count: int
    """
    Total count of policies.
    """


@dataclass
class ListQuotaRequest:
    order_by: Optional[ListQuotaRequestOrderBy] = ListQuotaRequestOrderBy.NAME_ASC
    """
    Criteria for sorting results.
    """

    page_size: Optional[int] = 0
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int] = 0
    """
    Page number. Value must be greater than 1.
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID.
    """

    quotum_names: Optional[list[str]] = field(default_factory=list)
    """
    List of quotum names to filter from.
    """


@dataclass
class ListQuotaResponse:
    quota: list[Quotum]
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

    page_size: Optional[int] = 0
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int] = 0
    """
    Page number. Value must be greater than 1.
    """


@dataclass
class ListRulesResponse:
    rules: list[Rule]
    """
    Rules of the policy.
    """

    total_count: int
    """
    Total count of rules.
    """


@dataclass
class ListSSHKeysRequest:
    order_by: Optional[ListSSHKeysRequestOrderBy] = (
        ListSSHKeysRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of the SSH keys.
    """

    page: Optional[int] = 0
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    Number of items per page. Value must be between 1 and 100.
    """

    organization_id: Optional[str] = None
    """
    Filter by Organization ID.
    """

    name: Optional[str] = None
    """
    Name of group to find.
    """

    project_id: Optional[str] = None
    """
    Filter by Project ID.
    """

    disabled: Optional[bool] = False
    """
    Defines whether to include disabled SSH keys or not.
    """


@dataclass
class ListSSHKeysResponse:
    ssh_keys: list[SSHKey]
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
    certificates: list[SamlCertificate]
    """
    List of SAML certificates.
    """


@dataclass
class ListScimTokensRequest:
    scim_id: str
    """
    ID of the SCIM configuration.
    """

    order_by: Optional[ListScimTokensRequestOrderBy] = (
        ListScimTokensRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of SCIM tokens.
    """

    page: Optional[int] = 0
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    Number of items per page. Value must be between 1 and 100.
    """


@dataclass
class ListScimTokensResponse:
    scim_tokens: list[ScimToken]
    """
    List of SCIM tokens.
    """

    total_count: int
    """
    Total count of SCIM tokens.
    """


@dataclass
class ListUserWebAuthnAuthenticatorsRequest:
    user_id: str
    """
    A user ID to filter the authenticators for.
    """

    order_by: Optional[ListUserWebAuthnAuthenticatorsRequestOrderBy] = (
        ListUserWebAuthnAuthenticatorsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of the Authenticators.
    """

    page: Optional[int] = 0
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    Number of items per page. Value must be between 1 and 100.
    """


@dataclass
class ListUserWebAuthnAuthenticatorsResponse:
    total_count: int
    """
    The total number of authenticators.
    """

    authenticators: list[WebAuthnAuthenticator]
    """
    The list of authenticators.
    """


@dataclass
class ListUsersRequest:
    order_by: Optional[ListUsersRequestOrderBy] = ListUsersRequestOrderBy.CREATED_AT_ASC
    """
    Criteria for sorting results.
    """

    page_size: Optional[int] = 0
    """
    Number of results per page. Value must be between 1 and 100.
    """

    page: Optional[int] = 0
    """
    Page number. Value must be greater or equal to 1.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization to filter.
    """

    user_ids: Optional[list[str]] = field(default_factory=list)
    """
    Filter by list of IDs.
    """

    mfa: Optional[bool] = False
    """
    Filter by MFA status.
    """

    tag: Optional[str] = None
    """
    Filter by tags containing a given string.
    """

    type_: Optional[UserType] = UserType.UNKNOWN_TYPE
    """
    Filter by user type.
    """


@dataclass
class ListUsersResponse:
    users: list[User]
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

    login_password_enabled: bool
    """
    Defines whether login with a password is enabled for the Organization.
    """

    login_magic_code_enabled: bool
    """
    Defines whether login with an authentication code is enabled for the Organization.
    """

    login_oauth2_enabled: bool
    """
    Defines whether login through OAuth2 is enabled for the Organization.
    """

    login_saml_enabled: bool
    """
    Defines whether login through SAML is enabled for the Organization.
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

    grace_period_duration: Optional[str] = None
    """
    Duration of the grace period to renew password or enable MFA.
    """

    max_login_session_duration: Optional[str] = None
    """
    Maximum duration a login session will stay active before needing to relogin.
    """

    max_api_key_expiration_duration: Optional[str] = None
    """
    Maximum duration the `expires_at` field of an API key can represent. A value of 0 means there is no maximum duration.
    """


@dataclass
class ParseSamlMetadataRequest:
    file: ScwFile


@dataclass
class ParseSamlMetadataResponse:
    single_sign_on_url: str
    entity_id: str
    signing_certificates: list[str]


@dataclass
class RemoveGroupMemberRequest:
    group_id: str
    """
    ID of the group.
    """

    user_id: Optional[str] = None

    application_id: Optional[str] = None


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

    status: SamlStatus
    """
    Status of the SAML configuration.
    """

    entity_id: str
    """
    Entity ID of the SAML Identity Provider.
    """

    single_sign_on_url: str
    """
    Single Sign-On URL of the SAML Identity Provider.
    """

    service_provider: Optional[SamlServiceProvider] = None
    """
    Service Provider information.
    """


@dataclass
class Scim:
    id: str
    """
    ID of the SCIM configuration.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of SCIM configuration creation.
    """


@dataclass
class SetGroupMembersRequest:
    group_id: str
    user_ids: list[str]
    application_ids: list[str]


@dataclass
class SetOrganizationAliasRequest:
    alias: str
    """
    Alias of the Organization.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization.
    """


@dataclass
class SetRulesRequest:
    policy_id: str
    """
    Id of policy to update.
    """

    rules: list[RuleSpecs]
    """
    Rules of the policy to set.
    """


@dataclass
class SetRulesResponse:
    rules: list[Rule]
    """
    Rules of the policy.
    """


@dataclass
class StartUserWebAuthnRegistrationRequest:
    user_id: str
    """
    The ID of the user on which to start registering a WebAuthn authenticator.
    """

    origin: str
    """
    The URL from which the registration request originated.
    """


@dataclass
class StartUserWebAuthnRegistrationResponse:
    ceremony_id: str
    """
    A unique ID for this registration attempt, to reuse when calling FinishUserWebAuthnRegistration.
    """

    challenge: str
    """
    Random bytes constituting the challenge to solve for the credentials creation.
    """

    public_key_algorithms: list[int]
    """
    List of algorithms supported by the relying party, as COSE algorithm identifiers.
    """

    exclude_credentials: list[str]
    """
    List of credentials that cannot be used to fulfill the ceremony.
    """

    timeout: Optional[str] = None
    """
    Maximum duration of the registration ceremony, in milliseconds.
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

    default_project_id: Optional[str] = None
    """
    New default Project ID to set.
    """

    description: Optional[str] = None
    """
    New description to update.
    """

    expires_at: Optional[datetime] = None
    """
    New expiration date of the API key.
    """


@dataclass
class UpdateApplicationRequest:
    application_id: str
    """
    ID of the application to update.
    """

    name: Optional[str] = None
    """
    New name for the application (max length is 64 chars).
    """

    description: Optional[str] = None
    """
    New description for the application (max length is 200 chars).
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the application (maximum of 10 tags).
    """


@dataclass
class UpdateGroupRequest:
    group_id: str
    """
    ID of the group to update.
    """

    name: Optional[str] = None
    """
    New name for the group (max length is 64 chars). MUST be unique inside an Organization.
    """

    description: Optional[str] = None
    """
    New description for the group (max length is 200 chars).
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the group (maximum of 10 tags).
    """


@dataclass
class UpdateOrganizationLoginMethodsRequest:
    organization_id: Optional[str] = None
    """
    ID of the Organization.
    """

    login_password_enabled: Optional[bool] = False
    """
    Defines whether login with a password is enabled for the Organization.
    """

    login_oauth2_enabled: Optional[bool] = False
    """
    Defines whether login through OAuth2 is enabled for the Organization.
    """

    login_magic_code_enabled: Optional[bool] = False
    """
    Defines whether login with an authentication code is enabled for the Organization.
    """

    login_saml_enabled: Optional[bool] = False
    """
    Defines whether login through SAML is enabled for the Organization.
    """


@dataclass
class UpdateOrganizationSecuritySettingsRequest:
    organization_id: Optional[str] = None
    """
    ID of the Organization.
    """

    enforce_password_renewal: Optional[bool] = False
    """
    Defines whether password renewal is enforced during first login.
    """

    grace_period_duration: Optional[str] = None
    """
    Duration of the grace period to renew password or enable MFA.
    """

    login_attempts_before_locked: Optional[int] = 0
    """
    Number of login attempts before the account is locked.
    """

    max_login_session_duration: Optional[str] = None
    """
    Maximum duration a login session will stay active before needing to relogin.
    """

    max_api_key_expiration_duration: Optional[str] = None
    """
    Maximum duration the `expires_at` field of an API key can represent. A value of 0 means there is no maximum duration.
    """


@dataclass
class UpdatePolicyRequest:
    policy_id: str
    """
    Id of policy to update.
    """

    name: Optional[str] = None
    """
    New name for the policy (max length is 64 characters).
    """

    description: Optional[str] = None
    """
    New description of policy (max length is 200 characters).
    """

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the policy (maximum of 10 tags).
    """

    user_id: Optional[str] = None

    group_id: Optional[str] = None

    application_id: Optional[str] = None

    no_principal: Optional[bool] = False


@dataclass
class UpdateSSHKeyRequest:
    ssh_key_id: str
    name: Optional[str] = None
    """
    Name of the SSH key. Max length is 1000.
    """

    disabled: Optional[bool] = False
    """
    Enable or disable the SSH key.
    """


@dataclass
class UpdateSamlRequest:
    saml_id: str
    """
    ID of the SAML configuration.
    """

    entity_id: Optional[str] = None
    """
    Entity ID of the SAML Identity Provider.
    """

    single_sign_on_url: Optional[str] = None
    """
    Single Sign-On URL of the SAML Identity Provider.
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

    tags: Optional[list[str]] = field(default_factory=list)
    """
    New tags for the user (maximum of 10 tags).
    """

    email: Optional[str] = None
    """
    IAM member email.
    """

    first_name: Optional[str] = None
    """
    IAM member first name.
    """

    last_name: Optional[str] = None
    """
    IAM member last name.
    """

    phone_number: Optional[str] = None
    """
    IAM member phone number.
    """

    locale: Optional[str] = None
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
class UpdateWebAuthnAuthenticatorRequest:
    authenticator_id: str
    """
    The ID of the authenticator to update.
    """

    authenticator_name: Optional[str] = None
    """
    A new name for this authenticator.
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
    recovery_codes: list[str]
    """
    List of recovery codes usable for this OTP method.
    """
