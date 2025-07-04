# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ContractType,
    ListContractSignaturesRequestOrderBy,
    ListProjectsRequestOrderBy,
    QualificationAiMachineSubUseCase,
    QualificationArchitectureType,
    QualificationArchiveDataSubUseCase,
    QualificationContainerSubUseCase,
    QualificationDeploySoftwareSubUseCase,
    QualificationHostApplicationSubUseCase,
    QualificationHostWebsiteSubUseCase,
    QualificationOtherUseCaseSubUseCase,
    QualificationSetScalewayEnvironmentSubUseCase,
    QualificationShareDataSubUseCase,
    Contract,
    ContractSignature,
    QualificationAiMachine,
    QualificationArchiveData,
    QualificationContainer,
    QualificationDeploySoftware,
    QualificationHostApplication,
    QualificationHostWebsite,
    QualificationOtherUseCase,
    QualificationSetScalewayEnvironment,
    QualificationShareData,
    Qualification,
    Project,
    CheckContractSignatureResponse,
    ListContractSignaturesResponse,
    ListProjectsResponse,
    ProjectQualification,
    ContractApiCheckContractSignatureRequest,
    ContractApiCreateContractSignatureRequest,
    ProjectApiCreateProjectRequest,
    ProjectApiSetProjectQualificationRequest,
    ProjectApiUpdateProjectRequest,
)
from ...std.types import (
LanguageCode as StdLanguageCode,
)

