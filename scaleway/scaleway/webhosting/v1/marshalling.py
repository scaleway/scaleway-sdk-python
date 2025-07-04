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
    DnsRecordStatus,
    DnsRecordType,
    DnsRecordsStatus,
    DomainAction,
    DomainAvailabilityAction,
    DomainAvailabilityStatus,
    DomainDnsAction,
    DomainStatus,
    DomainZoneOwner,
    HostingStatus,
    ListDatabaseUsersRequestOrderBy,
    ListDatabasesRequestOrderBy,
    ListFtpAccountsRequestOrderBy,
    ListHostingsRequestOrderBy,
    ListMailAccountsRequestOrderBy,
    ListOffersRequestOrderBy,
    ListWebsitesRequestOrderBy,
    NameserverStatus,
    OfferOptionName,
    OfferOptionWarning,
    PlatformPlatformGroup,
    DatabaseUser,
    Database,
    FtpAccount,
    MailAccount,
    CheckUserOwnsDomainResponse,
    AutoConfigDomainDns,
    DnsRecord,
    Nameserver,
    DnsRecords,
    Domain,
    PlatformControlPanelUrls,
    OfferOption,
    PlatformControlPanel,
    HostingUser,
    Offer,
    Platform,
    Hosting,
    ControlPanel,
    ListControlPanelsResponse,
    ListDatabaseUsersResponse,
    ListDatabasesResponse,
    ListFtpAccountsResponse,
    HostingSummary,
    ListHostingsResponse,
    ListMailAccountsResponse,
    ListOffersResponse,
    Website,
    ListWebsitesResponse,
    ResetHostingPasswordResponse,
    ResourceSummary,
    DomainAvailability,
    SearchDomainsResponse,
    Session,
    DatabaseApiAssignDatabaseUserRequest,
    DatabaseApiChangeDatabaseUserPasswordRequest,
    CreateDatabaseRequestUser,
    DatabaseApiCreateDatabaseRequest,
    DatabaseApiCreateDatabaseUserRequest,
    DatabaseApiUnassignDatabaseUserRequest,
    DnsApiCheckUserOwnsDomainRequest,
    SyncDomainDnsRecordsRequestRecord,
    DnsApiSyncDomainDnsRecordsRequest,
    FtpAccountApiChangeFtpAccountPasswordRequest,
    FtpAccountApiCreateFtpAccountRequest,
    CreateHostingRequestDomainConfiguration,
    OfferOptionRequest,
    HostingApiCreateHostingRequest,
    HostingApiUpdateHostingRequest,
    MailAccountApiChangeMailAccountPasswordRequest,
    MailAccountApiCreateMailAccountRequest,
    MailAccountApiRemoveMailAccountRequest,
)
from ...std.types import (
LanguageCode as StdLanguageCode,
)

def unmarshal_DatabaseUser(data: Any) -> DatabaseUser:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DatabaseUser' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("username", str())
    args["username"] = field

    field = data.get("databases", [])
    args["databases"] = field

    return DatabaseUser(**args)

def unmarshal_Database(data: Any) -> Database:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("database_name", str())
    args["database_name"] = field

    field = data.get("users", [])
    args["users"] = field

    return Database(**args)

def unmarshal_FtpAccount(data: Any) -> FtpAccount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'FtpAccount' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("username", str())
    args["username"] = field

    field = data.get("path", str())
    args["path"] = field

    return FtpAccount(**args)

def unmarshal_MailAccount(data: Any) -> MailAccount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MailAccount' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("username", str())
    args["username"] = field

    return MailAccount(**args)

def unmarshal_CheckUserOwnsDomainResponse(data: Any) -> CheckUserOwnsDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckUserOwnsDomainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("owns_domain", False)
    args["owns_domain"] = field

    return CheckUserOwnsDomainResponse(**args)

def unmarshal_AutoConfigDomainDns(data: Any) -> AutoConfigDomainDns:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AutoConfigDomainDns' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("nameservers", False)
    args["nameservers"] = field

    field = data.get("web_records", False)
    args["web_records"] = field

    field = data.get("mail_records", False)
    args["mail_records"] = field

    field = data.get("all_records", False)
    args["all_records"] = field

    field = data.get("none", False)
    args["none"] = field

    return AutoConfigDomainDns(**args)

