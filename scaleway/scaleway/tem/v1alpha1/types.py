# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class BlocklistType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    MAILBOX_FULL = "mailbox_full"
    MAILBOX_NOT_FOUND = "mailbox_not_found"

    def __str__(self) -> str:
        return str(self.value)


class DomainLastStatusAutoconfigStateReason(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_REASON = "unknown_reason"
    PERMISSION_DENIED = "permission_denied"
    DOMAIN_NOT_FOUND = "domain_not_found"

    def __str__(self) -> str:
        return str(self.value)


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
    BLOCKLISTED = "blocklisted"

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


class ListBlocklistsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    ENDS_AT_DESC = "ends_at_desc"
    ENDS_AT_ASC = "ends_at_asc"

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


class OfferName(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_NAME = "unknown_name"
    ESSENTIAL = "essential"
    SCALE = "scale"

    def __str__(self) -> str:
        return str(self.value)


class PoolStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    DISABLED = "disabled"
    CREATING = "creating"
    READY = "ready"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)


class ProjectSettingsPeriodicReportFrequency(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_FREQUENCY = "unknown_frequency"
    MONTHLY = "monthly"
    WEEKLY = "weekly"
    DAILY = "daily"

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
    EMAIL_BLOCKLISTED = "email_blocklisted"
    BLOCKLIST_CREATED = "blocklist_created"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class DomainRecordsDKIM:
    name: str
    """
    Name of the DKIM TXT record.
    """

    value: str
    """
    Value of the DKIM TXT record.
    """


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
class DomainRecordsMX:
    name: str
    """
    Name of the MX record.
    """

    value: str
    """
    Value of the MX record.
    """


@dataclass
class DomainRecordsSPF:
    name: str
    """
    Name of the SPF TXT record.
    """

    value: str
    """
    Value of the SPF TXT record.
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

    tried_at: Optional[datetime] = None
    """
    Date of the attempt to send the email.
    """


@dataclass
class DomainRecords:
    dmarc: Optional[DomainRecordsDMARC] = None
    """
    DMARC TXT record specification.
    """

    dkim: Optional[DomainRecordsDKIM] = None
    """
    DKIM TXT record specification.
    """

    spf: Optional[DomainRecordsSPF] = None
    """
    SPF TXT record specification.
    """

    mx: Optional[DomainRecordsMX] = None
    """
    MX record specification.
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

    scored_at: Optional[datetime] = None
    """
    Time and date the score was calculated.
    """

    previous_score: Optional[int] = 0
    """
    The previously-calculated domain's reputation score.
    """

    previous_scored_at: Optional[datetime] = None
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
class Blocklist:
    id: str
    """
    ID of the blocklist.
    """

    domain_id: str
    """
    Domain ID linked to the blocklist.
    """

    email: str
    """
    Email blocked by the blocklist.
    """

    type_: BlocklistType
    """
    Type of block for this email.
    """

    reason: str
    """
    Reason to block this email.
    """

    custom: bool
    """
    True if this blocklist was created manually. False for an automatic Transactional Email blocklist.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of the blocklist creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of the blocklist's last update.
    """

    ends_at: Optional[datetime] = None
    """
    Date and time when the blocklist ends. Empty if the blocklist has no end.
    """


@dataclass
class CreateEmailRequestAddress:
    email: str
    """
    Email address.
    """

    name: Optional[str] = None
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

    rcpt_to: str
    """
    Deprecated. Email address of the recipient.
    """

    mail_rcpt: str
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

    last_tries: list[EmailTry]
    """
    Information about the last three attempts to send the email.
    """

    flags: list[EmailFlag]
    """
    Flags categorize emails. They allow you to obtain more information about recurring errors, for example.
    """

    created_at: Optional[datetime] = None
    """
    Creation date of the email object.
    """

    updated_at: Optional[datetime] = None
    """
    Last update of the email object.
    """

    status_details: Optional[str] = None
    """
    Additional status information.
    """


@dataclass
class DomainLastStatusAutoconfigState:
    enabled: bool
    """
    Enable or disable the auto-configuration of domain DNS records.
    """

    autoconfigurable: bool
    """
    Whether the domain can be auto-configured or not.
    """

    reason: Optional[DomainLastStatusAutoconfigStateReason] = (
        DomainLastStatusAutoconfigStateReason.UNKNOWN_REASON
    )
    """
    The reason that the domain cannot be auto-configurable.
    """


@dataclass
class DomainLastStatusDkimRecord:
    status: DomainLastStatusRecordStatus
    """
    Status of the DKIM record's configuration.
    """

    last_valid_at: Optional[datetime] = None
    """
    Time and date the DKIM record was last valid.
    """

    error: Optional[str] = None
    """
    An error text displays in case the record is not valid.
    """


@dataclass
class DomainLastStatusDmarcRecord:
    status: DomainLastStatusRecordStatus
    """
    Status of the DMARC record's configuration.
    """

    last_valid_at: Optional[datetime] = None
    """
    Time and date the DMARC record was last valid.
    """

    error: Optional[str] = None
    """
    An error text displays in case the record is not valid.
    """


@dataclass
class DomainLastStatusMXRecord:
    status: DomainLastStatusRecordStatus
    """
    Status of the MX record's configuration. This record is optional to validate a domain, but highly recommended.
    """

    last_valid_at: Optional[datetime] = None
    """
    Time and date the MX record was last valid.
    """

    error: Optional[str] = None
    """
    An error text displays in case the record is not valid.
    """


@dataclass
class DomainLastStatusSpfRecord:
    status: DomainLastStatusRecordStatus
    """
    Status of the SPF record's configuration.
    """

    last_valid_at: Optional[datetime] = None
    """
    Time and date the SPF record was last valid.
    """

    error: Optional[str] = None
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

    autoconfig: bool
    """
    Status of auto-configuration for the domain's DNS zone.
    """

    region: ScwRegion
    """
    Region to target. If none is passed will use default region from the config.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of domain creation.
    """

    next_check_at: Optional[datetime] = None
    """
    Date and time of the next scheduled check.
    """

    last_valid_at: Optional[datetime] = None
    """
    Date and time the domain was last valid.
    """

    revoked_at: Optional[datetime] = None
    """
    Date and time of the domain's deletion.
    """

    last_error: Optional[str] = None
    """
    Deprecated. Error message returned if the last check failed.
    """

    statistics: Optional[DomainStatistics] = None
    """
    Domain's statistics.
    """

    reputation: Optional[DomainReputation] = None
    """
    The domain's reputation is available when your domain is checked and has sent enough emails.
    """

    records: Optional[DomainRecords] = None
    """
    List of records to configure to validate a domain.
    """


@dataclass
class OfferSubscription:
    organization_id: str
    """
    ID of the offer-subscription Organization.
    """

    project_id: str
    """
    ID of the offer-subscription Project.
    """

    offer_name: OfferName
    """
    Name of the offer associated with the Project.
    """

    sla: float
    """
    Service Level Agreement percentage of the offer-subscription.
    """

    max_domains: int
    """
    Max number of domains that can be associated with the offer-subscription for a particular Project.
    """

    max_dedicated_ips: int
    """
    Max number of dedicated IPs that can be associated with the offer-subscription for a particular Project.
    """

    max_webhooks_per_domain: int
    """
    Max number of webhooks that can be associated with the offer-subscription for a particular Project.
    """

    max_custom_blocklists_per_domain: int
    """
    Max number of custom blocklists that can be associated with the offer-subscription for a particular Project.
    """

    included_monthly_emails: int
    """
    Number of emails included in the offer-subscription per month.
    """

    subscribed_at: Optional[datetime] = None
    """
    Date and time of the subscription.
    """

    cancellation_available_at: Optional[datetime] = None
    """
    Date and time of the end of the offer-subscription commitment.
    """


@dataclass
class Offer:
    name: OfferName
    """
    Name of the offer.
    """

    sla: float
    """
    Service Level Agreement percentage of the offer.
    """

    max_domains: int
    """
    Max number of checked domains that can be associated with the offer.
    """

    max_dedicated_ips: int
    """
    Max number of dedicated IPs that can be associated with the offer.
    """

    included_monthly_emails: int
    """
    Number of emails included in the offer per month.
    """

    max_webhooks_per_domain: int
    """
    Max number of webhooks that can be associated with the offer.
    """

    max_custom_blocklists_per_domain: int
    """
    Max number of active custom blocklists that can be associated with the offer.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of the offer creation.
    """

    commitment_period: Optional[str] = None
    """
    Period of commitment.
    """


@dataclass
class Pool:
    project_id: str
    """
    ID of the Project.
    """

    status: PoolStatus
    """
    Status of the pool.
    """

    ips: list[str]
    """
    IPs of the pool.
    """

    details: Optional[str] = None
    """
    Details of the pool.
    """

    zone: Optional[ScwZone] = None
    """
    Zone of the pool.
    """

    reverse: Optional[str] = None
    """
    Reverse hostname of all IPs of the pool.
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

    created_at: Optional[datetime] = None
    """
    Date and time of the Webhook Event creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of last Webhook Event updates.
    """

    email_id: Optional[str] = None
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

    event_types: list[WebhookEventType]
    """
    List of event types that will trigger a Webhook Event.
    """

    sns_arn: str
    """
    Scaleway SNS ARN topic to push the events to.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of the Webhook creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of last Webhook updates.
    """


@dataclass
class ProjectSettingsPeriodicReport:
    enabled: bool
    """
    Enable or disable periodic report notifications.
    """

    frequency: ProjectSettingsPeriodicReportFrequency
    """
    At which frequency you receive periodic report notifications.
    """

    sending_hour: int
    """
    At which hour you receive periodic report notifications.
    """

    sending_day: int
    """
    On which day you receive periodic report notifications (1-7 weekly, 1-28 monthly).
    """


@dataclass
class UpdateProjectSettingsRequestUpdatePeriodicReport:
    enabled: Optional[bool] = False
    """
    (Optional) Enable or disable periodic report notifications.
    """

    frequency: Optional[ProjectSettingsPeriodicReportFrequency] = (
        ProjectSettingsPeriodicReportFrequency.UNKNOWN_FREQUENCY
    )
    """
    (Optional) Frequency at which you receive periodic report notifications.
    """

    sending_hour: Optional[int] = 0
    """
    (Optional) Hour at which you receive periodic report notifications.
    """

    sending_day: Optional[int] = 0
    """
    (Optional) On which day you receive periodic report notifications (1-7 weekly, 1-28 monthly).
    """


@dataclass
class BulkCreateBlocklistsRequest:
    domain_id: str
    """
    Domain ID linked to the blocklist.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    emails: Optional[list[str]] = field(default_factory=list)
    """
    Email blocked by the blocklist.
    """

    type_: Optional[BlocklistType] = BlocklistType.UNKNOWN_TYPE
    """
    Type of blocklist.
    """

    reason: Optional[str] = None
    """
    Reason to block the email.
    """


@dataclass
class BulkCreateBlocklistsResponse:
    blocklists: list[Blocklist]
    """
    List of blocklist created.
    """


@dataclass
class CancelEmailRequest:
    email_id: str
    """
    ID of the email to cancel.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class CheckDomainRequest:
    domain_id: str
    """
    ID of the domain to check.
    """

    region: Optional[ScwRegion] = None
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
    Deprecated. Accept Scaleway's Terms of Service.
    """

    autoconfig: bool
    """
    Activate auto-configuration of the domain's DNS zone.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    to: Optional[list[CreateEmailRequestAddress]] = field(default_factory=list)
    """
    An array of the primary recipient's information.
    """

    cc: Optional[list[CreateEmailRequestAddress]] = field(default_factory=list)
    """
    An array of the carbon copy recipient's information.
    """

    bcc: Optional[list[CreateEmailRequestAddress]] = field(default_factory=list)
    """
    An array of the blind carbon copy recipient's information.
    """

    project_id: Optional[str] = None
    """
    ID of the Project in which to create the email.
    """

    attachments: Optional[list[CreateEmailRequestAttachment]] = field(
        default_factory=list
    )
    """
    Array of attachments.
    """

    send_before: Optional[datetime] = None
    """
    Maximum date to deliver the email.
    """

    additional_headers: Optional[list[CreateEmailRequestHeader]] = field(
        default_factory=list
    )
    """
    Array of additional headers as key-value.
    """


@dataclass
class CreateEmailResponse:
    emails: list[Email]
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the project to which the Webhook belongs.
    """

    event_types: Optional[list[WebhookEventType]] = field(default_factory=list)
    """
    List of event types that will trigger an event.
    """


@dataclass
class DeleteBlocklistRequest:
    blocklist_id: str
    """
    ID of the blocklist to delete.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class DeleteWebhookRequest:
    webhook_id: str
    """
    ID of the Webhook to delete.
    """

    region: Optional[ScwRegion] = None
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

    spf_record: Optional[DomainLastStatusSpfRecord] = None
    """
    The SPF record verification data.
    """

    dkim_record: Optional[DomainLastStatusDkimRecord] = None
    """
    The DKIM record verification data.
    """

    dmarc_record: Optional[DomainLastStatusDmarcRecord] = None
    """
    The DMARC record verification data.
    """

    mx_record: Optional[DomainLastStatusMXRecord] = None
    """
    The MX record verification data.
    """

    autoconfig_state: Optional[DomainLastStatusAutoconfigState] = None
    """
    The verification state of domain auto-configuration.
    """


@dataclass
class GetDomainLastStatusRequest:
    domain_id: str
    """
    ID of the domain to get records status.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetDomainRequest:
    domain_id: str
    """
    ID of the domain.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetEmailRequest:
    email_id: str
    """
    ID of the email to retrieve.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetProjectConsumptionRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the project.
    """


@dataclass
class GetProjectSettingsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the project.
    """


@dataclass
class GetStatisticsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    (Optional) Number of emails for this Project.
    """

    domain_id: Optional[str] = None
    """
    (Optional) Number of emails sent from this domain (must be coherent with the `project_id` and the `organization_id`).
    """

    since: Optional[datetime] = None
    """
    (Optional) Number of emails created after this date.
    """

    until: Optional[datetime] = None
    """
    (Optional) Number of emails created before this date.
    """

    mail_from: Optional[str] = None
    """
    (Optional) Number of emails sent with this sender's email address.
    """


@dataclass
class GetWebhookRequest:
    webhook_id: str
    """
    ID of the Webhook to check.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListBlocklistsRequest:
    domain_id: str
    """
    (Optional) Filter by a domain ID.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListBlocklistsRequestOrderBy] = (
        ListBlocklistsRequestOrderBy.CREATED_AT_DESC
    )
    """
    (Optional) List blocklist corresponding to specific criteria.
    """

    page: Optional[int] = 0
    """
    (Optional) Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    (Optional) Requested page size. Value must be between 1 and 100.
    """

    email: Optional[str] = None
    """
    (Optional) Filter by an email address.
    """

    type_: Optional[BlocklistType] = BlocklistType.UNKNOWN_TYPE
    """
    (Optional) Filter by a blocklist type.
    """

    custom: Optional[bool] = False
    """
    (Optional) Filter by custom blocklist (true) or automatic Transactional Email blocklist (false).
    """


@dataclass
class ListBlocklistsResponse:
    total_count: int
    """
    Number of blocklists matching the requested criteria.
    """

    blocklists: list[Blocklist]
    """
    Single page of blocklists matching the requested criteria.
    """


@dataclass
class ListDomainsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    Requested page size. Value must be between 1 and 1000.
    """

    project_id: Optional[str] = None
    """
    (Optional) ID of the Project in which to list the domains.
    """

    status: Optional[list[DomainStatus]] = field(default_factory=list)
    """
    (Optional) List domains under specific statuses.
    """

    organization_id: Optional[str] = None
    """
    (Optional) ID of the Organization in which to list the domains.
    """

    name: Optional[str] = None
    """
    (Optional) Names of the domains to list.
    """


@dataclass
class ListDomainsResponse:
    total_count: int
    """
    Number of domains that match the request (without pagination).
    """

    domains: list[Domain]
    """
    Single page of domains matching the requested criteria.
    """


@dataclass
class ListEmailsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    page_size: Optional[int] = 0
    project_id: Optional[str] = None
    """
    (Optional) ID of the Project in which to list the emails.
    """

    domain_id: Optional[str] = None
    """
    (Optional) ID of the domain for which to list the emails.
    """

    message_id: Optional[str] = None
    """
    (Optional) ID of the message for which to list the emails.
    """

    since: Optional[datetime] = None
    """
    (Optional) List emails created after this date.
    """

    until: Optional[datetime] = None
    """
    (Optional) List emails created before this date.
    """

    mail_from: Optional[str] = None
    """
    (Optional) List emails sent with this sender's email address.
    """

    mail_to: Optional[str] = None
    """
    Deprecated. List emails sent to this recipient's email address.
    """

    mail_rcpt: Optional[str] = None
    """
    (Optional) List emails sent to this recipient's email address.
    """

    statuses: Optional[list[EmailStatus]] = field(default_factory=list)
    """
    (Optional) List emails with any of these statuses.
    """

    subject: Optional[str] = None
    """
    (Optional) List emails with this subject.
    """

    search: Optional[str] = None
    """
    (Optional) List emails by searching to all fields.
    """

    order_by: Optional[ListEmailsRequestOrderBy] = (
        ListEmailsRequestOrderBy.CREATED_AT_DESC
    )
    """
    (Optional) List emails corresponding to specific criteria.
    """

    flags: Optional[list[EmailFlag]] = field(default_factory=list)
    """
    (Optional) List emails containing only specific flags.
    """


@dataclass
class ListEmailsResponse:
    total_count: int
    """
    Number of emails matching the requested criteria.
    """

    emails: list[Email]
    """
    Single page of emails matching the requested criteria.
    """


@dataclass
class ListOfferSubscriptionsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """


@dataclass
class ListOfferSubscriptionsResponse:
    total_count: int
    """
    Number of offer-subscriptions matching the requested criteria.
    """

    offer_subscriptions: list[OfferSubscription]
    """
    Single page of offer-subscriptions matching the requested criteria.
    """


@dataclass
class ListOffersRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class ListOffersResponse:
    total_count: int
    """
    Number of offers matching the requested criteria.
    """

    offers: list[Offer]
    """
    Single page of offers matching the requested criteria.
    """


@dataclass
class ListPoolsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int] = 0
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    Requested page size. Value must be between 1 and 1000.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """


@dataclass
class ListPoolsResponse:
    total_count: int
    """
    Number of pools matching the requested criteria.
    """

    pools: list[Pool]
    """
    Single page of pools matching the requested criteria.
    """


@dataclass
class ListWebhookEventsRequest:
    webhook_id: str
    """
    ID of the Webhook linked to the events.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListWebhookEventsRequestOrderBy] = (
        ListWebhookEventsRequestOrderBy.CREATED_AT_DESC
    )
    """
    (Optional) List Webhook events corresponding to specific criteria.
    """

    page: Optional[int] = 0
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    Requested page size. Value must be between 1 and 100.
    """

    email_id: Optional[str] = None
    """
    ID of the email linked to the events.
    """

    event_types: Optional[list[WebhookEventType]] = field(default_factory=list)
    """
    List of event types linked to the events.
    """

    statuses: Optional[list[WebhookEventStatus]] = field(default_factory=list)
    """
    List of event statuses.
    """

    project_id: Optional[str] = None
    """
    ID of the webhook Project.
    """

    organization_id: Optional[str] = None
    """
    ID of the webhook Organization.
    """

    domain_id: Optional[str] = None
    """
    ID of the domain to watch for triggering events.
    """


@dataclass
class ListWebhookEventsResponse:
    total_count: int
    """
    Number of Webhook events matching the requested criteria.
    """

    webhook_events: list[WebhookEvent]
    """
    Single page of Webhook events matching the requested criteria.
    """


@dataclass
class ListWebhooksRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    order_by: Optional[ListWebhooksRequestOrderBy] = (
        ListWebhooksRequestOrderBy.CREATED_AT_DESC
    )
    """
    (Optional) List Webhooks corresponding to specific criteria.
    """

    page: Optional[int] = 0
    """
    (Optional) Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    (Optional) Requested page size. Value must be between 1 and 100.
    """

    project_id: Optional[str] = None
    """
    (Optional) ID of the Project for which to list the Webhooks.
    """

    organization_id: Optional[str] = None
    """
    (Optional) ID of the Organization for which to list the Webhooks.
    """

    domain_id: Optional[str] = None
    """
    (Optional) ID of the Domain for which to list the Webhooks.
    """


@dataclass
class ListWebhooksResponse:
    total_count: int
    """
    Number of Webhooks matching the requested criteria.
    """

    webhooks: list[Webhook]
    """
    Single page of Webhooks matching the requested criteria.
    """


@dataclass
class ProjectConsumption:
    project_id: str
    """
    ID of the project.
    """

    domains_count: int
    """
    Number of domains in the project.
    """

    dedicated_ips_count: int
    """
    Number of dedicated IP in the project.
    """

    monthly_emails_count: int
    """
    Number of emails sent during the current month in the project.
    """

    webhooks_count: int
    """
    Number of webhooks in the project.
    """

    custom_blocklists_count: int
    """
    Number of custom blocklists in the project.
    """


@dataclass
class ProjectSettings:
    periodic_report: Optional[ProjectSettingsPeriodicReport] = None
    """
    Information about your periodic report.
    """


@dataclass
class RevokeDomainRequest:
    domain_id: str
    """
    ID of the domain to delete.
    """

    region: Optional[ScwRegion] = None
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

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    autoconfig: Optional[bool] = False
    """
    (Optional) If set to true, activate auto-configuration of the domain's DNS zone.
    """


@dataclass
class UpdateOfferSubscriptionRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the Project.
    """

    name: Optional[OfferName] = OfferName.UNKNOWN_NAME
    """
    Name of the offer-subscription.
    """


@dataclass
class UpdateProjectSettingsRequest:
    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    project_id: Optional[str] = None
    """
    ID of the project.
    """

    periodic_report: Optional[UpdateProjectSettingsRequestUpdatePeriodicReport] = None
    """
    Periodic report update details - all fields are optional.
    """


@dataclass
class UpdateWebhookRequest:
    webhook_id: str
    """
    ID of the Webhook to update.
    """

    region: Optional[ScwRegion] = None
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str] = None
    """
    Name of the Webhook to update.
    """

    event_types: Optional[list[WebhookEventType]] = field(default_factory=list)
    """
    List of event types to update.
    """

    sns_arn: Optional[str] = None
    """
    Scaleway SNS ARN topic to update.
    """
