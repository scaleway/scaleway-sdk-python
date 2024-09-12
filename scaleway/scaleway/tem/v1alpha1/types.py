# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class DomainLastStatusRecordStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RECORD_STATUS = "unknown_record_status"
    VALID = "valid"
    INVALID = "invalid"
    NOT_FOUND = "not_found"

    def __str__(self) -> str:
        return str(self.value)


class DomainReputationStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    EXCELLENT = "excellent"
    GOOD = "good"
    AVERAGE = "average"
    BAD = "bad"

    def __str__(self) -> str:
        return str(self.value)


class DomainStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    CHECKED = "checked"
    UNCHECKED = "unchecked"
    INVALID = "invalid"
    LOCKED = "locked"
    REVOKED = "revoked"
    PENDING = "pending"
    AUTOCONFIGURING = "autoconfiguring"

    def __str__(self) -> str:
        return str(self.value)


class EmailFlag(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_FLAG = "unknown_flag"
    SOFT_BOUNCE = "soft_bounce"
    HARD_BOUNCE = "hard_bounce"
    SPAM = "spam"
    MAILBOX_FULL = "mailbox_full"
    MAILBOX_NOT_FOUND = "mailbox_not_found"
    GREYLISTED = "greylisted"
    SEND_BEFORE_EXPIRATION = "send_before_expiration"

    def __str__(self) -> str:
        return str(self.value)


class EmailRcptType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_RCPT_TYPE = "unknown_rcpt_type"
    TO = "to"
    CC = "cc"
    BCC = "bcc"

    def __str__(self) -> str:
        return str(self.value)


class EmailStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    NEW = "new"
    SENDING = "sending"
    SENT = "sent"
    FAILED = "failed"
    CANCELED = "canceled"

    def __str__(self) -> str:
        return str(self.value)


class ListEmailsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    STATUS_DESC = "status_desc"
    STATUS_ASC = "status_asc"
    MAIL_FROM_DESC = "mail_from_desc"
    MAIL_FROM_ASC = "mail_from_asc"
    MAIL_RCPT_DESC = "mail_rcpt_desc"
    MAIL_RCPT_ASC = "mail_rcpt_asc"
    SUBJECT_DESC = "subject_desc"
    SUBJECT_ASC = "subject_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListWebhookEventsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListWebhooksRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)


class WebhookEventStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    SENDING = "sending"
    SENT = "sent"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)


class WebhookEventType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    EMAIL_QUEUED = "email_queued"
    EMAIL_DROPPED = "email_dropped"
    EMAIL_DEFERRED = "email_deferred"
    EMAIL_DELIVERED = "email_delivered"
    EMAIL_SPAM = "email_spam"
    EMAIL_MAILBOX_NOT_FOUND = "email_mailbox_not_found"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class DomainRecordsDMARC:
    name: str
    """
    Name of the DMARC TXT record.
    """

    value: str
    """
    Value of the DMARC TXT record.
    """


@dataclass
class EmailTry:
    rank: int
    """
    Rank number of this attempt to send the email.
    """

    code: int
    """
    The SMTP status code received after the attempt. 0 if the attempt did not reach an SMTP server.
    """

    message: str
    """
    The SMTP message received. If the attempt did not reach an SMTP server, the message returned explains what happened.
    """

    tried_at: Optional[datetime]
    """
    Date of the attempt to send the email.
    """


@dataclass
class DomainRecords:
    dmarc: Optional[DomainRecordsDMARC]
    """
    DMARC TXT record specification.
    """


@dataclass
class DomainReputation:
    status: DomainReputationStatus
    """
    Status of your domain's reputation.
    """

    score: int
    """
    A range from 0 to 100 that determines your domain's reputation score. A score of `0` means a bad domain reputation and a score of `100` means an excellent domain reputation.
    """

    scored_at: Optional[datetime]
    """
    Time and date the score was calculated.
    """

    previous_score: Optional[int]
    """
    The previously-calculated domain's reputation score.
    """

    previous_scored_at: Optional[datetime]
    """
    Time and date the previous reputation score was calculated.
    """


@dataclass
class DomainStatistics:
    total_count: int

    sent_count: int

    failed_count: int

    canceled_count: int


@dataclass
class CreateEmailRequestAddress:
    email: str
    """
    Email address.
    """

    name: Optional[str]
    """
    (Optional) Name displayed.
    """


@dataclass
class CreateEmailRequestAttachment:
    name: str
    """
    Filename of the attachment.
    """

    type_: str
    """
    MIME type of the attachment.
    """

    content: str
    """
    Content of the attachment encoded in base64.
    """


@dataclass
class CreateEmailRequestHeader:
    key: str
    """
    Email header key.
    """

    value: str
    """
    Email header value.
    """


