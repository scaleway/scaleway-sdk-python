# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    DomainRecordDNSType,
    DomainRecordLevel,
    DomainRecordStatus,
    DomainStatus,
    MailboxStatus,
    MailboxSubscriptionPeriod,
    Mailbox,
    Domain,
    BatchCreateMailboxesResponse,
    DomainRecord,
    GetDomainRecordsResponse,
    ListDomainsResponse,
    ListMailboxesResponse,
    BatchCreateMailboxesRequestMailboxParameters,
    BatchCreateMailboxesRequest,
    CreateDomainRequest,
    UpdateMailboxRequest,
)


def unmarshal_Mailbox(data: Any) -> Mailbox:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Mailbox' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("domain_id", None)
    if field is not None:
        args["domain_id"] = field
    else:
        args["domain_id"] = None

    field = data.get("email", None)
    if field is not None:
        args["email"] = field
    else:
        args["email"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = MailboxStatus.UNKNOWN_STATUS

    field = data.get("subscription_period", None)
    if field is not None:
        args["subscription_period"] = field
    else:
        args["subscription_period"] = (
            MailboxSubscriptionPeriod.UNKNOWN_SUBSCRIPTION_PERIOD
        )

    field = data.get("next_subscription_period", None)
    if field is not None:
        args["next_subscription_period"] = field
    else:
        args["next_subscription_period"] = (
            MailboxSubscriptionPeriod.UNKNOWN_SUBSCRIPTION_PERIOD
        )

    field = data.get("subscription_period_started_at", None)
    if field is not None:
        args["subscription_period_started_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["subscription_period_started_at"] = None

    field = data.get("next_subscription_period_starts_at", None)
    if field is not None:
        args["next_subscription_period_starts_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["next_subscription_period_starts_at"] = None

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

    field = data.get("deletion_scheduled_at", None)
    if field is not None:
        args["deletion_scheduled_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["deletion_scheduled_at"] = None

    return Mailbox(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
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

    field = data.get("mailbox_total_count", None)
    if field is not None:
        args["mailbox_total_count"] = field
    else:
        args["mailbox_total_count"] = 0

    field = data.get("webmail_url", None)
    if field is not None:
        args["webmail_url"] = field
    else:
        args["webmail_url"] = None

    field = data.get("imap_url", None)
    if field is not None:
        args["imap_url"] = field
    else:
        args["imap_url"] = None

    field = data.get("pop3_url", None)
    if field is not None:
        args["pop3_url"] = field
    else:
        args["pop3_url"] = None

    field = data.get("smtp_url", None)
    if field is not None:
        args["smtp_url"] = field
    else:
        args["smtp_url"] = None

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

    return Domain(**args)


def unmarshal_BatchCreateMailboxesResponse(data: Any) -> BatchCreateMailboxesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BatchCreateMailboxesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("mailboxes", None)
    if field is not None:
        args["mailboxes"] = (
            [unmarshal_Mailbox(v) for v in field] if field is not None else None
        )
    else:
        args["mailboxes"] = []

    return BatchCreateMailboxesResponse(**args)


def unmarshal_DomainRecord(data: Any) -> DomainRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecord' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("domain_id", None)
    if field is not None:
        args["domain_id"] = field
    else:
        args["domain_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainRecordStatus.UNKNOWN_STATUS

    field = data.get("level", None)
    if field is not None:
        args["level"] = field
    else:
        args["level"] = DomainRecordLevel.UNKNOWN_LEVEL

    field = data.get("dns_type", None)
    if field is not None:
        args["dns_type"] = field
    else:
        args["dns_type"] = DomainRecordDNSType.UNKNOWN_DNS_TYPE

    field = data.get("dns_name", None)
    if field is not None:
        args["dns_name"] = field
    else:
        args["dns_name"] = None

    field = data.get("dns_value", None)
    if field is not None:
        args["dns_value"] = field
    else:
        args["dns_value"] = None

    field = data.get("error", None)
    if field is not None:
        args["error"] = field
    else:
        args["error"] = None

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

    return DomainRecord(**args)


def unmarshal_GetDomainRecordsResponse(data: Any) -> GetDomainRecordsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetDomainRecordsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("autoconfig", None)
    if field is not None:
        args["autoconfig"] = unmarshal_DomainRecord(field)
    else:
        args["autoconfig"] = None

    field = data.get("autodiscover", None)
    if field is not None:
        args["autodiscover"] = unmarshal_DomainRecord(field)
    else:
        args["autodiscover"] = None

    field = data.get("caldav", None)
    if field is not None:
        args["caldav"] = unmarshal_DomainRecord(field)
    else:
        args["caldav"] = None

    field = data.get("carddav", None)
    if field is not None:
        args["carddav"] = unmarshal_DomainRecord(field)
    else:
        args["carddav"] = None

    field = data.get("dkim", None)
    if field is not None:
        args["dkim"] = unmarshal_DomainRecord(field)
    else:
        args["dkim"] = None

    field = data.get("dmarc", None)
    if field is not None:
        args["dmarc"] = unmarshal_DomainRecord(field)
    else:
        args["dmarc"] = None

    field = data.get("domain_validation", None)
    if field is not None:
        args["domain_validation"] = unmarshal_DomainRecord(field)
    else:
        args["domain_validation"] = None

    field = data.get("imap", None)
    if field is not None:
        args["imap"] = unmarshal_DomainRecord(field)
    else:
        args["imap"] = None

    field = data.get("mx", None)
    if field is not None:
        args["mx"] = unmarshal_DomainRecord(field)
    else:
        args["mx"] = None

    field = data.get("pop3", None)
    if field is not None:
        args["pop3"] = unmarshal_DomainRecord(field)
    else:
        args["pop3"] = None

    field = data.get("spf", None)
    if field is not None:
        args["spf"] = unmarshal_DomainRecord(field)
    else:
        args["spf"] = None

    field = data.get("submission", None)
    if field is not None:
        args["submission"] = unmarshal_DomainRecord(field)
    else:
        args["submission"] = None

    return GetDomainRecordsResponse(**args)


def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("domains", None)
    if field is not None:
        args["domains"] = (
            [unmarshal_Domain(v) for v in field] if field is not None else None
        )
    else:
        args["domains"] = []

    return ListDomainsResponse(**args)


def unmarshal_ListMailboxesResponse(data: Any) -> ListMailboxesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListMailboxesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("mailboxes", None)
    if field is not None:
        args["mailboxes"] = (
            [unmarshal_Mailbox(v) for v in field] if field is not None else None
        )
    else:
        args["mailboxes"] = []

    return ListMailboxesResponse(**args)


def marshal_BatchCreateMailboxesRequestMailboxParameters(
    request: BatchCreateMailboxesRequestMailboxParameters,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.local_part is not None:
        output["local_part"] = request.local_part

    if request.password is not None:
        output["password"] = request.password

    return output


def marshal_BatchCreateMailboxesRequest(
    request: BatchCreateMailboxesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain_id is not None:
        output["domain_id"] = request.domain_id

    if request.mailboxes is not None:
        output["mailboxes"] = [
            marshal_BatchCreateMailboxesRequestMailboxParameters(item, defaults)
            for item in request.mailboxes
        ]

    if request.subscription_period is not None:
        output["subscription_period"] = request.subscription_period

    return output


def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_UpdateMailboxRequest(
    request: UpdateMailboxRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.subscription_period is not None:
        output["subscription_period"] = request.subscription_period

    if request.new_password is not None:
        output["new_password"] = request.new_password

    return output
