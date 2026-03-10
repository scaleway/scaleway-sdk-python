# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    BlocklistType,
    DomainLastStatusAutoconfigStateReason,
    DomainLastStatusRecordStatus,
    DomainReputationStatus,
    DomainStatus,
    EmailFlag,
    EmailRcptType,
    EmailStatus,
    OfferName,
    PoolStatus,
    ProjectSettingsPeriodicReportFrequency,
    WebhookEventStatus,
    WebhookEventType,
    EmailTry,
    Email,
    DomainRecordsDKIM,
    DomainRecordsDMARC,
    DomainRecordsMX,
    DomainRecordsSPF,
    DomainRecords,
    DomainReputation,
    DomainStatistics,
    Domain,
    OfferSubscription,
    Webhook,
    Blocklist,
    BulkCreateBlocklistsResponse,
    CreateEmailResponse,
    DomainLastStatusAutoconfigState,
    DomainLastStatusDkimRecord,
    DomainLastStatusDmarcRecord,
    DomainLastStatusMXRecord,
    DomainLastStatusSpfRecord,
    DomainLastStatus,
    ListBlocklistsResponse,
    ListDomainsResponse,
    ListEmailsResponse,
    ListOfferSubscriptionsResponse,
    Offer,
    ListOffersResponse,
    Pool,
    ListPoolsResponse,
    WebhookEvent,
    ListWebhookEventsResponse,
    ListWebhooksResponse,
    ProjectConsumption,
    ProjectSettingsPeriodicReport,
    ProjectSettings,
    Statistics,
    BulkCreateBlocklistsRequest,
    CreateDomainRequest,
    CreateEmailRequestAddress,
    CreateEmailRequestAttachment,
    CreateEmailRequestHeader,
    CreateEmailRequest,
    CreateWebhookRequest,
    UpdateDomainRequest,
    UpdateOfferSubscriptionRequest,
    UpdateProjectSettingsRequestUpdatePeriodicReport,
    UpdateProjectSettingsRequest,
    UpdateWebhookRequest,
)


