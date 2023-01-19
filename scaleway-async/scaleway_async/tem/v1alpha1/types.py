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


class DomainStatus(str, Enum):
    UNKNOWN = "unknown"
    CHECKED = "checked"
    UNCHECKED = "unchecked"
    INVALID = "invalid"
    LOCKED = "locked"
    REVOKED = "revoked"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class EmailRcptType(str, Enum):
    UNKNOWN_RCPT_TYPE = "unknown_rcpt_type"
    TO = "to"
    CC = "cc"
    BCC = "bcc"

    def __str__(self) -> str:
        return str(self.value)


class EmailStatus(str, Enum):
    UNKNOWN = "unknown"
    NEW = "new"
    SENDING = "sending"
    SENT = "sent"
    FAILED = "failed"
    CANCELED = "canceled"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class CreateEmailRequestAddress:
    """
    Create email request. address
    """

    email: str
    """
    Email address
    """

    name: Optional[str]
    """
    Optional display name
    """


@dataclass
class CreateEmailRequestAttachment:
    """
    Create email request. attachment
    """

    name: str
    """
    Filename of the attachment
    """

    type_: str
    """
    MIME type of the attachment (Currently only allow, text files, pdf and html files)
    """

    content: str
    """
    Content of the attachment, encoded in base64
    """


@dataclass
class CreateEmailResponse:
    """
    Create email response
    """

    emails: List[Email]
    """
    Single page of emails matching the requested criteria
    """


@dataclass
class Domain:
    """
    Domain
    """

    id: str
    """
    ID of the domain
    """

    organization_id: str
    """
    ID of the organization to which the domain belongs
    """

    project_id: str
    """
    ID of the project
    """

    name: str
    """
    Domain name (example.com)
    """

    status: DomainStatus
    """
    Status of the domain
    """

    created_at: Optional[datetime]
    """
    Date and time of domain's creation
    """

    next_check_at: Optional[datetime]
    """
    Date and time of the next scheduled check
    """

    last_valid_at: Optional[datetime]
    """
    Date and time the domain was last found to be valid
    """

    revoked_at: Optional[datetime]
    """
    Date and time of the revocation of the domain
    """

    last_error: Optional[str]
    """
    Error message if the last check failed
    """

    spf_config: str
    """
    Snippet of the SPF record that should be registered in the DNS zone
    """

    dkim_config: str
    """
    DKIM public key, as should be recorded in the DNS zone
    """

    statistics: Optional[DomainStatistics]
    """
    Domain's statistics
    """

    region: Region


@dataclass
class DomainStatistics:
    total_count: int

    sent_count: int

    failed_count: int

    canceled_count: int


@dataclass
class Email:
    """
    Email
    """

    id: str
    """
    Technical ID of the email
    """

    message_id: str
    """
    MessageID of the email
    """

    project_id: str
    """
    ID of the project to which the email belongs
    """

    mail_from: str
    """
    Email address of the sender
    """

    rcpt_to: str
    """
    Email address of the recipient
    """

    rcpt_type: EmailRcptType
    """
    Type of the recipient
    """

    created_at: Optional[datetime]
    """
    Creation date of the email object
    """

    updated_at: Optional[datetime]
    """
    Last update time of the email object
    """

    status: EmailStatus
    """
    Status of the email
    """

    status_details: Optional[str]
    """
    Additional information on the status
    """

    try_count: int
    """
    Total number of attempts to send the email
    """

    last_tries: List[EmailTry]
    """
    Informations about the latest three attempts to send the email
    """


@dataclass
class EmailTry:
    """
    Email. try
    """

    rank: int
    """
    Rank number of this attempt to send the email
    """

    tried_at: Optional[datetime]
    """
    Date of the attempt
    """

    code: int
    """
    The SMTP status code received after the attempt. 0 if the attempt did not reach an SMTP server.
    """

    message: str
    """
    The SMTP message received, if any. If the attempt did not reach an SMTP server, the message says why.
    """


@dataclass
class ListDomainsResponse:
    """
    List domains response
    """

    total_count: int
    """
    Total number of domains matching the request (without pagination)
    """

    domains: List[Domain]


