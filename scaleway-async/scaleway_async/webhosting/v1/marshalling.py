# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    unmarshal_Money,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    BackupItemType,
    BackupStatus,
    CheckFreeDomainAvailabilityResponseUnavailableReason,
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
    NameserverStatus,
    OfferOptionName,
    OfferOptionWarning,
    PlatformPlatformGroup,
    ProgressStatus,
    Backup,
    DatabaseUser,
    Database,
    FtpAccount,
    AutoConfigDomainDns,
    HostingDomainCustomDomain,
    HostingDomain,
    HostingSummary,
    MailAccount,
    Website,
    FreeDomain,
    CheckFreeDomainAvailabilityResponse,
    CheckUserOwnsDomainResponse,
    DnsRecord,
    Nameserver,
    DnsRecords,
    Domain,
    PlatformControlPanelUrls,
    ControlPanel,
    OfferOption,
    PlatformControlPanel,
    HostingUser,
    Offer,
    Platform,
    Hosting,
    BackupItem,
    BackupItemGroup,
    ListBackupItemsResponse,
    ListBackupsResponse,
    ListControlPanelsResponse,
    ListDatabaseUsersResponse,
    ListDatabasesResponse,
    ListFreeRootDomainsResponse,
    ListFtpAccountsResponse,
    ListHostingsResponse,
    ListMailAccountsResponse,
    ListOffersResponse,
    ProgressSummary,
    ListRecentProgressesResponse,
    ListWebsitesResponse,
    Progress,
    ResetHostingPasswordResponse,
    ResourceSummary,
    RestoreBackupItemsResponse,
    RestoreBackupResponse,
    DomainAvailability,
    SearchDomainsResponse,
    Session,
    BackupApiRestoreBackupItemsRequest,
    DatabaseApiAssignDatabaseUserRequest,
    DatabaseApiChangeDatabaseUserPasswordRequest,
    CreateDatabaseRequestUser,
    DatabaseApiCreateDatabaseRequest,
    DatabaseApiCreateDatabaseUserRequest,
    DatabaseApiUnassignDatabaseUserRequest,
    DnsApiCheckUserOwnsDomainRequest,
    SyncDomainDnsRecordsRequestRecord,
    DnsApiSyncDomainDnsRecordsRequest,
    FreeDomainApiCheckFreeDomainAvailabilityRequest,
    FtpAccountApiChangeFtpAccountPasswordRequest,
    FtpAccountApiCreateFtpAccountRequest,
    HostingApiAddCustomDomainRequest,
    CreateHostingRequestDomainConfiguration,
    OfferOptionRequest,
    HostingApiCreateHostingRequest,
    HostingApiDeleteHostingDomainsRequest,
    HostingApiMigrateControlPanelRequest,
    HostingApiRemoveCustomDomainRequest,
    HostingApiUpdateHostingFreeDomainRequest,
    HostingApiUpdateHostingRequest,
    MailAccountApiChangeMailAccountPasswordRequest,
    MailAccountApiCreateMailAccountRequest,
    MailAccountApiRemoveMailAccountRequest,
    WebsiteApiCreateWebsiteRequest,
)
from ...std.types import (
    LanguageCode as StdLanguageCode,
)


def unmarshal_Backup(data: Any) -> Backup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Backup' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = BackupStatus.UNKNOWN_BACKUP_STATUS

    field = data.get("total_items", None)
    if field is not None:
        args["total_items"] = field
    else:
        args["total_items"] = 0

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return Backup(**args)


def unmarshal_DatabaseUser(data: Any) -> DatabaseUser:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DatabaseUser' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("username", None)
    if field is not None:
        args["username"] = field
    else:
        args["username"] = None

    field = data.get("databases", None)
    if field is not None:
        args["databases"] = field
    else:
        args["databases"] = []

    return DatabaseUser(**args)


def unmarshal_Database(data: Any) -> Database:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("database_name", None)
    if field is not None:
        args["database_name"] = field
    else:
        args["database_name"] = None

    field = data.get("users", None)
    if field is not None:
        args["users"] = field
    else:
        args["users"] = []

    return Database(**args)