def unmarshal_DnsRecord(data: Any) -> DnsRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DnsRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("type", getattr(DnsRecordType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("ttl", 0)
    args["ttl"] = field

    field = data.get("value", str())
    args["value"] = field

    field = data.get("status", getattr(DnsRecordStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("raw_data", str())
    args["raw_data"] = field

    field = data.get("priority", None)
    args["priority"] = field

    return DnsRecord(**args)

def unmarshal_Nameserver(data: Any) -> Nameserver:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Nameserver' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("status", getattr(NameserverStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("is_default", False)
    args["is_default"] = field

    return Nameserver(**args)

def unmarshal_DnsRecords(data: Any) -> DnsRecords:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DnsRecords' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", [])
    args["records"] = [unmarshal_DnsRecord(v) for v in field] if field is not None else None

    field = data.get("name_servers", [])
    args["name_servers"] = [unmarshal_Nameserver(v) for v in field] if field is not None else None

    field = data.get("status", getattr(DnsRecordsStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("dns_config", None)
    args["dns_config"] = [DomainDnsAction(v) for v in field] if field is not None else None

    field = data.get("auto_config_domain_dns", None)
    args["auto_config_domain_dns"] = unmarshal_AutoConfigDomainDns(field) if field is not None else None

    return DnsRecords(**args)

def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("status", getattr(DomainStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("owner", getattr(DomainZoneOwner, "UNKNOWN_ZONE_OWNER"))
    args["owner"] = field

    field = data.get("available_actions", [])
    args["available_actions"] = [DomainAction(v) for v in field] if field is not None else None

    field = data.get("available_dns_actions", None)
    args["available_dns_actions"] = [DomainDnsAction(v) for v in field] if field is not None else None

    field = data.get("auto_config_domain_dns", None)
    args["auto_config_domain_dns"] = unmarshal_AutoConfigDomainDns(field) if field is not None else None

    return Domain(**args)

def unmarshal_PlatformControlPanelUrls(data: Any) -> PlatformControlPanelUrls:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlatformControlPanelUrls' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dashboard", str())
    args["dashboard"] = field

    field = data.get("webmail", str())
    args["webmail"] = field

    return PlatformControlPanelUrls(**args)

def unmarshal_OfferOption(data: Any) -> OfferOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", getattr(OfferOptionName, "UNKNOWN_NAME"))
    args["name"] = field

    field = data.get("billing_operation_path", str())
    args["billing_operation_path"] = field

    field = data.get("min_value", 0)
    args["min_value"] = field

    field = data.get("current_value", 0)
    args["current_value"] = field

    field = data.get("max_value", 0)
    args["max_value"] = field

    field = data.get("quota_warning", getattr(OfferOptionWarning, "UNKNOWN_WARNING"))
    args["quota_warning"] = field

    field = data.get("price", None)
    args["price"] = unmarshal_Money(field) if field is not None else None

    return OfferOption(**args)

def unmarshal_PlatformControlPanel(data: Any) -> PlatformControlPanel:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlatformControlPanel' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("urls", None)
    args["urls"] = unmarshal_PlatformControlPanelUrls(field) if field is not None else None

    return PlatformControlPanel(**args)

def unmarshal_HostingUser(data: Any) -> HostingUser:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HostingUser' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("username", str())
    args["username"] = field

    field = data.get("contact_email", str())
    args["contact_email"] = field

    field = data.get("one_time_password", None)
    args["one_time_password"] = field

    field = data.get("one_time_password_b64", None)
    args["one_time_password_b64"] = field

    return HostingUser(**args)

def unmarshal_Offer(data: Any) -> Offer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("billing_operation_path", str())
    args["billing_operation_path"] = field

    field = data.get("options", [])
    args["options"] = [unmarshal_OfferOption(v) for v in field] if field is not None else None

    field = data.get("available", False)
    args["available"] = field

    field = data.get("control_panel_name", str())
    args["control_panel_name"] = field

    field = data.get("end_of_life", False)
    args["end_of_life"] = field

    field = data.get("quota_warning", getattr(OfferOptionWarning, "UNKNOWN_WARNING"))
    args["quota_warning"] = field

    field = data.get("price", None)
    args["price"] = unmarshal_Money(field) if field is not None else None

    return Offer(**args)

def unmarshal_Platform(data: Any) -> Platform:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Platform' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("number", 0)
    args["number"] = field

    field = data.get("group_name", getattr(PlatformPlatformGroup, "UNKNOWN_GROUP"))
    args["group_name"] = field

    field = data.get("ipv4", str())
    args["ipv4"] = field

    field = data.get("ipv6", str())
    args["ipv6"] = field

    field = data.get("control_panel", None)
    args["control_panel"] = unmarshal_PlatformControlPanel(field) if field is not None else None

    return Platform(**args)

def unmarshal_Hosting(data: Any) -> Hosting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Hosting' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("status", getattr(HostingStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("ipv4", str())
    args["ipv4"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("protected", False)
    args["protected"] = field

    field = data.get("domain_status", getattr(DomainStatus, "UNKNOWN_STATUS"))
    args["domain_status"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("offer", None)
    args["offer"] = unmarshal_Offer(field) if field is not None else None

    field = data.get("platform", None)
    args["platform"] = unmarshal_Platform(field) if field is not None else None

    field = data.get("dns_status", None)
    args["dns_status"] = field

    field = data.get("user", None)
    args["user"] = unmarshal_HostingUser(field) if field is not None else None

    return Hosting(**args)

def unmarshal_ControlPanel(data: Any) -> ControlPanel:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ControlPanel' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("available", False)
    args["available"] = field

    field = data.get("logo_url", str())
    args["logo_url"] = field

    field = data.get("available_languages", [])
    args["available_languages"] = [StdLanguageCode(v) for v in field] if field is not None else None

    return ControlPanel(**args)

def unmarshal_ListControlPanelsResponse(data: Any) -> ListControlPanelsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListControlPanelsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("control_panels", [])
    args["control_panels"] = [unmarshal_ControlPanel(v) for v in field] if field is not None else None

    return ListControlPanelsResponse(**args)

def unmarshal_ListDatabaseUsersResponse(data: Any) -> ListDatabaseUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabaseUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("users", [])
    args["users"] = [unmarshal_DatabaseUser(v) for v in field] if field is not None else None

    return ListDatabaseUsersResponse(**args)

def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("databases", [])
    args["databases"] = [unmarshal_Database(v) for v in field] if field is not None else None

    return ListDatabasesResponse(**args)

def unmarshal_ListFtpAccountsResponse(data: Any) -> ListFtpAccountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFtpAccountsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("ftp_accounts", [])
    args["ftp_accounts"] = [unmarshal_FtpAccount(v) for v in field] if field is not None else None

    return ListFtpAccountsResponse(**args)

def unmarshal_HostingSummary(data: Any) -> HostingSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HostingSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("status", getattr(HostingStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("protected", False)
    args["protected"] = field

    field = data.get("offer_name", str())
    args["offer_name"] = field

    field = data.get("domain_status", getattr(DomainStatus, "UNKNOWN_STATUS"))
    args["domain_status"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("dns_status", None)
    args["dns_status"] = field

    return HostingSummary(**args)

def unmarshal_ListHostingsResponse(data: Any) -> ListHostingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHostingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("hostings", [])
    args["hostings"] = [unmarshal_HostingSummary(v) for v in field] if field is not None else None

    return ListHostingsResponse(**args)

def unmarshal_ListMailAccountsResponse(data: Any) -> ListMailAccountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListMailAccountsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("mail_accounts", [])
    args["mail_accounts"] = [unmarshal_MailAccount(v) for v in field] if field is not None else None

    return ListMailAccountsResponse(**args)

def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("offers", [])
    args["offers"] = [unmarshal_Offer(v) for v in field] if field is not None else None

    return ListOffersResponse(**args)

def unmarshal_Website(data: Any) -> Website:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Website' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", str())
    args["domain"] = field

    field = data.get("path", str())
    args["path"] = field

    field = data.get("ssl_status", False)
    args["ssl_status"] = field

    return Website(**args)

def unmarshal_ListWebsitesResponse(data: Any) -> ListWebsitesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWebsitesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("websites", [])
    args["websites"] = [unmarshal_Website(v) for v in field] if field is not None else None

    return ListWebsitesResponse(**args)

def unmarshal_ResetHostingPasswordResponse(data: Any) -> ResetHostingPasswordResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ResetHostingPasswordResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("one_time_password_b64", str())
    args["one_time_password_b64"] = field

    field = data.get("one_time_password", None)
    args["one_time_password"] = field

    return ResetHostingPasswordResponse(**args)

def unmarshal_ResourceSummary(data: Any) -> ResourceSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ResourceSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("databases_count", 0)
    args["databases_count"] = field

    field = data.get("mail_accounts_count", 0)
    args["mail_accounts_count"] = field

    field = data.get("ftp_accounts_count", 0)
    args["ftp_accounts_count"] = field

    field = data.get("websites_count", 0)
    args["websites_count"] = field

    return ResourceSummary(**args)

def unmarshal_DomainAvailability(data: Any) -> DomainAvailability:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainAvailability' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("zone_name", str())
    args["zone_name"] = field

    field = data.get("status", getattr(DomainAvailabilityStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("available_actions", [])
    args["available_actions"] = [DomainAvailabilityAction(v) for v in field] if field is not None else None

    field = data.get("can_create_hosting", False)
    args["can_create_hosting"] = field

    field = data.get("price", None)
    args["price"] = unmarshal_Money(field) if field is not None else None

    return DomainAvailability(**args)

def unmarshal_SearchDomainsResponse(data: Any) -> SearchDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SearchDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domains_available", [])
    args["domains_available"] = [unmarshal_DomainAvailability(v) for v in field] if field is not None else None

    return SearchDomainsResponse(**args)

def unmarshal_Session(data: Any) -> Session:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Session' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("url", str())
    args["url"] = field

    return Session(**args)

def marshal_DatabaseApiAssignDatabaseUserRequest(
    request: DatabaseApiAssignDatabaseUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()


    return output

def marshal_DatabaseApiChangeDatabaseUserPasswordRequest(
    request: DatabaseApiChangeDatabaseUserPasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()


    return output

def marshal_CreateDatabaseRequestUser(
    request: CreateDatabaseRequestUser,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()


    return output

def marshal_DatabaseApiCreateDatabaseRequest(
    request: DatabaseApiCreateDatabaseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="new_user", value=request.new_user,marshal_func=marshal_CreateDatabaseRequestUser
            ),
            OneOfPossibility(param="existing_username", value=request.existing_username,marshal_func=None
            ),
        ]),
    )

    if request.database_name is not None:
        output["database_name"] = request.database_name
    else:
        output["database_name"] = str()


    return output

def marshal_DatabaseApiCreateDatabaseUserRequest(
    request: DatabaseApiCreateDatabaseUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()


    return output

def marshal_DatabaseApiUnassignDatabaseUserRequest(
    request: DatabaseApiUnassignDatabaseUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()


    return output

def marshal_DnsApiCheckUserOwnsDomainRequest(
    request: DnsApiCheckUserOwnsDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_AutoConfigDomainDns(
    request: AutoConfigDomainDns,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.nameservers is not None:
        output["nameservers"] = request.nameservers
    else:
        output["nameservers"] = False

    if request.web_records is not None:
        output["web_records"] = request.web_records
    else:
        output["web_records"] = False

    if request.mail_records is not None:
        output["mail_records"] = request.mail_records
    else:
        output["mail_records"] = False

    if request.all_records is not None:
        output["all_records"] = request.all_records
    else:
        output["all_records"] = False

    if request.none is not None:
        output["none"] = request.none
    else:
        output["none"] = False


    return output

def marshal_SyncDomainDnsRecordsRequestRecord(
    request: SyncDomainDnsRecordsRequestRecord,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = str()


    return output

def marshal_DnsApiSyncDomainDnsRecordsRequest(
    request: DnsApiSyncDomainDnsRecordsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.update_web_records is not None:
        output["update_web_records"] = request.update_web_records
    else:
        output["update_web_records"] = None

    if request.update_mail_records is not None:
        output["update_mail_records"] = request.update_mail_records
    else:
        output["update_mail_records"] = None

    if request.update_all_records is not None:
        output["update_all_records"] = request.update_all_records
    else:
        output["update_all_records"] = None

    if request.update_nameservers is not None:
        output["update_nameservers"] = request.update_nameservers
    else:
        output["update_nameservers"] = None

    if request.custom_records is not None:
        output["custom_records"] = [marshal_SyncDomainDnsRecordsRequestRecord(item, defaults) for item in request.custom_records]
    else:
        output["custom_records"] = None

    if request.auto_config_domain_dns is not None:
        output["auto_config_domain_dns"] = marshal_AutoConfigDomainDns(request.auto_config_domain_dns, defaults)
    else:
        output["auto_config_domain_dns"] = None


    return output

def marshal_FtpAccountApiChangeFtpAccountPasswordRequest(
    request: FtpAccountApiChangeFtpAccountPasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()


    return output

def marshal_FtpAccountApiCreateFtpAccountRequest(
    request: FtpAccountApiCreateFtpAccountRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()

    if request.path is not None:
        output["path"] = request.path
    else:
        output["path"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()


    return output

def marshal_CreateHostingRequestDomainConfiguration(
    request: CreateHostingRequestDomainConfiguration,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.update_nameservers is not None:
        output["update_nameservers"] = request.update_nameservers
    else:
        output["update_nameservers"] = str()

    if request.update_web_record is not None:
        output["update_web_record"] = request.update_web_record
    else:
        output["update_web_record"] = str()

    if request.update_mail_record is not None:
        output["update_mail_record"] = request.update_mail_record
    else:
        output["update_mail_record"] = str()

    if request.update_all_records is not None:
        output["update_all_records"] = request.update_all_records
    else:
        output["update_all_records"] = str()


    return output

def marshal_OfferOptionRequest(
    request: OfferOptionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id
    else:
        output["id"] = str()

    if request.quantity is not None:
        output["quantity"] = request.quantity
    else:
        output["quantity"] = 0


    return output

def marshal_HostingApiCreateHostingRequest(
    request: HostingApiCreateHostingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id
    else:
        output["offer_id"] = str()

    if request.email is not None:
        output["email"] = request.email
    else:
        output["email"] = str()

    if request.domain is not None:
        output["domain"] = request.domain
    else:
        output["domain"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.offer_options is not None:
        output["offer_options"] = [marshal_OfferOptionRequest(item, defaults) for item in request.offer_options]
    else:
        output["offer_options"] = None

    if request.language is not None:
        output["language"] = str(request.language)
    else:
        output["language"] = None

    if request.domain_configuration is not None:
        output["domain_configuration"] = marshal_CreateHostingRequestDomainConfiguration(request.domain_configuration, defaults)
    else:
        output["domain_configuration"] = None

    if request.skip_welcome_email is not None:
        output["skip_welcome_email"] = request.skip_welcome_email
    else:
        output["skip_welcome_email"] = None

    if request.auto_config_domain_dns is not None:
        output["auto_config_domain_dns"] = marshal_AutoConfigDomainDns(request.auto_config_domain_dns, defaults)
    else:
        output["auto_config_domain_dns"] = None


    return output

def marshal_HostingApiUpdateHostingRequest(
    request: HostingApiUpdateHostingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email
    else:
        output["email"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.offer_options is not None:
        output["offer_options"] = [marshal_OfferOptionRequest(item, defaults) for item in request.offer_options]
    else:
        output["offer_options"] = None

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id
    else:
        output["offer_id"] = None

    if request.protected is not None:
        output["protected"] = request.protected
    else:
        output["protected"] = None


    return output

def marshal_MailAccountApiChangeMailAccountPasswordRequest(
    request: MailAccountApiChangeMailAccountPasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain
    else:
        output["domain"] = str()

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()


    return output

def marshal_MailAccountApiCreateMailAccountRequest(
    request: MailAccountApiCreateMailAccountRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain
    else:
        output["domain"] = str()

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = str()


    return output

def marshal_MailAccountApiRemoveMailAccountRequest(
    request: MailAccountApiRemoveMailAccountRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain
    else:
        output["domain"] = str()

    if request.username is not None:
        output["username"] = request.username
    else:
        output["username"] = str()


    return output
