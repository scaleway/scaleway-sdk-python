# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages,
    validate_path_param,
    wait_for_resource,
)
from .types import (
    DomainStatus,
    EmailStatus,
    ListEmailsRequestOrderBy,
    CreateEmailRequestAddress,
    CreateEmailRequestAttachment,
    CreateEmailResponse,
    Domain,
    DomainLastStatus,
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
    unmarshal_DomainLastStatus,
    unmarshal_ListDomainsResponse,
    unmarshal_ListEmailsResponse,
    unmarshal_Statistics,
)


class TemV1Alpha1API(API):
    """
    Transactional Email API.

    Transactional Email API.
    """

    def create_email(
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
        Send an email.
        You must specify the `region`, the sender and the recipient's information and the `project_id` to send an email from a checked domain. The subject of the email must contain at least 6 characters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param from_: Sender information. Must be from a checked domain declared in the Project.
        :param to: An array of the primary recipient's information.
        :param cc: An array of the carbon copy recipient's information.
        :param bcc: An array of the blind carbon copy recipient's information.
        :param subject: Subject of the email.
        :param text: Text content.
        :param html: HTML content.
        :param project_id: ID of the Project in which to create the email.
        :param attachments: Array of attachments.
        :param send_before: Maximum date to deliver the email.
        :return: :class:`CreateEmailResponse <CreateEmailResponse>`

        Usage:
        ::

            result = api.create_email(
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

    def get_email(
        self,
        *,
        email_id: str,
        region: Optional[Region] = None,
    ) -> Email:
        """
        Get an email.
        Retrieve information about a specific email using the `email_id` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param email_id: ID of the email to retrieve.
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = api.get_email(email_id="example")
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
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Email, bool]] = None,
    ) -> Email:
        """
        Waits for :class:`Email <Email>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param email_id: ID of the email to retrieve.
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
        order_by: ListEmailsRequestOrderBy = ListEmailsRequestOrderBy.CREATED_AT_DESC,
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
        :return: :class:`List[ListEmailsResponse] <List[ListEmailsResponse]>`

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
            },
        )

    def get_statistics(
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
        region: Optional[Region] = None,
    ) -> Email:
        """
        Cancel an email.
        You can cancel the sending of an email if it has not been sent yet. You must specify the `region` and the `email_id` of the email you want to cancel.
        :param region: Region to target. If none is passed will use default region from the config.
        :param email_id: ID of the email to cancel.
        :return: :class:`Email <Email>`

        Usage:
        ::

            result = api.cancel_email(email_id="example")
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

    def create_domain(
        self,
        *,
        domain_name: str,
        accept_tos: bool,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> Domain:
        """
        Register a domain in a project.
        You must specify the `region`, `project_id` and `domain_name` to register a domain in a specific Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the project to which the domain belongs.
        :param domain_name: Fully qualified domain dame.
        :param accept_tos: Accept Scaleway's Terms of Service.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.create_domain(
                domain_name="example",
                accept_tos=True,
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
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Get information about a domain.
        Retrieve information about a specific domain using the `region` and `domain_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param domain_id: ID of the domain.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.get_domain(domain_id="example")
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
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Domain, bool]] = None,
    ) -> Domain:
        """
        Waits for :class:`Domain <Domain>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param domain_id: ID of the domain.
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
        Retrieve domains in a specific project or in a specific Organization using the `region` parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Page size.
        :param project_id:
        :param status:
        :param organization_id:
        :param name:
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
        Retrieve domains in a specific project or in a specific Organization using the `region` parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Requested page number. Value must be greater or equal to 1.
        :param page_size: Page size.
        :param project_id:
        :param status:
        :param organization_id:
        :param name:
        :return: :class:`List[ListDomainsResponse] <List[ListDomainsResponse]>`

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
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Delete a domain.
        You must specify the domain you want to delete by the `region` and `domain_id`. Deleting a domain is permanent and cannot be undone.
        :param region: Region to target. If none is passed will use default region from the config.
        :param domain_id: ID of the domain to delete.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.revoke_domain(domain_id="example")
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

    def check_domain(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
    ) -> Domain:
        """
        Domain DNS check.
        Perform an immediate DNS check of a domain using the `region` and `domain_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param domain_id: ID of the domain to check.
        :return: :class:`Domain <Domain>`

        Usage:
        ::

            result = api.check_domain(domain_id="example")
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

    def check_domain_last_status(
        self,
        *,
        domain_id: str,
        region: Optional[Region] = None,
    ) -> DomainLastStatus:
        """
        Display SPF and DKIM records status and potential errors.
        Display SPF and DKIM records status and potential errors, including the found records to make debugging easier.
        :param region: Region to target. If none is passed will use default region from the config.
        :param domain_id: ID of the domain to delete.
        :return: :class:`DomainLastStatus <DomainLastStatus>`

        Usage:
        ::

            result = api.check_domain_last_status(domain_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_domain_id = validate_path_param("domain_id", domain_id)

        res = self._request(
            "POST",
            f"/transactional-email/v1alpha1/regions/{param_region}/domains/{param_domain_id}/verification",
        )

        self._throw_on_error(res)
        return unmarshal_DomainLastStatus(res.json())
