# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    ScwFile,
    unmarshal_ScwFile,
)
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages_async,
)
from .types import (
    ContractType,
    ListContractSignaturesRequestOrderBy,
    ListProjectsRequestOrderBy,
    CheckContractSignatureResponse,
    ContractApiCheckContractSignatureRequest,
    ContractApiCreateContractSignatureRequest,
    ContractSignature,
    ListContractSignaturesResponse,
    ListProjectsResponse,
    Project,
    ProjectApiCreateProjectRequest,
    ProjectApiSetProjectQualificationRequest,
    ProjectApiUpdateProjectRequest,
    ProjectQualification,
    Qualification,
)
from .marshalling import (
    unmarshal_ContractSignature,
    unmarshal_Project,
    unmarshal_CheckContractSignatureResponse,
    unmarshal_ListContractSignaturesResponse,
    unmarshal_ListProjectsResponse,
    unmarshal_ProjectQualification,
    marshal_ContractApiCheckContractSignatureRequest,
    marshal_ContractApiCreateContractSignatureRequest,
    marshal_ProjectApiCreateProjectRequest,
    marshal_ProjectApiSetProjectQualificationRequest,
    marshal_ProjectApiUpdateProjectRequest,
)
from ...std.types import (
    LanguageCode as StdLanguageCode,
)


