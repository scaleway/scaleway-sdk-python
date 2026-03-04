# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    BlocklistType,
    DomainStatus,
    EmailFlag,
    EmailStatus,
    ListBlocklistsRequestOrderBy,
    ListEmailsRequestOrderBy,
    ListWebhookEventsRequestOrderBy,
    ListWebhooksRequestOrderBy,
    OfferName,
    WebhookEventStatus,
    WebhookEventType,
    Blocklist,
    BulkCreateBlocklistsRequest,
    BulkCreateBlocklistsResponse,
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
    ListBlocklistsResponse,
    ListDomainsResponse,
    ListEmailsResponse,
    ListOfferSubscriptionsResponse,
    ListOffersResponse,
    ListPoolsResponse,
    ListWebhookEventsResponse,
    ListWebhooksResponse,
    OfferSubscription,
    Pool,
    ProjectConsumption,
    ProjectSettings,
    Statistics,
    UpdateDomainRequest,
    UpdateOfferSubscriptionRequest,
    UpdateProjectSettingsRequest,
    UpdateProjectSettingsRequestUpdatePeriodicReport,
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
    unmarshal_OfferSubscription,
    unmarshal_Webhook,
    unmarshal_BulkCreateBlocklistsResponse,
    unmarshal_CreateEmailResponse,
    unmarshal_DomainLastStatus,
    unmarshal_ListBlocklistsResponse,
    unmarshal_ListDomainsResponse,
    unmarshal_ListEmailsResponse,
    unmarshal_ListOfferSubscriptionsResponse,
    unmarshal_ListOffersResponse,
    unmarshal_ListPoolsResponse,
    unmarshal_ListWebhookEventsResponse,
    unmarshal_ListWebhooksResponse,
    unmarshal_ProjectConsumption,
    unmarshal_ProjectSettings,
    unmarshal_Statistics,
    marshal_BulkCreateBlocklistsRequest,
    marshal_CreateDomainRequest,
    marshal_CreateEmailRequest,
    marshal_CreateWebhookRequest,
    marshal_UpdateDomainRequest,
    marshal_UpdateOfferSubscriptionRequest,
    marshal_UpdateProjectSettingsRequest,
    marshal_UpdateWebhookRequest,
)


