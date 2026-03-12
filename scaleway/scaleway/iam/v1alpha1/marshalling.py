# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    marshal_ScwFile,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    GracePeriodType,
    LocalityType,
    LogAction,
    LogResourceType,
    PermissionSetScopeType,
    SamlCertificateOrigin,
    SamlCertificateType,
    SamlStatus,
    UserStatus,
    UserType,
    JWT,
    APIKey,
    Application,
    Group,
    Log,
    Policy,
    QuotumLimit,
    Quotum,
    SSHKey,
    SamlCertificate,
    WebAuthnAuthenticator,
    User,
    ScimToken,
    CreateScimTokenResponse,
    EncodedJWT,
    FinishUserWebAuthnRegistrationResponse,
    ConnectionConnectedOrganization,
    ConnectionConnectedUser,
    Connection,
    GetUserConnectionsResponse,
    InitiateUserConnectionResponse,
    ListAPIKeysResponse,
    ListApplicationsResponse,
    GracePeriod,
    ListGracePeriodsResponse,
    ListGroupsResponse,
    ListJWTsResponse,
    ListLogsResponse,
    PermissionSet,
    ListPermissionSetsResponse,
    ListPoliciesResponse,
    ListQuotaResponse,
    Rule,
    ListRulesResponse,
    ListSSHKeysResponse,
    ListSamlCertificatesResponse,
    ListScimTokensResponse,
    ListUserWebAuthnAuthenticatorsResponse,
    ListUsersResponse,
    MFAOTP,
    Organization,
    OrganizationSecuritySettings,
    ParseSamlMetadataResponse,
    SamlServiceProvider,
    Saml,
    Scim,
    SetRulesResponse,
    StartUserWebAuthnRegistrationResponse,
    ValidateUserMFAOTPResponse,
    AddGroupMemberRequest,
    AddGroupMembersRequest,
    AddSamlCertificateRequest,
    CreateAPIKeyRequest,
    CreateApplicationRequest,
    CreateGroupRequest,
    CreateJWTRequest,
    RuleSpecs,
    CreatePolicyRequest,
    CreateSSHKeyRequest,
    CreateUserRequestMember,
    CreateUserRequest,
    FinishUserWebAuthnRegistrationRequest,
    JoinUserConnectionRequest,
    ParseSamlMetadataRequest,
    RemoveGroupMemberRequest,
    RemoveUserConnectionRequest,
    SetGroupMembersRequest,
    SetOrganizationAliasRequest,
    SetRulesRequest,
    UpdateAPIKeyRequest,
    UpdateApplicationRequest,
    UpdateGroupRequest,
    UpdateOrganizationLoginMethodsRequest,
    UpdateOrganizationSecuritySettingsRequest,
    UpdatePolicyRequest,
    UpdateSSHKeyRequest,
    UpdateSamlRequest,
    UpdateUserPasswordRequest,
    UpdateUserRequest,
    UpdateUserUsernameRequest,
    UpdateWebAuthnAuthenticatorRequest,
    ValidateUserMFAOTPRequest,
)


