# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

from scaleway_core.utils import (
    StrEnumMeta,
)

from ...std.types import (
    LanguageCode as StdLanguageCode,
)


class ContractType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    GLOBAL = "global"
    K8S = "k8s"
    INSTANCE = "instance"
    CONTAINER = "container"
    BAREMETAL = "baremetal"

    def __str__(self) -> str:
        return str(self.value)


class ListContractSignaturesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    SIGNED_AT_ASC = "signed_at_asc"
    SIGNED_AT_DESC = "signed_at_desc"
    EXPIRES_AT_ASC = "expires_at_asc"
    EXPIRES_AT_DESC = "expires_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListProjectsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Contract:
    id: str
    """
    ID of the contract.
    """

    type_: ContractType
    """
    The type of the contract.
    """

    name: str
    """
    The name of the contract.
    """

    version: int
    """
    The version of the contract.
    """

    created_at: Optional[datetime]
    """
    The creation date of the contract.
    """

    updated_at: Optional[datetime]
    """
    The last modification date of the contract.
    """


@dataclass
class ContractSignature:
    id: str
    """
    ID of the contract signature.
    """

    organization_id: str
    """
    The Organization ID which signed the contract.
    """

    created_at: Optional[datetime]
    """
    The creation date of the contract signature.
    """

    signed_at: Optional[datetime]
    """
    The signing date of the contract signature.
    """

    expires_at: Optional[datetime]
    """
    The expiration date of the contract signature.
    """

    contract: Optional[Contract]
    """
    The contract signed.
    """


@dataclass
class Project:
    id: str
    """
    ID of the Project.
    """

    name: str
    """
    Name of the Project.
    """

    organization_id: str
    """
    Organization ID of the Project.
    """

    description: str
    """
    Description of the Project.
    """

    created_at: Optional[datetime]
    """
    Creation date of the Project.
    """

    updated_at: Optional[datetime]
    """
    Update date of the Project.
    """


@dataclass
class CheckContractSignatureResponse:
    created: bool
    """
    Whether a signature has been requested for this contract.
    """

    validated: bool
    """
    Whether the signature for this contract has been validated.
    """


@dataclass
class ContractApiCheckContractSignatureRequest:
    contract_name: str
    """
    Filter on contract name.
    """

    organization_id: Optional[str]
    """
    ID of the Organization to check the contract signature for.
    """

    contract_type: Optional[ContractType]
    """
    Filter on contract type.
    """


@dataclass
class ContractApiCreateContractSignatureRequest:
    contract_name: str
    """
    The name of the contract.
    """

    validated: bool
    """
    Whether the contract is validated at creation.
    """

    contract_type: Optional[ContractType]
    """
    The type of the contract.
    """

    organization_id: Optional[str]
    """
    ID of the Organization.
    """


@dataclass
class ContractApiDownloadContractSignatureRequest:
    contract_signature_id: str
    """
    The contract signature ID.
    """

    locale: Optional[StdLanguageCode]
    """
    The locale requested for the content of the contract.
    """


@dataclass
class ContractApiListContractSignaturesRequest:
    page: Optional[int]
    """
    The page number for the returned contracts.
    """

    page_size: Optional[int]
    """
    The maximum number of contracts per page.
    """

    order_by: Optional[ListContractSignaturesRequestOrderBy]
    """
    How the contracts are ordered in the response.
    """

    organization_id: Optional[str]
    """
    Filter on Organization ID.
    """


@dataclass
class ContractApiValidateContractSignatureRequest:
    contract_signature_id: str
    """
    The contract linked to your Organization you want to sign.
    """


@dataclass
class ListContractSignaturesResponse:
    total_count: int
    """
    The total number of contract signatures.
    """

    contract_signatures: List[ContractSignature]
    """
    The paginated returned contract signatures.
    """


@dataclass
class ListProjectsResponse:
    total_count: int
    """
    Total number of Projects.
    """

    projects: List[Project]
    """
    Paginated returned Projects.
    """


@dataclass
class ProjectApiCreateProjectRequest:
    description: str
    """
    Description of the Project.
    """

    name: Optional[str]
    """
    Name of the Project.
    """

    organization_id: Optional[str]
    """
    Organization ID of the Project.
    """


@dataclass
class ProjectApiDeleteProjectRequest:
    project_id: Optional[str]
    """
    Project ID of the Project.
    """


@dataclass
class ProjectApiGetProjectRequest:
    project_id: Optional[str]
    """
    Project ID of the Project.
    """


@dataclass
class ProjectApiListProjectsRequest:
    organization_id: Optional[str]
    """
    Organization ID of the Project.
    """

    name: Optional[str]
    """
    Name of the Project.
    """

    page: Optional[int]
    """
    Page number for the returned Projects.
    """

    page_size: Optional[int]
    """
    Maximum number of Project per page.
    """

    order_by: Optional[ListProjectsRequestOrderBy]
    """
    Sort order of the returned Projects.
    """

    project_ids: Optional[List[str]]
    """
    Project IDs to filter for. The results will be limited to any Projects with an ID in this array.
    """


@dataclass
class ProjectApiUpdateProjectRequest:
    project_id: Optional[str]
    """
    Project ID of the Project.
    """

    name: Optional[str]
    """
    Name of the Project.
    """

    description: Optional[str]
    """
    Description of the Project.
    """