def unmarshal_FtpAccount(data: Any) -> FtpAccount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'FtpAccount' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("username", None)
    if field is not None:
        args["username"] = field
    else:
        args["username"] = None

    field = data.get("path", None)
    if field is not None:
        args["path"] = field
    else:
        args["path"] = None

    return FtpAccount(**args)


def unmarshal_AutoConfigDomainDns(data: Any) -> AutoConfigDomainDns:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AutoConfigDomainDns' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("nameservers", None)
    if field is not None:
        args["nameservers"] = field
    else:
        args["nameservers"] = False

    field = data.get("web_records", None)
    if field is not None:
        args["web_records"] = field
    else:
        args["web_records"] = False

    field = data.get("mail_records", None)
    if field is not None:
        args["mail_records"] = field
    else:
        args["mail_records"] = False

    field = data.get("all_records", None)
    if field is not None:
        args["all_records"] = field
    else:
        args["all_records"] = False

    field = data.get("none", None)
    if field is not None:
        args["none"] = field
    else:
        args["none"] = False

    return AutoConfigDomainDns(**args)


def unmarshal_HostingDomainCustomDomain(data: Any) -> HostingDomainCustomDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HostingDomainCustomDomain' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("domain_status", None)
    if field is not None:
        args["domain_status"] = field
    else:
        args["domain_status"] = DomainStatus.UNKNOWN_STATUS

    field = data.get("dns_status", None)
    if field is not None:
        args["dns_status"] = field
    else:
        args["dns_status"] = DnsRecordsStatus.UNKNOWN_STATUS

    field = data.get("auto_config_domain_dns", None)
    if field is not None:
        args["auto_config_domain_dns"] = unmarshal_AutoConfigDomainDns(field)
    else:
        args["auto_config_domain_dns"] = None

    return HostingDomainCustomDomain(**args)


def unmarshal_HostingDomain(data: Any) -> HostingDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HostingDomain' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("subdomain", None)
    if field is not None:
        args["subdomain"] = field
    else:
        args["subdomain"] = None

    field = data.get("custom_domain", None)
    if field is not None:
        args["custom_domain"] = unmarshal_HostingDomainCustomDomain(field)
    else:
        args["custom_domain"] = None

    return HostingDomain(**args)


def unmarshal_HostingSummary(data: Any) -> HostingSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HostingSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = HostingStatus.UNKNOWN_STATUS

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("protected", None)
    if field is not None:
        args["protected"] = field
    else:
        args["protected"] = False

    field = data.get("dns_status", None)
    if field is not None:
        args["dns_status"] = field
    else:
        args["dns_status"] = DnsRecordsStatus.UNKNOWN_STATUS

    field = data.get("offer_name", None)
    if field is not None:
        args["offer_name"] = field
    else:
        args["offer_name"] = None

    field = data.get("domain_status", None)
    if field is not None:
        args["domain_status"] = field
    else:
        args["domain_status"] = DomainStatus.UNKNOWN_STATUS

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

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

    field = data.get("domain_info", None)
    if field is not None:
        args["domain_info"] = unmarshal_HostingDomain(field)
    else:
        args["domain_info"] = None

    return HostingSummary(**args)


def unmarshal_MailAccount(data: Any) -> MailAccount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MailAccount' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("username", None)
    if field is not None:
        args["username"] = field
    else:
        args["username"] = None

    return MailAccount(**args)


def unmarshal_Website(data: Any) -> Website:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Website' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("path", None)
    if field is not None:
        args["path"] = field
    else:
        args["path"] = None

    field = data.get("ssl_status", None)
    if field is not None:
        args["ssl_status"] = field
    else:
        args["ssl_status"] = False

    return Website(**args)


def unmarshal_FreeDomain(data: Any) -> FreeDomain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'FreeDomain' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("slug", None)
    if field is not None:
        args["slug"] = field
    else:
        args["slug"] = None

    field = data.get("root_domain", None)
    if field is not None:
        args["root_domain"] = field
    else:
        args["root_domain"] = None

    return FreeDomain(**args)


