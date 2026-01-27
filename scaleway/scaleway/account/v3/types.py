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
    NETWORK = "network"
    CORE = "core"

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


class QualificationAiMachineSubUseCase(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUB_USE_CASE = "unknown_sub_use_case"

    def __str__(self) -> str:
        return str(self.value)


class QualificationArchitectureType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ARCHITECTURE_TYPE = "unknown_architecture_type"
    OBJECT_STORAGE = "object_storage"
    WEB_HOSTING = "web_hosting"
    INSTANCE = "instance"
    ELASTIC = "elastic"
    KUBERNETES = "kubernetes"
    SERVERLESS = "serverless"
    DEDICATED_SERVER = "dedicated_server"
    OTHER_ARCHITECTURE_TYPE = "other_architecture_type"

    def __str__(self) -> str:
        return str(self.value)


class QualificationArchiveDataSubUseCase(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUB_USE_CASE = "unknown_sub_use_case"

    def __str__(self) -> str:
        return str(self.value)


class QualificationContainerSubUseCase(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUB_USE_CASE = "unknown_sub_use_case"

    def __str__(self) -> str:
        return str(self.value)


class QualificationDeploySoftwareSubUseCase(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUB_USE_CASE = "unknown_sub_use_case"

    def __str__(self) -> str:
        return str(self.value)


class QualificationHostApplicationSubUseCase(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUB_USE_CASE = "unknown_sub_use_case"
    SAAS_APP = "saas_app"
    GOVERNMENT_APP = "government_app"

    def __str__(self) -> str:
        return str(self.value)


class QualificationHostWebsiteSubUseCase(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUB_USE_CASE = "unknown_sub_use_case"
    INFORMATION_WEBSITE = "information_website"
    ECOMMERCE_WEBSITE = "ecommerce_website"
    HIGH_WEBSITE = "high_website"
    OTHER_SUB_USE_CASE = "other_sub_use_case"

    def __str__(self) -> str:
        return str(self.value)


class QualificationOtherUseCaseSubUseCase(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUB_USE_CASE = "unknown_sub_use_case"

    def __str__(self) -> str:
        return str(self.value)


class QualificationSetScalewayEnvironmentSubUseCase(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUB_USE_CASE = "unknown_sub_use_case"

    def __str__(self) -> str:
        return str(self.value)


class QualificationShareDataSubUseCase(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SUB_USE_CASE = "unknown_sub_use_case"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class QualificationAiMachine:
    sub_use_case: QualificationAiMachineSubUseCase


@dataclass
class QualificationArchiveData:
    sub_use_case: QualificationArchiveDataSubUseCase


@dataclass
class QualificationContainer:
    sub_use_case: QualificationContainerSubUseCase


@dataclass
class QualificationDeploySoftware:
    sub_use_case: QualificationDeploySoftwareSubUseCase


@dataclass
class QualificationHostApplication:
    sub_use_case: QualificationHostApplicationSubUseCase


@dataclass
class QualificationHostWebsite:
    sub_use_case: QualificationHostWebsiteSubUseCase


@dataclass
class QualificationOtherUseCase:
    sub_use_case: QualificationOtherUseCaseSubUseCase


@dataclass
class QualificationSetScalewayEnvironment:
    sub_use_case: QualificationSetScalewayEnvironmentSubUseCase


@dataclass
class QualificationShareData:
    sub_use_case: QualificationShareDataSubUseCase


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

    created_at: Optional[datetime] = None
    """
    The creation date of the contract.
    """

    updated_at: Optional[datetime] = None
    """
    The last modification date of the contract.
    """


@dataclass
class Qualification:
    architecture_type: QualificationArchitectureType
    """
    Architecture type of the qualification.
    """

    host_website: Optional[QualificationHostWebsite] = None

    host_application: Optional[QualificationHostApplication] = None

    deploy_software: Optional[QualificationDeploySoftware] = None

    set_scaleway_environment: Optional[QualificationSetScalewayEnvironment] = None

    ai_machine: Optional[QualificationAiMachine] = None

    container: Optional[QualificationContainer] = None

    archive_data: Optional[QualificationArchiveData] = None

    share_data: Optional[QualificationShareData] = None

    other_use_case: Optional[QualificationOtherUseCase] = None


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

    created_at: Optional[datetime] = None
    """
    The creation date of the contract signature.
    """

    signed_at: Optional[datetime] = None
    """
    The signing date of the contract signature.
    """

    expires_at: Optional[datetime] = None
    """
    The expiration date of the contract signature.
    """

    contract: Optional[Contract] = None
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

    created_at: Optional[datetime] = None
    """
    Creation date of the Project.
    """

    updated_at: Optional[datetime] = None
    """
    Update date of the Project.
    """

    qualification: Optional[Qualification] = None
    """
    Qualification of the Project.
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

    organization_id: Optional[str] = None
    """
    ID of the Organization to check the contract signature for.
    """

    contract_type: Optional[ContractType] = ContractType.UNKNOWN_TYPE
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

    contract_type: Optional[ContractType] = ContractType.UNKNOWN_TYPE
    """
    The type of the contract.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization.
    """


@dataclass
class ContractApiDownloadContractSignatureRequest:
    contract_signature_id: str
    """
    The contract signature ID.
    """

    locale: Optional[StdLanguageCode] = StdLanguageCode.UNKNOWN_LANGUAGE_CODE
    """
    The locale requested for the content of the contract.
    """


@dataclass
class ContractApiListContractSignaturesRequest:
    page: Optional[int] = 0
    """
    The page number for the returned contracts.
    """

    page_size: Optional[int] = 0
    """
    The maximum number of contracts per page.
    """

    order_by: Optional[ListContractSignaturesRequestOrderBy] = (
        ListContractSignaturesRequestOrderBy.SIGNED_AT_ASC
    )
    """
    How the contracts are ordered in the response.
    """

    organization_id: Optional[str] = None
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

    contract_signatures: list[ContractSignature]
    """
    The paginated returned contract signatures.
    """


@dataclass
class ListProjectsResponse:
    total_count: int
    """
    Total number of Projects.
    """

    projects: list[Project]
    """
    Paginated returned Projects.
    """


@dataclass
class ProjectApiCreateProjectRequest:
    description: str
    """
    Description of the Project.
    """

    name: Optional[str] = None
    """
    Name of the Project.
    """

    organization_id: Optional[str] = None
    """
    Organization ID of the Project.
    """


@dataclass
class ProjectApiDeleteProjectRequest:
    project_id: Optional[str] = None
    """
    Project ID of the Project.
    """


@dataclass
class ProjectApiGetProjectRequest:
    project_id: Optional[str] = None
    """
    Project ID of the Project.
    """


@dataclass
class ProjectApiListProjectsRequest:
    organization_id: Optional[str] = None
    """
    Organization ID of the Project.
    """

    name: Optional[str] = None
    """
    Name of the Project.
    """

    page: Optional[int] = 0
    """
    Page number for the returned Projects.
    """

    page_size: Optional[int] = 0
    """
    Maximum number of Project per page.
    """

    order_by: Optional[ListProjectsRequestOrderBy] = (
        ListProjectsRequestOrderBy.CREATED_AT_ASC
    )
    """
    Sort order of the returned Projects.
    """

    project_ids: Optional[list[str]] = field(default_factory=list)
    """
    Project IDs to filter for. The results will be limited to any Projects with an ID in this array.
    """


@dataclass
class ProjectApiSetProjectQualificationRequest:
    project_id: Optional[str] = None
    """
    Project ID.
    """

    qualification: Optional[Qualification] = None
    """
    Use case chosen for the Project.
    """


@dataclass
class ProjectApiUpdateProjectRequest:
    project_id: Optional[str] = None
    """
    Project ID of the Project.
    """

    name: Optional[str] = None
    """
    Name of the Project.
    """

    description: Optional[str] = None
    """
    Description of the Project.
    """


@dataclass
class ProjectQualification:
    project_id: str
    """
    Project ID.
    """

    qualification: Optional[Qualification] = None
    """
    Qualification of the Project.
    """
