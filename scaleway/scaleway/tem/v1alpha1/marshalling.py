# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    EmailFlag,
    WebhookEventType,
    EmailTry,
    Email,
    DomainRecordsDMARC,
    DomainRecords,
    DomainReputation,
    DomainStatistics,
    Domain,
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
    WebhookEvent,
    ListWebhookEventsResponse,
    ListWebhooksResponse,
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

    field = data.get("rank", None)
    if field is not None:
        args["rank"] = field

    field = data.get("code", None)
    if field is not None:
        args["code"] = field

    field = data.get("message", None)
    if field is not None:
        args["message"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("message_id", None)
    if field is not None:
        args["message_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("mail_from", None)
    if field is not None:
        args["mail_from"] = field

    field = data.get("mail_rcpt", None)
    if field is not None:
        args["mail_rcpt"] = field

    field = data.get("rcpt_to", None)
    if field is not None:
        args["rcpt_to"] = field
    else:
        args["rcpt_to"] = None

    field = data.get("rcpt_type", None)
    if field is not None:
        args["rcpt_type"] = field

    field = data.get("subject", None)
    if field is not None:
        args["subject"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("try_count", None)
    if field is not None:
        args["try_count"] = field

    field = data.get("last_tries", None)
    if field is not None:
        args["last_tries"] = (
            [unmarshal_EmailTry(v) for v in field] if field is not None else None
        )

    field = data.get("flags", None)
    if field is not None:
        args["flags"] = [EmailFlag(v) for v in field] if field is not None else None

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


def unmarshal_DomainRecordsDMARC(data: Any) -> DomainRecordsDMARC:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecordsDMARC' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("value", None)
    if field is not None:
        args["value"] = field

    return DomainRecordsDMARC(**args)


def unmarshal_DomainRecords(data: Any) -> DomainRecords:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainRecords' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("dmarc", None)
    if field is not None:
        args["dmarc"] = unmarshal_DomainRecordsDMARC(field)
    else:
        args["dmarc"] = None

    return DomainRecords(**args)


def unmarshal_DomainReputation(data: Any) -> DomainReputation:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainReputation' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("score", None)
    if field is not None:
        args["score"] = field

    field = data.get("scored_at", None)
    if field is not None:
        args["scored_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["scored_at"] = None

    field = data.get("previous_score", None)
    if field is not None:
        args["previous_score"] = field
    else:
        args["previous_score"] = None

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

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("sent_count", None)
    if field is not None:
        args["sent_count"] = field

    field = data.get("failed_count", None)
    if field is not None:
        args["failed_count"] = field

    field = data.get("canceled_count", None)
    if field is not None:
        args["canceled_count"] = field

    return DomainStatistics(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("spf_config", None)
    if field is not None:
        args["spf_config"] = field

    field = data.get("dkim_config", None)
    if field is not None:
        args["dkim_config"] = field

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

    field = data.get("region", None)
    if field is not None:
        args["region"] = field

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


def unmarshal_Webhook(data: Any) -> Webhook:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Webhook' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("domain_id", None)
    if field is not None:
        args["domain_id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("name", None)
    if field is not None:
        args["name"] = field

    field = data.get("event_types", None)
    if field is not None:
        args["event_types"] = (
            [WebhookEventType(v) for v in field] if field is not None else None
        )

    field = data.get("sns_arn", None)
    if field is not None:
        args["sns_arn"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("domain_id", None)
    if field is not None:
        args["domain_id"] = field

    field = data.get("email", None)
    if field is not None:
        args["email"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field

    field = data.get("custom", None)
    if field is not None:
        args["custom"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("blocklists", None)
    if field is not None:
        args["blocklists"] = (
            [unmarshal_Blocklist(v) for v in field] if field is not None else None
        )

    return BulkCreateBlocklistsResponse(**args)


def unmarshal_CreateEmailResponse(data: Any) -> CreateEmailResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateEmailResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("emails", None)
    if field is not None:
        args["emails"] = (
            [unmarshal_Email(v) for v in field] if field is not None else None
        )

    return CreateEmailResponse(**args)


def unmarshal_DomainLastStatusAutoconfigState(
    data: Any,
) -> DomainLastStatusAutoconfigState:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusAutoconfigState' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field

    field = data.get("autoconfigurable", None)
    if field is not None:
        args["autoconfigurable"] = field

    field = data.get("reason", None)
    if field is not None:
        args["reason"] = field
    else:
        args["reason"] = None

    return DomainLastStatusAutoconfigState(**args)


def unmarshal_DomainLastStatusDkimRecord(data: Any) -> DomainLastStatusDkimRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusDkimRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

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


def unmarshal_DomainLastStatusSpfRecord(data: Any) -> DomainLastStatusSpfRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusSpfRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("domain_id", None)
    if field is not None:
        args["domain_id"] = field

    field = data.get("domain_name", None)
    if field is not None:
        args["domain_name"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("blocklists", None)
    if field is not None:
        args["blocklists"] = (
            [unmarshal_Blocklist(v) for v in field] if field is not None else None
        )

    return ListBlocklistsResponse(**args)


def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("domains", None)
    if field is not None:
        args["domains"] = (
            [unmarshal_Domain(v) for v in field] if field is not None else None
        )

    return ListDomainsResponse(**args)


def unmarshal_ListEmailsResponse(data: Any) -> ListEmailsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListEmailsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("emails", None)
    if field is not None:
        args["emails"] = (
            [unmarshal_Email(v) for v in field] if field is not None else None
        )

    return ListEmailsResponse(**args)


def unmarshal_WebhookEvent(data: Any) -> WebhookEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'WebhookEvent' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field

    field = data.get("webhook_id", None)
    if field is not None:
        args["webhook_id"] = field

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field

    field = data.get("domain_id", None)
    if field is not None:
        args["domain_id"] = field

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field

    field = data.get("status", None)
    if field is not None:
        args["status"] = field

    field = data.get("data", None)
    if field is not None:
        args["data"] = field

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

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("webhook_events", None)
    if field is not None:
        args["webhook_events"] = (
            [unmarshal_WebhookEvent(v) for v in field] if field is not None else None
        )

    return ListWebhookEventsResponse(**args)


def unmarshal_ListWebhooksResponse(data: Any) -> ListWebhooksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListWebhooksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("webhooks", None)
    if field is not None:
        args["webhooks"] = (
            [unmarshal_Webhook(v) for v in field] if field is not None else None
        )

    return ListWebhooksResponse(**args)


def unmarshal_ProjectSettingsPeriodicReport(data: Any) -> ProjectSettingsPeriodicReport:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectSettingsPeriodicReport' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("enabled", None)
    if field is not None:
        args["enabled"] = field

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field

    field = data.get("sending_hour", None)
    if field is not None:
        args["sending_hour"] = field

    field = data.get("sending_day", None)
    if field is not None:
        args["sending_day"] = field

    return ProjectSettingsPeriodicReport(**args)


def unmarshal_ProjectSettings(data: Any) -> ProjectSettings:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectSettings' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

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

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field

    field = data.get("new_count", None)
    if field is not None:
        args["new_count"] = field

    field = data.get("sending_count", None)
    if field is not None:
        args["sending_count"] = field

    field = data.get("sent_count", None)
    if field is not None:
        args["sent_count"] = field

    field = data.get("failed_count", None)
    if field is not None:
        args["failed_count"] = field

    field = data.get("canceled_count", None)
    if field is not None:
        args["canceled_count"] = field

    return Statistics(**args)


def marshal_BulkCreateBlocklistsRequest(
    request: BulkCreateBlocklistsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain_id is not None:
        output["domain_id"] = request.domain_id

    if request.emails is not None:
        output["emails"] = request.emails

    if request.type_ is not None:
        output["type"] = str(request.type_)

    if request.reason is not None:
        output["reason"] = request.reason

    return output


def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain_name is not None:
        output["domain_name"] = request.domain_name

    if request.accept_tos is not None:
        output["accept_tos"] = request.accept_tos

    if request.autoconfig is not None:
        output["autoconfig"] = request.autoconfig

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_CreateEmailRequestAddress(
    request: CreateEmailRequestAddress,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreateEmailRequestAttachment(
    request: CreateEmailRequestAttachment,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.key is not None:
        output["key"] = request.key

    if request.value is not None:
        output["value"] = request.value

    return output


def marshal_CreateEmailRequest(
    request: CreateEmailRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
        output["project_id"] = request.project_id or defaults.default_project_id

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain_id is not None:
        output["domain_id"] = request.domain_id

    if request.name is not None:
        output["name"] = request.name

    if request.sns_arn is not None:
        output["sns_arn"] = request.sns_arn

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.event_types is not None:
        output["event_types"] = [str(item) for item in request.event_types]

    return output


def marshal_UpdateDomainRequest(
    request: UpdateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.autoconfig is not None:
        output["autoconfig"] = request.autoconfig

    return output


def marshal_UpdateProjectSettingsRequestUpdatePeriodicReport(
    request: UpdateProjectSettingsRequestUpdatePeriodicReport,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.enabled is not None:
        output["enabled"] = request.enabled

    if request.frequency is not None:
        output["frequency"] = str(request.frequency)

    if request.sending_hour is not None:
        output["sending_hour"] = request.sending_hour

    if request.sending_day is not None:
        output["sending_day"] = request.sending_day

    return output


def marshal_UpdateProjectSettingsRequest(
    request: UpdateProjectSettingsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

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
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.event_types is not None:
        output["event_types"] = [str(item) for item in request.event_types]

    if request.sns_arn is not None:
        output["sns_arn"] = request.sns_arn

    return output