@dataclass
class Email:
    id: str
    """
    Technical ID of the email.
    """

    message_id: str
    """
    Message ID of the email.
    """

    project_id: str
    """
    ID of the Project to which the email belongs.
    """

    mail_from: str
    """
    Email address of the sender.
    """

    mail_rcpt: str
    """
    Email address of the recipient.
    """

    rcpt_to: Optional[str]
    """
    Email address of the recipient.
    """

    rcpt_type: EmailRcptType
    """
    Type of recipient.
    """

    subject: str
    """
    Subject of the email.
    """

    status: EmailStatus
    """
    Status of the email.
    """

    try_count: int
    """
    Number of attempts to send the email.
    """

    last_tries: List[EmailTry]
    """
    Information about the last three attempts to send the email.
    """

    flags: List[EmailFlag]
    """
    Flags categorize emails. They allow you to obtain more information about recurring errors, for example.
    """

    created_at: Optional[datetime]
    """
    Creation date of the email object.
    """

    updated_at: Optional[datetime]
    """
    Last update of the email object.
    """

    status_details: Optional[str]
    """
    Additional status information.
    """


@dataclass
class DomainLastStatusDkimRecord:
    status: DomainLastStatusRecordStatus
    """
    Status of the DKIM record's configuration.
    """

    last_valid_at: Optional[datetime]
    """
    Time and date the DKIM record was last valid.
    """

    error: Optional[str]
    """
    An error text displays in case the record is not valid.
    """


@dataclass
class DomainLastStatusDmarcRecord:
    status: DomainLastStatusRecordStatus
    """
    Status of the DMARC record's configuration.
    """

    last_valid_at: Optional[datetime]
    """
    Time and date the DMARC record was last valid.
    """

    error: Optional[str]
    """
    An error text displays in case the record is not valid.
    """


@dataclass
class DomainLastStatusSpfRecord:
    status: DomainLastStatusRecordStatus
    """
    Status of the SPF record's configuration.
    """

    last_valid_at: Optional[datetime]
    """
    Time and date the SPF record was last valid.
    """

    error: Optional[str]
    """
    An error text displays in case the record is not valid.
    """


@dataclass
class Domain:
    id: str
    """
    ID of the domain.
    """

    organization_id: str
    """
    ID of the domain's Organization.
    """

    project_id: str
    """
    ID of the domain's Project.
    """

    name: str
    """
    Domain name (example.com).
    """

    status: DomainStatus
    """
    Status of the domain.
    """

    spf_config: str
    """
    Snippet of the SPF record to register in the DNS zone.
    """

    dkim_config: str
    """
    DKIM public key to record in the DNS zone.
    """

    created_at: Optional[datetime]
    """
    Date and time of domain creation.
    """

    next_check_at: Optional[datetime]
    """
    Date and time of the next scheduled check.
    """

    last_valid_at: Optional[datetime]
    """
    Date and time the domain was last valid.
    """

    autoconfig: bool
    """
    Status of auto-configuration for the domain's DNS zone.
    """

    region: Region
    """
    Region to target. If none is passed will use default region from the config.
    """

    revoked_at: Optional[datetime]
    """
    Date and time of the domain's deletion.
    """

    last_error: Optional[str]
    """
    Error message returned if the last check failed.
    """

    statistics: Optional[DomainStatistics]
    """
    Domain's statistics.
    """

    reputation: Optional[DomainReputation]
    """
    The domain's reputation is available when your domain is checked and has sent enough emails.
    """

    records: Optional[DomainRecords]
    """
    List of records to configure to validate a domain.
    """


@dataclass
class WebhookEvent:
    id: str
    """
    ID of the Webhook Event.
    """

    webhook_id: str
    """
    ID of the Webhook that triggers the Event.
    """

    organization_id: str
    """
    ID of the Webhook Event Organization.
    """

    project_id: str
    """
    ID of the Webhook Event Project.
    """

    domain_id: str
    """
    ID of the webhook event domain.
    """

    type_: WebhookEventType
    """
    Type of the Webhook Event.
    """

    status: WebhookEventStatus
    """
    Status of the Webhook Event.
    """

    data: str
    """
    Data sent to the Webhook destination.
    """

    created_at: Optional[datetime]
    """
    Date and time of the Webhook Event creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of last Webhook Event updates.
    """

    email_id: Optional[str]
    """
    Optional Email ID if the event is triggered by an Email resource.
    """


