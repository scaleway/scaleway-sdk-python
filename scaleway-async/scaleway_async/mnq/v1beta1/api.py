# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    ListNatsAccountsRequestOrderBy,
    ListNatsCredentialsRequestOrderBy,
    ListSnsCredentialsRequestOrderBy,
    ListSqsCredentialsRequestOrderBy,
    ListNatsAccountsResponse,
    ListNatsCredentialsResponse,
    ListSnsCredentialsResponse,
    ListSqsCredentialsResponse,
    NatsAccount,
    NatsApiCreateNatsAccountRequest,
    NatsApiCreateNatsCredentialsRequest,
    NatsApiUpdateNatsAccountRequest,
    NatsCredentials,
    SnsApiActivateSnsRequest,
    SnsApiCreateSnsCredentialsRequest,
    SnsApiDeactivateSnsRequest,
    SnsApiUpdateSnsCredentialsRequest,
    SnsCredentials,
    SnsInfo,
    SnsPermissions,
    SqsApiActivateSqsRequest,
    SqsApiCreateSqsCredentialsRequest,
    SqsApiDeactivateSqsRequest,
    SqsApiUpdateSqsCredentialsRequest,
    SqsCredentials,
    SqsInfo,
    SqsPermissions,
)
from .marshalling import (
    unmarshal_NatsAccount,
    unmarshal_NatsCredentials,
    unmarshal_SnsCredentials,
    unmarshal_SqsCredentials,
    unmarshal_ListNatsAccountsResponse,
    unmarshal_ListNatsCredentialsResponse,
    unmarshal_ListSnsCredentialsResponse,
    unmarshal_ListSqsCredentialsResponse,
    unmarshal_SnsInfo,
    unmarshal_SqsInfo,
    marshal_NatsApiCreateNatsAccountRequest,
    marshal_NatsApiCreateNatsCredentialsRequest,
    marshal_NatsApiUpdateNatsAccountRequest,
    marshal_SnsApiActivateSnsRequest,
    marshal_SnsApiCreateSnsCredentialsRequest,
    marshal_SnsApiDeactivateSnsRequest,
    marshal_SnsApiUpdateSnsCredentialsRequest,
    marshal_SqsApiActivateSqsRequest,
    marshal_SqsApiCreateSqsCredentialsRequest,
    marshal_SqsApiDeactivateSqsRequest,
    marshal_SqsApiUpdateSqsCredentialsRequest,
)