def unmarshal_Contract(data: Any) -> Contract:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Contract' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("type", getattr(ContractType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("version", 0)
    args["version"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Contract(**args)

def unmarshal_ContractSignature(data: Any) -> ContractSignature:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContractSignature' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("signed_at", None)
    args["signed_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("contract", None)
    args["contract"] = unmarshal_Contract(field) if field is not None else None

    return ContractSignature(**args)

def unmarshal_QualificationAiMachine(data: Any) -> QualificationAiMachine:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationAiMachine' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sub_use_case", str())
    args["sub_use_case"] = field

    return QualificationAiMachine(**args)

def unmarshal_QualificationArchiveData(data: Any) -> QualificationArchiveData:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationArchiveData' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sub_use_case", str())
    args["sub_use_case"] = field

    return QualificationArchiveData(**args)

def unmarshal_QualificationContainer(data: Any) -> QualificationContainer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationContainer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sub_use_case", str())
    args["sub_use_case"] = field

    return QualificationContainer(**args)

def unmarshal_QualificationDeploySoftware(data: Any) -> QualificationDeploySoftware:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationDeploySoftware' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sub_use_case", str())
    args["sub_use_case"] = field

    return QualificationDeploySoftware(**args)

def unmarshal_QualificationHostApplication(data: Any) -> QualificationHostApplication:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationHostApplication' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sub_use_case", str())
    args["sub_use_case"] = field

    return QualificationHostApplication(**args)

def unmarshal_QualificationHostWebsite(data: Any) -> QualificationHostWebsite:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationHostWebsite' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sub_use_case", str())
    args["sub_use_case"] = field

    return QualificationHostWebsite(**args)

def unmarshal_QualificationOtherUseCase(data: Any) -> QualificationOtherUseCase:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationOtherUseCase' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sub_use_case", str())
    args["sub_use_case"] = field

    return QualificationOtherUseCase(**args)

def unmarshal_QualificationSetScalewayEnvironment(data: Any) -> QualificationSetScalewayEnvironment:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationSetScalewayEnvironment' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sub_use_case", str())
    args["sub_use_case"] = field

    return QualificationSetScalewayEnvironment(**args)

def unmarshal_QualificationShareData(data: Any) -> QualificationShareData:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationShareData' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sub_use_case", str())
    args["sub_use_case"] = field

    return QualificationShareData(**args)

def unmarshal_Qualification(data: Any) -> Qualification:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Qualification' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("architecture_type", getattr(QualificationArchitectureType, "UNKNOWN_ARCHITECTURE_TYPE"))
    args["architecture_type"] = field

    field = data.get("host_website", None)
    args["host_website"] = unmarshal_QualificationHostWebsite(field) if field is not None else None

    field = data.get("host_application", None)
    args["host_application"] = unmarshal_QualificationHostApplication(field) if field is not None else None

    field = data.get("deploy_software", None)
    args["deploy_software"] = unmarshal_QualificationDeploySoftware(field) if field is not None else None

    field = data.get("set_scaleway_environment", None)
    args["set_scaleway_environment"] = unmarshal_QualificationSetScalewayEnvironment(field) if field is not None else None

    field = data.get("ai_machine", None)
    args["ai_machine"] = unmarshal_QualificationAiMachine(field) if field is not None else None

    field = data.get("container", None)
    args["container"] = unmarshal_QualificationContainer(field) if field is not None else None

    field = data.get("archive_data", None)
    args["archive_data"] = unmarshal_QualificationArchiveData(field) if field is not None else None

    field = data.get("share_data", None)
    args["share_data"] = unmarshal_QualificationShareData(field) if field is not None else None

    field = data.get("other_use_case", None)
    args["other_use_case"] = unmarshal_QualificationOtherUseCase(field) if field is not None else None

    return Qualification(**args)

def unmarshal_Project(data: Any) -> Project:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Project' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("qualification", None)
    args["qualification"] = unmarshal_Qualification(field) if field is not None else None

    return Project(**args)

def unmarshal_CheckContractSignatureResponse(data: Any) -> CheckContractSignatureResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckContractSignatureResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created", False)
    args["created"] = field

    field = data.get("validated", False)
    args["validated"] = field

    return CheckContractSignatureResponse(**args)

def unmarshal_ListContractSignaturesResponse(data: Any) -> ListContractSignaturesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListContractSignaturesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("contract_signatures", [])
    args["contract_signatures"] = [unmarshal_ContractSignature(v) for v in field] if field is not None else None

    return ListContractSignaturesResponse(**args)

def unmarshal_ListProjectsResponse(data: Any) -> ListProjectsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProjectsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("projects", [])
    args["projects"] = [unmarshal_Project(v) for v in field] if field is not None else None

    return ListProjectsResponse(**args)

def unmarshal_ProjectQualification(data: Any) -> ProjectQualification:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectQualification' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("qualification", None)
    args["qualification"] = unmarshal_Qualification(field) if field is not None else None

    return ProjectQualification(**args)

def marshal_ContractApiCheckContractSignatureRequest(
    request: ContractApiCheckContractSignatureRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.contract_name is not None:
        output["contract_name"] = request.contract_name
    else:
        output["contract_name"] = str()

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id or defaults.default_organization_id
    else:
        output["organization_id"] = None

    if request.contract_type is not None:
        output["contract_type"] = str(request.contract_type)
    else:
        output["contract_type"] = None


    return output

def marshal_ContractApiCreateContractSignatureRequest(
    request: ContractApiCreateContractSignatureRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.contract_name is not None:
        output["contract_name"] = request.contract_name
    else:
        output["contract_name"] = str()

    if request.validated is not None:
        output["validated"] = request.validated
    else:
        output["validated"] = False

    if request.contract_type is not None:
        output["contract_type"] = str(request.contract_type)
    else:
        output["contract_type"] = None

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id or defaults.default_organization_id
    else:
        output["organization_id"] = None


    return output

def marshal_ProjectApiCreateProjectRequest(
    request: ProjectApiCreateProjectRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id or defaults.default_organization_id
    else:
        output["organization_id"] = None


    return output

def marshal_QualificationAiMachine(
    request: QualificationAiMachine,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = str(request.sub_use_case)
    else:
        output["sub_use_case"] = str()


    return output

def marshal_QualificationArchiveData(
    request: QualificationArchiveData,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = str(request.sub_use_case)
    else:
        output["sub_use_case"] = str()


    return output

def marshal_QualificationContainer(
    request: QualificationContainer,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = str(request.sub_use_case)
    else:
        output["sub_use_case"] = str()


    return output

def marshal_QualificationDeploySoftware(
    request: QualificationDeploySoftware,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = str(request.sub_use_case)
    else:
        output["sub_use_case"] = str()


    return output

def marshal_QualificationHostApplication(
    request: QualificationHostApplication,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = str(request.sub_use_case)
    else:
        output["sub_use_case"] = str()


    return output

def marshal_QualificationHostWebsite(
    request: QualificationHostWebsite,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = str(request.sub_use_case)
    else:
        output["sub_use_case"] = str()


    return output

def marshal_QualificationOtherUseCase(
    request: QualificationOtherUseCase,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = str(request.sub_use_case)
    else:
        output["sub_use_case"] = str()


    return output

def marshal_QualificationSetScalewayEnvironment(
    request: QualificationSetScalewayEnvironment,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = str(request.sub_use_case)
    else:
        output["sub_use_case"] = str()


    return output

def marshal_QualificationShareData(
    request: QualificationShareData,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = str(request.sub_use_case)
    else:
        output["sub_use_case"] = str()


    return output

def marshal_Qualification(
    request: Qualification,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="host_website", value=request.host_website,marshal_func=marshal_QualificationHostWebsite
            ),
            OneOfPossibility(param="host_application", value=request.host_application,marshal_func=marshal_QualificationHostApplication
            ),
            OneOfPossibility(param="deploy_software", value=request.deploy_software,marshal_func=marshal_QualificationDeploySoftware
            ),
            OneOfPossibility(param="set_scaleway_environment", value=request.set_scaleway_environment,marshal_func=marshal_QualificationSetScalewayEnvironment
            ),
            OneOfPossibility(param="ai_machine", value=request.ai_machine,marshal_func=marshal_QualificationAiMachine
            ),
            OneOfPossibility(param="container", value=request.container,marshal_func=marshal_QualificationContainer
            ),
            OneOfPossibility(param="archive_data", value=request.archive_data,marshal_func=marshal_QualificationArchiveData
            ),
            OneOfPossibility(param="share_data", value=request.share_data,marshal_func=marshal_QualificationShareData
            ),
            OneOfPossibility(param="other_use_case", value=request.other_use_case,marshal_func=marshal_QualificationOtherUseCase
            ),
        ]),
    )

    if request.architecture_type is not None:
        output["architecture_type"] = str(request.architecture_type)
    else:
        output["architecture_type"] = getattr(QualificationArchitectureType, "UNKNOWN_ARCHITECTURE_TYPE")


    return output

def marshal_ProjectApiSetProjectQualificationRequest(
    request: ProjectApiSetProjectQualificationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.qualification is not None:
        output["qualification"] = marshal_Qualification(request.qualification, defaults)
    else:
        output["qualification"] = None


    return output

def marshal_ProjectApiUpdateProjectRequest(
    request: ProjectApiUpdateProjectRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output