class AccountV3ContractAPI(API):
    """
    The Contract API allows you to manage contracts.
    """

    async def download_contract_signature(
        self,
        *,
        contract_signature_id: str,
        locale: Optional[StdLanguageCode] = None,
    ) -> ScwFile:
        """
        Download a contract content.
        :param contract_signature_id: The contract signature ID.
        :param locale: The locale requested for the content of the contract.
        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = await api.download_contract_signature(
                contract_signature_id="example",
            )
        """

        param_contract_signature_id = validate_path_param(
            "contract_signature_id", contract_signature_id
        )

        res = self._request(
            "GET",
            f"/account/v3/contract-signatures/{param_contract_signature_id}/download",
            params={
                "locale": locale,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    async def create_contract_signature(
        self,
        *,
        contract_name: str,
        validated: bool,
        contract_type: Optional[ContractType] = None,
        organization_id: Optional[str] = None,
    ) -> ContractSignature:
        """
        Create a signature for your Organization for the latest version of the requested contract.
        :param contract_name: The name of the contract.
        :param validated: Whether the contract is validated at creation.
        :param contract_type: The type of the contract.
        :param organization_id: ID of the Organization.
        :return: :class:`ContractSignature <ContractSignature>`

        Usage:
        ::

            result = await api.create_contract_signature(
                contract_name="example",
                validated=False,
            )
        """

        res = self._request(
            "POST",
            "/account/v3/contract-signatures",
            body=marshal_ContractApiCreateContractSignatureRequest(
                ContractApiCreateContractSignatureRequest(
                    contract_name=contract_name,
                    validated=validated,
                    contract_type=contract_type,
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ContractSignature(res.json())

    async def validate_contract_signature(
        self,
        *,
        contract_signature_id: str,
    ) -> ContractSignature:
        """
        Sign a contract for your Organization.
        :param contract_signature_id: The contract linked to your Organization you want to sign.
        :return: :class:`ContractSignature <ContractSignature>`

        Usage:
        ::

            result = await api.validate_contract_signature(
                contract_signature_id="example",
            )
        """

        param_contract_signature_id = validate_path_param(
            "contract_signature_id", contract_signature_id
        )

        res = self._request(
            "POST",
            f"/account/v3/contract-signatures/{param_contract_signature_id}/validate",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_ContractSignature(res.json())

    async def check_contract_signature(
        self,
        *,
        contract_name: str,
        organization_id: Optional[str] = None,
        contract_type: Optional[ContractType] = None,
    ) -> CheckContractSignatureResponse:
        """
        Check if a contract is signed for your Organization.
        :param contract_name: Filter on contract name.
        :param organization_id: ID of the Organization to check the contract signature for.
        :param contract_type: Filter on contract type.
        :return: :class:`CheckContractSignatureResponse <CheckContractSignatureResponse>`

        Usage:
        ::

            result = await api.check_contract_signature(
                contract_name="example",
            )
        """

        res = self._request(
            "POST",
            "/account/v3/contract-signatures/check",
            body=marshal_ContractApiCheckContractSignatureRequest(
                ContractApiCheckContractSignatureRequest(
                    contract_name=contract_name,
                    organization_id=organization_id,
                    contract_type=contract_type,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CheckContractSignatureResponse(res.json())

    async def list_contract_signatures(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListContractSignaturesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
    ) -> ListContractSignaturesResponse:
        """
        List contract signatures for an Organization.
        :param page: The page number for the returned contracts.
        :param page_size: The maximum number of contracts per page.
        :param order_by: How the contracts are ordered in the response.
        :param organization_id: Filter on Organization ID.
        :return: :class:`ListContractSignaturesResponse <ListContractSignaturesResponse>`

        Usage:
        ::

            result = await api.list_contract_signatures()
        """

        res = self._request(
            "GET",
            "/account/v3/contract-signatures",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListContractSignaturesResponse(res.json())

    async def list_contract_signatures_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListContractSignaturesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
    ) -> list[ContractSignature]:
        """
        List contract signatures for an Organization.
        :param page: The page number for the returned contracts.
        :param page_size: The maximum number of contracts per page.
        :param order_by: How the contracts are ordered in the response.
        :param organization_id: Filter on Organization ID.
        :return: :class:`list[ContractSignature] <list[ContractSignature]>`

        Usage:
        ::

            result = await api.list_contract_signatures_all()
        """

        return await fetch_all_pages_async(
            type=ListContractSignaturesResponse,
            key="contract_signatures",
            fetcher=self.list_contract_signatures,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "organization_id": organization_id,
            },
        )


class AccountV3ProjectAPI(API):
    """
    This API allows you to manage your Scaleway Projects.
    """

    async def create_project(
        self,
        *,
        description: str,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> Project:
        """
        Create a new Project for an Organization.
        Generate a new Project for an Organization, specifying its configuration including name and description.
        :param description: Description of the Project.
        :param name: Name of the Project.
        :param organization_id: Organization ID of the Project.
        :return: :class:`Project <Project>`

        Usage:
        ::

            result = await api.create_project(
                description="example",
            )
        """

        res = self._request(
            "POST",
            "/account/v3/projects",
            body=marshal_ProjectApiCreateProjectRequest(
                ProjectApiCreateProjectRequest(
                    description=description,
                    name=name or random_name(prefix="proj"),
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Project(res.json())

    async def list_projects(
        self,
        *,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProjectsRequestOrderBy] = None,
        project_ids: Optional[list[str]] = None,
    ) -> ListProjectsResponse:
        """
        List all Projects of an Organization.
        List all Projects of an Organization. The response will include the total number of Projects as well as their associated Organizations, names, and IDs. Other information includes the creation and update date of the Project.
        :param organization_id: Organization ID of the Project.
        :param name: Name of the Project.
        :param page: Page number for the returned Projects.
        :param page_size: Maximum number of Project per page.
        :param order_by: Sort order of the returned Projects.
        :param project_ids: Project IDs to filter for. The results will be limited to any Projects with an ID in this array.
        :return: :class:`ListProjectsResponse <ListProjectsResponse>`

        Usage:
        ::

            result = await api.list_projects()
        """

        res = self._request(
            "GET",
            "/account/v3/projects",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_ids": project_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListProjectsResponse(res.json())

    async def list_projects_all(
        self,
        *,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProjectsRequestOrderBy] = None,
        project_ids: Optional[list[str]] = None,
    ) -> list[Project]:
        """
        List all Projects of an Organization.
        List all Projects of an Organization. The response will include the total number of Projects as well as their associated Organizations, names, and IDs. Other information includes the creation and update date of the Project.
        :param organization_id: Organization ID of the Project.
        :param name: Name of the Project.
        :param page: Page number for the returned Projects.
        :param page_size: Maximum number of Project per page.
        :param order_by: Sort order of the returned Projects.
        :param project_ids: Project IDs to filter for. The results will be limited to any Projects with an ID in this array.
        :return: :class:`list[Project] <list[Project]>`

        Usage:
        ::

            result = await api.list_projects_all()
        """

        return await fetch_all_pages_async(
            type=ListProjectsResponse,
            key="projects",
            fetcher=self.list_projects,
            args={
                "organization_id": organization_id,
                "name": name,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_ids": project_ids,
            },
        )

    async def get_project(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Project:
        """
        Get an existing Project.
        Retrieve information about an existing Project, specified by its Project ID. Its full details, including ID, name and description, are returned in the response object.
        :param project_id: Project ID of the Project.
        :return: :class:`Project <Project>`

        Usage:
        ::

            result = await api.get_project()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "GET",
            f"/account/v3/projects/{param_project_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Project(res.json())

    async def delete_project(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> None:
        """
        Delete an existing Project.
        Delete an existing Project, specified by its Project ID. The Project needs to be empty (meaning there are no resources left in it) to be deleted effectively. Note that deleting a Project is permanent, and cannot be undone.
        :param project_id: Project ID of the Project.

        Usage:
        ::

            result = await api.delete_project()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "DELETE",
            f"/account/v3/projects/{param_project_id}",
        )

        self._throw_on_error(res)

    async def update_project(
        self,
        *,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Project:
        """
        Update Project.
        Update the parameters of an existing Project, specified by its Project ID. These parameters include the name and description.
        :param project_id: Project ID of the Project.
        :param name: Name of the Project.
        :param description: Description of the Project.
        :return: :class:`Project <Project>`

        Usage:
        ::

            result = await api.update_project()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "PATCH",
            f"/account/v3/projects/{param_project_id}",
            body=marshal_ProjectApiUpdateProjectRequest(
                ProjectApiUpdateProjectRequest(
                    project_id=project_id,
                    name=name,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Project(res.json())

    async def set_project_qualification(
        self,
        *,
        project_id: Optional[str] = None,
        qualification: Optional[Qualification] = None,
    ) -> ProjectQualification:
        """
        Set project use case.
        Set the project use case for a new or existing Project, specified by its Project ID. You can customize the use case, sub use case, and architecture type you want to use in the Project.
        :param project_id: Project ID.
        :param qualification: Use case chosen for the Project.
        :return: :class:`ProjectQualification <ProjectQualification>`

        Usage:
        ::

            result = await api.set_project_qualification()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "POST",
            f"/account/v3/projects/{param_project_id}/project-qualification",
            body=marshal_ProjectApiSetProjectQualificationRequest(
                ProjectApiSetProjectQualificationRequest(
                    project_id=project_id,
                    qualification=qualification,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ProjectQualification(res.json())