@dataclass
class Webhook:
    id: str
    """
    ID of the Webhook.
    """

    domain_id: str
    """
    ID of the Domain to watch for triggering events.
    """

    organization_id: str
    """
    ID of the Webhook Organization.
    """

    project_id: str
    """
    ID of the Webhook Project.
    """

    name: str
    """
    Name of the Webhook.
    """

    event_types: List[WebhookEventType]
    """
    List of event types that will trigger a Webhook Event.
    """

    sns_arn: str
    """
    Scaleway SNS ARN topic to push the events to.
    """

    created_at: Optional[datetime]
    """
    Date and time of the Webhook creation.
    """

    updated_at: Optional[datetime]
    """
    Date and time of last Webhook updates.
    """


@dataclass
class CancelEmailRequest:
    email_id: str
    """
    ID of the email to cancel.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CheckDomainRequest:
    domain_id: str
    """
    ID of the domain to check.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CreateDomainRequest:
    domain_name: str
    """
    Fully qualified domain dame.
    """

    accept_tos: bool
    """
    Accept Scaleway's Terms of Service.
    """

    autoconfig: bool
    """
    Activate auto-configuration of the domain's DNS zone.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the project to which the domain belongs.
    """


@dataclass
class CreateEmailRequest:
    from_: CreateEmailRequestAddress
    """
    Sender information. Must be from a checked domain declared in the Project.
    """

    subject: str
    """
    Subject of the email.
    """

    text: str
    """
    Text content.
    """

    html: str
    """
    HTML content.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    to: Optional[List[CreateEmailRequestAddress]]
    """
    An array of the primary recipient's information.
    """

    cc: Optional[List[CreateEmailRequestAddress]]
    """
    An array of the carbon copy recipient's information.
    """

    bcc: Optional[List[CreateEmailRequestAddress]]
    """
    An array of the blind carbon copy recipient's information.
    """

    project_id: Optional[str]
    """
    ID of the Project in which to create the email.
    """

    attachments: Optional[List[CreateEmailRequestAttachment]]
    """
    Array of attachments.
    """

    send_before: Optional[datetime]
    """
    Maximum date to deliver the email.
    """

    additional_headers: Optional[List[CreateEmailRequestHeader]]
    """
    Array of additional headers as key-value.
    """


@dataclass
class CreateEmailResponse:
    emails: List[Email]
    """
    Single page of emails matching the requested criteria.
    """


@dataclass
class CreateWebhookRequest:
    domain_id: str
    """
    ID of the Domain to watch for triggering events.
    """

    name: str
    """
    Name of the Webhook.
    """

    sns_arn: str
    """
    Scaleway SNS ARN topic to push the events to.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    ID of the project to which the Webhook belongs.
    """

    event_types: Optional[List[WebhookEventType]]
    """
    List of event types that will trigger an event.
    """


@dataclass
class DeleteWebhookRequest:
    webhook_id: str
    """
    ID of the Webhook to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DomainLastStatus:
    domain_id: str
    """
    The ID of the domain.
    """

    domain_name: str
    """
    The domain name (example.com).
    """

    spf_record: Optional[DomainLastStatusSpfRecord]
    """
    The SPF record verification data.
    """

    dkim_record: Optional[DomainLastStatusDkimRecord]
    """
    The DKIM record verification data.
    """

    dmarc_record: Optional[DomainLastStatusDmarcRecord]
    """
    The DMARC record verification data.
    """


@dataclass
class GetDomainLastStatusRequest:
    domain_id: str
    """
    ID of the domain to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDomainRequest:
    domain_id: str
    """
    ID of the domain.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetEmailRequest:
    email_id: str
    """
    ID of the email to retrieve.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetStatisticsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str]
    """
    (Optional) Number of emails for this Project.
    """

    domain_id: Optional[str]
    """
    (Optional) Number of emails sent from this domain (must be coherent with the `project_id` and the `organization_id`).
    """

    since: Optional[datetime]
    """
    (Optional) Number of emails created after this date.
    """

    until: Optional[datetime]
    """
    (Optional) Number of emails created before this date.
    """

    mail_from: Optional[str]
    """
    (Optional) Number of emails sent with this sender's email address.
    """


@dataclass
class GetWebhookRequest:
    webhook_id: str
    """
    ID of the Webhook to check.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListDomainsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int]
    """
    Requested page size. Value must be between 1 and 1000.
    """

    project_id: Optional[str]
    """
    (Optional) ID of the Project in which to list the domains.
    """

    status: Optional[List[DomainStatus]]
    """
    (Optional) List domains under specific statuses.
    """

    organization_id: Optional[str]
    """
    (Optional) ID of the Organization in which to list the domains.
    """

    name: Optional[str]
    """
    (Optional) Names of the domains to list.
    """


@dataclass
class ListDomainsResponse:
    total_count: int
    """
    Number of domains that match the request (without pagination).
    """

    domains: List[Domain]
    """
    Single page of domains matching the requested criteria.
    """