def unmarshal_JWT(data: Any) -> JWT:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JWT' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("jti", None)
    if field is not None:
        args["jti"] = field
    else:
        args["jti"] = None

    field = data.get("issuer_id", None)
    if field is not None:
        args["issuer_id"] = field
    else:
        args["issuer_id"] = None

    field = data.get("audience_id", None)
    if field is not None:
        args["audience_id"] = field
    else:
        args["audience_id"] = None

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field
    else:
        args["ip"] = None

    field = data.get("user_agent", None)
    if field is not None:
        args["user_agent"] = field
    else:
        args["user_agent"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    return JWT(**args)


def unmarshal_APIKey(data: Any) -> APIKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'APIKey' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("access_key", None)
    if field is not None:
        args["access_key"] = field
    else:
        args["access_key"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("default_project_id", None)
    if field is not None:
        args["default_project_id"] = field
    else:
        args["default_project_id"] = None

    field = data.get("secret_key", None)
    if field is not None:
        args["secret_key"] = field
    else:
        args["secret_key"] = None

    field = data.get("application_id", None)
    if field is not None:
        args["application_id"] = field
    else:
        args["application_id"] = None

    field = data.get("editable", None)
    if field is not None:
        args["editable"] = field
    else:
        args["editable"] = False

    field = data.get("deletable", None)
    if field is not None:
        args["deletable"] = field
    else:
        args["deletable"] = False

    field = data.get("managed", None)
    if field is not None:
        args["managed"] = field
    else:
        args["managed"] = False

    field = data.get("creation_ip", None)
    if field is not None:
        args["creation_ip"] = field
    else:
        args["creation_ip"] = None

    field = data.get("user_id", None)
    if field is not None:
        args["user_id"] = field
    else:
        args["user_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    return APIKey(**args)


def unmarshal_Application(data: Any) -> Application:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Application' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("editable", None)
    if field is not None:
        args["editable"] = field
    else:
        args["editable"] = False

    field = data.get("deletable", None)
    if field is not None:
        args["deletable"] = field
    else:
        args["deletable"] = False

    field = data.get("managed", None)
    if field is not None:
        args["managed"] = field
    else:
        args["managed"] = False

    field = data.get("nb_api_keys", None)
    if field is not None:
        args["nb_api_keys"] = field
    else:
        args["nb_api_keys"] = 0

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return Application(**args)


def unmarshal_Group(data: Any) -> Group:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Group' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("user_ids", None)
    if field is not None:
        args["user_ids"] = field
    else:
        args["user_ids"] = []

    field = data.get("application_ids", None)
    if field is not None:
        args["application_ids"] = field
    else:
        args["application_ids"] = []

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("editable", None)
    if field is not None:
        args["editable"] = field
    else:
        args["editable"] = False

    field = data.get("deletable", None)
    if field is not None:
        args["deletable"] = field
    else:
        args["deletable"] = False

    field = data.get("managed", None)
    if field is not None:
        args["managed"] = field
    else:
        args["managed"] = False

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return Group(**args)


def unmarshal_Log(data: Any) -> Log:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Log' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("ip", None)
    if field is not None:
        args["ip"] = field
    else:
        args["ip"] = None

    field = data.get("user_agent", None)
    if field is not None:
        args["user_agent"] = field
    else:
        args["user_agent"] = None

    field = data.get("action", None)
    if field is not None:
        args["action"] = field
    else:
        args["action"] = LogAction.UNKNOWN_ACTION

    field = data.get("bearer_id", None)
    if field is not None:
        args["bearer_id"] = field
    else:
        args["bearer_id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("resource_type", None)
    if field is not None:
        args["resource_type"] = field
    else:
        args["resource_type"] = LogResourceType.UNKNOWN_RESOURCE_TYPE

    field = data.get("resource_id", None)
    if field is not None:
        args["resource_id"] = field
    else:
        args["resource_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return Log(**args)


def unmarshal_Policy(data: Any) -> Policy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Policy' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("editable", None)
    if field is not None:
        args["editable"] = field
    else:
        args["editable"] = False

    field = data.get("deletable", None)
    if field is not None:
        args["deletable"] = field
    else:
        args["deletable"] = False

    field = data.get("managed", None)
    if field is not None:
        args["managed"] = field
    else:
        args["managed"] = False

    field = data.get("nb_rules", None)
    if field is not None:
        args["nb_rules"] = field
    else:
        args["nb_rules"] = 0

    field = data.get("nb_scopes", None)
    if field is not None:
        args["nb_scopes"] = field
    else:
        args["nb_scopes"] = 0

    field = data.get("nb_permission_sets", None)
    if field is not None:
        args["nb_permission_sets"] = field
    else:
        args["nb_permission_sets"] = 0

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("user_id", None)
    if field is not None:
        args["user_id"] = field
    else:
        args["user_id"] = None

    field = data.get("group_id", None)
    if field is not None:
        args["group_id"] = field
    else:
        args["group_id"] = None

    field = data.get("application_id", None)
    if field is not None:
        args["application_id"] = field
    else:
        args["application_id"] = None

    field = data.get("no_principal", None)
    if field is not None:
        args["no_principal"] = field
    else:
        args["no_principal"] = False

    return Policy(**args)


def unmarshal_QuotumLimit(data: Any) -> QuotumLimit:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QuotumLimit' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("global", None)
    if field is not None:
        args["global_"] = field
    else:
        args["global_"] = False

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("limit", None)
    if field is not None:
        args["limit"] = field
    else:
        args["limit"] = 0

    field = data.get("unlimited", None)
    if field is not None:
        args["unlimited"] = field
    else:
        args["unlimited"] = False

    return QuotumLimit(**args)


def unmarshal_Quotum(data: Any) -> Quotum:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Quotum' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("pretty_name", None)
    if field is not None:
        args["pretty_name"] = field
    else:
        args["pretty_name"] = None

    field = data.get("unit", None)
    if field is not None:
        args["unit"] = field
    else:
        args["unit"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("locality_type", None)
    if field is not None:
        args["locality_type"] = field
    else:
        args["locality_type"] = LocalityType.GLOBAL

    field = data.get("limits", None)
    if field is not None:
        args["limits"] = (
            [unmarshal_QuotumLimit(v) for v in field] if field is not None else None
        )
    else:
        args["limits"] = []

    field = data.get("limit", None)
    if field is not None:
        args["limit"] = field
    else:
        args["limit"] = 0

    field = data.get("unlimited", None)
    if field is not None:
        args["unlimited"] = field
    else:
        args["unlimited"] = False

    return Quotum(**args)


def unmarshal_SSHKey(data: Any) -> SSHKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SSHKey' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("public_key", None)
    if field is not None:
        args["public_key"] = field
    else:
        args["public_key"] = None

    field = data.get("fingerprint", None)
    if field is not None:
        args["fingerprint"] = field
    else:
        args["fingerprint"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("disabled", None)
    if field is not None:
        args["disabled"] = field
    else:
        args["disabled"] = False

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return SSHKey(**args)


def unmarshal_SamlCertificate(data: Any) -> SamlCertificate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SamlCertificate' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = SamlCertificateType.UNKNOWN_CERTIFICATE_TYPE

    field = data.get("origin", None)
    if field is not None:
        args["origin"] = field
    else:
        args["origin"] = SamlCertificateOrigin.UNKNOWN_CERTIFICATE_ORIGIN

    field = data.get("content", None)
    if field is not None:
        args["content"] = field
    else:
        args["content"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    return SamlCertificate(**args)


def unmarshal_WebAuthnAuthenticator(data: Any) -> WebAuthnAuthenticator:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'WebAuthnAuthenticator' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("last_login_at", None)
    if field is not None:
        args["last_login_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_login_at"] = None

    return WebAuthnAuthenticator(**args)


def unmarshal_User(data: Any) -> User:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("email", None)
    if field is not None:
        args["email"] = field
    else:
        args["email"] = None

    field = data.get("username", None)
    if field is not None:
        args["username"] = field
    else:
        args["username"] = None

    field = data.get("first_name", None)
    if field is not None:
        args["first_name"] = field
    else:
        args["first_name"] = None

    field = data.get("last_name", None)
    if field is not None:
        args["last_name"] = field
    else:
        args["last_name"] = None

    field = data.get("phone_number", None)
    if field is not None:
        args["phone_number"] = field
    else:
        args["phone_number"] = None

    field = data.get("locale", None)
    if field is not None:
        args["locale"] = field
    else:
        args["locale"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("deletable", None)
    if field is not None:
        args["deletable"] = field
    else:
        args["deletable"] = False

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("last_login_at", None)
    if field is not None:
        args["last_login_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_login_at"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = UserType.UNKNOWN_TYPE

    field = data.get("two_factor_enabled", None)
    if field is not None:
        args["two_factor_enabled"] = field
    else:
        args["two_factor_enabled"] = False

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = UserStatus.UNKNOWN_STATUS

    field = data.get("mfa", None)
    if field is not None:
        args["mfa"] = field
    else:
        args["mfa"] = False

    field = data.get("account_root_user_id", None)
    if field is not None:
        args["account_root_user_id"] = field
    else:
        args["account_root_user_id"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("locked", None)
    if field is not None:
        args["locked"] = field
    else:
        args["locked"] = False

    return User(**args)


def unmarshal_ScimToken(data: Any) -> ScimToken:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ScimToken' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("scim_id", None)
    if field is not None:
        args["scim_id"] = field
    else:
        args["scim_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    return ScimToken(**args)


def unmarshal_CreateScimTokenResponse(data: Any) -> CreateScimTokenResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateScimTokenResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("bearer_token", None)
    if field is not None:
        args["bearer_token"] = field
    else:
        args["bearer_token"] = None

    field = data.get("token", None)
    if field is not None:
        args["token"] = unmarshal_ScimToken(field)
    else:
        args["token"] = None

    return CreateScimTokenResponse(**args)


def unmarshal_EncodedJWT(data: Any) -> EncodedJWT:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EncodedJWT' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("token", None)
    if field is not None:
        args["token"] = field
    else:
        args["token"] = None

    field = data.get("renew_token", None)
    if field is not None:
        args["renew_token"] = field
    else:
        args["renew_token"] = None

    field = data.get("jwt", None)
    if field is not None:
        args["jwt"] = unmarshal_JWT(field)
    else:
        args["jwt"] = None

    return EncodedJWT(**args)


def unmarshal_FinishUserWebAuthnRegistrationResponse(
    data: Any,
) -> FinishUserWebAuthnRegistrationResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'FinishUserWebAuthnRegistrationResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("authenticator_id", None)
    if field is not None:
        args["authenticator_id"] = field
    else:
        args["authenticator_id"] = None

    return FinishUserWebAuthnRegistrationResponse(**args)


def unmarshal_ConnectionConnectedOrganization(
    data: Any,
) -> ConnectionConnectedOrganization:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ConnectionConnectedOrganization' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("locked", None)
    if field is not None:
        args["locked"] = field
    else:
        args["locked"] = None

    return ConnectionConnectedOrganization(**args)


def unmarshal_ConnectionConnectedUser(data: Any) -> ConnectionConnectedUser:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ConnectionConnectedUser' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("username", None)
    if field is not None:
        args["username"] = field
    else:
        args["username"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return ConnectionConnectedUser(**args)


def unmarshal_Connection(data: Any) -> Connection:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Connection' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("organization", None)
    if field is not None:
        args["organization"] = unmarshal_ConnectionConnectedOrganization(field)
    else:
        args["organization"] = None

    field = data.get("user", None)
    if field is not None:
        args["user"] = unmarshal_ConnectionConnectedUser(field)
    else:
        args["user"] = None

    return Connection(**args)


def unmarshal_GetUserConnectionsResponse(data: Any) -> GetUserConnectionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetUserConnectionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("connections", None)
    if field is not None:
        args["connections"] = (
            [unmarshal_Connection(v) for v in field] if field is not None else None
        )
    else:
        args["connections"] = []

    return GetUserConnectionsResponse(**args)


def unmarshal_InitiateUserConnectionResponse(
    data: Any,
) -> InitiateUserConnectionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InitiateUserConnectionResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("token", None)
    if field is not None:
        args["token"] = field
    else:
        args["token"] = None

    return InitiateUserConnectionResponse(**args)


def unmarshal_ListAPIKeysResponse(data: Any) -> ListAPIKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAPIKeysResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("api_keys", None)
    if field is not None:
        args["api_keys"] = (
            [unmarshal_APIKey(v) for v in field] if field is not None else None
        )
    else:
        args["api_keys"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListAPIKeysResponse(**args)


def unmarshal_ListApplicationsResponse(data: Any) -> ListApplicationsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListApplicationsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("applications", None)
    if field is not None:
        args["applications"] = (
            [unmarshal_Application(v) for v in field] if field is not None else None
        )
    else:
        args["applications"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListApplicationsResponse(**args)


def unmarshal_GracePeriod(data: Any) -> GracePeriod:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GracePeriod' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = GracePeriodType.UNKNOWN_GRACE_PERIOD_TYPE

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    return GracePeriod(**args)


def unmarshal_ListGracePeriodsResponse(data: Any) -> ListGracePeriodsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGracePeriodsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("grace_periods", None)
    if field is not None:
        args["grace_periods"] = (
            [unmarshal_GracePeriod(v) for v in field] if field is not None else None
        )
    else:
        args["grace_periods"] = []

    return ListGracePeriodsResponse(**args)


def unmarshal_ListGroupsResponse(data: Any) -> ListGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGroupsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("groups", None)
    if field is not None:
        args["groups"] = (
            [unmarshal_Group(v) for v in field] if field is not None else None
        )
    else:
        args["groups"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListGroupsResponse(**args)


def unmarshal_ListJWTsResponse(data: Any) -> ListJWTsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJWTsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("jwts", None)
    if field is not None:
        args["jwts"] = [unmarshal_JWT(v) for v in field] if field is not None else None
    else:
        args["jwts"] = None

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    return ListJWTsResponse(**args)


def unmarshal_ListLogsResponse(data: Any) -> ListLogsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLogsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("logs", None)
    if field is not None:
        args["logs"] = [unmarshal_Log(v) for v in field] if field is not None else None
    else:
        args["logs"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListLogsResponse(**args)


def unmarshal_PermissionSet(data: Any) -> PermissionSet:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PermissionSet' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("scope_type", None)
    if field is not None:
        args["scope_type"] = field
    else:
        args["scope_type"] = PermissionSetScopeType.UNKNOWN_SCOPE_TYPE

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("categories", None)
    if field is not None:
        args["categories"] = field
    else:
        args["categories"] = []

    return PermissionSet(**args)


def unmarshal_ListPermissionSetsResponse(data: Any) -> ListPermissionSetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPermissionSetsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("permission_sets", None)
    if field is not None:
        args["permission_sets"] = (
            [unmarshal_PermissionSet(v) for v in field] if field is not None else None
        )
    else:
        args["permission_sets"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListPermissionSetsResponse(**args)


def unmarshal_ListPoliciesResponse(data: Any) -> ListPoliciesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPoliciesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("policies", None)
    if field is not None:
        args["policies"] = (
            [unmarshal_Policy(v) for v in field] if field is not None else None
        )
    else:
        args["policies"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListPoliciesResponse(**args)


def unmarshal_ListQuotaResponse(data: Any) -> ListQuotaResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListQuotaResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("quota", None)
    if field is not None:
        args["quota"] = (
            [unmarshal_Quotum(v) for v in field] if field is not None else None
        )
    else:
        args["quota"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListQuotaResponse(**args)


def unmarshal_Rule(data: Any) -> Rule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Rule' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("permission_sets_scope_type", None)
    if field is not None:
        args["permission_sets_scope_type"] = field
    else:
        args["permission_sets_scope_type"] = PermissionSetScopeType.UNKNOWN_SCOPE_TYPE

    field = data.get("condition", None)
    if field is not None:
        args["condition"] = field
    else:
        args["condition"] = None

    field = data.get("permission_set_names", None)
    if field is not None:
        args["permission_set_names"] = field
    else:
        args["permission_set_names"] = []

    field = data.get("project_ids", None)
    if field is not None:
        args["project_ids"] = field
    else:
        args["project_ids"] = []

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("account_root_user_id", None)
    if field is not None:
        args["account_root_user_id"] = field
    else:
        args["account_root_user_id"] = None

    return Rule(**args)


def unmarshal_ListRulesResponse(data: Any) -> ListRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_Rule(v) for v in field] if field is not None else None
        )
    else:
        args["rules"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListRulesResponse(**args)


def unmarshal_ListSSHKeysResponse(data: Any) -> ListSSHKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSSHKeysResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ssh_keys", None)
    if field is not None:
        args["ssh_keys"] = (
            [unmarshal_SSHKey(v) for v in field] if field is not None else None
        )
    else:
        args["ssh_keys"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListSSHKeysResponse(**args)


def unmarshal_ListSamlCertificatesResponse(data: Any) -> ListSamlCertificatesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSamlCertificatesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("certificates", None)
    if field is not None:
        args["certificates"] = (
            [unmarshal_SamlCertificate(v) for v in field] if field is not None else None
        )
    else:
        args["certificates"] = []

    return ListSamlCertificatesResponse(**args)


def unmarshal_ListScimTokensResponse(data: Any) -> ListScimTokensResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListScimTokensResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("scim_tokens", None)
    if field is not None:
        args["scim_tokens"] = (
            [unmarshal_ScimToken(v) for v in field] if field is not None else None
        )
    else:
        args["scim_tokens"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListScimTokensResponse(**args)


def unmarshal_ListUserWebAuthnAuthenticatorsResponse(
    data: Any,
) -> ListUserWebAuthnAuthenticatorsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListUserWebAuthnAuthenticatorsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("authenticators", None)
    if field is not None:
        args["authenticators"] = (
            [unmarshal_WebAuthnAuthenticator(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["authenticators"] = []

    return ListUserWebAuthnAuthenticatorsResponse(**args)


def unmarshal_ListUsersResponse(data: Any) -> ListUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListUsersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("users", None)
    if field is not None:
        args["users"] = (
            [unmarshal_User(v) for v in field] if field is not None else None
        )
    else:
        args["users"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListUsersResponse(**args)


def unmarshal_MFAOTP(data: Any) -> MFAOTP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MFAOTP' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("secret", None)
    if field is not None:
        args["secret"] = field
    else:
        args["secret"] = None

    return MFAOTP(**args)


def unmarshal_Organization(data: Any) -> Organization:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Organization' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("alias", None)
    if field is not None:
        args["alias"] = field
    else:
        args["alias"] = None

    field = data.get("login_password_enabled", None)
    if field is not None:
        args["login_password_enabled"] = field
    else:
        args["login_password_enabled"] = False

    field = data.get("login_magic_code_enabled", None)
    if field is not None:
        args["login_magic_code_enabled"] = field
    else:
        args["login_magic_code_enabled"] = False

    field = data.get("login_oauth2_enabled", None)
    if field is not None:
        args["login_oauth2_enabled"] = field
    else:
        args["login_oauth2_enabled"] = False

    field = data.get("login_saml_enabled", None)
    if field is not None:
        args["login_saml_enabled"] = field
    else:
        args["login_saml_enabled"] = False

    return Organization(**args)


def unmarshal_OrganizationSecuritySettings(data: Any) -> OrganizationSecuritySettings:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OrganizationSecuritySettings' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("enforce_password_renewal", None)
    if field is not None:
        args["enforce_password_renewal"] = field
    else:
        args["enforce_password_renewal"] = False

    field = data.get("login_attempts_before_locked", None)
    if field is not None:
        args["login_attempts_before_locked"] = field
    else:
        args["login_attempts_before_locked"] = 0

    field = data.get("grace_period_duration", None)
    if field is not None:
        args["grace_period_duration"] = field
    else:
        args["grace_period_duration"] = None

    field = data.get("max_login_session_duration", None)
    if field is not None:
        args["max_login_session_duration"] = field
    else:
        args["max_login_session_duration"] = None

    field = data.get("max_api_key_expiration_duration", None)
    if field is not None:
        args["max_api_key_expiration_duration"] = field
    else:
        args["max_api_key_expiration_duration"] = None

    return OrganizationSecuritySettings(**args)


def unmarshal_ParseSamlMetadataResponse(data: Any) -> ParseSamlMetadataResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ParseSamlMetadataResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("single_sign_on_url", None)
    if field is not None:
        args["single_sign_on_url"] = field
    else:
        args["single_sign_on_url"] = None

    field = data.get("entity_id", None)
    if field is not None:
        args["entity_id"] = field
    else:
        args["entity_id"] = None

    field = data.get("signing_certificates", None)
    if field is not None:
        args["signing_certificates"] = field
    else:
        args["signing_certificates"] = None

    return ParseSamlMetadataResponse(**args)


def unmarshal_SamlServiceProvider(data: Any) -> SamlServiceProvider:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SamlServiceProvider' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("entity_id", None)
    if field is not None:
        args["entity_id"] = field
    else:
        args["entity_id"] = None

    field = data.get("assertion_consumer_service_url", None)
    if field is not None:
        args["assertion_consumer_service_url"] = field
    else:
        args["assertion_consumer_service_url"] = None

    return SamlServiceProvider(**args)


def unmarshal_Saml(data: Any) -> Saml:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Saml' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = SamlStatus.UNKNOWN_SAML_STATUS

    field = data.get("entity_id", None)
    if field is not None:
        args["entity_id"] = field
    else:
        args["entity_id"] = None

    field = data.get("single_sign_on_url", None)
    if field is not None:
        args["single_sign_on_url"] = field
    else:
        args["single_sign_on_url"] = None

    field = data.get("service_provider", None)
    if field is not None:
        args["service_provider"] = unmarshal_SamlServiceProvider(field)
    else:
        args["service_provider"] = None

    return Saml(**args)


def unmarshal_Scim(data: Any) -> Scim:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Scim' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return Scim(**args)


def unmarshal_SetRulesResponse(data: Any) -> SetRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rules", None)
    if field is not None:
        args["rules"] = (
            [unmarshal_Rule(v) for v in field] if field is not None else None
        )
    else:
        args["rules"] = []

    return SetRulesResponse(**args)


def unmarshal_StartUserWebAuthnRegistrationResponse(
    data: Any,
) -> StartUserWebAuthnRegistrationResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'StartUserWebAuthnRegistrationResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ceremony_id", None)
    if field is not None:
        args["ceremony_id"] = field
    else:
        args["ceremony_id"] = None

    field = data.get("challenge", None)
    if field is not None:
        args["challenge"] = field
    else:
        args["challenge"] = None

    field = data.get("public_key_algorithms", None)
    if field is not None:
        args["public_key_algorithms"] = field
    else:
        args["public_key_algorithms"] = []

    field = data.get("exclude_credentials", None)
    if field is not None:
        args["exclude_credentials"] = field
    else:
        args["exclude_credentials"] = []

    field = data.get("timeout", None)
    if field is not None:
        args["timeout"] = field
    else:
        args["timeout"] = None

    return StartUserWebAuthnRegistrationResponse(**args)


def unmarshal_ValidateUserMFAOTPResponse(data: Any) -> ValidateUserMFAOTPResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ValidateUserMFAOTPResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("recovery_codes", None)
    if field is not None:
        args["recovery_codes"] = field
    else:
        args["recovery_codes"] = []

    return ValidateUserMFAOTPResponse(**args)


def marshal_AddGroupMemberRequest(
    request: AddGroupMemberRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="user_id", value=request.user_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="application_id",
                    value=request.application_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    return output


def marshal_AddGroupMembersRequest(
    request: AddGroupMembersRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.user_ids is not None:
        output["user_ids"] = request.user_ids

    if request.application_ids is not None:
        output["application_ids"] = request.application_ids

    return output


def marshal_AddSamlCertificateRequest(
    request: AddSamlCertificateRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_

    if request.content is not None:
        output["content"] = request.content

    return output


def marshal_CreateAPIKeyRequest(
    request: CreateAPIKeyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="application_id",
                    value=request.application_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="user_id", value=request.user_id, marshal_func=None
                ),
            ]
        ),
    )

    if request.description is not None:
        output["description"] = request.description

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    if request.default_project_id is not None:
        output["default_project_id"] = request.default_project_id

    return output


def marshal_CreateApplicationRequest(
    request: CreateApplicationRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateGroupRequest(
    request: CreateGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.name is not None:
        output["name"] = request.name

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateJWTRequest(
    request: CreateJWTRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.user_id is not None:
        output["user_id"] = request.user_id

    if request.referrer is not None:
        output["referrer"] = request.referrer

    return output


def marshal_RuleSpecs(
    request: RuleSpecs,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="project_ids", value=request.project_ids, marshal_func=None
                ),
                OneOfPossibility(
                    param="organization_id",
                    value=request.organization_id,
                    default=defaults.default_organization_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.condition is not None:
        output["condition"] = request.condition

    if request.permission_set_names is not None:
        output["permission_set_names"] = request.permission_set_names

    return output


def marshal_CreatePolicyRequest(
    request: CreatePolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="user_id", value=request.user_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="group_id", value=request.group_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="application_id",
                    value=request.application_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="no_principal", value=request.no_principal, marshal_func=None
                ),
            ]
        ),
    )

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.rules is not None:
        output["rules"] = [marshal_RuleSpecs(item, defaults) for item in request.rules]

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_CreateSSHKeyRequest(
    request: CreateSSHKeyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.public_key is not None:
        output["public_key"] = request.public_key

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_CreateUserRequestMember(
    request: CreateUserRequestMember,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    if request.send_password_email is not None:
        output["send_password_email"] = request.send_password_email

    if request.send_welcome_email is not None:
        output["send_welcome_email"] = request.send_welcome_email

    if request.username is not None:
        output["username"] = request.username

    if request.password is not None:
        output["password"] = request.password

    if request.first_name is not None:
        output["first_name"] = request.first_name

    if request.last_name is not None:
        output["last_name"] = request.last_name

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number

    if request.locale is not None:
        output["locale"] = request.locale

    return output


def marshal_CreateUserRequest(
    request: CreateUserRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(param="email", value=request.email, marshal_func=None),
                OneOfPossibility(
                    param="member",
                    value=request.member,
                    marshal_func=marshal_CreateUserRequestMember,
                ),
            ]
        ),
    )

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_FinishUserWebAuthnRegistrationRequest(
    request: FinishUserWebAuthnRegistrationRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.ceremony_id is not None:
        output["ceremony_id"] = request.ceremony_id

    if request.authenticator_name is not None:
        output["authenticator_name"] = request.authenticator_name

    if request.origin is not None:
        output["origin"] = request.origin

    if request.raw_id is not None:
        output["raw_id"] = request.raw_id

    if request.client_data_json is not None:
        output["client_data_json"] = request.client_data_json

    if request.authenticator_data is not None:
        output["authenticator_data"] = request.authenticator_data

    if request.attestation_object is not None:
        output["attestation_object"] = request.attestation_object

    if request.public_key is not None:
        output["public_key"] = request.public_key

    if request.public_key_algorithm is not None:
        output["public_key_algorithm"] = request.public_key_algorithm

    return output


def marshal_JoinUserConnectionRequest(
    request: JoinUserConnectionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.token is not None:
        output["token"] = request.token

    return output


def marshal_ParseSamlMetadataRequest(
    request: ParseSamlMetadataRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.file is not None:
        output["file"] = marshal_ScwFile(request.file, defaults)

    return output


def marshal_RemoveGroupMemberRequest(
    request: RemoveGroupMemberRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="user_id", value=request.user_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="application_id",
                    value=request.application_id,
                    marshal_func=None,
                ),
            ]
        ),
    )

    return output


def marshal_RemoveUserConnectionRequest(
    request: RemoveUserConnectionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.target_user_id is not None:
        output["target_user_id"] = request.target_user_id

    return output


def marshal_SetGroupMembersRequest(
    request: SetGroupMembersRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.user_ids is not None:
        output["user_ids"] = request.user_ids

    if request.application_ids is not None:
        output["application_ids"] = request.application_ids

    return output


def marshal_SetOrganizationAliasRequest(
    request: SetOrganizationAliasRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.alias is not None:
        output["alias"] = request.alias

    return output


def marshal_SetRulesRequest(
    request: SetRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.policy_id is not None:
        output["policy_id"] = request.policy_id

    if request.rules is not None:
        output["rules"] = [marshal_RuleSpecs(item, defaults) for item in request.rules]

    return output


def marshal_UpdateAPIKeyRequest(
    request: UpdateAPIKeyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.default_project_id is not None:
        output["default_project_id"] = request.default_project_id

    if request.description is not None:
        output["description"] = request.description

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()

    return output


def marshal_UpdateApplicationRequest(
    request: UpdateApplicationRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateGroupRequest(
    request: UpdateGroupRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateOrganizationLoginMethodsRequest(
    request: UpdateOrganizationLoginMethodsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.login_password_enabled is not None:
        output["login_password_enabled"] = request.login_password_enabled

    if request.login_oauth2_enabled is not None:
        output["login_oauth2_enabled"] = request.login_oauth2_enabled

    if request.login_magic_code_enabled is not None:
        output["login_magic_code_enabled"] = request.login_magic_code_enabled

    if request.login_saml_enabled is not None:
        output["login_saml_enabled"] = request.login_saml_enabled

    return output


def marshal_UpdateOrganizationSecuritySettingsRequest(
    request: UpdateOrganizationSecuritySettingsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.enforce_password_renewal is not None:
        output["enforce_password_renewal"] = request.enforce_password_renewal

    if request.grace_period_duration is not None:
        output["grace_period_duration"] = request.grace_period_duration

    if request.login_attempts_before_locked is not None:
        output["login_attempts_before_locked"] = request.login_attempts_before_locked

    if request.max_login_session_duration is not None:
        output["max_login_session_duration"] = request.max_login_session_duration

    if request.max_api_key_expiration_duration is not None:
        output["max_api_key_expiration_duration"] = (
            request.max_api_key_expiration_duration
        )

    return output


def marshal_UpdatePolicyRequest(
    request: UpdatePolicyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="user_id", value=request.user_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="group_id", value=request.group_id, marshal_func=None
                ),
                OneOfPossibility(
                    param="application_id",
                    value=request.application_id,
                    marshal_func=None,
                ),
                OneOfPossibility(
                    param="no_principal", value=request.no_principal, marshal_func=None
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateSSHKeyRequest(
    request: UpdateSSHKeyRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.disabled is not None:
        output["disabled"] = request.disabled

    return output


def marshal_UpdateSamlRequest(
    request: UpdateSamlRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.entity_id is not None:
        output["entity_id"] = request.entity_id

    if request.single_sign_on_url is not None:
        output["single_sign_on_url"] = request.single_sign_on_url

    return output


def marshal_UpdateUserPasswordRequest(
    request: UpdateUserPasswordRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_UpdateUserRequest(
    request: UpdateUserRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags

    if request.email is not None:
        output["email"] = request.email

    if request.first_name is not None:
        output["first_name"] = request.first_name

    if request.last_name is not None:
        output["last_name"] = request.last_name

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number

    if request.locale is not None:
        output["locale"] = request.locale

    return output


def marshal_UpdateUserUsernameRequest(
    request: UpdateUserUsernameRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    return output


def marshal_UpdateWebAuthnAuthenticatorRequest(
    request: UpdateWebAuthnAuthenticatorRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.authenticator_name is not None:
        output["authenticator_name"] = request.authenticator_name

    return output


def marshal_ValidateUserMFAOTPRequest(
    request: ValidateUserMFAOTPRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.one_time_password is not None:
        output["one_time_password"] = request.one_time_password

    return output
