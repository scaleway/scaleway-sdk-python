# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages_async,
    validate_path_param,
    wait_for_resource_async,
)
from .types import (
    DomainStatus,
    EmailStatus,
    CreateEmailRequestAddress,
    CreateEmailRequestAttachment,
    CreateEmailResponse,
    Domain,
    Email,
    ListDomainsResponse,
    ListEmailsResponse,
    Statistics,
    CreateEmailRequest,
    CreateDomainRequest,
)
from .content import (
    DOMAIN_TRANSIENT_STATUSES,
    EMAIL_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_CreateDomainRequest,
    marshal_CreateEmailRequest,
    unmarshal_Domain,
    unmarshal_Email,
    unmarshal_CreateEmailResponse,
    unmarshal_ListDomainsResponse,
    unmarshal_ListEmailsResponse,
    unmarshal_Statistics,
)


class TemV1Alpha1API(API):
    """
    Transactional Email API.

    Tem.
    """

    async def create_email(
        self,
        *,
        subject: str,
        text: str,
        html: str,
        region: Optional[Region] = None,
        from_: Optional[CreateEmailRequestAddress] = None,
        to: Optional[List[CreateEmailRequestAddress]] = None,
        cc: Optional[List[CreateEmailRequestAddress]] = None,
        bcc: Optional[List[CreateEmailRequestAddress]] = None,
        project_id: Optional[str] = None,
        attachments: Optional[List[CreateEmailRequestAttachment]] = None,
        send_before: Optional[datetime] = None,
    ) -> CreateEmailResponse:
        """
        Send an email
        :param region: Region to target. If none is passed will use default region from the config
        :param from_: Sender information (must be from a checked domain declared in the project)
        :param to: Array of recipient information (limited to 1 recipient)
        :param cc: Array of recipient information (unimplemented)
        :param bcc: Array of recipient information (unimplemented)
        :param subject: Message subject
        :param text: Text content
        :param html: HTML content
        :param project_id: ID of the project in which to create the email
        :param attachments: Array of attachments
        :param send_before: Maximum date to deliver mail
        :return: :class:`CreateEmailResponse <CreateEmailResponse>`

        Usage:
        ::

            result = await api.create_email(
                subject="example",
                text="example",
                html="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/emails",
            body=marshal_CreateEmailRequest(
                CreateEmailRequest(
                    subject=subject,
                    text=text,
                    html=html,
                    region=region,
                    from_=from_,
                    to=to,
                    cc=cc,
                    bcc=bcc,
                    project_id=project_id,
                    attachments=attachments,
                    send_before=send_before,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CreateEmailResponse(res.json())

    async def get_email(
        self,
        *,
        email_id: str,
        region: Optional[Region] = None,
    ) -> Email:
        """
        Get information about an email
        :param region: Region to target. If none is passed will use default region from the config
        :param email_id: ID of the email to retrieve
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = await api.get_email(email_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_email_id = validate_path_param("email_id", email_id)

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/emails/{param_email_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Email(res.json())

    async def wait_for_email(
        self,
        *,
        email_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Email, Union[bool, Awaitable[bool]]]] = None,
    ) -> Email:
        """
        Waits for :class:`Email <Email>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param email_id: ID of the email to retrieve
        :param options: The options for the waiter
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = api.wait_for_email(email_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in EMAIL_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_email,
            options=options,
            args={
                "email_id": email_id,
                "region": region,
            },
        )

    async def list_emails(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        domain_id: Optional[str] = None,
        message_id: Optional[str] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        mail_from: Optional[str] = None,
        mail_to: Optional[str] = None,
        statuses: Optional[List[EmailStatus]] = None,
    ) -> ListEmailsResponse:
        """
        List emails sent from a domain and/or for a project and/or for an organization
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param project_id: Optional ID of the project in which to list the emails
        :param domain_id: Optional ID of the domain for which to list the emails
        :param message_id: Optional ID of the message for which to list the emails
        :param since: Optional, list emails created after this date
        :param until: Optional, list emails created before this date
        :param mail_from: Optional, list emails sent with this `mail_from` sender's address
        :param mail_to: Optional, list emails sent with this `mail_to` recipient's address
        :param statuses: Optional, list emails having any of this status
        :return: :class:`ListEmailsResponse <ListEmailsResponse>`

        Usage:
        ::

            result = await api.list_emails()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/emails",
            params={
                "domain_id": domain_id,
                "mail_from": mail_from,
                "mail_to": mail_to,
                "message_id": message_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "since": since,
                "statuses": statuses,
                "until": until,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListEmailsResponse(res.json())

    async def list_emails_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        domain_id: Optional[str] = None,
        message_id: Optional[str] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        mail_from: Optional[str] = None,
        mail_to: Optional[str] = None,
        statuses: Optional[List[EmailStatus]] = None,
    ) -> List[Email]:
        """
        List emails sent from a domain and/or for a project and/or for an organization
        :param region: Region to target. If none is passed will use default region from the config
        :param page:
        :param page_size:
        :param project_id: Optional ID of the project in which to list the emails
        :param domain_id: Optional ID of the domain for which to list the emails
        :param message_id: Optional ID of the message for which to list the emails
        :param since: Optional, list emails created after this date
        :param until: Optional, list emails created before this date
        :param mail_from: Optional, list emails sent with this `mail_from` sender's address
        :param mail_to: Optional, list emails sent with this `mail_to` recipient's address
        :param statuses: Optional, list emails having any of this status
        :return: :class:`List[ListEmailsResponse] <List[ListEmailsResponse]>`

        Usage:
        ::

            result = await api.list_emails_all()
        """

        return await fetch_all_pages_async(
            type=ListEmailsResponse,
            key="emails",
            fetcher=self.list_emails,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "domain_id": domain_id,
                "message_id": message_id,
                "since": since,
                "until": until,
                "mail_from": mail_from,
                "mail_to": mail_to,
                "statuses": statuses,
            },
        )

    async def get_statistics(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        domain_id: Optional[str] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        mail_from: Optional[str] = None,
    ) -> Statistics:
        """
        Get statistics on the email statuses
        :param region: Region to target. If none is passed will use default region from the config
        :param project_id: Optional, count emails for this project
        :param domain_id: Optional, count emails send from this domain (must be coherent with the `project_id` and the `organization_id`)
        :param since: Optional, count emails created after this date
        :param until: Optional, count emails created before this date
        :param mail_from: Optional, count emails sent with this `mail_from` sender's address
        :return: :class:`Statistics <Statistics>`

        Usage:
        ::

            result = await api.get_statistics()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/statistics",
            params={
                "domain_id": domain_id,
                "mail_from": mail_from,
                "project_id": project_id or self.client.default_project_id,
                "since": since,
                "until": until,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Statistics(res.json())

    async def cancel_email(
        self,
        *,
        email_id: str,
        region: Optional[Region] = None,
    ) -> Email:
        """
        Try to cancel an email if it has not yet been sent
        :param region: Region to target. If none is passed will use default region from the config
        :param email_id: ID of the email to cancel
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = await api.cancel_email(email_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_email_id = validate_path_param("email_id", email_id)

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/emails/{param_email_id}/cancel",
        )

        self._throw_on_error(res)
        return unmarshal_Email(res.json())

    async def create_domain(
        self,
        *,
        domain_name: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> Domain:
        """
        Register a domain in a project
        :param region: Region to target. If none is passed will use default region from the config
        :param project_id:
        :param domain_name:
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.create_domain(domain_name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/domains",
            body=marshal_CreateDomainRequest(
                CreateDomainRequest(
                    domain_name=domain_name,
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    async def get_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Get information about a domain
        :param region: Region to target. If none is passed will use default region from the config
        :param domain_id: ID of the domain
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.get_domain(domain_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/domains/{param_domain_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    async def wait_for_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Domain, Union[bool, Awaitable[bool]]]] = None,
    ) -> Domain:
        """
        Waits for :class:`Domain <Domain>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config
        :param domain_id: ID of the domain
        :param options: The options for the waiter
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.wait_for_domain(domain_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DOMAIN_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_domain,
            options=options,
            args={
                "domain_id": domain_id,
                "region": region,
            },
        )

    async def list_domains(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        status: Optional[List[DomainStatus]] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListDomainsResponse:
        """
        List domains in a project and/or in an organization
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number (1 for the first page)
        :param page_size: Page size
        :param project_id:
        :param status:
        :param organization_id:
        :param name:
        :return: :class:`ListDomainsResponse <ListDomainsResponse>`

        Usage:
        ::

            result = await api.list_domains()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/domains",
            params={
                "name": name,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDomainsResponse(res.json())

    async def list_domains_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        status: Optional[List[DomainStatus]] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[Domain]:
        """
        List domains in a project and/or in an organization
        :param region: Region to target. If none is passed will use default region from the config
        :param page: Page number (1 for the first page)
        :param page_size: Page size
        :param project_id:
        :param status:
        :param organization_id:
        :param name:
        :return: :class:`List[ListDomainsResponse] <List[ListDomainsResponse]>`

        Usage:
        ::

            result = await api.list_domains_all()
        """

        return await fetch_all_pages_async(
            type=ListDomainsResponse,
            key="domains",
            fetcher=self.list_domains,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "status": status,
                "organization_id": organization_id,
                "name": name,
            },
        )

    async def revoke_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Revoke a domain
        :param region: Region to target. If none is passed will use default region from the config
        :param domain_id: ID of the domain to revoke
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.revoke_domain(domain_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/domains/{param_domain_id}/revoke",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    async def check_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Ask for an immediate check of a domain (DNS check)
        :param region: Region to target. If none is passed will use default region from the config
        :param domain_id: ID of the domain to check
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.check_domain(domain_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/domains/{param_domain_id}/check",
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())