@dataclass
class ListEmailsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    project_id: Optional[str]
    """
    (Optional) ID of the Project in which to list the emails.
    """

    domain_id: Optional[str]
    """
    (Optional) ID of the domain for which to list the emails.
    """

    message_id: Optional[str]
    """
    (Optional) ID of the message for which to list the emails.
    """

    since: Optional[datetime]
    """
    (Optional) List emails created after this date.
    """

    until: Optional[datetime]
    """
    (Optional) List emails created before this date.
    """

    mail_from: Optional[str]
    """
    (Optional) List emails sent with this sender's email address.
    """

    mail_to: Optional[str]
    """
    List emails sent to this recipient's email address.
    """

    mail_rcpt: Optional[str]
    """
    (Optional) List emails sent to this recipient's email address.
    """

    statuses: Optional[List[EmailStatus]]
    """
    (Optional) List emails with any of these statuses.
    """

    subject: Optional[str]
    """
    (Optional) List emails with this subject.
    """

    search: Optional[str]
    """
    (Optional) List emails by searching to all fields.
    """

    order_by: Optional[ListEmailsRequestOrderBy]
    """
    (Optional) List emails corresponding to specific criteria.
    """

    flags: Optional[List[EmailFlag]]
    """
    (Optional) List emails containing only specific flags.
    """


@dataclass
class ListEmailsResponse:
    total_count: int
    """
    Number of emails matching the requested criteria.
    """

    emails: List[Email]
    """
    Single page of emails matching the requested criteria.
    """


@dataclass
class ListWebhookEventsRequest:
    webhook_id: str
    """
    ID of the Webhook linked to the events.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListWebhookEventsRequestOrderBy]
    """
    (Optional) List Webhook events corresponding to specific criteria.
    """

    page: Optional[int]
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int]
    """
    Requested page size. Value must be between 1 and 100.
    """

    email_id: Optional[str]
    """
    ID of the email linked to the events.
    """

    event_types: Optional[List[WebhookEventType]]
    """
    List of event types linked to the events.
    """

    statuses: Optional[List[WebhookEventStatus]]
    """
    List of event statuses.
    """

    project_id: Optional[str]
    """
    ID of the webhook Project.
    """

    organization_id: Optional[str]
    """
    ID of the webhook Organization.
    """

    domain_id: Optional[str]
    """
    ID of the domain to watch for triggering events.
    """


@dataclass
class ListWebhookEventsResponse:
    total_count: int
    """
    Number of Webhook events matching the requested criteria.
    """

    webhook_events: List[WebhookEvent]
    """
    Single page of Webhook events matching the requested criteria.
    """


@dataclass
class ListWebhooksRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListWebhooksRequestOrderBy]
    """
    (Optional) List Webhooks corresponding to specific criteria.
    """

    page: Optional[int]
    """
    (Optional) Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int]
    """
    (Optional) Requested page size. Value must be between 1 and 100.
    """

    project_id: Optional[str]
    """
    (Optional) ID of the Project for which to list the Webhooks.
    """

    organization_id: Optional[str]
    """
    (Optional) ID of the Organization for which to list the Webhooks.
    """

    domain_id: Optional[str]
    """
    (Optional) ID of the Domain for which to list the Webhooks.
    """


@dataclass
class ListWebhooksResponse:
    total_count: int
    """
    Number of Webhooks matching the requested criteria.
    """

    webhooks: List[Webhook]
    """
    Single page of Webhooks matching the requested criteria.
    """


@dataclass
class RevokeDomainRequest:
    domain_id: str
    """
    ID of the domain to delete.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class Statistics:
    total_count: int
    """
    Total number of emails matching the requested criteria.
    """

    new_count: int
    """
    Number of emails still in the `new` transient state. This means emails received from the API but not yet processed.
    """

    sending_count: int
    """
    Number of emails still in the `sending` transient state. This means emails received from the API but not yet in their final status.
    """

    sent_count: int
    """
    Number of emails in the final `sent` state. This means emails that have been delivered to the target mail system.
    """

    failed_count: int
    """
    Number of emails in the final `failed` state. This means emails that have been refused by the target mail system with a final error status.
    """

    canceled_count: int
    """
    Number of emails in the final `canceled` state. This means emails that have been canceled upon request.
    """


@dataclass
class UpdateDomainRequest:
    domain_id: str
    """
    ID of the domain to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    autoconfig: Optional[bool]
    """
    (Optional) If set to true, activate auto-configuration of the domain's DNS zone.
    """


@dataclass
class UpdateWebhookRequest:
    webhook_id: str
    """
    ID of the Webhook to update.
    """

    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the Webhook to update.
    """

    event_types: Optional[List[WebhookEventType]]
    """
    List of event types to update.
    """

    sns_arn: Optional[str]
    """
    Scaleway SNS ARN topic to update.
    """
