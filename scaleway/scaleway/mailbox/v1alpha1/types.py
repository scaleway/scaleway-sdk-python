# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.utils import (
    StrEnumMeta,
)


class DomainRecordDNSType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DNS_TYPE = "unknown_dns_type"
    CNAME_DNS_TYPE = "cname_dns_type"
    MX_DNS_TYPE = "mx_dns_type"
    SRV_DNS_TYPE = "srv_dns_type"
    TXT_DNS_TYPE = "txt_dns_type"

    def __str__(self) -> str:
        return str(self.value)


class DomainRecordLevel(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_LEVEL = "unknown_level"
    REQUIRED = "required"
    RECOMMENDED = "recommended"
    OPTIONAL = "optional"

    def __str__(self) -> str:
        return str(self.value)


class DomainRecordStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    VALIDATING = "validating"
    VALID = "valid"
    INVALID = "invalid"
    NOT_FOUND = "not_found"

    def __str__(self) -> str:
        return str(self.value)


class DomainStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    WAITING_VALIDATION = "waiting_validation"
    VALIDATING = "validating"
    VALIDATION_FAILED = "validation_failed"
    PROVISIONING = "provisioning"
    READY = "ready"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)


class ListDomainsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    NAME_DESC = "name_desc"
    NAME_ASC = "name_asc"
    MAILBOX_TOTAL_COUNT_DESC = "mailbox_total_count_desc"
    MAILBOX_TOTAL_COUNT_ASC = "mailbox_total_count_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListMailboxesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"
    UPDATED_AT_DESC = "updated_at_desc"
    UPDATED_AT_ASC = "updated_at_asc"
    EMAIL_DESC = "email_desc"
    EMAIL_ASC = "email_asc"

    def __str__(self) -> str:
        return str(self.value)


class MailboxStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    CREATING = "creating"
    WAITING_PAYMENT = "waiting_payment"
    WAITING_DOMAIN = "waiting_domain"
    READY = "ready"
    DELETION_SCHEDULED = "deletion_scheduled"
    LOCKED = "locked"
    RENEWING = "renewing"
    DELETING = "deleting"
    RESTORING = "restoring"
    PAYMENT_FAILED = "payment_failed"

    def __str__(self) -> str:
        return str(self.value)