def unmarshal_CheckFreeDomainAvailabilityResponse(
    data: Any,
) -> CheckFreeDomainAvailabilityResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckFreeDomainAvailabilityResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("is_available", None)
    if field is not None:
        args["is_available"] = field
    else:
        args["is_available"] = False

    field = data.get("free_domain", None)
    if field is not None:
        args["free_domain"] = unmarshal_FreeDomain(field)
    else:
        args["free_domain"] = None

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = (
            CheckFreeDomainAvailabilityResponseUnavailableReason.UNAVAILABLE_REASON_UNKNOWN
        )

    return CheckFreeDomainAvailabilityResponse(**args)


def unmarshal_CheckUserOwnsDomainResponse(data: Any) -> CheckUserOwnsDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckUserOwnsDomainResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("owns_domain", None)
    if field is not None:
        args["owns_domain"] = field
    else:
        args["owns_domain"] = False

    return CheckUserOwnsDomainResponse(**args)


def unmarshal_DnsRecord(data: Any) -> DnsRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DnsRecord' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = DnsRecordType.UNKNOWN_TYPE

    field = data.get("ttl", None)
    if field is not None:
        args["ttl"] = field
    else:
        args["ttl"] = 0

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DnsRecordStatus.UNKNOWN_STATUS

    field = data.get("raw_data", None)
    if field is not None:
        args["raw_data"] = field
    else:
        args["raw_data"] = None

    field = data.get("priority", None)
    if field is not None:
        args["priority"] = field
    else:
        args["priority"] = 0

    return DnsRecord(**args)