@dataclass
class ListEmailsResponse:
    """
    List emails response
    """

    total_count: int
    """
    Count of all emails matching the requested criteria
    """

    emails: List[Email]
    """
    Single page of emails matching the requested criteria
    """


@dataclass
class Statistics:
    """
    Statistics
    """

    total_count: int
    """
    Total number of emails matching the request criteria
    """

    new_count: int
    """
    Number of emails still in the `new` transient state (received from the API, not yet processed)
    """

    sending_count: int
    """
    Number of emails still in the `sending` transient state (received from the API, not yet in their final status)
    """

    sent_count: int
    """
    Number of emails in the final `sent` state (have been delivered to the target mail system)
    """

    failed_count: int
    """
    Number of emails in the final `failed` state (refused by the target mail system with a final error status)
    """

    canceled_count: int
    """
    Number of emails in the final `canceled` state (canceled by customer's request)
    """


@dataclass
class CreateEmailRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    from_: Optional[CreateEmailRequestAddress]
    """
    Sender information (must be from a checked domain declared in the project)
    """

    to: Optional[List[CreateEmailRequestAddress]]
    """
    Array of recipient information (limited to 1 recipient)
    """

    cc: Optional[List[CreateEmailRequestAddress]]
    """
    Array of recipient information (unimplemented)
    """

    bcc: Optional[List[CreateEmailRequestAddress]]
    """
    Array of recipient information (unimplemented)
    """

    subject: str
    """
    Message subject
    """

    text: str
    """
    Text content
    """

    html: str
    """
    HTML content
    """

    project_id: Optional[str]
    """
    ID of the project in which to create the email
    """

    attachments: Optional[List[CreateEmailRequestAttachment]]
    """
    Array of attachments
    """

    send_before: Optional[datetime]
    """
    Maximum date to deliver mail
    """


@dataclass
class GetEmailRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    email_id: str
    """
    ID of the email to retrieve
    """


@dataclass
class ListEmailsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]

    page_size: Optional[int]

    project_id: Optional[str]
    """
    Optional ID of the project in which to list the emails
    """

    domain_id: Optional[str]
    """
    Optional ID of the domain for which to list the emails
    """

    message_id: Optional[str]
    """
    Optional ID of the message for which to list the emails
    """

    since: Optional[datetime]
    """
    Optional, list emails created after this date
    """

    until: Optional[datetime]
    """
    Optional, list emails created before this date
    """

    mail_from: Optional[str]
    """
    Optional, list emails sent with this `mail_from` sender's address
    """

    mail_to: Optional[str]
    """
    Optional, list emails sent with this `mail_to` recipient's address
    """

    statuses: Optional[List[EmailStatus]]
    """
    Optional, list emails having any of this status
    """


@dataclass
class GetStatisticsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    project_id: Optional[str]
    """
    Optional, count emails for this project
    """

    domain_id: Optional[str]
    """
    Optional, count emails send from this domain (must be coherent with the `project_id` and the `organization_id`)
    """

    since: Optional[datetime]
    """
    Optional, count emails created after this date
    """

    until: Optional[datetime]
    """
    Optional, count emails created before this date
    """

    mail_from: Optional[str]
    """
    Optional, count emails sent with this `mail_from` sender's address
    """


@dataclass
class CancelEmailRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    email_id: str
    """
    ID of the email to cancel
    """


@dataclass
class CreateDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    project_id: Optional[str]

    domain_name: str


@dataclass
class GetDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    domain_id: str
    """
    ID of the domain
    """


@dataclass
class ListDomainsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    page: Optional[int]
    """
    Page number (1 for the first page)
    """

    page_size: Optional[int]
    """
    Page size
    """

    project_id: Optional[str]

    status: Optional[List[DomainStatus]]

    organization_id: Optional[str]

    name: Optional[str]


@dataclass
class RevokeDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    domain_id: str
    """
    ID of the domain to revoke
    """


@dataclass
class CheckDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config
    """

    domain_id: str
    """
    ID of the domain to check
    """
