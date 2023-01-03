# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    CreateEmailRequestAddress,
    CreateEmailRequestAttachment,
    CreateEmailResponse,
    Domain,
    DomainStatistics,
    Email,
    EmailTry,
    ListDomainsResponse,
    ListEmailsResponse,
    Statistics,
    CreateEmailRequest,
    CreateDomainRequest,
)


def unmarshal_DomainStatistics(data: Any) -> DomainStatistics:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainStatistics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("canceled_count")
    args["canceled_count"] = field

    field = data.get("failed_count")
    args["failed_count"] = field

    field = data.get("sent_count")
    args["sent_count"] = field

    field = data.get("total_count")
    args["total_count"] = field

    return DomainStatistics(**args)


def unmarshal_EmailTry(data: Any) -> EmailTry:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'EmailTry' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("code")
    args["code"] = field

    field = data.get("message")
    args["message"] = field

    field = data.get("rank")
    args["rank"] = field

    field = data.get("tried_at")
    args["tried_at"] = parser.isoparse(field) if type(field) is str else field

    return EmailTry(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("dkim_config")
    args["dkim_config"] = field

    field = data.get("id")
    args["id"] = field

    field = data.get("last_error")
    args["last_error"] = field

    field = data.get("last_valid_at")
    args["last_valid_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("name")
    args["name"] = field

    field = data.get("next_check_at")
    args["next_check_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("organization_id")
    args["organization_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("region")
    args["region"] = field

    field = data.get("revoked_at")
    args["revoked_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("spf_config")
    args["spf_config"] = field

    field = data.get("statistics")
    args["statistics"] = (
        unmarshal_DomainStatistics(field) if field is not None else None
    )

    field = data.get("status")
    args["status"] = field

    return Domain(**args)


def unmarshal_Email(data: Any) -> Email:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Email' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at")
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("id")
    args["id"] = field

    field = data.get("last_tries")
    args["last_tries"] = [unmarshal_EmailTry(v) for v in data["last_tries"]]

    field = data.get("mail_from")
    args["mail_from"] = field

    field = data.get("message_id")
    args["message_id"] = field

    field = data.get("project_id")
    args["project_id"] = field

    field = data.get("rcpt_to")
    args["rcpt_to"] = field

    field = data.get("rcpt_type")
    args["rcpt_type"] = field

    field = data.get("status")
    args["status"] = field

    field = data.get("status_details")
    args["status_details"] = field

    field = data.get("try_count")
    args["try_count"] = field

    field = data.get("updated_at")
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return Email(**args)


def unmarshal_CreateEmailResponse(data: Any) -> CreateEmailResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'CreateEmailResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("emails")
    args["emails"] = [unmarshal_Email(v) for v in data["emails"]]

    return CreateEmailResponse(**args)


def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domains")
    args["domains"] = [unmarshal_Domain(v) for v in data["domains"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListDomainsResponse(**args)


def unmarshal_ListEmailsResponse(data: Any) -> ListEmailsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListEmailsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("emails")
    args["emails"] = [unmarshal_Email(v) for v in data["emails"]]

    field = data.get("total_count")
    args["total_count"] = field

    return ListEmailsResponse(**args)


def unmarshal_Statistics(data: Any) -> Statistics:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Statistics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("canceled_count")
    args["canceled_count"] = field

    field = data.get("failed_count")
    args["failed_count"] = field

    field = data.get("new_count")
    args["new_count"] = field

    field = data.get("sending_count")
    args["sending_count"] = field

    field = data.get("sent_count")
    args["sent_count"] = field

    field = data.get("total_count")
    args["total_count"] = field

    return Statistics(**args)


def marshal_CreateEmailRequestAddress(
    request: CreateEmailRequestAddress,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "email": request.email,
        "name": request.name,
    }


def marshal_CreateEmailRequestAttachment(
    request: CreateEmailRequestAttachment,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "content": request.content,
        "name": request.name,
        "type": request.type_,
    }


def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "domain_name": request.domain_name,
        "project_id": request.project_id or defaults.default_project_id,
    }


def marshal_CreateEmailRequest(
    request: CreateEmailRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    return {
        "attachments": [
            marshal_CreateEmailRequestAttachment(v, defaults)
            for v in request.attachments
        ]
        if request.attachments is not None
        else None,
        "bcc": [marshal_CreateEmailRequestAddress(v, defaults) for v in request.bcc]
        if request.bcc is not None
        else None,
        "cc": [marshal_CreateEmailRequestAddress(v, defaults) for v in request.cc]
        if request.cc is not None
        else None,
        "from": marshal_CreateEmailRequestAddress(request.from_, defaults)
        if request.from_ is not None
        else None,
        "html": request.html,
        "project_id": request.project_id or defaults.default_project_id,
        "send_before": request.send_before,
        "subject": request.subject,
        "text": request.text,
        "to": [marshal_CreateEmailRequestAddress(v, defaults) for v in request.to]
        if request.to is not None
        else None,
    }