def unmarshal_Nameserver(data: Any) -> Nameserver:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Nameserver' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field
    else:
        args["hostname"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = NameserverStatus.UNKNOWN_STATUS

    field = data.get("is_default", None)
    if field is not None:
        args["is_default"] = field
    else:
        args["is_default"] = False

    return Nameserver(**args)


def unmarshal_DnsRecords(data: Any) -> DnsRecords:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DnsRecords' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("records", None)
    if field is not None:
        args["records"] = (
            [unmarshal_DnsRecord(v) for v in field] if field is not None else None
        )
    else:
        args["records"] = []

    field = data.get("name_servers", None)
    if field is not None:
        args["name_servers"] = (
            [unmarshal_Nameserver(v) for v in field] if field is not None else None
        )
    else:
        args["name_servers"] = []

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DnsRecordsStatus.UNKNOWN_STATUS

    field = data.get("dns_config", None)
    if field is not None:
        args["dns_config"] = (
            [DomainDnsAction(v) for v in field] if field is not None else None
        )
    else:
        args["dns_config"] = []

    field = data.get("auto_config_domain_dns", None)
    if field is not None:
        args["auto_config_domain_dns"] = unmarshal_AutoConfigDomainDns(field)
    else:
        args["auto_config_domain_dns"] = None

    return DnsRecords(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainStatus.UNKNOWN_STATUS

    field = data.get("owner", None)
    if field is not None:
        args["owner"] = field
    else:
        args["owner"] = DomainZoneOwner.UNKNOWN_ZONE_OWNER

    field = data.get("zone_domain_name", None)
    if field is not None:
        args["zone_domain_name"] = field
    else:
        args["zone_domain_name"] = None

    field = data.get("available_actions", None)
    if field is not None:
        args["available_actions"] = (
            [DomainAction(v) for v in field] if field is not None else None
        )
    else:
        args["available_actions"] = []

    field = data.get("available_dns_actions", None)
    if field is not None:
        args["available_dns_actions"] = (
            [DomainDnsAction(v) for v in field] if field is not None else None
        )
    else:
        args["available_dns_actions"] = []

    field = data.get("auto_config_domain_dns", None)
    if field is not None:
        args["auto_config_domain_dns"] = unmarshal_AutoConfigDomainDns(field)
    else:
        args["auto_config_domain_dns"] = None

    return Domain(**args)


def unmarshal_PlatformControlPanelUrls(data: Any) -> PlatformControlPanelUrls:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlatformControlPanelUrls' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("dashboard", None)
    if field is not None:
        args["dashboard"] = field
    else:
        args["dashboard"] = None

    field = data.get("webmail", None)
    if field is not None:
        args["webmail"] = field
    else:
        args["webmail"] = None

    return PlatformControlPanelUrls(**args)


def unmarshal_ControlPanel(data: Any) -> ControlPanel:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ControlPanel' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("available", None)
    if field is not None:
        args["available"] = field
    else:
        args["available"] = False

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field
    else:
        args["logo_url"] = None

    field = data.get("available_languages", None)
    if field is not None:
        args["available_languages"] = (
            [StdLanguageCode(v) for v in field] if field is not None else None
        )
    else:
        args["available_languages"] = []

    return ControlPanel(**args)


def unmarshal_OfferOption(data: Any) -> OfferOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferOption' failed as data isn't a dictionary."
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
        args["name"] = OfferOptionName.UNKNOWN_NAME

    field = data.get("billing_operation_path", None)
    if field is not None:
        args["billing_operation_path"] = field
    else:
        args["billing_operation_path"] = None

    field = data.get("min_value", None)
    if field is not None:
        args["min_value"] = field
    else:
        args["min_value"] = 0

    field = data.get("current_value", None)
    if field is not None:
        args["current_value"] = field
    else:
        args["current_value"] = 0

    field = data.get("max_value", None)
    if field is not None:
        args["max_value"] = field
    else:
        args["max_value"] = 0

    field = data.get("quota_warning", None)
    if field is not None:
        args["quota_warning"] = field
    else:
        args["quota_warning"] = OfferOptionWarning.UNKNOWN_WARNING

    field = data.get("price", None)
    if field is not None:
        args["price"] = unmarshal_Money(field)
    else:
        args["price"] = None

    return OfferOption(**args)


def unmarshal_PlatformControlPanel(data: Any) -> PlatformControlPanel:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlatformControlPanel' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("urls", None)
    if field is not None:
        args["urls"] = unmarshal_PlatformControlPanelUrls(field)
    else:
        args["urls"] = None

    return PlatformControlPanel(**args)


def unmarshal_HostingUser(data: Any) -> HostingUser:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HostingUser' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("username", None)
    if field is not None:
        args["username"] = field
    else:
        args["username"] = None

    field = data.get("contact_email", None)
    if field is not None:
        args["contact_email"] = field
    else:
        args["contact_email"] = None

    field = data.get("one_time_password", None)
    if field is not None:
        args["one_time_password"] = field
    else:
        args["one_time_password"] = None

    field = data.get("one_time_password_b64", None)
    if field is not None:
        args["one_time_password_b64"] = field
    else:
        args["one_time_password_b64"] = None

    return HostingUser(**args)


def unmarshal_Offer(data: Any) -> Offer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Offer' failed as data isn't a dictionary."
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

    field = data.get("billing_operation_path", None)
    if field is not None:
        args["billing_operation_path"] = field
    else:
        args["billing_operation_path"] = None

    field = data.get("options", None)
    if field is not None:
        args["options"] = (
            [unmarshal_OfferOption(v) for v in field] if field is not None else None
        )
    else:
        args["options"] = []

    field = data.get("available", None)
    if field is not None:
        args["available"] = field
    else:
        args["available"] = False

    field = data.get("control_panel_name", None)
    if field is not None:
        args["control_panel_name"] = field
    else:
        args["control_panel_name"] = None

    field = data.get("end_of_life", None)
    if field is not None:
        args["end_of_life"] = field
    else:
        args["end_of_life"] = False

    field = data.get("quota_warning", None)
    if field is not None:
        args["quota_warning"] = field
    else:
        args["quota_warning"] = OfferOptionWarning.UNKNOWN_WARNING

    field = data.get("control_panels", None)
    if field is not None:
        args["control_panels"] = (
            [unmarshal_ControlPanel(v) for v in field] if field is not None else None
        )
    else:
        args["control_panels"] = []

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("price", None)
    if field is not None:
        args["price"] = unmarshal_Money(field)
    else:
        args["price"] = None

    return Offer(**args)


def unmarshal_Platform(data: Any) -> Platform:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Platform' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field
    else:
        args["hostname"] = None

    field = data.get("number", None)
    if field is not None:
        args["number"] = field
    else:
        args["number"] = 0

    field = data.get("group_name", None)
    if field is not None:
        args["group_name"] = field
    else:
        args["group_name"] = PlatformPlatformGroup.UNKNOWN_GROUP

    field = data.get("ipv4", None)
    if field is not None:
        args["ipv4"] = field
    else:
        args["ipv4"] = None

    field = data.get("ipv6", None)
    if field is not None:
        args["ipv6"] = field
    else:
        args["ipv6"] = None

    field = data.get("control_panel", None)
    if field is not None:
        args["control_panel"] = unmarshal_PlatformControlPanel(field)
    else:
        args["control_panel"] = None

    return Platform(**args)


def unmarshal_Hosting(data: Any) -> Hosting:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Hosting' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = HostingStatus.UNKNOWN_STATUS

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field
    else:
        args["domain"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("offer", None)
    if field is not None:
        args["offer"] = unmarshal_Offer(field)
    else:
        args["offer"] = None

    field = data.get("platform", None)
    if field is not None:
        args["platform"] = unmarshal_Platform(field)
    else:
        args["platform"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("dns_status", None)
    if field is not None:
        args["dns_status"] = field
    else:
        args["dns_status"] = DnsRecordsStatus.UNKNOWN_STATUS

    field = data.get("ipv4", None)
    if field is not None:
        args["ipv4"] = field
    else:
        args["ipv4"] = None

    field = data.get("protected", None)
    if field is not None:
        args["protected"] = field
    else:
        args["protected"] = False

    field = data.get("domain_status", None)
    if field is not None:
        args["domain_status"] = field
    else:
        args["domain_status"] = DomainStatus.UNKNOWN_STATUS

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("user", None)
    if field is not None:
        args["user"] = unmarshal_HostingUser(field)
    else:
        args["user"] = None

    field = data.get("domain_info", None)
    if field is not None:
        args["domain_info"] = unmarshal_HostingDomain(field)
    else:
        args["domain_info"] = None

    return Hosting(**args)


def unmarshal_BackupItem(data: Any) -> BackupItem:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BackupItem' failed as data isn't a dictionary."
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

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = BackupItemType.UNKNOWN_BACKUP_ITEM_TYPE

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = BackupStatus.UNKNOWN_BACKUP_STATUS

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    return BackupItem(**args)


def unmarshal_BackupItemGroup(data: Any) -> BackupItemGroup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BackupItemGroup' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = BackupItemType.UNKNOWN_BACKUP_ITEM_TYPE

    field = data.get("items", None)
    if field is not None:
        args["items"] = (
            [unmarshal_BackupItem(v) for v in field] if field is not None else None
        )
    else:
        args["items"] = []

    return BackupItemGroup(**args)


def unmarshal_ListBackupItemsResponse(data: Any) -> ListBackupItemsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackupItemsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("groups", None)
    if field is not None:
        args["groups"] = (
            [unmarshal_BackupItemGroup(v) for v in field] if field is not None else None
        )
    else:
        args["groups"] = []

    return ListBackupItemsResponse(**args)


def unmarshal_ListBackupsResponse(data: Any) -> ListBackupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackupsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("backups", None)
    if field is not None:
        args["backups"] = (
            [unmarshal_Backup(v) for v in field] if field is not None else None
        )
    else:
        args["backups"] = []

    return ListBackupsResponse(**args)


def unmarshal_ListControlPanelsResponse(data: Any) -> ListControlPanelsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListControlPanelsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("control_panels", None)
    if field is not None:
        args["control_panels"] = (
            [unmarshal_ControlPanel(v) for v in field] if field is not None else None
        )
    else:
        args["control_panels"] = []

    return ListControlPanelsResponse(**args)


def unmarshal_ListDatabaseUsersResponse(data: Any) -> ListDatabaseUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabaseUsersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("users", None)
    if field is not None:
        args["users"] = (
            [unmarshal_DatabaseUser(v) for v in field] if field is not None else None
        )
    else:
        args["users"] = []

    return ListDatabaseUsersResponse(**args)


def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("databases", None)
    if field is not None:
        args["databases"] = (
            [unmarshal_Database(v) for v in field] if field is not None else None
        )
    else:
        args["databases"] = []

    return ListDatabasesResponse(**args)


def unmarshal_ListFreeRootDomainsResponse(data: Any) -> ListFreeRootDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFreeRootDomainsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("root_domains", None)
    if field is not None:
        args["root_domains"] = field
    else:
        args["root_domains"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListFreeRootDomainsResponse(**args)


def unmarshal_ListFtpAccountsResponse(data: Any) -> ListFtpAccountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFtpAccountsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("ftp_accounts", None)
    if field is not None:
        args["ftp_accounts"] = (
            [unmarshal_FtpAccount(v) for v in field] if field is not None else None
        )
    else:
        args["ftp_accounts"] = []

    return ListFtpAccountsResponse(**args)


def unmarshal_ListHostingsResponse(data: Any) -> ListHostingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHostingsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("hostings", None)
    if field is not None:
        args["hostings"] = (
            [unmarshal_HostingSummary(v) for v in field] if field is not None else None
        )
    else:
        args["hostings"] = []

    return ListHostingsResponse(**args)


def unmarshal_ListMailAccountsResponse(data: Any) -> ListMailAccountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListMailAccountsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("mail_accounts", None)
    if field is not None:
        args["mail_accounts"] = (
            [unmarshal_MailAccount(v) for v in field] if field is not None else None
        )
    else:
        args["mail_accounts"] = []

    return ListMailAccountsResponse(**args)


def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("offers", None)
    if field is not None:
        args["offers"] = (
            [unmarshal_Offer(v) for v in field] if field is not None else None
        )
    else:
        args["offers"] = []

    return ListOffersResponse(**args)


def unmarshal_ProgressSummary(data: Any) -> ProgressSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProgressSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("backup_items_count", None)
    if field is not None:
        args["backup_items_count"] = field
    else:
        args["backup_items_count"] = 0

    field = data.get("percentage", None)
    if field is not None:
        args["percentage"] = field
    else:
        args["percentage"] = 0

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ProgressStatus.UNKNOWN_STATUS

    return ProgressSummary(**args)


def unmarshal_ListRecentProgressesResponse(data: Any) -> ListRecentProgressesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRecentProgressesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("progresses", None)
    if field is not None:
        args["progresses"] = (
            [unmarshal_ProgressSummary(v) for v in field] if field is not None else None
        )
    else:
        args["progresses"] = []

    return ListRecentProgressesResponse(**args)


def unmarshal_ListWebsitesResponse(data: Any) -> ListWebsitesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWebsitesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("websites", None)
    if field is not None:
        args["websites"] = (
            [unmarshal_Website(v) for v in field] if field is not None else None
        )
    else:
        args["websites"] = []

    return ListWebsitesResponse(**args)


def unmarshal_Progress(data: Any) -> Progress:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Progress' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("backup_item_groups", None)
    if field is not None:
        args["backup_item_groups"] = (
            [unmarshal_BackupItemGroup(v) for v in field] if field is not None else None
        )
    else:
        args["backup_item_groups"] = []

    field = data.get("percentage", None)
    if field is not None:
        args["percentage"] = field
    else:
        args["percentage"] = 0

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = ProgressStatus.UNKNOWN_STATUS

    return Progress(**args)


def unmarshal_ResetHostingPasswordResponse(data: Any) -> ResetHostingPasswordResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ResetHostingPasswordResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("one_time_password", None)
    if field is not None:
        args["one_time_password"] = field
    else:
        args["one_time_password"] = None

    field = data.get("one_time_password_b64", None)
    if field is not None:
        args["one_time_password_b64"] = field
    else:
        args["one_time_password_b64"] = None

    return ResetHostingPasswordResponse(**args)


def unmarshal_ResourceSummary(data: Any) -> ResourceSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ResourceSummary' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("databases_count", None)
    if field is not None:
        args["databases_count"] = field
    else:
        args["databases_count"] = 0

    field = data.get("mail_accounts_count", None)
    if field is not None:
        args["mail_accounts_count"] = field
    else:
        args["mail_accounts_count"] = 0

    field = data.get("ftp_accounts_count", None)
    if field is not None:
        args["ftp_accounts_count"] = field
    else:
        args["ftp_accounts_count"] = 0

    field = data.get("websites_count", None)
    if field is not None:
        args["websites_count"] = field
    else:
        args["websites_count"] = 0

    return ResourceSummary(**args)


def unmarshal_RestoreBackupItemsResponse(data: Any) -> RestoreBackupItemsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RestoreBackupItemsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("progress_id", None)
    if field is not None:
        args["progress_id"] = field
    else:
        args["progress_id"] = None

    return RestoreBackupItemsResponse(**args)


def unmarshal_RestoreBackupResponse(data: Any) -> RestoreBackupResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RestoreBackupResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("progress_id", None)
    if field is not None:
        args["progress_id"] = field
    else:
        args["progress_id"] = None

    return RestoreBackupResponse(**args)


def unmarshal_DomainAvailability(data: Any) -> DomainAvailability:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainAvailability' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("zone_name", None)
    if field is not None:
        args["zone_name"] = field
    else:
        args["zone_name"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainAvailabilityStatus.UNKNOWN_STATUS

    field = data.get("available_actions", None)
    if field is not None:
        args["available_actions"] = (
            [DomainAvailabilityAction(v) for v in field] if field is not None else None
        )
    else:
        args["available_actions"] = []

    field = data.get("can_create_hosting", None)
    if field is not None:
        args["can_create_hosting"] = field
    else:
        args["can_create_hosting"] = False

    field = data.get("price", None)
    if field is not None:
        args["price"] = unmarshal_Money(field)
    else:
        args["price"] = None

    return DomainAvailability(**args)


def unmarshal_SearchDomainsResponse(data: Any) -> SearchDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SearchDomainsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domains_available", None)
    if field is not None:
        args["domains_available"] = (
            [unmarshal_DomainAvailability(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["domains_available"] = []

    return SearchDomainsResponse(**args)


def unmarshal_Session(data: Any) -> Session:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Session' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("url", None)
    if field is not None:
        args["url"] = field
    else:
        args["url"] = None

    return Session(**args)


def marshal_BackupApiRestoreBackupItemsRequest(
    request: BackupApiRestoreBackupItemsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.item_ids is not None:
        output["item_ids"] = request.item_ids

    return output


def marshal_DatabaseApiAssignDatabaseUserRequest(
    request: DatabaseApiAssignDatabaseUserRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    return output


def marshal_DatabaseApiChangeDatabaseUserPasswordRequest(
    request: DatabaseApiChangeDatabaseUserPasswordRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_CreateDatabaseRequestUser(
    request: CreateDatabaseRequestUser,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_DatabaseApiCreateDatabaseRequest(
    request: DatabaseApiCreateDatabaseRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="new_user",
                    value=request.new_user,
                    marshal_func=marshal_CreateDatabaseRequestUser,
                ),
                OneOfPossibility(
                    param="existing_username",
                    value=request.existing_username,
                    marshal_func=None,
                ),
            ]
        ),
    )

    if request.database_name is not None:
        output["database_name"] = request.database_name

    return output


def marshal_DatabaseApiCreateDatabaseUserRequest(
    request: DatabaseApiCreateDatabaseUserRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_DatabaseApiUnassignDatabaseUserRequest(
    request: DatabaseApiUnassignDatabaseUserRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    return output


def marshal_DnsApiCheckUserOwnsDomainRequest(
    request: DnsApiCheckUserOwnsDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_AutoConfigDomainDns(
    request: AutoConfigDomainDns,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.nameservers is not None:
        output["nameservers"] = request.nameservers

    if request.web_records is not None:
        output["web_records"] = request.web_records

    if request.mail_records is not None:
        output["mail_records"] = request.mail_records

    if request.all_records is not None:
        output["all_records"] = request.all_records

    if request.none is not None:
        output["none"] = request.none

    return output


def marshal_SyncDomainDnsRecordsRequestRecord(
    request: SyncDomainDnsRecordsRequestRecord,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.type_ is not None:
        output["type"] = request.type_

    return output


def marshal_DnsApiSyncDomainDnsRecordsRequest(
    request: DnsApiSyncDomainDnsRecordsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.update_web_records is not None:
        output["update_web_records"] = request.update_web_records

    if request.update_mail_records is not None:
        output["update_mail_records"] = request.update_mail_records

    if request.update_all_records is not None:
        output["update_all_records"] = request.update_all_records

    if request.update_nameservers is not None:
        output["update_nameservers"] = request.update_nameservers

    if request.custom_records is not None:
        output["custom_records"] = [
            marshal_SyncDomainDnsRecordsRequestRecord(item, defaults)
            for item in request.custom_records
        ]

    if request.auto_config_domain_dns is not None:
        output["auto_config_domain_dns"] = marshal_AutoConfigDomainDns(
            request.auto_config_domain_dns, defaults
        )

    return output


def marshal_FreeDomainApiCheckFreeDomainAvailabilityRequest(
    request: FreeDomainApiCheckFreeDomainAvailabilityRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.slug is not None:
        output["slug"] = request.slug

    if request.root_domain is not None:
        output["root_domain"] = request.root_domain

    return output


def marshal_FtpAccountApiChangeFtpAccountPasswordRequest(
    request: FtpAccountApiChangeFtpAccountPasswordRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_FtpAccountApiCreateFtpAccountRequest(
    request: FtpAccountApiCreateFtpAccountRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    if request.path is not None:
        output["path"] = request.path

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_HostingApiAddCustomDomainRequest(
    request: HostingApiAddCustomDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain_name is not None:
        output["domain_name"] = request.domain_name

    return output


def marshal_CreateHostingRequestDomainConfiguration(
    request: CreateHostingRequestDomainConfiguration,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.update_nameservers is not None:
        output["update_nameservers"] = request.update_nameservers

    if request.update_web_record is not None:
        output["update_web_record"] = request.update_web_record

    if request.update_mail_record is not None:
        output["update_mail_record"] = request.update_mail_record

    if request.update_all_records is not None:
        output["update_all_records"] = request.update_all_records

    return output


def marshal_OfferOptionRequest(
    request: OfferOptionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.quantity is not None:
        output["quantity"] = request.quantity

    return output


def marshal_HostingApiCreateHostingRequest(
    request: HostingApiCreateHostingRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id

    if request.email is not None:
        output["email"] = request.email

    if request.domain is not None:
        output["domain"] = request.domain

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.subdomain is not None:
        output["subdomain"] = request.subdomain

    if request.offer_options is not None:
        output["offer_options"] = [
            marshal_OfferOptionRequest(item, defaults) for item in request.offer_options
        ]

    if request.language is not None:
        output["language"] = request.language

    if request.domain_configuration is not None:
        output["domain_configuration"] = (
            marshal_CreateHostingRequestDomainConfiguration(
                request.domain_configuration, defaults
            )
        )

    if request.skip_welcome_email is not None:
        output["skip_welcome_email"] = request.skip_welcome_email

    if request.auto_config_domain_dns is not None:
        output["auto_config_domain_dns"] = marshal_AutoConfigDomainDns(
            request.auto_config_domain_dns, defaults
        )

    return output


def marshal_HostingApiDeleteHostingDomainsRequest(
    request: HostingApiDeleteHostingDomainsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domains is not None:
        output["domains"] = request.domains

    return output


def marshal_HostingApiMigrateControlPanelRequest(
    request: HostingApiMigrateControlPanelRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.control_panel_name is not None:
        output["control_panel_name"] = request.control_panel_name

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id

    return output


def marshal_HostingApiRemoveCustomDomainRequest(
    request: HostingApiRemoveCustomDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain_name is not None:
        output["domain_name"] = request.domain_name

    return output


def marshal_HostingApiUpdateHostingFreeDomainRequest(
    request: HostingApiUpdateHostingFreeDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.free_domain is not None:
        output["free_domain"] = request.free_domain

    return output


def marshal_HostingApiUpdateHostingRequest(
    request: HostingApiUpdateHostingRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    if request.tags is not None:
        output["tags"] = request.tags

    if request.offer_options is not None:
        output["offer_options"] = [
            marshal_OfferOptionRequest(item, defaults) for item in request.offer_options
        ]

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id

    if request.protected is not None:
        output["protected"] = request.protected

    return output


def marshal_MailAccountApiChangeMailAccountPasswordRequest(
    request: MailAccountApiChangeMailAccountPasswordRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.username is not None:
        output["username"] = request.username

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_MailAccountApiCreateMailAccountRequest(
    request: MailAccountApiCreateMailAccountRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.username is not None:
        output["username"] = request.username

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_MailAccountApiRemoveMailAccountRequest(
    request: MailAccountApiRemoveMailAccountRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.username is not None:
        output["username"] = request.username

    return output


def marshal_WebsiteApiCreateWebsiteRequest(
    request: WebsiteApiCreateWebsiteRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain_name is not None:
        output["domain_name"] = request.domain_name

    return output
