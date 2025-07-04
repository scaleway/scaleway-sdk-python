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
    BlocklistType,
    DomainLastStatusAutoconfigStateReason,
    DomainLastStatusRecordStatus,
    DomainReputationStatus,
    DomainStatus,
    EmailFlag,
    EmailRcptType,
    EmailStatus,
    ListBlocklistsRequestOrderBy,
    ListEmailsRequestOrderBy,
    ListWebhookEventsRequestOrderBy,
    ListWebhooksRequestOrderBy,
    OfferName,
    PoolStatus,
    ProjectSettingsPeriodicReportFrequency,
    WebhookEventStatus,
    WebhookEventType,
    EmailTry,
    Email,
    DomainRecordsDMARC,
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

    args: Dict[str, Any] = {}

    field = data.get("rank", 0)
    args["rank"] = field

    field = data.get("code", 0)
    args["code"] = field

    field = data.get("message", str())
    args["message"] = field

    field = data.get("tried_at", None)
    args["tried_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return EmailTry(**args)

def unmarshal_Email(data: Any) -> Email:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Email' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("message_id", str())
    args["message_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("mail_from", str())
    args["mail_from"] = field

    field = data.get("mail_rcpt", str())
    args["mail_rcpt"] = field

    field = data.get("rcpt_to", None)
    args["rcpt_to"] = field

    field = data.get("rcpt_type", getattr(EmailRcptType, "UNKNOWN_RCPT_TYPE"))
    args["rcpt_type"] = field

    field = data.get("subject", str())
    args["subject"] = field

    field = data.get("status", getattr(EmailStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("try_count", 0)
    args["try_count"] = field

    field = data.get("last_tries", [])
    args["last_tries"] = [unmarshal_EmailTry(v) for v in field] if field is not None else None

    field = data.get("flags", [])
    args["flags"] = [EmailFlag(v) for v in field] if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("status_details", None)
    args["status_details"] = field

    return Email(**args)

def unmarshal_DomainRecordsDMARC(data: Any) -> DomainRecordsDMARC:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordsDMARC' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("value", str())
    args["value"] = field

    return DomainRecordsDMARC(**args)

def unmarshal_DomainRecords(data: Any) -> DomainRecords:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecords' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dmarc", None)
    args["dmarc"] = unmarshal_DomainRecordsDMARC(field) if field is not None else None

    return DomainRecords(**args)

def unmarshal_DomainReputation(data: Any) -> DomainReputation:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainReputation' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", getattr(DomainReputationStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("score", 0)
    args["score"] = field

    field = data.get("scored_at", None)
    args["scored_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("previous_score", None)
    args["previous_score"] = field

    field = data.get("previous_scored_at", None)
    args["previous_scored_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return DomainReputation(**args)

def unmarshal_DomainStatistics(data: Any) -> DomainStatistics:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainStatistics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("sent_count", str())
    args["sent_count"] = field

    field = data.get("failed_count", str())
    args["failed_count"] = field

    field = data.get("canceled_count", str())
    args["canceled_count"] = field

    return DomainStatistics(**args)

def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("status", getattr(DomainStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("spf_config", str())
    args["spf_config"] = field

    field = data.get("dkim_config", str())
    args["dkim_config"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("next_check_at", None)
    args["next_check_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("last_valid_at", None)
    args["last_valid_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("autoconfig", False)
    args["autoconfig"] = field

    field = data.get("region", )
    args["region"] = field

    field = data.get("revoked_at", None)
    args["revoked_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("last_error", None)
    args["last_error"] = field

    field = data.get("statistics", None)
    args["statistics"] = unmarshal_DomainStatistics(field) if field is not None else None

    field = data.get("reputation", None)
    args["reputation"] = unmarshal_DomainReputation(field) if field is not None else None

    field = data.get("records", None)
    args["records"] = unmarshal_DomainRecords(field) if field is not None else None

    return Domain(**args)

def unmarshal_OfferSubscription(data: Any) -> OfferSubscription:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferSubscription' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("offer_name", getattr(OfferName, "UNKNOWN_NAME"))
    args["offer_name"] = field

    field = data.get("sla", 0.0)
    args["sla"] = field

    field = data.get("max_domains", 0)
    args["max_domains"] = field

    field = data.get("max_dedicated_ips", 0)
    args["max_dedicated_ips"] = field

    field = data.get("max_webhooks_per_domain", 0)
    args["max_webhooks_per_domain"] = field

    field = data.get("max_custom_blocklists_per_domain", 0)
    args["max_custom_blocklists_per_domain"] = field

    field = data.get("included_monthly_emails", 0)
    args["included_monthly_emails"] = field

    field = data.get("subscribed_at", None)
    args["subscribed_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("cancellation_available_at", None)
    args["cancellation_available_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return OfferSubscription(**args)

def unmarshal_Webhook(data: Any) -> Webhook:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Webhook' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("domain_id", str())
    args["domain_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("event_types", [])
    args["event_types"] = [WebhookEventType(v) for v in field] if field is not None else None

    field = data.get("sns_arn", str())
    args["sns_arn"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Webhook(**args)

def unmarshal_Blocklist(data: Any) -> Blocklist:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Blocklist' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("domain_id", str())
    args["domain_id"] = field

    field = data.get("email", str())
    args["email"] = field

    field = data.get("type", getattr(BlocklistType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("reason", str())
    args["reason"] = field

    field = data.get("custom", False)
    args["custom"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("ends_at", None)
    args["ends_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Blocklist(**args)

def unmarshal_BulkCreateBlocklistsResponse(data: Any) -> BulkCreateBlocklistsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BulkCreateBlocklistsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("blocklists", [])
    args["blocklists"] = [unmarshal_Blocklist(v) for v in field] if field is not None else None

    return BulkCreateBlocklistsResponse(**args)

def unmarshal_CreateEmailResponse(data: Any) -> CreateEmailResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateEmailResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("emails", [])
    args["emails"] = [unmarshal_Email(v) for v in field] if field is not None else None

    return CreateEmailResponse(**args)

def unmarshal_DomainLastStatusAutoconfigState(data: Any) -> DomainLastStatusAutoconfigState:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusAutoconfigState' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", False)
    args["enabled"] = field

    field = data.get("autoconfigurable", False)
    args["autoconfigurable"] = field

    field = data.get("reason", None)
    args["reason"] = field

    return DomainLastStatusAutoconfigState(**args)

def unmarshal_DomainLastStatusDkimRecord(data: Any) -> DomainLastStatusDkimRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusDkimRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", getattr(DomainLastStatusRecordStatus, "UNKNOWN_RECORD_STATUS"))
    args["status"] = field

    field = data.get("last_valid_at", None)
    args["last_valid_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("error", None)
    args["error"] = field

    return DomainLastStatusDkimRecord(**args)

def unmarshal_DomainLastStatusDmarcRecord(data: Any) -> DomainLastStatusDmarcRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusDmarcRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", getattr(DomainLastStatusRecordStatus, "UNKNOWN_RECORD_STATUS"))
    args["status"] = field

    field = data.get("last_valid_at", None)
    args["last_valid_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("error", None)
    args["error"] = field

    return DomainLastStatusDmarcRecord(**args)

def unmarshal_DomainLastStatusSpfRecord(data: Any) -> DomainLastStatusSpfRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusSpfRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", getattr(DomainLastStatusRecordStatus, "UNKNOWN_RECORD_STATUS"))
    args["status"] = field

    field = data.get("last_valid_at", None)
    args["last_valid_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("error", None)
    args["error"] = field

    return DomainLastStatusSpfRecord(**args)

def unmarshal_DomainLastStatus(data: Any) -> DomainLastStatus:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatus' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain_id", str())
    args["domain_id"] = field

    field = data.get("domain_name", str())
    args["domain_name"] = field

    field = data.get("spf_record", None)
    args["spf_record"] = unmarshal_DomainLastStatusSpfRecord(field) if field is not None else None

    field = data.get("dkim_record", None)
    args["dkim_record"] = unmarshal_DomainLastStatusDkimRecord(field) if field is not None else None

    field = data.get("dmarc_record", None)
    args["dmarc_record"] = unmarshal_DomainLastStatusDmarcRecord(field) if field is not None else None

    field = data.get("autoconfig_state", None)
    args["autoconfig_state"] = unmarshal_DomainLastStatusAutoconfigState(field) if field is not None else None

    return DomainLastStatus(**args)

def unmarshal_ListBlocklistsResponse(data: Any) -> ListBlocklistsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBlocklistsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("blocklists", [])
    args["blocklists"] = [unmarshal_Blocklist(v) for v in field] if field is not None else None

    return ListBlocklistsResponse(**args)

def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("domains", [])
    args["domains"] = [unmarshal_Domain(v) for v in field] if field is not None else None

    return ListDomainsResponse(**args)

def unmarshal_ListEmailsResponse(data: Any) -> ListEmailsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListEmailsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("emails", [])
    args["emails"] = [unmarshal_Email(v) for v in field] if field is not None else None

    return ListEmailsResponse(**args)

def unmarshal_ListOfferSubscriptionsResponse(data: Any) -> ListOfferSubscriptionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOfferSubscriptionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("offer_subscriptions", [])
    args["offer_subscriptions"] = [unmarshal_OfferSubscription(v) for v in field] if field is not None else None

    return ListOfferSubscriptionsResponse(**args)

def unmarshal_Offer(data: Any) -> Offer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", getattr(OfferName, "UNKNOWN_NAME"))
    args["name"] = field

    field = data.get("sla", 0.0)
    args["sla"] = field

    field = data.get("max_domains", 0)
    args["max_domains"] = field

    field = data.get("max_dedicated_ips", 0)
    args["max_dedicated_ips"] = field

    field = data.get("included_monthly_emails", 0)
    args["included_monthly_emails"] = field

    field = data.get("max_webhooks_per_domain", 0)
    args["max_webhooks_per_domain"] = field

    field = data.get("max_custom_blocklists_per_domain", 0)
    args["max_custom_blocklists_per_domain"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("commitment_period", None)
    args["commitment_period"] = field

    return Offer(**args)

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

def unmarshal_Pool(data: Any) -> Pool:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Pool' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("status", getattr(PoolStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("ips", [])
    args["ips"] = field

    field = data.get("details", None)
    args["details"] = field

    field = data.get("zone", None)
    args["zone"] = field

    field = data.get("reverse", None)
    args["reverse"] = field

    return Pool(**args)

def unmarshal_ListPoolsResponse(data: Any) -> ListPoolsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPoolsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("pools", [])
    args["pools"] = [unmarshal_Pool(v) for v in field] if field is not None else None

    return ListPoolsResponse(**args)

def unmarshal_WebhookEvent(data: Any) -> WebhookEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'WebhookEvent' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("webhook_id", str())
    args["webhook_id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("domain_id", str())
    args["domain_id"] = field

    field = data.get("type", getattr(WebhookEventType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("status", getattr(WebhookEventStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("data", str())
    args["data"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("email_id", None)
    args["email_id"] = field

    return WebhookEvent(**args)

def unmarshal_ListWebhookEventsResponse(data: Any) -> ListWebhookEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWebhookEventsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("webhook_events", [])
    args["webhook_events"] = [unmarshal_WebhookEvent(v) for v in field] if field is not None else None

    return ListWebhookEventsResponse(**args)

def unmarshal_ListWebhooksResponse(data: Any) -> ListWebhooksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWebhooksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("webhooks", [])
    args["webhooks"] = [unmarshal_Webhook(v) for v in field] if field is not None else None

    return ListWebhooksResponse(**args)

def unmarshal_ProjectConsumption(data: Any) -> ProjectConsumption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectConsumption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("domains_count", 0)
    args["domains_count"] = field

    field = data.get("dedicated_ips_count", 0)
    args["dedicated_ips_count"] = field

    field = data.get("monthly_emails_count", 0)
    args["monthly_emails_count"] = field

    field = data.get("webhooks_count", 0)
    args["webhooks_count"] = field

    field = data.get("custom_blocklists_count", 0)
    args["custom_blocklists_count"] = field

    return ProjectConsumption(**args)

def unmarshal_ProjectSettingsPeriodicReport(data: Any) -> ProjectSettingsPeriodicReport:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectSettingsPeriodicReport' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", False)
    args["enabled"] = field

    field = data.get("frequency", getattr(ProjectSettingsPeriodicReportFrequency, "UNKNOWN_FREQUENCY"))
    args["frequency"] = field

    field = data.get("sending_hour", 0)
    args["sending_hour"] = field

    field = data.get("sending_day", 0)
    args["sending_day"] = field

    return ProjectSettingsPeriodicReport(**args)

def unmarshal_ProjectSettings(data: Any) -> ProjectSettings:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectSettings' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("periodic_report", None)
    args["periodic_report"] = unmarshal_ProjectSettingsPeriodicReport(field) if field is not None else None

    return ProjectSettings(**args)

def unmarshal_Statistics(data: Any) -> Statistics:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Statistics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("new_count", 0)
    args["new_count"] = field

    field = data.get("sending_count", 0)
    args["sending_count"] = field

    field = data.get("sent_count", 0)
    args["sent_count"] = field

    field = data.get("failed_count", 0)
    args["failed_count"] = field

    field = data.get("canceled_count", 0)
    args["canceled_count"] = field

    return Statistics(**args)

def marshal_BulkCreateBlocklistsRequest(
    request: BulkCreateBlocklistsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain_id is not None:
        output["domain_id"] = request.domain_id
    else:
        output["domain_id"] = str()

    if request.emails is not None:
        output["emails"] = request.emails
    else:
        output["emails"] = None

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = None

    if request.reason is not None:
        output["reason"] = request.reason
    else:
        output["reason"] = None


    return output

def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain_name is not None:
        output["domain_name"] = request.domain_name
    else:
        output["domain_name"] = str()

    if request.autoconfig is not None:
        output["autoconfig"] = request.autoconfig
    else:
        output["autoconfig"] = False

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.accept_tos is not None:
        output["accept_tos"] = request.accept_tos
    else:
        output["accept_tos"] = None


    return output

def marshal_CreateEmailRequestAddress(
    request: CreateEmailRequestAddress,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email
    else:
        output["email"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_CreateEmailRequestAttachment(
    request: CreateEmailRequestAttachment,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.type_ is not None:
        output["type"] = request.type_
    else:
        output["type"] = str()

    if request.content is not None:
        output["content"] = request.content
    else:
        output["content"] = str()


    return output

def marshal_CreateEmailRequestHeader(
    request: CreateEmailRequestHeader,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.key is not None:
        output["key"] = request.key
    else:
        output["key"] = str()

    if request.value is not None:
        output["value"] = request.value
    else:
        output["value"] = str()


    return output

def marshal_CreateEmailRequest(
    request: CreateEmailRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.from_ is not None:
        output["from"] = marshal_CreateEmailRequestAddress(request.from_, defaults)
    else:
        output["from"] = CreateEmailRequestAddress()

    if request.subject is not None:
        output["subject"] = request.subject
    else:
        output["subject"] = str()

    if request.text is not None:
        output["text"] = request.text
    else:
        output["text"] = str()

    if request.html is not None:
        output["html"] = request.html
    else:
        output["html"] = str()

    if request.to is not None:
        output["to"] = [marshal_CreateEmailRequestAddress(item, defaults) for item in request.to]
    else:
        output["to"] = None

    if request.cc is not None:
        output["cc"] = [marshal_CreateEmailRequestAddress(item, defaults) for item in request.cc]
    else:
        output["cc"] = None

    if request.bcc is not None:
        output["bcc"] = [marshal_CreateEmailRequestAddress(item, defaults) for item in request.bcc]
    else:
        output["bcc"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.attachments is not None:
        output["attachments"] = [marshal_CreateEmailRequestAttachment(item, defaults) for item in request.attachments]
    else:
        output["attachments"] = None

    if request.send_before is not None:
        output["send_before"] = request.send_before.isoformat()
    else:
        output["send_before"] = None

    if request.additional_headers is not None:
        output["additional_headers"] = [marshal_CreateEmailRequestHeader(item, defaults) for item in request.additional_headers]
    else:
        output["additional_headers"] = None


    return output

def marshal_CreateWebhookRequest(
    request: CreateWebhookRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain_id is not None:
        output["domain_id"] = request.domain_id
    else:
        output["domain_id"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.sns_arn is not None:
        output["sns_arn"] = request.sns_arn
    else:
        output["sns_arn"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.event_types is not None:
        output["event_types"] = [str(item) for item in request.event_types]
    else:
        output["event_types"] = None


    return output

def marshal_UpdateDomainRequest(
    request: UpdateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.autoconfig is not None:
        output["autoconfig"] = request.autoconfig
    else:
        output["autoconfig"] = None


    return output

def marshal_UpdateOfferSubscriptionRequest(
    request: UpdateOfferSubscriptionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.name is not None:
        output["name"] = str(request.name)
    else:
        output["name"] = None


    return output

def marshal_UpdateProjectSettingsRequestUpdatePeriodicReport(
    request: UpdateProjectSettingsRequestUpdatePeriodicReport,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enabled is not None:
        output["enabled"] = request.enabled
    else:
        output["enabled"] = None

    if request.frequency is not None:
        output["frequency"] = str(request.frequency)
    else:
        output["frequency"] = None

    if request.sending_hour is not None:
        output["sending_hour"] = request.sending_hour
    else:
        output["sending_hour"] = None

    if request.sending_day is not None:
        output["sending_day"] = request.sending_day
    else:
        output["sending_day"] = None


    return output

def marshal_UpdateProjectSettingsRequest(
    request: UpdateProjectSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.periodic_report is not None:
        output["periodic_report"] = marshal_UpdateProjectSettingsRequestUpdatePeriodicReport(request.periodic_report, defaults)
    else:
        output["periodic_report"] = None


    return output

def marshal_UpdateWebhookRequest(
    request: UpdateWebhookRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.event_types is not None:
        output["event_types"] = [str(item) for item in request.event_types]
    else:
        output["event_types"] = None

    if request.sns_arn is not None:
        output["sns_arn"] = request.sns_arn
    else:
        output["sns_arn"] = None


    return output
