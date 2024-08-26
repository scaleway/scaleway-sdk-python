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
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    DomainStatus,
    EmailFlag,
    EmailStatus,
    ListEmailsRequestOrderBy,
    ListWebhookEventsRequestOrderBy,
    ListWebhooksRequestOrderBy,
    WebhookEventStatus,
    WebhookEventType,
    CreateDomainRequest,
    CreateEmailRequest,
    CreateEmailRequestAddress,
    CreateEmailRequestAttachment,
    CreateEmailRequestHeader,
    CreateEmailResponse,
    CreateWebhookRequest,
    Domain,
    DomainLastStatus,
    Email,
    ListDomainsResponse,
    ListEmailsResponse,
    ListWebhookEventsResponse,
    ListWebhooksResponse,
    Statistics,
    UpdateDomainRequest,
    UpdateWebhookRequest,
    Webhook,
    WebhookEvent,
)
from .content import (
    DOMAIN_TRANSIENT_STATUSES,
    EMAIL_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Email,
    unmarshal_Domain,
    unmarshal_Webhook,
    unmarshal_CreateEmailResponse,
    unmarshal_DomainLastStatus,
    unmarshal_ListDomainsResponse,
    unmarshal_ListEmailsResponse,
    unmarshal_ListWebhookEventsResponse,
    unmarshal_ListWebhooksResponse,
    unmarshal_Statistics,
    marshal_CreateDomainRequest,
    marshal_CreateEmailRequest,
    marshal_CreateWebhookRequest,
    marshal_UpdateDomainRequest,
    marshal_UpdateWebhookRequest,
)


