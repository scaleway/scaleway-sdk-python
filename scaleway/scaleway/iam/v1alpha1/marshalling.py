# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    BearerType,
    GracePeriodType,
    ListAPIKeysRequestOrderBy,
    ListApplicationsRequestOrderBy,
    ListGroupsRequestOrderBy,
    ListJWTsRequestOrderBy,
    ListLogsRequestOrderBy,
    ListPermissionSetsRequestOrderBy,
    ListPoliciesRequestOrderBy,
    ListQuotaRequestOrderBy,
    ListSSHKeysRequestOrderBy,
    ListUsersRequestOrderBy,
    LocalityType,
    LogAction,
    LogResourceType,
    PermissionSetScopeType,
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
    User,
    EncodedJWT,
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
    ListUsersResponse,
    MFAOTP,
    Organization,
    OrganizationSecuritySettings,
    SetRulesResponse,
    ValidateUserMFAOTPResponse,
    AddGroupMemberRequest,
    AddGroupMembersRequest,
    CreateAPIKeyRequest,
    CreateApplicationRequest,
    CreateGroupRequest,
    CreateJWTRequest,
    RuleSpecs,
    CreatePolicyRequest,
    CreateSSHKeyRequest,
    CreateUserRequestMember,
    CreateUserRequest,
    JoinUserConnectionRequest,
    RemoveGroupMemberRequest,
    RemoveUserConnectionRequest,
    SetGroupMembersRequest,
    SetOrganizationAliasRequest,
    SetRulesRequest,
    UpdateAPIKeyRequest,
    UpdateApplicationRequest,
    UpdateGroupRequest,
    UpdateOrganizationSecuritySettingsRequest,
    UpdatePolicyRequest,
    UpdateSSHKeyRequest,
    UpdateUserPasswordRequest,
    UpdateUserRequest,
    UpdateUserUsernameRequest,
    ValidateUserMFAOTPRequest,
)