class MnqV1Beta1NatsAPI(API):
    """
    This API allows you to manage Scaleway Messaging and Queuing NATS accounts.
    """

    async def create_nats_account(
        self,
        *,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> NatsAccount:
        """
        Create a NATS account.
        Create a NATS account associated with a Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: NATS account name.
        :param project_id: Project containing the NATS account.
        :return: :class:`NatsAccount <NatsAccount>`

        Usage:
        ::

            result = await api.create_nats_account()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/nats-accounts",
            body=marshal_NatsApiCreateNatsAccountRequest(
                NatsApiCreateNatsAccountRequest(
                    region=region,
                    name=name or random_name(prefix="mnq"),
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_NatsAccount(res.json())

    async def delete_nats_account(
        self,
        *,
        nats_account_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete a NATS account.
        Delete a NATS account, specified by its NATS account ID. Note that deleting a NATS account is irreversible, and any credentials, streams, consumer and stored messages belonging to this NATS account will also be deleted.
        :param nats_account_id: ID of the NATS account to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_nats_account(
                nats_account_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_nats_account_id = validate_path_param("nats_account_id", nats_account_id)

        res = self._request(
            "DELETE",
            f"/mnq/v1beta1/regions/{param_region}/nats-accounts/{param_nats_account_id}",
        )

        self._throw_on_error(res)

    async def update_nats_account(
        self,
        *,
        nats_account_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
    ) -> NatsAccount:
        """
        Update the name of a NATS account.
        Update the name of a NATS account, specified by its NATS account ID.
        :param nats_account_id: ID of the NATS account to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: NATS account name.
        :return: :class:`NatsAccount <NatsAccount>`

        Usage:
        ::

            result = await api.update_nats_account(
                nats_account_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_nats_account_id = validate_path_param("nats_account_id", nats_account_id)

        res = self._request(
            "PATCH",
            f"/mnq/v1beta1/regions/{param_region}/nats-accounts/{param_nats_account_id}",
            body=marshal_NatsApiUpdateNatsAccountRequest(
                NatsApiUpdateNatsAccountRequest(
                    nats_account_id=nats_account_id,
                    region=region,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_NatsAccount(res.json())

    async def get_nats_account(
        self,
        *,
        nats_account_id: str,
        region: Optional[Region] = None,
    ) -> NatsAccount:
        """
        Get a NATS account.
        Retrieve information about an existing NATS account identified by its NATS account ID. Its full details, including name and endpoint, are returned in the response.
        :param nats_account_id: ID of the NATS account to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`NatsAccount <NatsAccount>`

        Usage:
        ::

            result = await api.get_nats_account(
                nats_account_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_nats_account_id = validate_path_param("nats_account_id", nats_account_id)

        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/nats-accounts/{param_nats_account_id}",
        )

        self._throw_on_error(res)
        return unmarshal_NatsAccount(res.json())

    async def list_nats_accounts(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNatsAccountsRequestOrderBy] = None,
    ) -> ListNatsAccountsResponse:
        """
        List NATS accounts.
        List all NATS accounts in the specified region, for a Scaleway Organization or Project. By default, the NATS accounts returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only NATS accounts in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of NATS accounts to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListNatsAccountsResponse <ListNatsAccountsResponse>`

        Usage:
        ::

            result = await api.list_nats_accounts()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/nats-accounts",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNatsAccountsResponse(res.json())

    async def list_nats_accounts_all(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNatsAccountsRequestOrderBy] = None,
    ) -> List[NatsAccount]:
        """
        List NATS accounts.
        List all NATS accounts in the specified region, for a Scaleway Organization or Project. By default, the NATS accounts returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only NATS accounts in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of NATS accounts to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`List[NatsAccount] <List[NatsAccount]>`

        Usage:
        ::

            result = await api.list_nats_accounts_all()
        """

        return await fetch_all_pages_async(
            type=ListNatsAccountsResponse,
            key="nats_accounts",
            fetcher=self.list_nats_accounts,
            args={
                "region": region,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def create_nats_credentials(
        self,
        *,
        nats_account_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
    ) -> NatsCredentials:
        """
        Create NATS credentials.
        Create a set of credentials for a NATS account, specified by its NATS account ID.
        :param nats_account_id: NATS account containing the credentials.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the credentials.
        :return: :class:`NatsCredentials <NatsCredentials>`

        Usage:
        ::

            result = await api.create_nats_credentials(
                nats_account_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/nats-credentials",
            body=marshal_NatsApiCreateNatsCredentialsRequest(
                NatsApiCreateNatsCredentialsRequest(
                    nats_account_id=nats_account_id,
                    region=region,
                    name=name or random_name(prefix="mnq"),
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_NatsCredentials(res.json())

    async def delete_nats_credentials(
        self,
        *,
        nats_credentials_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete NATS credentials.
        Delete a set of credentials, specified by their credentials ID. Deleting credentials is irreversible and cannot be undone. The credentials can no longer be used to access the NATS account, and active connections using this credentials will be closed.
        :param nats_credentials_id: ID of the credentials to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_nats_credentials(
                nats_credentials_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_nats_credentials_id = validate_path_param(
            "nats_credentials_id", nats_credentials_id
        )

        res = self._request(
            "DELETE",
            f"/mnq/v1beta1/regions/{param_region}/nats-credentials/{param_nats_credentials_id}",
        )

        self._throw_on_error(res)

    async def get_nats_credentials(
        self,
        *,
        nats_credentials_id: str,
        region: Optional[Region] = None,
    ) -> NatsCredentials:
        """
        Get NATS credentials.
        Retrieve an existing set of credentials, identified by the `nats_credentials_id`. The credentials themselves are NOT returned, only their metadata (NATS account ID, credentials name, etc), are returned in the response.
        :param nats_credentials_id: ID of the credentials to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`NatsCredentials <NatsCredentials>`

        Usage:
        ::

            result = await api.get_nats_credentials(
                nats_credentials_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_nats_credentials_id = validate_path_param(
            "nats_credentials_id", nats_credentials_id
        )

        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/nats-credentials/{param_nats_credentials_id}",
        )

        self._throw_on_error(res)
        return unmarshal_NatsCredentials(res.json())

    async def list_nats_credentials(
        self,
        *,
        region: Optional[Region] = None,
        nats_account_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNatsCredentialsRequestOrderBy] = None,
    ) -> ListNatsCredentialsResponse:
        """
        List NATS credentials.
        List existing credentials in the specified NATS account. The response contains only the metadata for the credentials, not the credentials themselves, which are only returned after a **Create Credentials** call.
        :param region: Region to target. If none is passed will use default region from the config.
        :param nats_account_id: Include only credentials for this NATS account.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListNatsCredentialsResponse <ListNatsCredentialsResponse>`

        Usage:
        ::

            result = await api.list_nats_credentials()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/nats-credentials",
            params={
                "nats_account_id": nats_account_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNatsCredentialsResponse(res.json())

    async def list_nats_credentials_all(
        self,
        *,
        region: Optional[Region] = None,
        nats_account_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNatsCredentialsRequestOrderBy] = None,
    ) -> List[NatsCredentials]:
        """
        List NATS credentials.
        List existing credentials in the specified NATS account. The response contains only the metadata for the credentials, not the credentials themselves, which are only returned after a **Create Credentials** call.
        :param region: Region to target. If none is passed will use default region from the config.
        :param nats_account_id: Include only credentials for this NATS account.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`List[NatsCredentials] <List[NatsCredentials]>`

        Usage:
        ::

            result = await api.list_nats_credentials_all()
        """

        return await fetch_all_pages_async(
            type=ListNatsCredentialsResponse,
            key="nats_credentials",
            fetcher=self.list_nats_credentials,
            args={
                "region": region,
                "nats_account_id": nats_account_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )


class MnqV1Beta1SnsAPI(API):
    """
    This API allows you to manage your Scaleway Messaging and Queuing SNS brokers.
    """

    async def activate_sns(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> SnsInfo:
        """
        Activate SNS.
        Activate SNS for the specified Project ID. SNS must be activated before any usage. Activating SNS does not trigger any billing, and you can deactivate at any time.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project on which to activate the SNS service.
        :return: :class:`SnsInfo <SnsInfo>`

        Usage:
        ::

            result = await api.activate_sns()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/activate-sns",
            body=marshal_SnsApiActivateSnsRequest(
                SnsApiActivateSnsRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SnsInfo(res.json())

    async def get_sns_info(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> SnsInfo:
        """
        Get SNS info.
        Retrieve the SNS information of the specified Project ID. Informations include the activation status and the SNS API endpoint URL.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project to retrieve SNS info from.
        :return: :class:`SnsInfo <SnsInfo>`

        Usage:
        ::

            result = await api.get_sns_info()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sns-info",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_SnsInfo(res.json())

    async def deactivate_sns(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> SnsInfo:
        """
        Deactivate SNS.
        Deactivate SNS for the specified Project ID.You must delete all topics and credentials before this call or you need to set the force_delete parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project on which to deactivate the SNS service.
        :return: :class:`SnsInfo <SnsInfo>`

        Usage:
        ::

            result = await api.deactivate_sns()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/deactivate-sns",
            body=marshal_SnsApiDeactivateSnsRequest(
                SnsApiDeactivateSnsRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SnsInfo(res.json())

    async def create_sns_credentials(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        permissions: Optional[SnsPermissions] = None,
    ) -> SnsCredentials:
        """
        Create SNS credentials.
        Create a set of credentials for SNS, specified by a Project ID. Credentials give the bearer access to topics, and the level of permissions can be defined granularly.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project containing the SNS credentials.
        :param name: Name of the credentials.
        :param permissions: Permissions associated with these credentials.
        :return: :class:`SnsCredentials <SnsCredentials>`

        Usage:
        ::

            result = await api.create_sns_credentials()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/sns-credentials",
            body=marshal_SnsApiCreateSnsCredentialsRequest(
                SnsApiCreateSnsCredentialsRequest(
                    region=region,
                    project_id=project_id,
                    name=name or random_name(prefix="mnq_sns"),
                    permissions=permissions,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SnsCredentials(res.json())

    async def delete_sns_credentials(
        self,
        *,
        sns_credentials_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete SNS credentials.
        Delete a set of SNS credentials, specified by their credentials ID. Deleting credentials is irreversible and cannot be undone. The credentials can then no longer be used to access SNS.
        :param sns_credentials_id: ID of the credentials to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_sns_credentials(
                sns_credentials_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_sns_credentials_id = validate_path_param(
            "sns_credentials_id", sns_credentials_id
        )

        res = self._request(
            "DELETE",
            f"/mnq/v1beta1/regions/{param_region}/sns-credentials/{param_sns_credentials_id}",
        )

        self._throw_on_error(res)

    async def update_sns_credentials(
        self,
        *,
        sns_credentials_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        permissions: Optional[SnsPermissions] = None,
    ) -> SnsCredentials:
        """
        Update SNS credentials.
        Update a set of SNS credentials. You can update the credentials' name, or their permissions.
        :param sns_credentials_id: ID of the SNS credentials to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the credentials.
        :param permissions: Permissions associated with these credentials.
        :return: :class:`SnsCredentials <SnsCredentials>`

        Usage:
        ::

            result = await api.update_sns_credentials(
                sns_credentials_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_sns_credentials_id = validate_path_param(
            "sns_credentials_id", sns_credentials_id
        )

        res = self._request(
            "PATCH",
            f"/mnq/v1beta1/regions/{param_region}/sns-credentials/{param_sns_credentials_id}",
            body=marshal_SnsApiUpdateSnsCredentialsRequest(
                SnsApiUpdateSnsCredentialsRequest(
                    sns_credentials_id=sns_credentials_id,
                    region=region,
                    name=name,
                    permissions=permissions,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SnsCredentials(res.json())

    async def get_sns_credentials(
        self,
        *,
        sns_credentials_id: str,
        region: Optional[Region] = None,
    ) -> SnsCredentials:
        """
        Get SNS credentials.
        Retrieve an existing set of credentials, identified by the `credentials_id`. The credentials themselves, as well as their metadata (name, project ID etc), are returned in the response.
        :param sns_credentials_id: ID of the SNS credentials to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SnsCredentials <SnsCredentials>`

        Usage:
        ::

            result = await api.get_sns_credentials(
                sns_credentials_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_sns_credentials_id = validate_path_param(
            "sns_credentials_id", sns_credentials_id
        )

        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sns-credentials/{param_sns_credentials_id}",
        )

        self._throw_on_error(res)
        return unmarshal_SnsCredentials(res.json())

    async def list_sns_credentials(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSnsCredentialsRequestOrderBy] = None,
    ) -> ListSnsCredentialsResponse:
        """
        List SNS credentials.
        List existing SNS credentials in the specified region. The response contains only the metadata for the credentials, not the credentials themselves.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only SNS credentials in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListSnsCredentialsResponse <ListSnsCredentialsResponse>`

        Usage:
        ::

            result = await api.list_sns_credentials()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sns-credentials",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSnsCredentialsResponse(res.json())

    async def list_sns_credentials_all(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSnsCredentialsRequestOrderBy] = None,
    ) -> List[SnsCredentials]:
        """
        List SNS credentials.
        List existing SNS credentials in the specified region. The response contains only the metadata for the credentials, not the credentials themselves.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only SNS credentials in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`List[SnsCredentials] <List[SnsCredentials]>`

        Usage:
        ::

            result = await api.list_sns_credentials_all()
        """

        return await fetch_all_pages_async(
            type=ListSnsCredentialsResponse,
            key="sns_credentials",
            fetcher=self.list_sns_credentials,
            args={
                "region": region,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )


class MnqV1Beta1SqsAPI(API):
    """
    This API allows you to manage your Scaleway Messaging and Queuing SQS brokers.
    """

    async def activate_sqs(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> SqsInfo:
        """
        Activate SQS.
        Activate SQS for the specified Project ID. SQS must be activated before any usage such as creating credentials and queues. Activating SQS does not trigger any billing, and you can deactivate at any time.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project on which to activate the SQS service.
        :return: :class:`SqsInfo <SqsInfo>`

        Usage:
        ::

            result = await api.activate_sqs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/activate-sqs",
            body=marshal_SqsApiActivateSqsRequest(
                SqsApiActivateSqsRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SqsInfo(res.json())

    async def get_sqs_info(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> SqsInfo:
        """
        Get SQS info.
        Retrieve the SQS information of the specified Project ID. Informations include the activation status and the SQS API endpoint URL.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project to retrieve SQS info from.
        :return: :class:`SqsInfo <SqsInfo>`

        Usage:
        ::

            result = await api.get_sqs_info()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sqs-info",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_SqsInfo(res.json())

    async def deactivate_sqs(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> SqsInfo:
        """
        Deactivate SQS.
        Deactivate SQS for the specified Project ID. You must delete all queues and credentials before this call or you need to set the force_delete parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project on which to deactivate the SQS service.
        :return: :class:`SqsInfo <SqsInfo>`

        Usage:
        ::

            result = await api.deactivate_sqs()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/deactivate-sqs",
            body=marshal_SqsApiDeactivateSqsRequest(
                SqsApiDeactivateSqsRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SqsInfo(res.json())

    async def create_sqs_credentials(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        permissions: Optional[SqsPermissions] = None,
    ) -> SqsCredentials:
        """
        Create SQS credentials.
        Create a set of credentials for SQS, specified by a Project ID. Credentials give the bearer access to queues, and the level of permissions can be defined granularly.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project containing the SQS credentials.
        :param name: Name of the credentials.
        :param permissions: Permissions associated with these credentials.
        :return: :class:`SqsCredentials <SqsCredentials>`

        Usage:
        ::

            result = await api.create_sqs_credentials()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/sqs-credentials",
            body=marshal_SqsApiCreateSqsCredentialsRequest(
                SqsApiCreateSqsCredentialsRequest(
                    region=region,
                    project_id=project_id,
                    name=name or random_name(prefix="mnq_sqs"),
                    permissions=permissions,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SqsCredentials(res.json())

    async def delete_sqs_credentials(
        self,
        *,
        sqs_credentials_id: str,
        region: Optional[Region] = None,
    ) -> None:
        """
        Delete SQS credentials.
        Delete a set of SQS credentials, specified by their credentials ID. Deleting credentials is irreversible and cannot be undone. The credentials can then no longer be used to access SQS.
        :param sqs_credentials_id: ID of the credentials to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = await api.delete_sqs_credentials(
                sqs_credentials_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_sqs_credentials_id = validate_path_param(
            "sqs_credentials_id", sqs_credentials_id
        )

        res = self._request(
            "DELETE",
            f"/mnq/v1beta1/regions/{param_region}/sqs-credentials/{param_sqs_credentials_id}",
        )

        self._throw_on_error(res)

    async def update_sqs_credentials(
        self,
        *,
        sqs_credentials_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        permissions: Optional[SqsPermissions] = None,
    ) -> SqsCredentials:
        """
        Update SQS credentials.
        Update a set of SQS credentials. You can update the credentials' name, or their permissions.
        :param sqs_credentials_id: ID of the SQS credentials to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the credentials.
        :param permissions: Permissions associated with these credentials.
        :return: :class:`SqsCredentials <SqsCredentials>`

        Usage:
        ::

            result = await api.update_sqs_credentials(
                sqs_credentials_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_sqs_credentials_id = validate_path_param(
            "sqs_credentials_id", sqs_credentials_id
        )

        res = self._request(
            "PATCH",
            f"/mnq/v1beta1/regions/{param_region}/sqs-credentials/{param_sqs_credentials_id}",
            body=marshal_SqsApiUpdateSqsCredentialsRequest(
                SqsApiUpdateSqsCredentialsRequest(
                    sqs_credentials_id=sqs_credentials_id,
                    region=region,
                    name=name,
                    permissions=permissions,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SqsCredentials(res.json())

    async def get_sqs_credentials(
        self,
        *,
        sqs_credentials_id: str,
        region: Optional[Region] = None,
    ) -> SqsCredentials:
        """
        Get SQS credentials.
        Retrieve an existing set of credentials, identified by the `credentials_id`. The credentials themselves, as well as their metadata (name, project ID etc), are returned in the response.
        :param sqs_credentials_id: ID of the SQS credentials to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SqsCredentials <SqsCredentials>`

        Usage:
        ::

            result = await api.get_sqs_credentials(
                sqs_credentials_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_sqs_credentials_id = validate_path_param(
            "sqs_credentials_id", sqs_credentials_id
        )

        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sqs-credentials/{param_sqs_credentials_id}",
        )

        self._throw_on_error(res)
        return unmarshal_SqsCredentials(res.json())

    async def list_sqs_credentials(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSqsCredentialsRequestOrderBy] = None,
    ) -> ListSqsCredentialsResponse:
        """
        List SQS credentials.
        List existing SQS credentials in the specified region. The response contains only the metadata for the credentials, not the credentials themselves.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only SQS credentials in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListSqsCredentialsResponse <ListSqsCredentialsResponse>`

        Usage:
        ::

            result = await api.list_sqs_credentials()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sqs-credentials",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSqsCredentialsResponse(res.json())

    async def list_sqs_credentials_all(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSqsCredentialsRequestOrderBy] = None,
    ) -> List[SqsCredentials]:
        """
        List SQS credentials.
        List existing SQS credentials in the specified region. The response contains only the metadata for the credentials, not the credentials themselves.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only SQS credentials in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`List[SqsCredentials] <List[SqsCredentials]>`

        Usage:
        ::

            result = await api.list_sqs_credentials_all()
        """

        return await fetch_all_pages_async(
            type=ListSqsCredentialsResponse,
            key="sqs_credentials",
            fetcher=self.list_sqs_credentials,
            args={
                "region": region,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