class TemV1Alpha1API(API):
    """
    This API allows you to manage your Transactional Email services.
    """

    async def create_email(
        self,
        *,
        from_: CreateEmailRequestAddress,
        subject: str,
        text: str,
        html: str,
        region: Optional[Region] = None,
        to: Optional[List[CreateEmailRequestAddress]] = None,
        cc: Optional[List[CreateEmailRequestAddress]] = None,
        bcc: Optional[List[CreateEmailRequestAddress]] = None,
        project_id: Optional[str] = None,
        attachments: Optional[List[CreateEmailRequestAttachment]] = None,
        send_before: Optional[datetime] = None,
        additional_headers: Optional[List[CreateEmailRequestHeader]] = None,
    ) -> CreateEmailResponse:
        """
        Send an email.
        You must specify the `region`, the sender and the recipient's information and the `project_id` to send an email from a checked domain. The subject of the email must contain at least 6 characters.
        :param from_: Sender information. Must be from a checked domain declared in the Project.
        :param subject: Subject of the email.
        :param text: Text content.
        :param html: HTML content.
        :param region: Region to target. If none is passed will use default region from the config.
        :param to: An array of the primary recipient's information.
        :param cc: An array of the carbon copy recipient's information.
        :param bcc: An array of the blind carbon copy recipient's information.
        :param project_id: ID of the Project in which to create the email.
        :param attachments: Array of attachments.
        :param send_before: Maximum date to deliver the email.
        :param additional_headers: Array of additional headers as key-value.
        :return: :class:`CreateEmailResponse <CreateEmailResponse>`

        Usage:
        ::

            result = await api.create_email(
                from=CreateEmailRequestAddress(),
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
                    from_=from_,
                    subject=subject,
                    text=text,
                    html=html,
                    region=region,
                    to=to,
                    cc=cc,
                    bcc=bcc,
                    project_id=project_id,
                    attachments=attachments,
                    send_before=send_before,
                    additional_headers=additional_headers,
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
        Get an email.
        Retrieve information about a specific email using the `email_id` and `region` parameters.
        :param email_id: ID of the email to retrieve.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = await api.get_email(
                email_id="example",
            )
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
        Get an email.
        Retrieve information about a specific email using the `email_id` and `region` parameters.
        :param email_id: ID of the email to retrieve.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = await api.get_email(
                email_id="example",
            )
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
        mail_rcpt: Optional[str] = None,
        statuses: Optional[List[EmailStatus]] = None,
        subject: Optional[str] = None,
        search: Optional[str] = None,
        order_by: Optional[ListEmailsRequestOrderBy] = None,
        flags: Optional[List[EmailFlag]] = None,
    ) -> ListEmailsResponse:
        """
        List emails.
        Retrieve the list of emails sent from a specific domain or for a specific Project or Organization. You must specify the `region`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param project_id: (Optional) ID of the Project in which to list the emails.
        :param domain_id: (Optional) ID of the domain for which to list the emails.
        :param message_id: (Optional) ID of the message for which to list the emails.
        :param since: (Optional) List emails created after this date.
        :param until: (Optional) List emails created before this date.
        :param mail_from: (Optional) List emails sent with this sender's email address.
        :param mail_to: List emails sent to this recipient's email address.
        :param mail_rcpt: (Optional) List emails sent to this recipient's email address.
        :param statuses: (Optional) List emails with any of these statuses.
        :param subject: (Optional) List emails with this subject.
        :param search: (Optional) List emails by searching to all fields.
        :param order_by: (Optional) List emails corresponding to specific criteria.
        :param flags: (Optional) List emails containing only specific flags.
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
                "flags": flags,
                "mail_from": mail_from,
                "mail_rcpt": mail_rcpt,
                "mail_to": mail_to,
                "message_id": message_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "search": search,
                "since": since,
                "statuses": statuses,
                "subject": subject,
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
        mail_rcpt: Optional[str] = None,
        statuses: Optional[List[EmailStatus]] = None,
        subject: Optional[str] = None,
        search: Optional[str] = None,
        order_by: Optional[ListEmailsRequestOrderBy] = None,
        flags: Optional[List[EmailFlag]] = None,
    ) -> List[Email]:
        """
        List emails.
        Retrieve the list of emails sent from a specific domain or for a specific Project or Organization. You must specify the `region`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page:
        :param page_size:
        :param project_id: (Optional) ID of the Project in which to list the emails.
        :param domain_id: (Optional) ID of the domain for which to list the emails.
        :param message_id: (Optional) ID of the message for which to list the emails.
        :param since: (Optional) List emails created after this date.
        :param until: (Optional) List emails created before this date.
        :param mail_from: (Optional) List emails sent with this sender's email address.
        :param mail_to: List emails sent to this recipient's email address.
        :param mail_rcpt: (Optional) List emails sent to this recipient's email address.
        :param statuses: (Optional) List emails with any of these statuses.
        :param subject: (Optional) List emails with this subject.
        :param search: (Optional) List emails by searching to all fields.
        :param order_by: (Optional) List emails corresponding to specific criteria.
        :param flags: (Optional) List emails containing only specific flags.
        :return: :class:`List[Email] <List[Email]>`

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
                "mail_rcpt": mail_rcpt,
                "statuses": statuses,
                "subject": subject,
                "search": search,
                "order_by": order_by,
                "flags": flags,
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
        Email statuses.
        Get information on your emails' statuses.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: (Optional) Number of emails for this Project.
        :param domain_id: (Optional) Number of emails sent from this domain (must be coherent with the `project_id` and the `organization_id`).
        :param since: (Optional) Number of emails created after this date.
        :param until: (Optional) Number of emails created before this date.
        :param mail_from: (Optional) Number of emails sent with this sender's email address.
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
        Cancel an email.
        You can cancel the sending of an email if it has not been sent yet. You must specify the `region` and the `email_id` of the email you want to cancel.
        :param email_id: ID of the email to cancel.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = await api.cancel_email(
                email_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_email_id = validate_path_param("email_id", email_id)

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/emails/{param_email_id}/cancel",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Email(res.json())

    async def create_domain(
        self,
        *,
        domain_name: str,
        accept_tos: bool,
        autoconfig: bool,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> Domain:
        """
        Register a domain in a project.
        You must specify the `region`, `project_id` and `domain_name` to register a domain in a specific Project.
        :param domain_name: Fully qualified domain dame.
        :param accept_tos: Accept Scaleway's Terms of Service.
        :param autoconfig: Activate auto-configuration of the domain's DNS zone.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the project to which the domain belongs.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.create_domain(
                domain_name="example",
                accept_tos=False,
                autoconfig=False,
            )
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
                    accept_tos=accept_tos,
                    autoconfig=autoconfig,
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
        Get information about a domain.
        Retrieve information about a specific domain using the `region` and `domain_id` parameters. Monitor your domain's reputation and improve **average** and **bad** reputation statuses, using your domain's **Email activity** tab on the [Scaleway console](https://console.scaleway.com/transactional-email/domains) to get a more detailed report. Check out our [dedicated documentation](https://www.scaleway.com/en/docs/managed-services/transactional-email/reference-content/understanding-tem-reputation-score/) to improve your domain's reputation.
        :param domain_id: ID of the domain.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.get_domain(
                domain_id="example",
            )
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
        Get information about a domain.
        Retrieve information about a specific domain using the `region` and `domain_id` parameters. Monitor your domain's reputation and improve **average** and **bad** reputation statuses, using your domain's **Email activity** tab on the [Scaleway console](https://console.scaleway.com/transactional-email/domains) to get a more detailed report. Check out our [dedicated documentation](https://www.scaleway.com/en/docs/managed-services/transactional-email/reference-content/understanding-tem-reputation-score/) to improve your domain's reputation.
        :param domain_id: ID of the domain.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.get_domain(
                domain_id="example",
            )
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
        List domains.
        Retrieve domains in a specific Project or in a specific Organization using the `region` parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 1000.
        :param project_id: (Optional) ID of the Project in which to list the domains.
        :param status: (Optional) List domains under specific statuses.
        :param organization_id: (Optional) ID of the Organization in which to list the domains.
        :param name: (Optional) Names of the domains to list.
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
        List domains.
        Retrieve domains in a specific Project or in a specific Organization using the `region` parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 1000.
        :param project_id: (Optional) ID of the Project in which to list the domains.
        :param status: (Optional) List domains under specific statuses.
        :param organization_id: (Optional) ID of the Organization in which to list the domains.
        :param name: (Optional) Names of the domains to list.
        :return: :class:`List[Domain] <List[Domain]>`

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
        Delete a domain.
        You must specify the domain you want to delete by the `region` and `domain_id`. Deleting a domain is permanent and cannot be undone.
        :param domain_id: ID of the domain to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.revoke_domain(
                domain_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/domains/{param_domain_id}/revoke",
            body={},
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
        Domain DNS check.
        Perform an immediate DNS check of a domain using the `region` and `domain_id` parameters.
        :param domain_id: ID of the domain to check.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.check_domain(
                domain_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/domains/{param_domain_id}/check",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    async def get_domain_last_status(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
    ) -> DomainLastStatus:
        """
        Display SPF and DKIM records status and potential errors.
        Display SPF and DKIM records status and potential errors, including the found records to make debugging easier.
        :param domain_id: ID of the domain to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DomainLastStatus <DomainLastStatus>`

        Usage:
        ::

            result = await api.get_domain_last_status(
                domain_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/domains/{param_domain_id}/verification",
        )

        self._throw_on_error(res)
        return unmarshal_DomainLastStatus(res.json())

    async def update_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
        autoconfig: Optional[bool] = None,
    ) -> Domain:
        """
        Update a domain.
        Update a domain auto-configuration.
        :param domain_id: ID of the domain to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param autoconfig: (Optional) If set to true, activate auto-configuration of the domain's DNS zone.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = await api.update_domain(
                domain_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "PATCH",
            f"/transactional-email/v1alpha1/regions/{param_region}/domains/{param_domain_id}",
            body=marshal_UpdateDomainRequest(
                UpdateDomainRequest(
                    domain_id=domain_id,
                    region=region,
                    autoconfig=autoconfig,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())

    async def create_webhook(
        self,
        *,
        domain_id: str,
        name: str,
        sns_arn: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        event_types: Optional[List[WebhookEventType]] = None,
    ) -> Webhook:
        """
        Create a Webhook.
        Create a new Webhook triggered by a list of event types and pushed to a Scaleway SNS ARN.
        :param domain_id: ID of the Domain to watch for triggering events.
        :param name: Name of the Webhook.
        :param sns_arn: Scaleway SNS ARN topic to push the events to.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the project to which the Webhook belongs.
        :param event_types: List of event types that will trigger an event.
        :return: :class:`Webhook <Webhook>`

        Usage:
        ::

            result = await api.create_webhook(
                domain_id="example",
                name="example",
                sns_arn="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/webhooks",
            body=marshal_CreateWebhookRequest(
                CreateWebhookRequest(
                    domain_id=domain_id,
                    name=name,
                    sns_arn=sns_arn,
                    region=region,
                    project_id=project_id,
                    event_types=event_types,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Webhook(res.json())

    async def list_webhooks(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListWebhooksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        domain_id: Optional[str] = None,
    ) -> ListWebhooksResponse:
        """
        List Webhooks.
        Retrieve Webhooks in a specific Project or in a specific Organization using the `region` parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: (Optional) List Webhooks corresponding to specific criteria.
        :param page: (Optional) Requested page number. Value must be greater or equal to 1.
        :param page_size: (Optional) Requested page size. Value must be between 1 and 100.
        :param project_id: (Optional) ID of the Project for which to list the Webhooks.
        :param organization_id: (Optional) ID of the Organization for which to list the Webhooks.
        :param domain_id: (Optional) ID of the Domain for which to list the Webhooks.
        :return: :class:`ListWebhooksResponse <ListWebhooksResponse>`

        Usage:
        ::

            result = await api.list_webhooks()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/webhooks",
            params={
                "domain_id": domain_id,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListWebhooksResponse(res.json())

    async def list_webhooks_all(
        self,
        *,
        region: Optional[Region] = None,
        order_by: Optional[ListWebhooksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        domain_id: Optional[str] = None,
    ) -> List[Webhook]:
        """
        List Webhooks.
        Retrieve Webhooks in a specific Project or in a specific Organization using the `region` parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: (Optional) List Webhooks corresponding to specific criteria.
        :param page: (Optional) Requested page number. Value must be greater or equal to 1.
        :param page_size: (Optional) Requested page size. Value must be between 1 and 100.
        :param project_id: (Optional) ID of the Project for which to list the Webhooks.
        :param organization_id: (Optional) ID of the Organization for which to list the Webhooks.
        :param domain_id: (Optional) ID of the Domain for which to list the Webhooks.
        :return: :class:`List[Webhook] <List[Webhook]>`

        Usage:
        ::

            result = await api.list_webhooks_all()
        """

        return await fetch_all_pages_async(
            type=ListWebhooksResponse,
            key="webhooks",
            fetcher=self.list_webhooks,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "organization_id": organization_id,
                "domain_id": domain_id,
            },
        )

    async def get_webhook(
        self,
        *,
        webhook_id: str,
        region: Optional[Region] = None,
    ) -> Webhook:
        """
        Get information about a Webhook.
        Retrieve information about a specific Webhook using the `webhook_id` and `region` parameters.
        :param webhook_id: ID of the Webhook to check.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Webhook <Webhook>`

        Usage:
        ::

            result = await api.get_webhook(
                webhook_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_webhook_id = validate_path_param("webhook_id", webhook_id)

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/webhooks/{param_webhook_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Webhook(res.json())

    async def update_webhook(
        self,
        *,
        webhook_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        event_types: Optional[List[WebhookEventType]] = None,
        sns_arn: Optional[str] = None,
    ) -> Webhook:
        """
        Update a Webhook.
        Update a Webhook events type, SNS ARN or name.
        :param webhook_id: ID of the Webhook to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the Webhook to update.
        :param event_types: List of event types to update.
        :param sns_arn: Scaleway SNS ARN topic to update.
        :return: :class:`Webhook <Webhook>`

        Usage:
        ::

            result = await api.update_webhook(
                webhook_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_webhook_id = validate_path_param("webhook_id", webhook_id)

        res = self._request(
            "PATCH",
            f"/transactional-email/v1alpha1/regions/{param_region}/webhooks/{param_webhook_id}",
            body=marshal_UpdateWebhookRequest(
                UpdateWebhookRequest(
                    webhook_id=webhook_id,
                    region=region,
                    name=name,
                    event_types=event_types,
                    sns_arn=sns_arn,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Webhook(res.json())

    async def delete_webhook(
        self,
        *,
        webhook_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a Webhook.
        You must specify the Webhook you want to delete by the `region` and `webhook_id`. Deleting a Webhook is permanent and cannot be undone.
        :param webhook_id: ID of the Webhook to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_webhook(
                webhook_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_webhook_id = validate_path_param("webhook_id", webhook_id)

        res = self._request(
            "DELETE",
            f"/transactional-email/v1alpha1/regions/{param_region}/webhooks/{param_webhook_id}",
        )

        self._throw_on_error(res)

    async def list_webhook_events(
        self,
        *,
        webhook_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListWebhookEventsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        email_id: Optional[str] = None,
        event_types: Optional[List[WebhookEventType]] = None,
        statuses: Optional[List[WebhookEventStatus]] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        domain_id: Optional[str] = None,
    ) -> ListWebhookEventsResponse:
        """
        List Webhook triggered events.
        Retrieve the list of Webhook events triggered from a specific Webhook or for a specific Project or Organization. You must specify the `region`.
        :param webhook_id: ID of the Webhook linked to the events.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: (Optional) List Webhook events corresponding to specific criteria.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 100.
        :param email_id: ID of the email linked to the events.
        :param event_types: List of event types linked to the events.
        :param statuses: List of event statuses.
        :param project_id: ID of the webhook Project.
        :param organization_id: ID of the webhook Organization.
        :param domain_id: ID of the domain to watch for triggering events.
        :return: :class:`ListWebhookEventsResponse <ListWebhookEventsResponse>`

        Usage:
        ::

            result = await api.list_webhook_events(
                webhook_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_webhook_id = validate_path_param("webhook_id", webhook_id)

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/webhooks/{param_webhook_id}/events",
            params={
                "domain_id": domain_id,
                "email_id": email_id,
                "event_types": event_types,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "statuses": statuses,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListWebhookEventsResponse(res.json())

    async def list_webhook_events_all(
        self,
        *,
        webhook_id: str,
        region: Optional[Region] = None,
        order_by: Optional[ListWebhookEventsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        email_id: Optional[str] = None,
        event_types: Optional[List[WebhookEventType]] = None,
        statuses: Optional[List[WebhookEventStatus]] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        domain_id: Optional[str] = None,
    ) -> List[WebhookEvent]:
        """
        List Webhook triggered events.
        Retrieve the list of Webhook events triggered from a specific Webhook or for a specific Project or Organization. You must specify the `region`.
        :param webhook_id: ID of the Webhook linked to the events.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: (Optional) List Webhook events corresponding to specific criteria.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 100.
        :param email_id: ID of the email linked to the events.
        :param event_types: List of event types linked to the events.
        :param statuses: List of event statuses.
        :param project_id: ID of the webhook Project.
        :param organization_id: ID of the webhook Organization.
        :param domain_id: ID of the domain to watch for triggering events.
        :return: :class:`List[WebhookEvent] <List[WebhookEvent]>`

        Usage:
        ::

            result = await api.list_webhook_events_all(
                webhook_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListWebhookEventsResponse,
            key="webhook_events",
            fetcher=self.list_webhook_events,
            args={
                "webhook_id": webhook_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "email_id": email_id,
                "event_types": event_types,
                "statuses": statuses,
                "project_id": project_id,
                "organization_id": organization_id,
                "domain_id": domain_id,
            },
        )