def unmarshal_JWT(data: Any) -> JWT:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'JWT' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("jti", str())
    args["jti"] = field

    field = data.get("issuer_id", str())
    args["issuer_id"] = field

    field = data.get("audience_id", str())
    args["audience_id"] = field

    field = data.get("ip", str())
    args["ip"] = field

    field = data.get("user_agent", str())
    args["user_agent"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return JWT(**args)

def unmarshal_APIKey(data: Any) -> APIKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'APIKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("access_key", str())
    args["access_key"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("default_project_id", str())
    args["default_project_id"] = field

    field = data.get("secret_key", None)
    args["secret_key"] = field

    field = data.get("application_id", None)
    args["application_id"] = field

    field = data.get("editable", False)
    args["editable"] = field

    field = data.get("deletable", False)
    args["deletable"] = field

    field = data.get("managed", False)
    args["managed"] = field

    field = data.get("creation_ip", str())
    args["creation_ip"] = field

    field = data.get("user_id", None)
    args["user_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return APIKey(**args)

def unmarshal_Application(data: Any) -> Application:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Application' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("editable", False)
    args["editable"] = field

    field = data.get("deletable", False)
    args["deletable"] = field

    field = data.get("managed", False)
    args["managed"] = field

    field = data.get("nb_api_keys", 0)
    args["nb_api_keys"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Application(**args)

def unmarshal_Group(data: Any) -> Group:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Group' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("user_ids", [])
    args["user_ids"] = field

    field = data.get("application_ids", [])
    args["application_ids"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("editable", False)
    args["editable"] = field

    field = data.get("deletable", False)
    args["deletable"] = field

    field = data.get("managed", False)
    args["managed"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Group(**args)

def unmarshal_Log(data: Any) -> Log:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Log' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("ip", str())
    args["ip"] = field

    field = data.get("user_agent", str())
    args["user_agent"] = field

    field = data.get("action", getattr(LogAction, "UNKNOWN_ACTION"))
    args["action"] = field

    field = data.get("bearer_id", str())
    args["bearer_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("resource_type", getattr(LogResourceType, "UNKNOWN_RESOURCE_TYPE"))
    args["resource_type"] = field

    field = data.get("resource_id", str())
    args["resource_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Log(**args)

def unmarshal_Policy(data: Any) -> Policy:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Policy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("editable", False)
    args["editable"] = field

    field = data.get("deletable", False)
    args["deletable"] = field

    field = data.get("managed", False)
    args["managed"] = field

    field = data.get("nb_rules", 0)
    args["nb_rules"] = field

    field = data.get("nb_scopes", 0)
    args["nb_scopes"] = field

    field = data.get("nb_permission_sets", 0)
    args["nb_permission_sets"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("user_id", None)
    args["user_id"] = field

    field = data.get("group_id", None)
    args["group_id"] = field

    field = data.get("application_id", None)
    args["application_id"] = field

    field = data.get("no_principal", None)
    args["no_principal"] = field

    return Policy(**args)

def unmarshal_QuotumLimit(data: Any) -> QuotumLimit:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QuotumLimit' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("global", None)
    args["global_"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("zone", None)
    args["zone"] = field

    field = data.get("limit", None)
    args["limit"] = field

    field = data.get("unlimited", None)
    args["unlimited"] = field

    return QuotumLimit(**args)

def unmarshal_Quotum(data: Any) -> Quotum:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Quotum' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("pretty_name", str())
    args["pretty_name"] = field

    field = data.get("unit", str())
    args["unit"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("locality_type", getattr(LocalityType, "GLOBAL"))
    args["locality_type"] = field

    field = data.get("limits", [])
    args["limits"] = [unmarshal_QuotumLimit(v) for v in field] if field is not None else None

    field = data.get("limit", None)
    args["limit"] = field

    field = data.get("unlimited", None)
    args["unlimited"] = field

    return Quotum(**args)

def unmarshal_SSHKey(data: Any) -> SSHKey:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SSHKey' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("public_key", str())
    args["public_key"] = field

    field = data.get("fingerprint", str())
    args["fingerprint"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("disabled", False)
    args["disabled"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return SSHKey(**args)

def unmarshal_User(data: Any) -> User:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'User' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("email", str())
    args["email"] = field

    field = data.get("username", str())
    args["username"] = field

    field = data.get("first_name", str())
    args["first_name"] = field

    field = data.get("last_name", str())
    args["last_name"] = field

    field = data.get("phone_number", str())
    args["phone_number"] = field

    field = data.get("locale", str())
    args["locale"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("deletable", False)
    args["deletable"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("last_login_at", None)
    args["last_login_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("type", getattr(UserType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("status", getattr(UserStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("mfa", False)
    args["mfa"] = field

    field = data.get("account_root_user_id", str())
    args["account_root_user_id"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("locked", False)
    args["locked"] = field

    field = data.get("two_factor_enabled", None)
    args["two_factor_enabled"] = field

    return User(**args)

def unmarshal_EncodedJWT(data: Any) -> EncodedJWT:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EncodedJWT' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("token", str())
    args["token"] = field

    field = data.get("renew_token", str())
    args["renew_token"] = field

    field = data.get("jwt", None)
    args["jwt"] = unmarshal_JWT(field) if field is not None else None

    return EncodedJWT(**args)

def unmarshal_ConnectionConnectedOrganization(data: Any) -> ConnectionConnectedOrganization:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ConnectionConnectedOrganization' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("locked", str())
    args["locked"] = field

    return ConnectionConnectedOrganization(**args)

def unmarshal_ConnectionConnectedUser(data: Any) -> ConnectionConnectedUser:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ConnectionConnectedUser' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("username", str())
    args["username"] = field

    field = data.get("type", str())
    args["type_"] = field

    return ConnectionConnectedUser(**args)

def unmarshal_Connection(data: Any) -> Connection:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Connection' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("organization", None)
    args["organization"] = unmarshal_ConnectionConnectedOrganization(field) if field is not None else None

    field = data.get("user", None)
    args["user"] = unmarshal_ConnectionConnectedUser(field) if field is not None else None

    return Connection(**args)

def unmarshal_GetUserConnectionsResponse(data: Any) -> GetUserConnectionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetUserConnectionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("connections", [])
    args["connections"] = [unmarshal_Connection(v) for v in field] if field is not None else None

    return GetUserConnectionsResponse(**args)

def unmarshal_InitiateUserConnectionResponse(data: Any) -> InitiateUserConnectionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InitiateUserConnectionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("token", str())
    args["token"] = field

    return InitiateUserConnectionResponse(**args)

def unmarshal_ListAPIKeysResponse(data: Any) -> ListAPIKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAPIKeysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("api_keys", [])
    args["api_keys"] = [unmarshal_APIKey(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListAPIKeysResponse(**args)

def unmarshal_ListApplicationsResponse(data: Any) -> ListApplicationsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListApplicationsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("applications", [])
    args["applications"] = [unmarshal_Application(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListApplicationsResponse(**args)

def unmarshal_GracePeriod(data: Any) -> GracePeriod:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GracePeriod' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(GracePeriodType, "UNKNOWN_GRACE_PERIOD_TYPE"))
    args["type_"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return GracePeriod(**args)

def unmarshal_ListGracePeriodsResponse(data: Any) -> ListGracePeriodsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGracePeriodsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("grace_periods", [])
    args["grace_periods"] = [unmarshal_GracePeriod(v) for v in field] if field is not None else None

    return ListGracePeriodsResponse(**args)

def unmarshal_ListGroupsResponse(data: Any) -> ListGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("groups", [])
    args["groups"] = [unmarshal_Group(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListGroupsResponse(**args)

def unmarshal_ListJWTsResponse(data: Any) -> ListJWTsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListJWTsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("jwts", str())
    args["jwts"] = [unmarshal_JWT(v) for v in field] if field is not None else None

    field = data.get("total_count", str())
    args["total_count"] = field

    return ListJWTsResponse(**args)

def unmarshal_ListLogsResponse(data: Any) -> ListLogsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLogsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("logs", [])
    args["logs"] = [unmarshal_Log(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListLogsResponse(**args)

def unmarshal_PermissionSet(data: Any) -> PermissionSet:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PermissionSet' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("scope_type", getattr(PermissionSetScopeType, "UNKNOWN_SCOPE_TYPE"))
    args["scope_type"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("categories", None)
    args["categories"] = field

    return PermissionSet(**args)

def unmarshal_ListPermissionSetsResponse(data: Any) -> ListPermissionSetsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPermissionSetsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("permission_sets", [])
    args["permission_sets"] = [unmarshal_PermissionSet(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListPermissionSetsResponse(**args)

def unmarshal_ListPoliciesResponse(data: Any) -> ListPoliciesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPoliciesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("policies", [])
    args["policies"] = [unmarshal_Policy(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListPoliciesResponse(**args)

def unmarshal_ListQuotaResponse(data: Any) -> ListQuotaResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListQuotaResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("quota", [])
    args["quota"] = [unmarshal_Quotum(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListQuotaResponse(**args)

def unmarshal_Rule(data: Any) -> Rule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Rule' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("permission_sets_scope_type", getattr(PermissionSetScopeType, "UNKNOWN_SCOPE_TYPE"))
    args["permission_sets_scope_type"] = field

    field = data.get("condition", str())
    args["condition"] = field

    field = data.get("permission_set_names", None)
    args["permission_set_names"] = field

    field = data.get("project_ids", None)
    args["project_ids"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("account_root_user_id", None)
    args["account_root_user_id"] = field

    return Rule(**args)

def unmarshal_ListRulesResponse(data: Any) -> ListRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_Rule(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListRulesResponse(**args)

def unmarshal_ListSSHKeysResponse(data: Any) -> ListSSHKeysResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSSHKeysResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ssh_keys", [])
    args["ssh_keys"] = [unmarshal_SSHKey(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListSSHKeysResponse(**args)

def unmarshal_ListUsersResponse(data: Any) -> ListUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("users", [])
    args["users"] = [unmarshal_User(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListUsersResponse(**args)

def unmarshal_MFAOTP(data: Any) -> MFAOTP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MFAOTP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secret", str())
    args["secret"] = field

    return MFAOTP(**args)

def unmarshal_Organization(data: Any) -> Organization:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Organization' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("alias", str())
    args["alias"] = field

    return Organization(**args)

def unmarshal_OrganizationSecuritySettings(data: Any) -> OrganizationSecuritySettings:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OrganizationSecuritySettings' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enforce_password_renewal", False)
    args["enforce_password_renewal"] = field

    field = data.get("login_attempts_before_locked", 0)
    args["login_attempts_before_locked"] = field

    field = data.get("grace_period_duration", None)
    args["grace_period_duration"] = field

    return OrganizationSecuritySettings(**args)

def unmarshal_SetRulesResponse(data: Any) -> SetRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetRulesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rules", [])
    args["rules"] = [unmarshal_Rule(v) for v in field] if field is not None else None

    return SetRulesResponse(**args)

def unmarshal_ValidateUserMFAOTPResponse(data: Any) -> ValidateUserMFAOTPResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ValidateUserMFAOTPResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("recovery_codes", [])
    args["recovery_codes"] = field

    return ValidateUserMFAOTPResponse(**args)

def marshal_AddGroupMemberRequest(
    request: AddGroupMemberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="user_id", value=request.user_id,marshal_func=None
            ),
            OneOfPossibility(param="application_id", value=request.application_id,marshal_func=None
            ),
        ]),
    )


    return output

def marshal_AddGroupMembersRequest(
    request: AddGroupMembersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.user_ids is not None:
        output["user_ids"] = request.user_ids
    else:
        output["user_ids"] = None

    if request.application_ids is not None:
        output["application_ids"] = request.application_ids
    else:
        output["application_ids"] = None


    return output

def marshal_CreateAPIKeyRequest(
    request: CreateAPIKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="application_id", value=request.application_id,marshal_func=None
            ),
            OneOfPossibility(param="user_id", value=request.user_id,marshal_func=None
            ),
        ]),
    )

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.isoformat()
    else:
        output["expires_at"] = None

    if request.default_project_id is not None:
        output["default_project_id"] = request.default_project_id
    else:
        output["default_project_id"] = None


    return output

def marshal_CreateApplicationRequest(
    request: CreateApplicationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id or defaults.default_organization_id
    else:
        output["organization_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_CreateGroupRequest(
    request: CreateGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id or defaults.default_organization_id
    else:
        output["organization_id"] = None

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_CreateJWTRequest(
    request: CreateJWTRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.user_id is not None:
        output["user_id"] = request.user_id
    else:
        output["user_id"] = str()

    if request.referrer is not None:
        output["referrer"] = request.referrer
    else:
        output["referrer"] = str()


    return output

def marshal_RuleSpecs(
    request: RuleSpecs,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project_ids", value=request.project_ids,marshal_func=None
            ),
            OneOfPossibility(param="organization_id", value=request.organization_id,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.condition is not None:
        output["condition"] = request.condition
    else:
        output["condition"] = str()

    if request.permission_set_names is not None:
        output["permission_set_names"] = request.permission_set_names
    else:
        output["permission_set_names"] = None


    return output

def marshal_CreatePolicyRequest(
    request: CreatePolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="user_id", value=request.user_id,marshal_func=None
            ),
            OneOfPossibility(param="group_id", value=request.group_id,marshal_func=None
            ),
            OneOfPossibility(param="application_id", value=request.application_id,marshal_func=None
            ),
            OneOfPossibility(param="no_principal", value=request.no_principal,marshal_func=None
            ),
        ]),
    )

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id or defaults.default_organization_id
    else:
        output["organization_id"] = None

    if request.rules is not None:
        output["rules"] = [marshal_RuleSpecs(item, defaults) for item in request.rules]
    else:
        output["rules"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_CreateSSHKeyRequest(
    request: CreateSSHKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.public_key is not None:
        output["public_key"] = request.public_key
    else:
        output["public_key"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_CreateUserRequestMember(
    request: CreateUserRequestMember,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email
    else:
        output["email"] = str()

    if request.send_password_email is not None:
        output["send_password_email"] = request.send_password_email
    else:
        output["send_password_email"] = False

    if request.send_welcome_email is not None:
        output["send_welcome_email"] = request.send_welcome_email
    else:
        output["send_welcome_email"] = False

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()

    if request.first_name is not None:
        output["first_name"] = request.first_name
    else:
        output["first_name"] = str()

    if request.last_name is not None:
        output["last_name"] = request.last_name
    else:
        output["last_name"] = str()

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number
    else:
        output["phone_number"] = str()

    if request.locale is not None:
        output["locale"] = request.locale
    else:
        output["locale"] = str()


    return output

def marshal_CreateUserRequest(
    request: CreateUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="email", value=request.email,marshal_func=None
            ),
            OneOfPossibility(param="member", value=request.member,marshal_func=marshal_CreateUserRequestMember
            ),
        ]),
    )

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id or defaults.default_organization_id
    else:
        output["organization_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_JoinUserConnectionRequest(
    request: JoinUserConnectionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.token is not None:
        output["token"] = request.token
    else:
        output["token"] = str()


    return output

def marshal_RemoveGroupMemberRequest(
    request: RemoveGroupMemberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="user_id", value=request.user_id,marshal_func=None
            ),
            OneOfPossibility(param="application_id", value=request.application_id,marshal_func=None
            ),
        ]),
    )


    return output

def marshal_RemoveUserConnectionRequest(
    request: RemoveUserConnectionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.target_user_id is not None:
        output["target_user_id"] = request.target_user_id
    else:
        output["target_user_id"] = str()


    return output

def marshal_SetGroupMembersRequest(
    request: SetGroupMembersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.user_ids is not None:
        output["user_ids"] = request.user_ids
    else:
        output["user_ids"] = str()

    if request.application_ids is not None:
        output["application_ids"] = request.application_ids
    else:
        output["application_ids"] = str()


    return output

def marshal_SetOrganizationAliasRequest(
    request: SetOrganizationAliasRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.alias is not None:
        output["alias"] = request.alias
    else:
        output["alias"] = str()


    return output

def marshal_SetRulesRequest(
    request: SetRulesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.policy_id is not None:
        output["policy_id"] = request.policy_id
    else:
        output["policy_id"] = str()

    if request.rules is not None:
        output["rules"] = [marshal_RuleSpecs(item, defaults) for item in request.rules]
    else:
        output["rules"] = str()


    return output

def marshal_UpdateAPIKeyRequest(
    request: UpdateAPIKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.default_project_id is not None:
        output["default_project_id"] = request.default_project_id
    else:
        output["default_project_id"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output

def marshal_UpdateApplicationRequest(
    request: UpdateApplicationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateGroupRequest(
    request: UpdateGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateOrganizationSecuritySettingsRequest(
    request: UpdateOrganizationSecuritySettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enforce_password_renewal is not None:
        output["enforce_password_renewal"] = request.enforce_password_renewal
    else:
        output["enforce_password_renewal"] = None

    if request.grace_period_duration is not None:
        output["grace_period_duration"] = request.grace_period_duration
    else:
        output["grace_period_duration"] = None

    if request.login_attempts_before_locked is not None:
        output["login_attempts_before_locked"] = request.login_attempts_before_locked
    else:
        output["login_attempts_before_locked"] = None


    return output

def marshal_UpdatePolicyRequest(
    request: UpdatePolicyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="user_id", value=request.user_id,marshal_func=None
            ),
            OneOfPossibility(param="group_id", value=request.group_id,marshal_func=None
            ),
            OneOfPossibility(param="application_id", value=request.application_id,marshal_func=None
            ),
            OneOfPossibility(param="no_principal", value=request.no_principal,marshal_func=None
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateSSHKeyRequest(
    request: UpdateSSHKeyRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.disabled is not None:
        output["disabled"] = request.disabled
    else:
        output["disabled"] = None


    return output

def marshal_UpdateUserPasswordRequest(
    request: UpdateUserPasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()


    return output

def marshal_UpdateUserRequest(
    request: UpdateUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.email is not None:
        output["email"] = request.email
    else:
        output["email"] = None

    if request.first_name is not None:
        output["first_name"] = request.first_name
    else:
        output["first_name"] = None

    if request.last_name is not None:
        output["last_name"] = request.last_name
    else:
        output["last_name"] = None

    if request.phone_number is not None:
        output["phone_number"] = request.phone_number
    else:
        output["phone_number"] = None

    if request.locale is not None:
        output["locale"] = request.locale
    else:
        output["locale"] = None


    return output

def marshal_UpdateUserUsernameRequest(
    request: UpdateUserUsernameRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()


    return output

def marshal_ValidateUserMFAOTPRequest(
    request: ValidateUserMFAOTPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.one_time_password is not None:
        output["one_time_password"] = request.one_time_password
    else:
        output["one_time_password"] = str()


    return output
