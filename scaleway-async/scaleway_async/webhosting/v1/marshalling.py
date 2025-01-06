# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
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
    DatabaseUser,
    Database,
    FtpAccount,
    MailAccount,
    CheckUserOwnsDomainResponse,
    DnsRecord,
    Nameserver,
    DnsRecords,
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

    field = data.get("username", None)
    if field is not None:
        args["username"] = field

    field = data.get("databases", None)
    if field is not None:
        args["databases"] = field

    return DatabaseUser(**args)


def unmarshal_Database(data: Any) -> Database:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Database' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("database_name", None)
    if field is not None:
        args["database_name"] = field

    field = data.get("users", None)
    if field is not None:
        args["users"] = field

    return Database(**args)


def unmarshal_FtpAccount(data: Any) -> FtpAccount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'FtpAccount' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("username", None)
    if field is not None:
        args["username"] = field

    field = data.get("path", None)
    if field is not None:
        args["path"] = field

    return FtpAccount(**args)


def unmarshal_MailAccount(data: Any) -> MailAccount:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MailAccount' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field

    field = data.get("username", None)
    if field is not None:
        args["username"] = field

    return MailAccount(**args)


def unmarshal_CheckUserOwnsDomainResponse(data: Any) -> CheckUserOwnsDomainResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckUserOwnsDomainResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("owns_domain", None)
    if field is not None:
        args["owns_domain"] = field

    return CheckUserOwnsDomainResponse(**args)


