# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    ContractType,
    QualificationArchitectureType,
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


def unmarshal_Contract(data: Any) -> Contract:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Contract' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = ContractType.UNKNOWN_TYPE

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = 0

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    return Contract(**args)


def unmarshal_ContractSignature(data: Any) -> ContractSignature:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ContractSignature' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("signed_at", None)
    if field is not None:
        args["signed_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["signed_at"] = None

    field = data.get("expires_at", None)
    if field is not None:
        args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["expires_at"] = None

    field = data.get("contract", None)
    if field is not None:
        args["contract"] = unmarshal_Contract(field)
    else:
        args["contract"] = None

    return ContractSignature(**args)


def unmarshal_QualificationAiMachine(data: Any) -> QualificationAiMachine:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationAiMachine' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sub_use_case", None)
    if field is not None:
        args["sub_use_case"] = field
    else:
        args["sub_use_case"] = None

    return QualificationAiMachine(**args)


def unmarshal_QualificationArchiveData(data: Any) -> QualificationArchiveData:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationArchiveData' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sub_use_case", None)
    if field is not None:
        args["sub_use_case"] = field
    else:
        args["sub_use_case"] = None

    return QualificationArchiveData(**args)


def unmarshal_QualificationContainer(data: Any) -> QualificationContainer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationContainer' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sub_use_case", None)
    if field is not None:
        args["sub_use_case"] = field
    else:
        args["sub_use_case"] = None

    return QualificationContainer(**args)


def unmarshal_QualificationDeploySoftware(data: Any) -> QualificationDeploySoftware:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationDeploySoftware' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sub_use_case", None)
    if field is not None:
        args["sub_use_case"] = field
    else:
        args["sub_use_case"] = None

    return QualificationDeploySoftware(**args)


def unmarshal_QualificationHostApplication(data: Any) -> QualificationHostApplication:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationHostApplication' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sub_use_case", None)
    if field is not None:
        args["sub_use_case"] = field
    else:
        args["sub_use_case"] = None

    return QualificationHostApplication(**args)


def unmarshal_QualificationHostWebsite(data: Any) -> QualificationHostWebsite:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationHostWebsite' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sub_use_case", None)
    if field is not None:
        args["sub_use_case"] = field
    else:
        args["sub_use_case"] = None

    return QualificationHostWebsite(**args)


def unmarshal_QualificationOtherUseCase(data: Any) -> QualificationOtherUseCase:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationOtherUseCase' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sub_use_case", None)
    if field is not None:
        args["sub_use_case"] = field
    else:
        args["sub_use_case"] = None

    return QualificationOtherUseCase(**args)


def unmarshal_QualificationSetScalewayEnvironment(
    data: Any,
) -> QualificationSetScalewayEnvironment:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationSetScalewayEnvironment' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sub_use_case", None)
    if field is not None:
        args["sub_use_case"] = field
    else:
        args["sub_use_case"] = None

    return QualificationSetScalewayEnvironment(**args)


def unmarshal_QualificationShareData(data: Any) -> QualificationShareData:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'QualificationShareData' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sub_use_case", None)
    if field is not None:
        args["sub_use_case"] = field
    else:
        args["sub_use_case"] = None

    return QualificationShareData(**args)


def unmarshal_Qualification(data: Any) -> Qualification:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Qualification' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("architecture_type", None)
    if field is not None:
        args["architecture_type"] = field
    else:
        args["architecture_type"] = (
            QualificationArchitectureType.UNKNOWN_ARCHITECTURE_TYPE
        )

    field = data.get("host_website", None)
    if field is not None:
        args["host_website"] = unmarshal_QualificationHostWebsite(field)
    else:
        args["host_website"] = None

    field = data.get("host_application", None)
    if field is not None:
        args["host_application"] = unmarshal_QualificationHostApplication(field)
    else:
        args["host_application"] = None

    field = data.get("deploy_software", None)
    if field is not None:
        args["deploy_software"] = unmarshal_QualificationDeploySoftware(field)
    else:
        args["deploy_software"] = None

    field = data.get("set_scaleway_environment", None)
    if field is not None:
        args["set_scaleway_environment"] = (
            unmarshal_QualificationSetScalewayEnvironment(field)
        )
    else:
        args["set_scaleway_environment"] = None

    field = data.get("ai_machine", None)
    if field is not None:
        args["ai_machine"] = unmarshal_QualificationAiMachine(field)
    else:
        args["ai_machine"] = None

    field = data.get("container", None)
    if field is not None:
        args["container"] = unmarshal_QualificationContainer(field)
    else:
        args["container"] = None

    field = data.get("archive_data", None)
    if field is not None:
        args["archive_data"] = unmarshal_QualificationArchiveData(field)
    else:
        args["archive_data"] = None

    field = data.get("share_data", None)
    if field is not None:
        args["share_data"] = unmarshal_QualificationShareData(field)
    else:
        args["share_data"] = None

    field = data.get("other_use_case", None)
    if field is not None:
        args["other_use_case"] = unmarshal_QualificationOtherUseCase(field)
    else:
        args["other_use_case"] = None

    return Qualification(**args)


def unmarshal_Project(data: Any) -> Project:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Project' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("updated_at", None)
    if field is not None:
        args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["updated_at"] = None

    field = data.get("qualification", None)
    if field is not None:
        args["qualification"] = unmarshal_Qualification(field)
    else:
        args["qualification"] = None

    return Project(**args)


def unmarshal_CheckContractSignatureResponse(
    data: Any,
) -> CheckContractSignatureResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CheckContractSignatureResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("created", None)
    if field is not None:
        args["created"] = field
    else:
        args["created"] = False

    field = data.get("validated", None)
    if field is not None:
        args["validated"] = field
    else:
        args["validated"] = False

    return CheckContractSignatureResponse(**args)


def unmarshal_ListContractSignaturesResponse(
    data: Any,
) -> ListContractSignaturesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListContractSignaturesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("contract_signatures", None)
    if field is not None:
        args["contract_signatures"] = (
            [unmarshal_ContractSignature(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["contract_signatures"] = []

    return ListContractSignaturesResponse(**args)


def unmarshal_ListProjectsResponse(data: Any) -> ListProjectsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProjectsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    field = data.get("projects", None)
    if field is not None:
        args["projects"] = (
            [unmarshal_Project(v) for v in field] if field is not None else None
        )
    else:
        args["projects"] = []

    return ListProjectsResponse(**args)


def unmarshal_ProjectQualification(data: Any) -> ProjectQualification:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProjectQualification' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("qualification", None)
    if field is not None:
        args["qualification"] = unmarshal_Qualification(field)
    else:
        args["qualification"] = None

    return ProjectQualification(**args)


def marshal_ContractApiCheckContractSignatureRequest(
    request: ContractApiCheckContractSignatureRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.contract_name is not None:
        output["contract_name"] = request.contract_name

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.contract_type is not None:
        output["contract_type"] = request.contract_type

    return output


def marshal_ContractApiCreateContractSignatureRequest(
    request: ContractApiCreateContractSignatureRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.contract_name is not None:
        output["contract_name"] = request.contract_name

    if request.validated is not None:
        output["validated"] = request.validated

    if request.contract_type is not None:
        output["contract_type"] = request.contract_type

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    return output


def marshal_ProjectApiCreateProjectRequest(
    request: ProjectApiCreateProjectRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.name is not None:
        output["name"] = request.name

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    return output


def marshal_QualificationAiMachine(
    request: QualificationAiMachine,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = request.sub_use_case

    return output


def marshal_QualificationArchiveData(
    request: QualificationArchiveData,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = request.sub_use_case

    return output


def marshal_QualificationContainer(
    request: QualificationContainer,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = request.sub_use_case

    return output


def marshal_QualificationDeploySoftware(
    request: QualificationDeploySoftware,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = request.sub_use_case

    return output


def marshal_QualificationHostApplication(
    request: QualificationHostApplication,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = request.sub_use_case

    return output


def marshal_QualificationHostWebsite(
    request: QualificationHostWebsite,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = request.sub_use_case

    return output


def marshal_QualificationOtherUseCase(
    request: QualificationOtherUseCase,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = request.sub_use_case

    return output


def marshal_QualificationSetScalewayEnvironment(
    request: QualificationSetScalewayEnvironment,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = request.sub_use_case

    return output


def marshal_QualificationShareData(
    request: QualificationShareData,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.sub_use_case is not None:
        output["sub_use_case"] = request.sub_use_case

    return output


def marshal_Qualification(
    request: Qualification,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="host_website",
                    value=request.host_website,
                    marshal_func=marshal_QualificationHostWebsite,
                ),
                OneOfPossibility(
                    param="host_application",
                    value=request.host_application,
                    marshal_func=marshal_QualificationHostApplication,
                ),
                OneOfPossibility(
                    param="deploy_software",
                    value=request.deploy_software,
                    marshal_func=marshal_QualificationDeploySoftware,
                ),
                OneOfPossibility(
                    param="set_scaleway_environment",
                    value=request.set_scaleway_environment,
                    marshal_func=marshal_QualificationSetScalewayEnvironment,
                ),
                OneOfPossibility(
                    param="ai_machine",
                    value=request.ai_machine,
                    marshal_func=marshal_QualificationAiMachine,
                ),
                OneOfPossibility(
                    param="container",
                    value=request.container,
                    marshal_func=marshal_QualificationContainer,
                ),
                OneOfPossibility(
                    param="archive_data",
                    value=request.archive_data,
                    marshal_func=marshal_QualificationArchiveData,
                ),
                OneOfPossibility(
                    param="share_data",
                    value=request.share_data,
                    marshal_func=marshal_QualificationShareData,
                ),
                OneOfPossibility(
                    param="other_use_case",
                    value=request.other_use_case,
                    marshal_func=marshal_QualificationOtherUseCase,
                ),
            ]
        ),
    )

    if request.architecture_type is not None:
        output["architecture_type"] = request.architecture_type

    return output


def marshal_ProjectApiSetProjectQualificationRequest(
    request: ProjectApiSetProjectQualificationRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.qualification is not None:
        output["qualification"] = marshal_Qualification(request.qualification, defaults)

    return output


def marshal_ProjectApiUpdateProjectRequest(
    request: ProjectApiUpdateProjectRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.description is not None:
        output["description"] = request.description

    return output