class MailboxSubscriptionPeriod(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUBSCRIPTION_PERIOD = "unknown_subscription_period"
    CANCELED = "canceled"
    MONTHLY = "monthly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class BatchCreateMailboxesRequestMailboxParameters:
    local_part: str
    password: str


@dataclass
class Mailbox:
    id: str
    """
    Unique identifier of the mailbox.
    """

    domain_id: str
    """
    ID of the domain to which the mailbox belongs.
    """

    email: str
    """
    Email address of the mailbox as local_part@domain.
    """

    status: MailboxStatus
    """
    Status of the mailbox.
    """

    subscription_period: MailboxSubscriptionPeriod
    """
    Subscription renewal period, it can be monthly, yearly or canceled if the subscription has been canceled.
    """

    next_subscription_period: MailboxSubscriptionPeriod
    """
    Next subscription renewal period, it can be monthly or yearly or canceled if the subscription has been canceled.
    """

    subscription_period_started_at: Optional[datetime] = None
    """
    Date and time of subscription period start.
    """

    next_subscription_period_starts_at: Optional[datetime] = None
    """
    Date and time when the next subscription period starts.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of mailbox creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time when the mailbox was last updated.
    """

    deletion_scheduled_at: Optional[datetime] = None
    """
    Date and time of the unrecoverable mailbox deletion.
    """


@dataclass
class DomainRecord:
    id: str
    """
    Unique identifier of the DNS record.
    """

    domain_id: str
    """
    ID of the domain to which the record belongs.
    """

    status: DomainRecordStatus
    """
    Status of the record.
    """

    level: DomainRecordLevel
    """
    Level of requirement of the record.
    """

    dns_type: DomainRecordDNSType
    """
    DNS type of the record.
    """

    dns_name: str
    """
    DNS name of the record.
    """

    dns_value: str
    """
    DNS value of the record.
    """

    error: Optional[str] = None
    """
    Error associated in case the record is not valid.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of record creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of record last updated.
    """


@dataclass
class Domain:
    id: str
    """
    Unique identifier of the domain.
    """

    project_id: str
    """
    ID of the Project to which the domain belongs.
    """

    name: str
    """
    Fully qualified domain name.
    """

    status: DomainStatus
    """
    Status of the domain.
    """

    mailbox_total_count: int
    """
    Number of mailboxes of the domain.
    """

    webmail_url: str
    """
    URL of the domain's webmail.
    """

    imap_url: str
    """
    URL of the domain's IMAP service.
    """

    pop3_url: str
    """
    URL of the domain's POP3 service.
    """

    smtp_url: str
    """
    URL of the domain's SMTP service.
    """

    created_at: Optional[datetime] = None
    """
    Date and time of domain creation.
    """

    updated_at: Optional[datetime] = None
    """
    Date and time of the domain's last update.
    """


@dataclass
class BatchCreateMailboxesRequest:
    domain_id: str
    """
    ID of the domain in which to create the mailboxes.
    """

    mailboxes: Optional[list[BatchCreateMailboxesRequestMailboxParameters]] = field(
        default_factory=list
    )
    """
    Parameters for the mailboxes to create.
    """

    subscription_period: Optional[MailboxSubscriptionPeriod] = (
        MailboxSubscriptionPeriod.UNKNOWN_SUBSCRIPTION_PERIOD
    )
    """
    Subscription renewal period, it can be monthly or yearly.
    """


@dataclass
class BatchCreateMailboxesResponse:
    mailboxes: list[Mailbox]
    """
    Mailboxes created.
    """


@dataclass
class CreateDomainRequest:
    name: str
    """
    Fully qualified domain name.
    """

    project_id: Optional[str] = None
    """
    ID of the project to which the domain belongs.
    """


@dataclass
class DeleteDomainRequest:
    domain_id: str
    """
    ID of the domain to delete.
    """


@dataclass
class DeleteMailboxRequest:
    mailbox_id: str
    """
    ID of the mailbox to delete.
    """


@dataclass
class GetDomainRecordsRequest:
    domain_id: str
    """
    (Optional) ID of the domain in which to get the records.
    """


@dataclass
class GetDomainRecordsResponse:
    autoconfig: Optional[DomainRecord] = None
    """
    Record designed to automatically configure an email client with the appropriate mail server settings using a standardized XML file format.
    """

    autodiscover: Optional[DomainRecord] = None
    """
    Record designed to automate the discovery of server settings to configure email clients like Outlook.
    """

    caldav: Optional[DomainRecord] = None
    """
    Record that allows clients to interact with calendar data stored on a server.
    """

    carddav: Optional[DomainRecord] = None
    """
    Record that allows clients to interact with contact data stored on a server.
    """

    dkim: Optional[DomainRecord] = None
    """
    Record that allows the DKIM email authentication method to be employed to verify the authenticity of an email message.
    """

    dmarc: Optional[DomainRecord] = None
    """
    Record that provides a mechanism for email receivers to determine if incoming messages are legitimate and were sent from authorized sources.
    """

    domain_validation: Optional[DomainRecord] = None
    """
    Record that provides a unique token to validate a domain ownership.
    """

    imap: Optional[DomainRecord] = None
    """
    Record that allows accessing the mailbox with the IMAP protocol.
    """

    mx: Optional[DomainRecord] = None
    """
    Record that directs emails to a mail server.
    """

    pop3: Optional[DomainRecord] = None
    """
    Record that allows accessing the mailbox with the POP3 protocol.
    """

    spf: Optional[DomainRecord] = None
    """
    Record that lists all the servers authorized to send emails from a particular domain.
    """

    submission: Optional[DomainRecord] = None
    """
    Record that allows the use of the SMTP submission mechanism.
    """


@dataclass
class GetDomainRequest:
    domain_id: str
    """
    ID of the domain to get.
    """


@dataclass
class GetMailboxRequest:
    mailbox_id: str
    """
    ID of the mailbox to get.
    """


@dataclass
class ListDomainsRequest:
    order_by: Optional[ListDomainsRequestOrderBy] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    project_id: Optional[str] = None
    statuses: Optional[list[DomainStatus]] = field(default_factory=list)
    search: Optional[str] = None


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
class ListMailboxesRequest:
    order_by: Optional[ListMailboxesRequestOrderBy] = (
        ListMailboxesRequestOrderBy.CREATED_AT_DESC
    )
    """
    Order matching mailbox by different criteria.
    """

    page: Optional[int] = 0
    """
    Requested page number. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    Requested page size. Value must be between 1 and 1000.
    """

    domain_id: Optional[str] = None
    """
    (Optional) ID of the domain in which to list the mailboxes.
    """

    statuses: Optional[list[MailboxStatus]] = field(default_factory=list)
    """
    (Optional) Filter mailboxes by their statuses.
    """

    search: Optional[str] = None
    """
    (Optional) Search term to filter mailboxes on name and local_part.
    """


@dataclass
class ListMailboxesResponse:
    total_count: int
    """
    Number of mailboxes that match the request (without pagination).
    """

    mailboxes: list[Mailbox]
    """
    Mailboxes matching the requested criteria.
    """


@dataclass
class RestoreMailboxRequest:
    mailbox_id: str
    """
    ID of the mailbox to restore.
    """


@dataclass
class UpdateMailboxRequest:
    mailbox_id: str
    """
    ID of the mailbox to update.
    """

    subscription_period: Optional[MailboxSubscriptionPeriod] = (
        MailboxSubscriptionPeriod.UNKNOWN_SUBSCRIPTION_PERIOD
    )
    """
    (Optional) New subscription period for the mailbox.
    """

    new_password: Optional[str] = None
    """
    (Optional) New password of the mailbox.
    """


@dataclass
class ValidateDomainRecordsRequest:
    domain_id: str