def unmarshal_EmailTry(data: Any) -> EmailTry:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EmailTry' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("rank", None)
    if field is not None:
        args["rank"] = field
    else:
        args["rank"] = 0

    field = data.get("code", None)
    if field is not None:
        args["code"] = field
    else:
        args["code"] = 0

    field = data.get("message", None)
    if field is not None:
        args["message"] = field
    else:
        args["message"] = None

    field = data.get("tried_at", None)
    if field is not None:
        args["tried_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["tried_at"] = None

    return EmailTry(**args)


def unmarshal_Email(data: Any) -> Email:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Email' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("message_id", None)
    if field is not None:
        args["message_id"] = field
    else:
        args["message_id"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("mail_from", None)
    if field is not None:
        args["mail_from"] = field
    else:
        args["mail_from"] = None

    field = data.get("rcpt_to", None)
    if field is not None:
        args["rcpt_to"] = field
    else:
        args["rcpt_to"] = None

    field = data.get("mail_rcpt", None)
    if field is not None:
        args["mail_rcpt"] = field
    else:
        args["mail_rcpt"] = None

    field = data.get("rcpt_type", None)
    if field is not None:
        args["rcpt_type"] = field
    else:
        args["rcpt_type"] = EmailRcptType.UNKNOWN_RCPT_TYPE

    field = data.get("subject", None)
    if field is not None:
        args["subject"] = field
    else:
        args["subject"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = EmailStatus.UNKNOWN

    field = data.get("try_count", None)
    if field is not None:
        args["try_count"] = field
    else:
        args["try_count"] = 0

    field = data.get("last_tries", None)
    if field is not None:
        args["last_tries"] = (
            [unmarshal_EmailTry(v) for v in field] if field is not None else None
        )
    else:
        args["last_tries"] = []

    field = data.get("flags", None)
    if field is not None:
        args["flags"] = [EmailFlag(v) for v in field] if field is not None else None
    else:
        args["flags"] = []

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

    field = data.get("status_details", None)
    if field is not None:
        args["status_details"] = field
    else:
        args["status_details"] = None

    return Email(**args)


def unmarshal_DomainRecordsDKIM(data: Any) -> DomainRecordsDKIM:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordsDKIM' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    return DomainRecordsDKIM(**args)


def unmarshal_DomainRecordsDMARC(data: Any) -> DomainRecordsDMARC:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordsDMARC' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    return DomainRecordsDMARC(**args)


def unmarshal_DomainRecordsMX(data: Any) -> DomainRecordsMX:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordsMX' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    return DomainRecordsMX(**args)


def unmarshal_DomainRecordsSPF(data: Any) -> DomainRecordsSPF:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordsSPF' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("value", None)
    if field is not None:
        args["value"] = field
    else:
        args["value"] = None

    return DomainRecordsSPF(**args)


def unmarshal_DomainRecords(data: Any) -> DomainRecords:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecords' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("dmarc", None)
    if field is not None:
        args["dmarc"] = unmarshal_DomainRecordsDMARC(field)
    else:
        args["dmarc"] = None

    field = data.get("dkim", None)
    if field is not None:
        args["dkim"] = unmarshal_DomainRecordsDKIM(field)
    else:
        args["dkim"] = None

    field = data.get("spf", None)
    if field is not None:
        args["spf"] = unmarshal_DomainRecordsSPF(field)
    else:
        args["spf"] = None

    field = data.get("mx", None)
    if field is not None:
        args["mx"] = unmarshal_DomainRecordsMX(field)
    else:
        args["mx"] = None

    return DomainRecords(**args)


def unmarshal_DomainReputation(data: Any) -> DomainReputation:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainReputation' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainReputationStatus.UNKNOWN_STATUS

    field = data.get("score", None)
    if field is not None:
        args["score"] = field
    else:
        args["score"] = 0

    field = data.get("scored_at", None)
    if field is not None:
        args["scored_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["scored_at"] = None

    field = data.get("previous_score", None)
    if field is not None:
        args["previous_score"] = field
    else:
        args["previous_score"] = 0

    field = data.get("previous_scored_at", None)
    if field is not None:
        args["previous_scored_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["previous_scored_at"] = None

    return DomainReputation(**args)


def unmarshal_DomainStatistics(data: Any) -> DomainStatistics:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainStatistics' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = None

    field = data.get("sent_count", None)
    if field is not None:
        args["sent_count"] = field
    else:
        args["sent_count"] = None

    field = data.get("failed_count", None)
    if field is not None:
        args["failed_count"] = field
    else:
        args["failed_count"] = None

    field = data.get("canceled_count", None)
    if field is not None:
        args["canceled_count"] = field
    else:
        args["canceled_count"] = None

    return DomainStatistics(**args)


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

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainStatus.UNKNOWN

    field = data.get("spf_config", None)
    if field is not None:
        args["spf_config"] = field
    else:
        args["spf_config"] = None

    field = data.get("dkim_config", None)
    if field is not None:
        args["dkim_config"] = field
    else:
        args["dkim_config"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("next_check_at", None)
    if field is not None:
        args["next_check_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["next_check_at"] = None

    field = data.get("last_valid_at", None)
    if field is not None:
        args["last_valid_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_valid_at"] = None

    field = data.get("autoconfig", None)
    if field is not None:
        args["autoconfig"] = field
    else:
        args["autoconfig"] = False

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("revoked_at", None)
    if field is not None:
        args["revoked_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["revoked_at"] = None

    field = data.get("last_error", None)
    if field is not None:
        args["last_error"] = field
    else:
        args["last_error"] = None

    field = data.get("statistics", None)
    if field is not None:
        args["statistics"] = unmarshal_DomainStatistics(field)
    else:
        args["statistics"] = None

    field = data.get("reputation", None)
    if field is not None:
        args["reputation"] = unmarshal_DomainReputation(field)
    else:
        args["reputation"] = None

    field = data.get("records", None)
    if field is not None:
        args["records"] = unmarshal_DomainRecords(field)
    else:
        args["records"] = None

    return Domain(**args)


def unmarshal_OfferSubscription(data: Any) -> OfferSubscription:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferSubscription' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

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

    field = data.get("offer_name", None)
    if field is not None:
        args["offer_name"] = field
    else:
        args["offer_name"] = OfferName.UNKNOWN_NAME

    field = data.get("sla", None)
    if field is not None:
        args["sla"] = field
    else:
        args["sla"] = 0.0

    field = data.get("max_domains", None)
    if field is not None:
        args["max_domains"] = field
    else:
        args["max_domains"] = 0

    field = data.get("max_dedicated_ips", None)
    if field is not None:
        args["max_dedicated_ips"] = field
    else:
        args["max_dedicated_ips"] = 0

    field = data.get("max_webhooks_per_domain", None)
    if field is not None:
        args["max_webhooks_per_domain"] = field
    else:
        args["max_webhooks_per_domain"] = 0

    field = data.get("max_custom_blocklists_per_domain", None)
    if field is not None:
        args["max_custom_blocklists_per_domain"] = field
    else:
        args["max_custom_blocklists_per_domain"] = 0

    field = data.get("included_monthly_emails", None)
    if field is not None:
        args["included_monthly_emails"] = field
    else:
        args["included_monthly_emails"] = 0

    field = data.get("subscribed_at", None)
    if field is not None:
        args["subscribed_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["subscribed_at"] = None

    field = data.get("cancellation_available_at", None)
    if field is not None:
        args["cancellation_available_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["cancellation_available_at"] = None

    return OfferSubscription(**args)


def unmarshal_Webhook(data: Any) -> Webhook:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Webhook' failed as data isn't a dictionary."
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

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("event_types", None)
    if field is not None:
        args["event_types"] = (
            [WebhookEventType(v) for v in field] if field is not None else None
        )
    else:
        args["event_types"] = []

    field = data.get("sns_arn", None)
    if field is not None:
        args["sns_arn"] = field
    else:
        args["sns_arn"] = None

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

    return Webhook(**args)


def unmarshal_Blocklist(data: Any) -> Blocklist:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Blocklist' failed as data isn't a dictionary."
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

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = BlocklistType.UNKNOWN_TYPE

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = None

    field = data.get("custom", None)
    if field is not None:
        args["custom"] = field
    else:
        args["custom"] = False

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

    field = data.get("ends_at", None)
    if field is not None:
        args["ends_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["ends_at"] = None

    return Blocklist(**args)


def unmarshal_BulkCreateBlocklistsResponse(data: Any) -> BulkCreateBlocklistsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BulkCreateBlocklistsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("blocklists", None)
    if field is not None:
        args["blocklists"] = (
            [unmarshal_Blocklist(v) for v in field] if field is not None else None
        )
    else:
        args["blocklists"] = []

    return BulkCreateBlocklistsResponse(**args)


def unmarshal_CreateEmailResponse(data: Any) -> CreateEmailResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateEmailResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("emails", None)
    if field is not None:
        args["emails"] = (
            [unmarshal_Email(v) for v in field] if field is not None else None
        )
    else:
        args["emails"] = []

    return CreateEmailResponse(**args)


def unmarshal_DomainLastStatusAutoconfigState(
    data: Any,
) -> DomainLastStatusAutoconfigState:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusAutoconfigState' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field
    else:
        args["enabled"] = False

    field = data.get("autoconfigurable", None)
    if field is not None:
        args["autoconfigurable"] = field
    else:
        args["autoconfigurable"] = False

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = DomainLastStatusAutoconfigStateReason.UNKNOWN_REASON

    return DomainLastStatusAutoconfigState(**args)


def unmarshal_DomainLastStatusDkimRecord(data: Any) -> DomainLastStatusDkimRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusDkimRecord' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainLastStatusRecordStatus.UNKNOWN_RECORD_STATUS

    field = data.get("last_valid_at", None)
    if field is not None:
        args["last_valid_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_valid_at"] = None

    field = data.get("error", None)
    if field is not None:
        args["error"] = field
    else:
        args["error"] = None

    return DomainLastStatusDkimRecord(**args)


def unmarshal_DomainLastStatusDmarcRecord(data: Any) -> DomainLastStatusDmarcRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusDmarcRecord' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainLastStatusRecordStatus.UNKNOWN_RECORD_STATUS

    field = data.get("last_valid_at", None)
    if field is not None:
        args["last_valid_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_valid_at"] = None

    field = data.get("error", None)
    if field is not None:
        args["error"] = field
    else:
        args["error"] = None

    return DomainLastStatusDmarcRecord(**args)


def unmarshal_DomainLastStatusMXRecord(data: Any) -> DomainLastStatusMXRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusMXRecord' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainLastStatusRecordStatus.UNKNOWN_RECORD_STATUS

    field = data.get("last_valid_at", None)
    if field is not None:
        args["last_valid_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_valid_at"] = None

    field = data.get("error", None)
    if field is not None:
        args["error"] = field
    else:
        args["error"] = None

    return DomainLastStatusMXRecord(**args)


def unmarshal_DomainLastStatusSpfRecord(data: Any) -> DomainLastStatusSpfRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusSpfRecord' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = DomainLastStatusRecordStatus.UNKNOWN_RECORD_STATUS

    field = data.get("last_valid_at", None)
    if field is not None:
        args["last_valid_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_valid_at"] = None

    field = data.get("error", None)
    if field is not None:
        args["error"] = field
    else:
        args["error"] = None

    return DomainLastStatusSpfRecord(**args)


def unmarshal_DomainLastStatus(data: Any) -> DomainLastStatus:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatus' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("domain_id", None)
    if field is not None:
        args["domain_id"] = field
    else:
        args["domain_id"] = None

    field = data.get("domain_name", None)
    if field is not None:
        args["domain_name"] = field
    else:
        args["domain_name"] = None

    field = data.get("spf_record", None)
    if field is not None:
        args["spf_record"] = unmarshal_DomainLastStatusSpfRecord(field)
    else:
        args["spf_record"] = None

    field = data.get("dkim_record", None)
    if field is not None:
        args["dkim_record"] = unmarshal_DomainLastStatusDkimRecord(field)
    else:
        args["dkim_record"] = None

    field = data.get("dmarc_record", None)
    if field is not None:
        args["dmarc_record"] = unmarshal_DomainLastStatusDmarcRecord(field)
    else:
        args["dmarc_record"] = None

    field = data.get("mx_record", None)
    if field is not None:
        args["mx_record"] = unmarshal_DomainLastStatusMXRecord(field)
    else:
        args["mx_record"] = None

    field = data.get("autoconfig_state", None)
    if field is not None:
        args["autoconfig_state"] = unmarshal_DomainLastStatusAutoconfigState(field)
    else:
        args["autoconfig_state"] = None

    return DomainLastStatus(**args)


def unmarshal_ListBlocklistsResponse(data: Any) -> ListBlocklistsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBlocklistsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("blocklists", None)
    if field is not None:
        args["blocklists"] = (
            [unmarshal_Blocklist(v) for v in field] if field is not None else None
        )
    else:
        args["blocklists"] = []

    return ListBlocklistsResponse(**args)


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


def unmarshal_ListEmailsResponse(data: Any) -> ListEmailsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListEmailsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("emails", None)
    if field is not None:
        args["emails"] = (
            [unmarshal_Email(v) for v in field] if field is not None else None
        )
    else:
        args["emails"] = []

    return ListEmailsResponse(**args)


def unmarshal_ListOfferSubscriptionsResponse(
    data: Any,
) -> ListOfferSubscriptionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOfferSubscriptionsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("offer_subscriptions", None)
    if field is not None:
        args["offer_subscriptions"] = (
            [unmarshal_OfferSubscription(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["offer_subscriptions"] = []

    return ListOfferSubscriptionsResponse(**args)


def unmarshal_Offer(data: Any) -> Offer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = OfferName.UNKNOWN_NAME

    field = data.get("sla", None)
    if field is not None:
        args["sla"] = field
    else:
        args["sla"] = 0.0

    field = data.get("max_domains", None)
    if field is not None:
        args["max_domains"] = field
    else:
        args["max_domains"] = 0

    field = data.get("max_dedicated_ips", None)
    if field is not None:
        args["max_dedicated_ips"] = field
    else:
        args["max_dedicated_ips"] = 0

    field = data.get("included_monthly_emails", None)
    if field is not None:
        args["included_monthly_emails"] = field
    else:
        args["included_monthly_emails"] = 0

    field = data.get("max_webhooks_per_domain", None)
    if field is not None:
        args["max_webhooks_per_domain"] = field
    else:
        args["max_webhooks_per_domain"] = 0

    field = data.get("max_custom_blocklists_per_domain", None)
    if field is not None:
        args["max_custom_blocklists_per_domain"] = field
    else:
        args["max_custom_blocklists_per_domain"] = 0

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("commitment_period", None)
    if field is not None:
        args["commitment_period"] = field
    else:
        args["commitment_period"] = None

    return Offer(**args)


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


def unmarshal_Pool(data: Any) -> Pool:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pool' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = PoolStatus.UNKNOWN_STATUS

    field = data.get("ips", None)
    if field is not None:
        args["ips"] = field
    else:
        args["ips"] = []

    field = data.get("details", None)
    if field is not None:
        args["details"] = field
    else:
        args["details"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("reverse", None)
    if field is not None:
        args["reverse"] = field
    else:
        args["reverse"] = None

    return Pool(**args)


def unmarshal_ListPoolsResponse(data: Any) -> ListPoolsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPoolsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("pools", None)
    if field is not None:
        args["pools"] = (
            [unmarshal_Pool(v) for v in field] if field is not None else None
        )
    else:
        args["pools"] = []

    return ListPoolsResponse(**args)


def unmarshal_WebhookEvent(data: Any) -> WebhookEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'WebhookEvent' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("webhook_id", None)
    if field is not None:
        args["webhook_id"] = field
    else:
        args["webhook_id"] = None

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

    field = data.get("domain_id", None)
    if field is not None:
        args["domain_id"] = field
    else:
        args["domain_id"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = WebhookEventType.UNKNOWN_TYPE

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = WebhookEventStatus.UNKNOWN_STATUS

    field = data.get("data", None)
    if field is not None:
        args["data"] = field
    else:
        args["data"] = None

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

    field = data.get("email_id", None)
    if field is not None:
        args["email_id"] = field
    else:
        args["email_id"] = None

    return WebhookEvent(**args)


def unmarshal_ListWebhookEventsResponse(data: Any) -> ListWebhookEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWebhookEventsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("webhook_events", None)
    if field is not None:
        args["webhook_events"] = (
            [unmarshal_WebhookEvent(v) for v in field] if field is not None else None
        )
    else:
        args["webhook_events"] = []

    return ListWebhookEventsResponse(**args)


def unmarshal_ListWebhooksResponse(data: Any) -> ListWebhooksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWebhooksResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("webhooks", None)
    if field is not None:
        args["webhooks"] = (
            [unmarshal_Webhook(v) for v in field] if field is not None else None
        )
    else:
        args["webhooks"] = []

    return ListWebhooksResponse(**args)


def unmarshal_ProjectConsumption(data: Any) -> ProjectConsumption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectConsumption' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("domains_count", None)
    if field is not None:
        args["domains_count"] = field
    else:
        args["domains_count"] = 0

    field = data.get("dedicated_ips_count", None)
    if field is not None:
        args["dedicated_ips_count"] = field
    else:
        args["dedicated_ips_count"] = 0

    field = data.get("monthly_emails_count", None)
    if field is not None:
        args["monthly_emails_count"] = field
    else:
        args["monthly_emails_count"] = 0

    field = data.get("webhooks_count", None)
    if field is not None:
        args["webhooks_count"] = field
    else:
        args["webhooks_count"] = 0

    field = data.get("custom_blocklists_count", None)
    if field is not None:
        args["custom_blocklists_count"] = field
    else:
        args["custom_blocklists_count"] = 0

    return ProjectConsumption(**args)


def unmarshal_ProjectSettingsPeriodicReport(data: Any) -> ProjectSettingsPeriodicReport:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectSettingsPeriodicReport' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field
    else:
        args["enabled"] = False

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field
    else:
        args["frequency"] = ProjectSettingsPeriodicReportFrequency.UNKNOWN_FREQUENCY

    field = data.get("sending_hour", None)
    if field is not None:
        args["sending_hour"] = field
    else:
        args["sending_hour"] = 0

    field = data.get("sending_day", None)
    if field is not None:
        args["sending_day"] = field
    else:
        args["sending_day"] = 0

    return ProjectSettingsPeriodicReport(**args)


def unmarshal_ProjectSettings(data: Any) -> ProjectSettings:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectSettings' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("periodic_report", None)
    if field is not None:
        args["periodic_report"] = unmarshal_ProjectSettingsPeriodicReport(field)
    else:
        args["periodic_report"] = None

    return ProjectSettings(**args)


def unmarshal_Statistics(data: Any) -> Statistics:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Statistics' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("new_count", None)
    if field is not None:
        args["new_count"] = field
    else:
        args["new_count"] = 0

    field = data.get("sending_count", None)
    if field is not None:
        args["sending_count"] = field
    else:
        args["sending_count"] = 0

    field = data.get("sent_count", None)
    if field is not None:
        args["sent_count"] = field
    else:
        args["sent_count"] = 0

    field = data.get("failed_count", None)
    if field is not None:
        args["failed_count"] = field
    else:
        args["failed_count"] = 0

    field = data.get("canceled_count", None)
    if field is not None:
        args["canceled_count"] = field
    else:
        args["canceled_count"] = 0

    return Statistics(**args)


def marshal_BulkCreateBlocklistsRequest(
    request: BulkCreateBlocklistsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain_id is not None:
        output["domain_id"] = request.domain_id

    if request.emails is not None:
        output["emails"] = request.emails

    if request.type_ is not None:
        output["type"] = request.type_

    if request.reason is not None:
        output["reason"] = request.reason

    return output


def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain_name is not None:
        output["domain_name"] = request.domain_name

    if request.accept_tos is not None:
        output["accept_tos"] = request.accept_tos

    if request.autoconfig is not None:
        output["autoconfig"] = request.autoconfig

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    return output


def marshal_CreateEmailRequestAddress(
    request: CreateEmailRequestAddress,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreateEmailRequestAttachment(
    request: CreateEmailRequestAttachment,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.type_ is not None:
        output["type"] = request.type_

    if request.content is not None:
        output["content"] = request.content

    return output


def marshal_CreateEmailRequestHeader(
    request: CreateEmailRequestHeader,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.key is not None:
        output["key"] = request.key

    if request.value is not None:
        output["value"] = request.value

    return output


def marshal_CreateEmailRequest(
    request: CreateEmailRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.from_ is not None:
        output["from"] = marshal_CreateEmailRequestAddress(request.from_, defaults)

    if request.subject is not None:
        output["subject"] = request.subject

    if request.text is not None:
        output["text"] = request.text

    if request.html is not None:
        output["html"] = request.html

    if request.to is not None:
        output["to"] = [
            marshal_CreateEmailRequestAddress(item, defaults) for item in request.to
        ]

    if request.cc is not None:
        output["cc"] = [
            marshal_CreateEmailRequestAddress(item, defaults) for item in request.cc
        ]

    if request.bcc is not None:
        output["bcc"] = [
            marshal_CreateEmailRequestAddress(item, defaults) for item in request.bcc
        ]

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.attachments is not None:
        output["attachments"] = [
            marshal_CreateEmailRequestAttachment(item, defaults)
            for item in request.attachments
        ]

    if request.send_before is not None:
        output["send_before"] = request.send_before.isoformat()

    if request.additional_headers is not None:
        output["additional_headers"] = [
            marshal_CreateEmailRequestHeader(item, defaults)
            for item in request.additional_headers
        ]

    return output


def marshal_CreateWebhookRequest(
    request: CreateWebhookRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.domain_id is not None:
        output["domain_id"] = request.domain_id

    if request.name is not None:
        output["name"] = request.name

    if request.sns_arn is not None:
        output["sns_arn"] = request.sns_arn

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.event_types is not None:
        output["event_types"] = [str(item) for item in request.event_types]

    return output


def marshal_UpdateDomainRequest(
    request: UpdateDomainRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.autoconfig is not None:
        output["autoconfig"] = request.autoconfig

    return output


def marshal_UpdateOfferSubscriptionRequest(
    request: UpdateOfferSubscriptionRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = defaults.default_project_id

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_UpdateProjectSettingsRequestUpdatePeriodicReport(
    request: UpdateProjectSettingsRequestUpdatePeriodicReport,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.enabled is not None:
        output["enabled"] = request.enabled

    if request.frequency is not None:
        output["frequency"] = request.frequency

    if request.sending_hour is not None:
        output["sending_hour"] = request.sending_hour

    if request.sending_day is not None:
        output["sending_day"] = request.sending_day

    return output


def marshal_UpdateProjectSettingsRequest(
    request: UpdateProjectSettingsRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.periodic_report is not None:
        output["periodic_report"] = (
            marshal_UpdateProjectSettingsRequestUpdatePeriodicReport(
                request.periodic_report, defaults
            )
        )

    return output


def marshal_UpdateWebhookRequest(
    request: UpdateWebhookRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.event_types is not None:
        output["event_types"] = [str(item) for item in request.event_types]

    if request.sns_arn is not None:
        output["sns_arn"] = request.sns_arn

    return output