class TemV1Alpha1API(API):
    """
    This API allows you to manage your Transactional Email services.
    """

    def create_email(
        self,
        *,
        from_: CreateEmailRequestAddress,
        subject: str,
        text: str,
        html: str,
        region: Optional[ScwRegion] = None,
        to: Optional[list[CreateEmailRequestAddress]] = None,
        cc: Optional[list[CreateEmailRequestAddress]] = None,
        bcc: Optional[list[CreateEmailRequestAddress]] = None,
        project_id: Optional[str] = None,
        attachments: Optional[list[CreateEmailRequestAttachment]] = None,
        send_before: Optional[datetime] = None,
        additional_headers: Optional[list[CreateEmailRequestHeader]] = None,
    ) -> CreateEmailResponse:
        """
        Send an email.
        You must specify the `region`, the sender and the recipient's information and the `project_id` to send an email from a checked domain.
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

            result = api.create_email(
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

    def get_email(
        self,
        *,
        email_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Email:
        """
        Get an email.
        Retrieve information about a specific email using the `email_id` and `region` parameters.
        :param email_id: ID of the email to retrieve.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = api.get_email(
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

    def wait_for_email(
        self,
        *,
        email_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Email, bool]] = None,
    ) -> Email:
        """
        Get an email.
        Retrieve information about a specific email using the `email_id` and `region` parameters.
        :param email_id: ID of the email to retrieve.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = api.get_email(
                email_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in EMAIL_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_email,
            options=options,
            args={
                "email_id": email_id,
                "region": region,
            },
        )

    def list_emails(
        self,
        *,
        region: Optional[ScwRegion] = None,
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
        statuses: Optional[list[EmailStatus]] = None,
        subject: Optional[str] = None,
        search: Optional[str] = None,
        order_by: Optional[ListEmailsRequestOrderBy] = None,
        flags: Optional[list[EmailFlag]] = None,
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
        :param mail_to: Deprecated. List emails sent to this recipient's email address.
        :param mail_rcpt: (Optional) List emails sent to this recipient's email address.
        :param statuses: (Optional) List emails with any of these statuses.
        :param subject: (Optional) List emails with this subject.
        :param search: (Optional) List emails by searching to all fields.
        :param order_by: (Optional) List emails corresponding to specific criteria.
        :param flags: (Optional) List emails containing only specific flags.
        :return: :class:`ListEmailsResponse <ListEmailsResponse>`

        Usage:
        ::

            result = api.list_emails()
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

    def list_emails_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
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
        statuses: Optional[list[EmailStatus]] = None,
        subject: Optional[str] = None,
        search: Optional[str] = None,
        order_by: Optional[ListEmailsRequestOrderBy] = None,
        flags: Optional[list[EmailFlag]] = None,
    ) -> list[Email]:
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
        :param mail_to: Deprecated. List emails sent to this recipient's email address.
        :param mail_rcpt: (Optional) List emails sent to this recipient's email address.
        :param statuses: (Optional) List emails with any of these statuses.
        :param subject: (Optional) List emails with this subject.
        :param search: (Optional) List emails by searching to all fields.
        :param order_by: (Optional) List emails corresponding to specific criteria.
        :param flags: (Optional) List emails containing only specific flags.
        :return: :class:`list[Email] <list[Email]>`

        Usage:
        ::

            result = api.list_emails_all()
        """

        return fetch_all_pages(
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

    def get_statistics(
        self,
        *,
        region: Optional[ScwRegion] = None,
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

            result = api.get_statistics()
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

    def cancel_email(
        self,
        *,
        email_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Email:
        """
        Cancel an email.
        You can cancel the sending of an email if it has not been sent yet. You must specify the `region` and the `email_id` of the email you want to cancel.
        :param email_id: ID of the email to cancel.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = api.cancel_email(
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

    def create_domain(
        self,
        *,
        domain_name: str,
        accept_tos: bool,
        autoconfig: bool,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> Domain:
        """
        Register a domain in a project.
        You must specify the `region`, `project_id` and `domain_name` to register a domain in a specific Project.
        :param domain_name: Fully qualified domain dame.
        :param accept_tos: Deprecated. Accept Scaleway's Terms of Service.
        :param autoconfig: Activate auto-configuration of the domain's DNS zone.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the project to which the domain belongs.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.create_domain(
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

    def get_domain(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Domain:
        """
        Get information about a domain.
        Retrieve information about a specific domain using the `region` and `domain_id` parameters. Monitor your domain's reputation and improve **average** and **bad** reputation statuses, using your domain's **Email activity** tab on the [Scaleway console](https://console.scaleway.com/transactional-email/domains) to get a more detailed report. Check out our [dedicated documentation](https://www.scaleway.com/en/docs/managed-services/transactional-email/reference-content/understanding-tem-reputation-score/) to improve your domain's reputation.
        :param domain_id: ID of the domain.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(
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

    def wait_for_domain(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Domain, bool]] = None,
    ) -> Domain:
        """
        Get information about a domain.
        Retrieve information about a specific domain using the `region` and `domain_id` parameters. Monitor your domain's reputation and improve **average** and **bad** reputation statuses, using your domain's **Email activity** tab on the [Scaleway console](https://console.scaleway.com/transactional-email/domains) to get a more detailed report. Check out our [dedicated documentation](https://www.scaleway.com/en/docs/managed-services/transactional-email/reference-content/understanding-tem-reputation-score/) to improve your domain's reputation.
        :param domain_id: ID of the domain.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(
                domain_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DOMAIN_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_domain,
            options=options,
            args={
                "domain_id": domain_id,
                "region": region,
            },
        )

    def list_domains(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        status: Optional[list[DomainStatus]] = None,
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

            result = api.list_domains()
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

    def list_domains_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        status: Optional[list[DomainStatus]] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> list[Domain]:
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
        :return: :class:`list[Domain] <list[Domain]>`

        Usage:
        ::

            result = api.list_domains_all()
        """

        return fetch_all_pages(
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

    def revoke_domain(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Domain:
        """
        Delete a domain.
        You must specify the domain you want to delete by the `region` and `domain_id`. Deleting a domain is permanent and cannot be undone.
        :param domain_id: ID of the domain to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.revoke_domain(
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

    def check_domain(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Domain:
        """
        Domain DNS check.
        Perform an immediate DNS check of a domain using the `region` and `domain_id` parameters.
        :param domain_id: ID of the domain to check.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.check_domain(
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

    def get_domain_last_status(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
    ) -> DomainLastStatus:
        """
        Display SPF, DKIM, DMARC and MX records status and potential errors.
        Display SPF, DKIM, DMARC and MX records status and potential errors, including the found records to make debugging easier.
        :param domain_id: ID of the domain to get records status.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DomainLastStatus <DomainLastStatus>`

        Usage:
        ::

            result = api.get_domain_last_status(
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

    def update_domain(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
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

            result = api.update_domain(
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

    def create_webhook(
        self,
        *,
        domain_id: str,
        name: str,
        sns_arn: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        event_types: Optional[list[WebhookEventType]] = None,
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

            result = api.create_webhook(
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

    def list_webhooks(
        self,
        *,
        region: Optional[ScwRegion] = None,
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

            result = api.list_webhooks()
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

    def list_webhooks_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListWebhooksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        domain_id: Optional[str] = None,
    ) -> list[Webhook]:
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
        :return: :class:`list[Webhook] <list[Webhook]>`

        Usage:
        ::

            result = api.list_webhooks_all()
        """

        return fetch_all_pages(
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

    def get_webhook(
        self,
        *,
        webhook_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Webhook:
        """
        Get information about a Webhook.
        Retrieve information about a specific Webhook using the `webhook_id` and `region` parameters.
        :param webhook_id: ID of the Webhook to check.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Webhook <Webhook>`

        Usage:
        ::

            result = api.get_webhook(
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

    def update_webhook(
        self,
        *,
        webhook_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        event_types: Optional[list[WebhookEventType]] = None,
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

            result = api.update_webhook(
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

    def delete_webhook(
        self,
        *,
        webhook_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a Webhook.
        You must specify the Webhook you want to delete by the `region` and `webhook_id`. Deleting a Webhook is permanent and cannot be undone.
        :param webhook_id: ID of the Webhook to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_webhook(
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

    def list_webhook_events(
        self,
        *,
        webhook_id: str,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListWebhookEventsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        email_id: Optional[str] = None,
        event_types: Optional[list[WebhookEventType]] = None,
        statuses: Optional[list[WebhookEventStatus]] = None,
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

            result = api.list_webhook_events(
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

    def list_webhook_events_all(
        self,
        *,
        webhook_id: str,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListWebhookEventsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        email_id: Optional[str] = None,
        event_types: Optional[list[WebhookEventType]] = None,
        statuses: Optional[list[WebhookEventStatus]] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        domain_id: Optional[str] = None,
    ) -> list[WebhookEvent]:
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
        :return: :class:`list[WebhookEvent] <list[WebhookEvent]>`

        Usage:
        ::

            result = api.list_webhook_events_all(
                webhook_id="example",
            )
        """

        return fetch_all_pages(
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

    def get_project_settings(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> ProjectSettings:
        """
        List project settings.
        Retrieve the project settings including periodic reports.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the project.
        :return: :class:`ProjectSettings <ProjectSettings>`

        Usage:
        ::

            result = api.get_project_settings()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/project/{param_project_id}/settings",
        )

        self._throw_on_error(res)
        return unmarshal_ProjectSettings(res.json())

    def update_project_settings(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        periodic_report: Optional[
            UpdateProjectSettingsRequestUpdatePeriodicReport
        ] = None,
    ) -> ProjectSettings:
        """
        Update project settings.
        Update the project settings including periodic reports.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the project.
        :param periodic_report: Periodic report update details - all fields are optional.
        :return: :class:`ProjectSettings <ProjectSettings>`

        Usage:
        ::

            result = api.update_project_settings()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "PATCH",
            f"/transactional-email/v1alpha1/regions/{param_region}/project/{param_project_id}/settings",
            body=marshal_UpdateProjectSettingsRequest(
                UpdateProjectSettingsRequest(
                    region=region,
                    project_id=project_id,
                    periodic_report=periodic_report,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ProjectSettings(res.json())

    def list_blocklists(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListBlocklistsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        email: Optional[str] = None,
        type_: Optional[BlocklistType] = None,
        custom: Optional[bool] = None,
    ) -> ListBlocklistsResponse:
        """
        List blocklists.
        Retrieve the list of blocklists.
        :param domain_id: (Optional) Filter by a domain ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: (Optional) List blocklist corresponding to specific criteria.
        :param page: (Optional) Requested page number. Value must be greater or equal to 1.
        :param page_size: (Optional) Requested page size. Value must be between 1 and 100.
        :param email: (Optional) Filter by an email address.
        :param type_: (Optional) Filter by a blocklist type.
        :param custom: (Optional) Filter by custom blocklist (true) or automatic Transactional Email blocklist (false).
        :return: :class:`ListBlocklistsResponse <ListBlocklistsResponse>`

        Usage:
        ::

            result = api.list_blocklists(
                domain_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/blocklists",
            params={
                "custom": custom,
                "domain_id": domain_id,
                "email": email,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBlocklistsResponse(res.json())

    def list_blocklists_all(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListBlocklistsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        email: Optional[str] = None,
        type_: Optional[BlocklistType] = None,
        custom: Optional[bool] = None,
    ) -> list[Blocklist]:
        """
        List blocklists.
        Retrieve the list of blocklists.
        :param domain_id: (Optional) Filter by a domain ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: (Optional) List blocklist corresponding to specific criteria.
        :param page: (Optional) Requested page number. Value must be greater or equal to 1.
        :param page_size: (Optional) Requested page size. Value must be between 1 and 100.
        :param email: (Optional) Filter by an email address.
        :param type_: (Optional) Filter by a blocklist type.
        :param custom: (Optional) Filter by custom blocklist (true) or automatic Transactional Email blocklist (false).
        :return: :class:`list[Blocklist] <list[Blocklist]>`

        Usage:
        ::

            result = api.list_blocklists_all(
                domain_id="example",
            )
        """

        return fetch_all_pages(
            type=ListBlocklistsResponse,
            key="blocklists",
            fetcher=self.list_blocklists,
            args={
                "domain_id": domain_id,
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "email": email,
                "type_": type_,
                "custom": custom,
            },
        )

    def bulk_create_blocklists(
        self,
        *,
        domain_id: str,
        region: Optional[ScwRegion] = None,
        emails: Optional[list[str]] = None,
        type_: Optional[BlocklistType] = None,
        reason: Optional[str] = None,
    ) -> BulkCreateBlocklistsResponse:
        """
        Bulk create blocklists.
        Create multiple blocklists in a specific Project or Organization using the `region` parameter.
        :param domain_id: Domain ID linked to the blocklist.
        :param region: Region to target. If none is passed will use default region from the config.
        :param emails: Email blocked by the blocklist.
        :param type_: Type of blocklist.
        :param reason: Reason to block the email.
        :return: :class:`BulkCreateBlocklistsResponse <BulkCreateBlocklistsResponse>`

        Usage:
        ::

            result = api.bulk_create_blocklists(
                domain_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/blocklists",
            body=marshal_BulkCreateBlocklistsRequest(
                BulkCreateBlocklistsRequest(
                    domain_id=domain_id,
                    region=region,
                    emails=emails,
                    type_=type_,
                    reason=reason,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BulkCreateBlocklistsResponse(res.json())

    def delete_blocklist(
        self,
        *,
        blocklist_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a blocklist.
        You must specify the blocklist you want to delete by the `region` and `blocklist_id`.
        :param blocklist_id: ID of the blocklist to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_blocklist(
                blocklist_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_blocklist_id = validate_path_param("blocklist_id", blocklist_id)

        res = self._request(
            "DELETE",
            f"/transactional-email/v1alpha1/regions/{param_region}/blocklists/{param_blocklist_id}",
        )

        self._throw_on_error(res)

    def list_offer_subscriptions(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> ListOfferSubscriptionsResponse:
        """
        Get information about subscribed offers.
        Retrieve information about the offers you are subscribed to using the `project_id` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project.
        :return: :class:`ListOfferSubscriptionsResponse <ListOfferSubscriptionsResponse>`

        Usage:
        ::

            result = api.list_offer_subscriptions()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/offer-subscriptions",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOfferSubscriptionsResponse(res.json())

    def update_offer_subscription(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        name: Optional[OfferName] = None,
    ) -> OfferSubscription:
        """
        Update a subscribed offer.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project.
        :param name: Name of the offer-subscription.
        :return: :class:`OfferSubscription <OfferSubscription>`

        Usage:
        ::

            result = api.update_offer_subscription()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "PATCH",
            f"/transactional-email/v1alpha1/regions/{param_region}/offer-subscriptions",
            body=marshal_UpdateOfferSubscriptionRequest(
                UpdateOfferSubscriptionRequest(
                    region=region,
                    project_id=project_id,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_OfferSubscription(res.json())

    def list_offers(
        self,
        *,
        region: Optional[ScwRegion] = None,
    ) -> ListOffersResponse:
        """
        List the available offers.
        Retrieve the list of the available and free-of-charge offers you can subscribe to.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ListOffersResponse <ListOffersResponse>`

        Usage:
        ::

            result = api.list_offers()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/offers",
        )

        self._throw_on_error(res)
        return unmarshal_ListOffersResponse(res.json())

    def list_pools(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> ListPoolsResponse:
        """
        Get information about a sending pool.
        Retrieve information about a sending pool, including its creation status and configuration parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 1000.
        :param project_id: ID of the Project.
        :return: :class:`ListPoolsResponse <ListPoolsResponse>`

        Usage:
        ::

            result = api.list_pools()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/pools",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPoolsResponse(res.json())

    def list_pools_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> list[Pool]:
        """
        Get information about a sending pool.
        Retrieve information about a sending pool, including its creation status and configuration parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Requested page size. Value must be between 1 and 1000.
        :param project_id: ID of the Project.
        :return: :class:`list[Pool] <list[Pool]>`

        Usage:
        ::

            result = api.list_pools_all()
        """

        return fetch_all_pages(
            type=ListPoolsResponse,
            key="pools",
            fetcher=self.list_pools,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
            },
        )

    def get_project_consumption(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> ProjectConsumption:
        """
        Get project resource consumption.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the project.
        :return: :class:`ProjectConsumption <ProjectConsumption>`

        Usage:
        ::

            result = api.get_project_consumption()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/transactional-email/v1alpha1/regions/{param_region}/project-consumption",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ProjectConsumption(res.json())