def unmarshal_DnsRecord(data: Any) -> DnsRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DnsRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("ttl", None)
    if field is not None:
        args["ttl"] = field

    field = data.get("value", None)
    if field is not None:
        args["value"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("priority", None)
    if field is not None:
        args["priority"] = field
    else:
        args["priority"] = None

    return DnsRecord(**args)


def unmarshal_Nameserver(data: Any) -> Nameserver:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Nameserver' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("is_default", None)
    if field is not None:
        args["is_default"] = field

    return Nameserver(**args)


def unmarshal_DnsRecords(data: Any) -> DnsRecords:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DnsRecords' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("records", None)
    if field is not None:
        args["records"] = (
            [unmarshal_DnsRecord(v) for v in field] if field is not None else None
        )

    field = data.get("name_servers", None)
    if field is not None:
        args["name_servers"] = (
            [unmarshal_Nameserver(v) for v in field] if field is not None else None
        )

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    return DnsRecords(**args)


def unmarshal_PlatformControlPanelUrls(data: Any) -> PlatformControlPanelUrls:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PlatformControlPanelUrls' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dashboard", None)
    if field is not None:
        args["dashboard"] = field

    field = data.get("webmail", None)
    if field is not None:
        args["webmail"] = field

    return PlatformControlPanelUrls(**args)


def unmarshal_OfferOption(data: Any) -> OfferOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("billing_operation_path", None)
    if field is not None:
        args["billing_operation_path"] = field

    field = data.get("min_value", None)
    if field is not None:
        args["min_value"] = field

    field = data.get("current_value", None)
    if field is not None:
        args["current_value"] = field

    field = data.get("max_value", None)
    if field is not None:
        args["max_value"] = field

    field = data.get("quota_warning", None)
    if field is not None:
        args["quota_warning"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("username", None)
    if field is not None:
        args["username"] = field

    field = data.get("contact_email", None)
    if field is not None:
        args["contact_email"] = field

    field = data.get("one_time_password", None)
    if field is not None:
        args["one_time_password"] = field
    else:
        args["one_time_password"] = None

    return HostingUser(**args)


def unmarshal_Offer(data: Any) -> Offer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("billing_operation_path", None)
    if field is not None:
        args["billing_operation_path"] = field

    field = data.get("options", None)
    if field is not None:
        args["options"] = (
            [unmarshal_OfferOption(v) for v in field] if field is not None else None
        )

    field = data.get("available", None)
    if field is not None:
        args["available"] = field

    field = data.get("control_panel_name", None)
    if field is not None:
        args["control_panel_name"] = field

    field = data.get("end_of_life", None)
    if field is not None:
        args["end_of_life"] = field

    field = data.get("quota_warning", None)
    if field is not None:
        args["quota_warning"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("hostname", None)
    if field is not None:
        args["hostname"] = field

    field = data.get("number", None)
    if field is not None:
        args["number"] = field

    field = data.get("group_name", None)
    if field is not None:
        args["group_name"] = field

    field = data.get("ipv4", None)
    if field is not None:
        args["ipv4"] = field

    field = data.get("ipv6", None)
    if field is not None:
        args["ipv6"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field

    field = data.get("dns_status", None)
    if field is not None:
        args["dns_status"] = field

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("ipv4", None)
    if field is not None:
        args["ipv4"] = field

    field = data.get("protected", None)
    if field is not None:
        args["protected"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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

    field = data.get("user", None)
    if field is not None:
        args["user"] = unmarshal_HostingUser(field)
    else:
        args["user"] = None

    return Hosting(**args)


def unmarshal_ControlPanel(data: Any) -> ControlPanel:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ControlPanel' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("available", None)
    if field is not None:
        args["available"] = field

    field = data.get("logo_url", None)
    if field is not None:
        args["logo_url"] = field

    field = data.get("available_languages", None)
    if field is not None:
        args["available_languages"] = (
            [StdLanguageCode(v) for v in field] if field is not None else None
        )

    return ControlPanel(**args)


def unmarshal_ListControlPanelsResponse(data: Any) -> ListControlPanelsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListControlPanelsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("control_panels", None)
    if field is not None:
        args["control_panels"] = (
            [unmarshal_ControlPanel(v) for v in field] if field is not None else None
        )

    return ListControlPanelsResponse(**args)


def unmarshal_ListDatabaseUsersResponse(data: Any) -> ListDatabaseUsersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabaseUsersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("users", None)
    if field is not None:
        args["users"] = (
            [unmarshal_DatabaseUser(v) for v in field] if field is not None else None
        )

    return ListDatabaseUsersResponse(**args)


def unmarshal_ListDatabasesResponse(data: Any) -> ListDatabasesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDatabasesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("databases", None)
    if field is not None:
        args["databases"] = (
            [unmarshal_Database(v) for v in field] if field is not None else None
        )

    return ListDatabasesResponse(**args)


def unmarshal_ListFtpAccountsResponse(data: Any) -> ListFtpAccountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFtpAccountsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("ftp_accounts", None)
    if field is not None:
        args["ftp_accounts"] = (
            [unmarshal_FtpAccount(v) for v in field] if field is not None else None
        )

    return ListFtpAccountsResponse(**args)


def unmarshal_HostingSummary(data: Any) -> HostingSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HostingSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field

    field = data.get("protected", None)
    if field is not None:
        args["protected"] = field

    field = data.get("dns_status", None)
    if field is not None:
        args["dns_status"] = field

    field = data.get("offer_name", None)
    if field is not None:
        args["offer_name"] = field

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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

    return HostingSummary(**args)


def unmarshal_ListHostingsResponse(data: Any) -> ListHostingsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListHostingsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("hostings", None)
    if field is not None:
        args["hostings"] = (
            [unmarshal_HostingSummary(v) for v in field] if field is not None else None
        )

    return ListHostingsResponse(**args)


def unmarshal_ListMailAccountsResponse(data: Any) -> ListMailAccountsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListMailAccountsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("mail_accounts", None)
    if field is not None:
        args["mail_accounts"] = (
            [unmarshal_MailAccount(v) for v in field] if field is not None else None
        )

    return ListMailAccountsResponse(**args)


def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("offers", None)
    if field is not None:
        args["offers"] = (
            [unmarshal_Offer(v) for v in field] if field is not None else None
        )

    return ListOffersResponse(**args)


def unmarshal_Website(data: Any) -> Website:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Website' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain", None)
    if field is not None:
        args["domain"] = field

    field = data.get("path", None)
    if field is not None:
        args["path"] = field

    field = data.get("ssl_status", None)
    if field is not None:
        args["ssl_status"] = field

    return Website(**args)


def unmarshal_ListWebsitesResponse(data: Any) -> ListWebsitesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWebsitesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("websites", None)
    if field is not None:
        args["websites"] = (
            [unmarshal_Website(v) for v in field] if field is not None else None
        )

    return ListWebsitesResponse(**args)


def unmarshal_ResetHostingPasswordResponse(data: Any) -> ResetHostingPasswordResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ResetHostingPasswordResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("one_time_password", None)
    if field is not None:
        args["one_time_password"] = field

    return ResetHostingPasswordResponse(**args)


def unmarshal_ResourceSummary(data: Any) -> ResourceSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ResourceSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("databases_count", None)
    if field is not None:
        args["databases_count"] = field

    field = data.get("mail_accounts_count", None)
    if field is not None:
        args["mail_accounts_count"] = field

    field = data.get("ftp_accounts_count", None)
    if field is not None:
        args["ftp_accounts_count"] = field

    field = data.get("websites_count", None)
    if field is not None:
        args["websites_count"] = field

    return ResourceSummary(**args)


def unmarshal_Session(data: Any) -> Session:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Session' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("url", None)
    if field is not None:
        args["url"] = field

    return Session(**args)


def marshal_DatabaseApiAssignDatabaseUserRequest(
    request: DatabaseApiAssignDatabaseUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    return output


def marshal_DatabaseApiChangeDatabaseUserPasswordRequest(
    request: DatabaseApiChangeDatabaseUserPasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_CreateDatabaseRequestUser(
    request: CreateDatabaseRequestUser,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_DatabaseApiCreateDatabaseRequest(
    request: DatabaseApiCreateDatabaseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility("new_user", request.new_user),
                OneOfPossibility("existing_username", request.existing_username),
            ]
        ),
    )

    if request.database_name is not None:
        output["database_name"] = request.database_name

    return output


def marshal_DatabaseApiCreateDatabaseUserRequest(
    request: DatabaseApiCreateDatabaseUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_DatabaseApiUnassignDatabaseUserRequest(
    request: DatabaseApiUnassignDatabaseUserRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    return output


def marshal_DnsApiCheckUserOwnsDomainRequest(
    request: DnsApiCheckUserOwnsDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_SyncDomainDnsRecordsRequestRecord(
    request: SyncDomainDnsRecordsRequestRecord,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.type_ is not None:
        output["type"] = str(request.type_)

    return output


def marshal_DnsApiSyncDomainDnsRecordsRequest(
    request: DnsApiSyncDomainDnsRecordsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.update_web_records is not None:
        output["update_web_records"] = request.update_web_records

    if request.update_mail_records is not None:
        output["update_mail_records"] = request.update_mail_records

    if request.update_all_records is not None:
        output["update_all_records"] = request.update_all_records

    if request.custom_records is not None:
        output["custom_records"] = [
            marshal_SyncDomainDnsRecordsRequestRecord(item, defaults)
            for item in request.custom_records
        ]

    return output


def marshal_FtpAccountApiChangeFtpAccountPasswordRequest(
    request: FtpAccountApiChangeFtpAccountPasswordRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_FtpAccountApiCreateFtpAccountRequest(
    request: FtpAccountApiCreateFtpAccountRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.username is not None:
        output["username"] = request.username

    if request.path is not None:
        output["path"] = request.path

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_CreateHostingRequestDomainConfiguration(
    request: CreateHostingRequestDomainConfiguration,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.id is not None:
        output["id"] = request.id

    if request.quantity is not None:
        output["quantity"] = request.quantity

    return output


def marshal_HostingApiCreateHostingRequest(
    request: HostingApiCreateHostingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id

    if request.email is not None:
        output["email"] = request.email

    if request.domain is not None:
        output["domain"] = request.domain

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.tags is not None:
        output["tags"] = request.tags

    if request.offer_options is not None:
        output["offer_options"] = [
            marshal_OfferOptionRequest(item, defaults) for item in request.offer_options
        ]

    if request.language is not None:
        output["language"] = str(request.language)

    if request.domain_configuration is not None:
        output["domain_configuration"] = (
            marshal_CreateHostingRequestDomainConfiguration(
                request.domain_configuration, defaults
            )
        )

    if request.skip_welcome_email is not None:
        output["skip_welcome_email"] = request.skip_welcome_email

    return output


def marshal_HostingApiUpdateHostingRequest(
    request: HostingApiUpdateHostingRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain is not None:
        output["domain"] = request.domain

    if request.username is not None:
        output["username"] = request.username

    return output
