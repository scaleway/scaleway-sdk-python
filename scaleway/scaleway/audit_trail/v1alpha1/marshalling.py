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
    AlertRuleStatus,
    AuthenticationEventFailureReason,
    AuthenticationEventMFAType,
    AuthenticationEventMethod,
    AuthenticationEventOrigin,
    AuthenticationEventResult,
    SystemEventKind,
    ExportJobS3,
    ExportJobStatus,
    ExportJob,
    AlertRule,
    DisableAlertRulesResponse,
    EnableAlertRulesResponse,
    ListAlertRulesResponse,
    AccountContractSignatureInfoAccountContractInfo,
    AccountContractSignatureInfo,
    AccountOrganizationInfo,
    AccountProjectInfo,
    AccountUserInfo,
    AppleSiliconRunnerInfo,
    AppleSiliconServerInfo,
    AuditTrailExportJobInfo,
    BaremetalServerInfo,
    BaremetalSettingInfo,
    EdgeServicesBackendStageInfo,
    EdgeServicesCacheStageInfo,
    EdgeServicesDNSStageInfo,
    EdgeServicesPipelineInfo,
    EdgeServicesPlanInfo,
    EdgeServicesRouteRulesInfo,
    EdgeServicesRouteStageInfo,
    EdgeServicesTLSStageInfo,
    EdgeServicesWAFStageInfo,
    InstanceServerInfo,
    IpamIpInfo,
    KeyManagerKeyInfo,
    KubernetesACLInfo,
    KubernetesClusterInfo,
    KubernetesNodeInfo,
    KubernetesPoolInfo,
    LoadBalancerAclInfo,
    LoadBalancerBackendInfo,
    LoadBalancerCertificateInfo,
    LoadBalancerFrontendInfo,
    LoadBalancerIpInfo,
    LoadBalancerLbInfo,
    LoadBalancerRouteInfo,
    SecretManagerSecretInfo,
    SecretManagerSecretVersionInfo,
    VpcGwGatewayInfo,
    VpcGwGatewayNetworkInfo,
    VpcPrivateNetworkInfo,
    VpcRouteInfo,
    VpcSubnetInfo,
    Resource,
    AuthenticationEvent,
    ListAuthenticationEventsResponse,
    EventPrincipal,
    Event,
    SystemEvent,
    ListCombinedEventsResponseCombinedEvent,
    ListCombinedEventsResponse,
    ListEventsResponse,
    ListExportJobsResponse,
    ProductService,
    Product,
    ListProductsResponse,
    ListSystemEventsResponse,
    SetEnabledAlertRulesResponse,
    CreateExportJobRequest,
    DisableAlertRulesRequest,
    EnableAlertRulesRequest,
    SetEnabledAlertRulesRequest,
)
from ...std.types import (
    CountryCode as StdCountryCode,
)


def unmarshal_ExportJobS3(data: Any) -> ExportJobS3:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExportJobS3' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("bucket", None)
    if field is not None:
        args["bucket"] = field
    else:
        args["bucket"] = None

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("prefix", None)
    if field is not None:
        args["prefix"] = field
    else:
        args["prefix"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    return ExportJobS3(**args)


def unmarshal_ExportJobStatus(data: Any) -> ExportJobStatus:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExportJobStatus' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("code", None)
    if field is not None:
        args["code"] = field
    else:
        args["code"] = None

    field = data.get("message", None)
    if field is not None:
        args["message"] = field
    else:
        args["message"] = None

    return ExportJobStatus(**args)


def unmarshal_ExportJob(data: Any) -> ExportJob:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ExportJob' failed as data isn't a dictionary."
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

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = []

    field = data.get("s3", None)
    if field is not None:
        args["s3"] = unmarshal_ExportJobS3(field)
    else:
        args["s3"] = None

    field = data.get("created_at", None)
    if field is not None:
        args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["created_at"] = None

    field = data.get("last_run_at", None)
    if field is not None:
        args["last_run_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["last_run_at"] = None

    field = data.get("last_status", None)
    if field is not None:
        args["last_status"] = unmarshal_ExportJobStatus(field)
    else:
        args["last_status"] = None

    return ExportJob(**args)


def unmarshal_AlertRule(data: Any) -> AlertRule:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AlertRule' failed as data isn't a dictionary."
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

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = AlertRuleStatus.UNKNOWN_STATUS

    return AlertRule(**args)


def unmarshal_DisableAlertRulesResponse(data: Any) -> DisableAlertRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DisableAlertRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("alert_rules", None)
    if field is not None:
        args["alert_rules"] = (
            [unmarshal_AlertRule(v) for v in field] if field is not None else None
        )
    else:
        args["alert_rules"] = []

    return DisableAlertRulesResponse(**args)


def unmarshal_EnableAlertRulesResponse(data: Any) -> EnableAlertRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EnableAlertRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("alert_rules", None)
    if field is not None:
        args["alert_rules"] = (
            [unmarshal_AlertRule(v) for v in field] if field is not None else None
        )
    else:
        args["alert_rules"] = []

    return EnableAlertRulesResponse(**args)


def unmarshal_ListAlertRulesResponse(data: Any) -> ListAlertRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAlertRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("alert_rules", None)
    if field is not None:
        args["alert_rules"] = (
            [unmarshal_AlertRule(v) for v in field] if field is not None else None
        )
    else:
        args["alert_rules"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListAlertRulesResponse(**args)


def unmarshal_AccountContractSignatureInfoAccountContractInfo(
    data: Any,
) -> AccountContractSignatureInfoAccountContractInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccountContractSignatureInfoAccountContractInfo' failed as data isn't a dictionary."
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
        args["type_"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("version", None)
    if field is not None:
        args["version"] = field
    else:
        args["version"] = None

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

    return AccountContractSignatureInfoAccountContractInfo(**args)


def unmarshal_AccountContractSignatureInfo(data: Any) -> AccountContractSignatureInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccountContractSignatureInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("signed_by_account_root_user_id", None)
    if field is not None:
        args["signed_by_account_root_user_id"] = field
    else:
        args["signed_by_account_root_user_id"] = None

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
        args["contract"] = unmarshal_AccountContractSignatureInfoAccountContractInfo(
            field
        )
    else:
        args["contract"] = None

    return AccountContractSignatureInfo(**args)


def unmarshal_AccountOrganizationInfo(data: Any) -> AccountOrganizationInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccountOrganizationInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return AccountOrganizationInfo(**args)


def unmarshal_AccountProjectInfo(data: Any) -> AccountProjectInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccountProjectInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    return AccountProjectInfo(**args)


def unmarshal_AccountUserInfo(data: Any) -> AccountUserInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AccountUserInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("email", None)
    if field is not None:
        args["email"] = field
    else:
        args["email"] = None

    field = data.get("phone_number", None)
    if field is not None:
        args["phone_number"] = field
    else:
        args["phone_number"] = None

    return AccountUserInfo(**args)


def unmarshal_AppleSiliconRunnerInfo(data: Any) -> AppleSiliconRunnerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AppleSiliconRunnerInfo' failed as data isn't a dictionary."
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

    return AppleSiliconRunnerInfo(**args)


def unmarshal_AppleSiliconServerInfo(data: Any) -> AppleSiliconServerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AppleSiliconServerInfo' failed as data isn't a dictionary."
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

    return AppleSiliconServerInfo(**args)


def unmarshal_AuditTrailExportJobInfo(data: Any) -> AuditTrailExportJobInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AuditTrailExportJobInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return AuditTrailExportJobInfo(**args)


def unmarshal_BaremetalServerInfo(data: Any) -> BaremetalServerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BaremetalServerInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("tags", None)
    if field is not None:
        args["tags"] = field
    else:
        args["tags"] = None

    return BaremetalServerInfo(**args)


def unmarshal_BaremetalSettingInfo(data: Any) -> BaremetalSettingInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BaremetalSettingInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return BaremetalSettingInfo(**args)


def unmarshal_EdgeServicesBackendStageInfo(data: Any) -> EdgeServicesBackendStageInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EdgeServicesBackendStageInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    return EdgeServicesBackendStageInfo(**args)


def unmarshal_EdgeServicesCacheStageInfo(data: Any) -> EdgeServicesCacheStageInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EdgeServicesCacheStageInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    return EdgeServicesCacheStageInfo(**args)


def unmarshal_EdgeServicesDNSStageInfo(data: Any) -> EdgeServicesDNSStageInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EdgeServicesDNSStageInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    return EdgeServicesDNSStageInfo(**args)


def unmarshal_EdgeServicesPipelineInfo(data: Any) -> EdgeServicesPipelineInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EdgeServicesPipelineInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return EdgeServicesPipelineInfo(**args)


def unmarshal_EdgeServicesPlanInfo(data: Any) -> EdgeServicesPlanInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EdgeServicesPlanInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return EdgeServicesPlanInfo(**args)


def unmarshal_EdgeServicesRouteRulesInfo(data: Any) -> EdgeServicesRouteRulesInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EdgeServicesRouteRulesInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("route_stage_id", None)
    if field is not None:
        args["route_stage_id"] = field
    else:
        args["route_stage_id"] = None

    return EdgeServicesRouteRulesInfo(**args)


def unmarshal_EdgeServicesRouteStageInfo(data: Any) -> EdgeServicesRouteStageInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EdgeServicesRouteStageInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    return EdgeServicesRouteStageInfo(**args)


def unmarshal_EdgeServicesTLSStageInfo(data: Any) -> EdgeServicesTLSStageInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EdgeServicesTLSStageInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    return EdgeServicesTLSStageInfo(**args)


def unmarshal_EdgeServicesWAFStageInfo(data: Any) -> EdgeServicesWAFStageInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EdgeServicesWAFStageInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("pipeline_id", None)
    if field is not None:
        args["pipeline_id"] = field
    else:
        args["pipeline_id"] = None

    return EdgeServicesWAFStageInfo(**args)


def unmarshal_InstanceServerInfo(data: Any) -> InstanceServerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InstanceServerInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return InstanceServerInfo(**args)


def unmarshal_IpamIpInfo(data: Any) -> IpamIpInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IpamIpInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("address", None)
    if field is not None:
        args["address"] = field
    else:
        args["address"] = None

    return IpamIpInfo(**args)


def unmarshal_KeyManagerKeyInfo(data: Any) -> KeyManagerKeyInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KeyManagerKeyInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return KeyManagerKeyInfo(**args)


def unmarshal_KubernetesACLInfo(data: Any) -> KubernetesACLInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KubernetesACLInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return KubernetesACLInfo(**args)


def unmarshal_KubernetesClusterInfo(data: Any) -> KubernetesClusterInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KubernetesClusterInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return KubernetesClusterInfo(**args)


def unmarshal_KubernetesNodeInfo(data: Any) -> KubernetesNodeInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KubernetesNodeInfo' failed as data isn't a dictionary."
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

    return KubernetesNodeInfo(**args)


def unmarshal_KubernetesPoolInfo(data: Any) -> KubernetesPoolInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'KubernetesPoolInfo' failed as data isn't a dictionary."
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

    return KubernetesPoolInfo(**args)


def unmarshal_LoadBalancerAclInfo(data: Any) -> LoadBalancerAclInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LoadBalancerAclInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("frontend_id", None)
    if field is not None:
        args["frontend_id"] = field
    else:
        args["frontend_id"] = None

    return LoadBalancerAclInfo(**args)


def unmarshal_LoadBalancerBackendInfo(data: Any) -> LoadBalancerBackendInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LoadBalancerBackendInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("lb_id", None)
    if field is not None:
        args["lb_id"] = field
    else:
        args["lb_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return LoadBalancerBackendInfo(**args)


def unmarshal_LoadBalancerCertificateInfo(data: Any) -> LoadBalancerCertificateInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LoadBalancerCertificateInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("lb_id", None)
    if field is not None:
        args["lb_id"] = field
    else:
        args["lb_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return LoadBalancerCertificateInfo(**args)


def unmarshal_LoadBalancerFrontendInfo(data: Any) -> LoadBalancerFrontendInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LoadBalancerFrontendInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("lb_id", None)
    if field is not None:
        args["lb_id"] = field
    else:
        args["lb_id"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return LoadBalancerFrontendInfo(**args)


def unmarshal_LoadBalancerIpInfo(data: Any) -> LoadBalancerIpInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LoadBalancerIpInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("ip_address", None)
    if field is not None:
        args["ip_address"] = field
    else:
        args["ip_address"] = None

    field = data.get("lb_id", None)
    if field is not None:
        args["lb_id"] = field
    else:
        args["lb_id"] = None

    return LoadBalancerIpInfo(**args)


def unmarshal_LoadBalancerLbInfo(data: Any) -> LoadBalancerLbInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LoadBalancerLbInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    return LoadBalancerLbInfo(**args)


def unmarshal_LoadBalancerRouteInfo(data: Any) -> LoadBalancerRouteInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LoadBalancerRouteInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("frontend_id", None)
    if field is not None:
        args["frontend_id"] = field
    else:
        args["frontend_id"] = None

    field = data.get("backend_id", None)
    if field is not None:
        args["backend_id"] = field
    else:
        args["backend_id"] = None

    return LoadBalancerRouteInfo(**args)


def unmarshal_SecretManagerSecretInfo(data: Any) -> SecretManagerSecretInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretManagerSecretInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("path", None)
    if field is not None:
        args["path"] = field
    else:
        args["path"] = None

    field = data.get("key_id", None)
    if field is not None:
        args["key_id"] = field
    else:
        args["key_id"] = None

    return SecretManagerSecretInfo(**args)


def unmarshal_SecretManagerSecretVersionInfo(
    data: Any,
) -> SecretManagerSecretVersionInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SecretManagerSecretVersionInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("revision", None)
    if field is not None:
        args["revision"] = field
    else:
        args["revision"] = None

    return SecretManagerSecretVersionInfo(**args)


def unmarshal_VpcGwGatewayInfo(data: Any) -> VpcGwGatewayInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VpcGwGatewayInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("gateway_type_id", None)
    if field is not None:
        args["gateway_type_id"] = field
    else:
        args["gateway_type_id"] = None

    field = data.get("vpc_id", None)
    if field is not None:
        args["vpc_id"] = field
    else:
        args["vpc_id"] = None

    field = data.get("public_ip_id", None)
    if field is not None:
        args["public_ip_id"] = field
    else:
        args["public_ip_id"] = None

    return VpcGwGatewayInfo(**args)


def unmarshal_VpcGwGatewayNetworkInfo(data: Any) -> VpcGwGatewayNetworkInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VpcGwGatewayNetworkInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("gateway_id", None)
    if field is not None:
        args["gateway_id"] = field
    else:
        args["gateway_id"] = None

    field = data.get("pn_id", None)
    if field is not None:
        args["pn_id"] = field
    else:
        args["pn_id"] = None

    field = data.get("address", None)
    if field is not None:
        args["address"] = field
    else:
        args["address"] = None

    return VpcGwGatewayNetworkInfo(**args)


def unmarshal_VpcPrivateNetworkInfo(data: Any) -> VpcPrivateNetworkInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VpcPrivateNetworkInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("vpc_id", None)
    if field is not None:
        args["vpc_id"] = field
    else:
        args["vpc_id"] = None

    field = data.get("push_default_route", None)
    if field is not None:
        args["push_default_route"] = field
    else:
        args["push_default_route"] = None

    return VpcPrivateNetworkInfo(**args)


def unmarshal_VpcRouteInfo(data: Any) -> VpcRouteInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VpcRouteInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("vpc_id", None)
    if field is not None:
        args["vpc_id"] = field
    else:
        args["vpc_id"] = None

    field = data.get("destination", None)
    if field is not None:
        args["destination"] = field
    else:
        args["destination"] = None

    field = data.get("nexthop_resource_key", None)
    if field is not None:
        args["nexthop_resource_key"] = field
    else:
        args["nexthop_resource_key"] = None

    field = data.get("nexthop_private_network_key", None)
    if field is not None:
        args["nexthop_private_network_key"] = field
    else:
        args["nexthop_private_network_key"] = None

    return VpcRouteInfo(**args)


def unmarshal_VpcSubnetInfo(data: Any) -> VpcSubnetInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'VpcSubnetInfo' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("subnet_cidr", None)
    if field is not None:
        args["subnet_cidr"] = field
    else:
        args["subnet_cidr"] = None

    field = data.get("vpc_id", None)
    if field is not None:
        args["vpc_id"] = field
    else:
        args["vpc_id"] = None

    return VpcSubnetInfo(**args)


def unmarshal_Resource(data: Any) -> Resource:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Resource' failed as data isn't a dictionary."
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
        args["type_"] = None

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

    field = data.get("deleted_at", None)
    if field is not None:
        args["deleted_at"] = parser.isoparse(field) if isinstance(field, str) else field
    else:
        args["deleted_at"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("secm_secret_info", None)
    if field is not None:
        args["secm_secret_info"] = unmarshal_SecretManagerSecretInfo(field)
    else:
        args["secm_secret_info"] = None

    field = data.get("secm_secret_version_info", None)
    if field is not None:
        args["secm_secret_version_info"] = unmarshal_SecretManagerSecretVersionInfo(
            field
        )
    else:
        args["secm_secret_version_info"] = None

    field = data.get("kube_cluster_info", None)
    if field is not None:
        args["kube_cluster_info"] = unmarshal_KubernetesClusterInfo(field)
    else:
        args["kube_cluster_info"] = None

    field = data.get("kube_pool_info", None)
    if field is not None:
        args["kube_pool_info"] = unmarshal_KubernetesPoolInfo(field)
    else:
        args["kube_pool_info"] = None

    field = data.get("kube_node_info", None)
    if field is not None:
        args["kube_node_info"] = unmarshal_KubernetesNodeInfo(field)
    else:
        args["kube_node_info"] = None

    field = data.get("kube_acl_info", None)
    if field is not None:
        args["kube_acl_info"] = unmarshal_KubernetesACLInfo(field)
    else:
        args["kube_acl_info"] = None

    field = data.get("keym_key_info", None)
    if field is not None:
        args["keym_key_info"] = unmarshal_KeyManagerKeyInfo(field)
    else:
        args["keym_key_info"] = None

    field = data.get("secret_manager_secret_info", None)
    if field is not None:
        args["secret_manager_secret_info"] = unmarshal_SecretManagerSecretInfo(field)
    else:
        args["secret_manager_secret_info"] = None

    field = data.get("secret_manager_version_info", None)
    if field is not None:
        args["secret_manager_version_info"] = unmarshal_SecretManagerSecretVersionInfo(
            field
        )
    else:
        args["secret_manager_version_info"] = None

    field = data.get("key_manager_key_info", None)
    if field is not None:
        args["key_manager_key_info"] = unmarshal_KeyManagerKeyInfo(field)
    else:
        args["key_manager_key_info"] = None

    field = data.get("account_user_info", None)
    if field is not None:
        args["account_user_info"] = unmarshal_AccountUserInfo(field)
    else:
        args["account_user_info"] = None

    field = data.get("account_organization_info", None)
    if field is not None:
        args["account_organization_info"] = unmarshal_AccountOrganizationInfo(field)
    else:
        args["account_organization_info"] = None

    field = data.get("instance_server_info", None)
    if field is not None:
        args["instance_server_info"] = unmarshal_InstanceServerInfo(field)
    else:
        args["instance_server_info"] = None

    field = data.get("apple_silicon_server_info", None)
    if field is not None:
        args["apple_silicon_server_info"] = unmarshal_AppleSiliconServerInfo(field)
    else:
        args["apple_silicon_server_info"] = None

    field = data.get("account_project_info", None)
    if field is not None:
        args["account_project_info"] = unmarshal_AccountProjectInfo(field)
    else:
        args["account_project_info"] = None

    field = data.get("baremetal_server_info", None)
    if field is not None:
        args["baremetal_server_info"] = unmarshal_BaremetalServerInfo(field)
    else:
        args["baremetal_server_info"] = None

    field = data.get("baremetal_setting_info", None)
    if field is not None:
        args["baremetal_setting_info"] = unmarshal_BaremetalSettingInfo(field)
    else:
        args["baremetal_setting_info"] = None

    field = data.get("ipam_ip_info", None)
    if field is not None:
        args["ipam_ip_info"] = unmarshal_IpamIpInfo(field)
    else:
        args["ipam_ip_info"] = None

    field = data.get("load_balancer_lb_info", None)
    if field is not None:
        args["load_balancer_lb_info"] = unmarshal_LoadBalancerLbInfo(field)
    else:
        args["load_balancer_lb_info"] = None

    field = data.get("load_balancer_ip_info", None)
    if field is not None:
        args["load_balancer_ip_info"] = unmarshal_LoadBalancerIpInfo(field)
    else:
        args["load_balancer_ip_info"] = None

    field = data.get("load_balancer_frontend_info", None)
    if field is not None:
        args["load_balancer_frontend_info"] = unmarshal_LoadBalancerFrontendInfo(field)
    else:
        args["load_balancer_frontend_info"] = None

    field = data.get("load_balancer_backend_info", None)
    if field is not None:
        args["load_balancer_backend_info"] = unmarshal_LoadBalancerBackendInfo(field)
    else:
        args["load_balancer_backend_info"] = None

    field = data.get("load_balancer_route_info", None)
    if field is not None:
        args["load_balancer_route_info"] = unmarshal_LoadBalancerRouteInfo(field)
    else:
        args["load_balancer_route_info"] = None

    field = data.get("load_balancer_acl_info", None)
    if field is not None:
        args["load_balancer_acl_info"] = unmarshal_LoadBalancerAclInfo(field)
    else:
        args["load_balancer_acl_info"] = None

    field = data.get("load_balancer_certificate_info", None)
    if field is not None:
        args["load_balancer_certificate_info"] = unmarshal_LoadBalancerCertificateInfo(
            field
        )
    else:
        args["load_balancer_certificate_info"] = None

    field = data.get("edge_services_plan_info", None)
    if field is not None:
        args["edge_services_plan_info"] = unmarshal_EdgeServicesPlanInfo(field)
    else:
        args["edge_services_plan_info"] = None

    field = data.get("edge_services_pipeline_info", None)
    if field is not None:
        args["edge_services_pipeline_info"] = unmarshal_EdgeServicesPipelineInfo(field)
    else:
        args["edge_services_pipeline_info"] = None

    field = data.get("edge_services_dns_stage_info", None)
    if field is not None:
        args["edge_services_dns_stage_info"] = unmarshal_EdgeServicesDNSStageInfo(field)
    else:
        args["edge_services_dns_stage_info"] = None

    field = data.get("edge_services_tls_stage_info", None)
    if field is not None:
        args["edge_services_tls_stage_info"] = unmarshal_EdgeServicesTLSStageInfo(field)
    else:
        args["edge_services_tls_stage_info"] = None

    field = data.get("edge_services_cache_stage_info", None)
    if field is not None:
        args["edge_services_cache_stage_info"] = unmarshal_EdgeServicesCacheStageInfo(
            field
        )
    else:
        args["edge_services_cache_stage_info"] = None

    field = data.get("edge_services_route_stage_info", None)
    if field is not None:
        args["edge_services_route_stage_info"] = unmarshal_EdgeServicesRouteStageInfo(
            field
        )
    else:
        args["edge_services_route_stage_info"] = None

    field = data.get("edge_services_route_rules_info", None)
    if field is not None:
        args["edge_services_route_rules_info"] = unmarshal_EdgeServicesRouteRulesInfo(
            field
        )
    else:
        args["edge_services_route_rules_info"] = None

    field = data.get("edge_services_waf_stage_info", None)
    if field is not None:
        args["edge_services_waf_stage_info"] = unmarshal_EdgeServicesWAFStageInfo(field)
    else:
        args["edge_services_waf_stage_info"] = None

    field = data.get("edge_services_backend_stage_info", None)
    if field is not None:
        args["edge_services_backend_stage_info"] = (
            unmarshal_EdgeServicesBackendStageInfo(field)
        )
    else:
        args["edge_services_backend_stage_info"] = None

    field = data.get("account_contract_signature_info", None)
    if field is not None:
        args["account_contract_signature_info"] = (
            unmarshal_AccountContractSignatureInfo(field)
        )
    else:
        args["account_contract_signature_info"] = None

    field = data.get("vpc_subnet_info", None)
    if field is not None:
        args["vpc_subnet_info"] = unmarshal_VpcSubnetInfo(field)
    else:
        args["vpc_subnet_info"] = None

    field = data.get("vpc_route_info", None)
    if field is not None:
        args["vpc_route_info"] = unmarshal_VpcRouteInfo(field)
    else:
        args["vpc_route_info"] = None

    field = data.get("vpc_private_network_info", None)
    if field is not None:
        args["vpc_private_network_info"] = unmarshal_VpcPrivateNetworkInfo(field)
    else:
        args["vpc_private_network_info"] = None

    field = data.get("audit_trail_export_job_info", None)
    if field is not None:
        args["audit_trail_export_job_info"] = unmarshal_AuditTrailExportJobInfo(field)
    else:
        args["audit_trail_export_job_info"] = None

    field = data.get("vpc_gw_gateway_info", None)
    if field is not None:
        args["vpc_gw_gateway_info"] = unmarshal_VpcGwGatewayInfo(field)
    else:
        args["vpc_gw_gateway_info"] = None

    field = data.get("vpc_gw_gateway_network_info", None)
    if field is not None:
        args["vpc_gw_gateway_network_info"] = unmarshal_VpcGwGatewayNetworkInfo(field)
    else:
        args["vpc_gw_gateway_network_info"] = None

    field = data.get("apple_silicon_runner_info", None)
    if field is not None:
        args["apple_silicon_runner_info"] = unmarshal_AppleSiliconRunnerInfo(field)
    else:
        args["apple_silicon_runner_info"] = None

    return Resource(**args)


def unmarshal_AuthenticationEvent(data: Any) -> AuthenticationEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AuthenticationEvent' failed as data isn't a dictionary."
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

    field = data.get("source_ip", None)
    if field is not None:
        args["source_ip"] = field
    else:
        args["source_ip"] = None

    field = data.get("resources", None)
    if field is not None:
        args["resources"] = (
            [unmarshal_Resource(v) for v in field] if field is not None else None
        )
    else:
        args["resources"] = []

    field = data.get("result", None)
    if field is not None:
        args["result"] = field
    else:
        args["result"] = AuthenticationEventResult.UNKNOWN_RESULT

    field = data.get("method", None)
    if field is not None:
        args["method"] = field
    else:
        args["method"] = AuthenticationEventMethod.UNKNOWN_METHOD

    field = data.get("origin", None)
    if field is not None:
        args["origin"] = field
    else:
        args["origin"] = AuthenticationEventOrigin.UNKNOWN_ORIGIN

    field = data.get("recorded_at", None)
    if field is not None:
        args["recorded_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["recorded_at"] = None

    field = data.get("user_agent", None)
    if field is not None:
        args["user_agent"] = field
    else:
        args["user_agent"] = None

    field = data.get("failure_reason", None)
    if field is not None:
        args["failure_reason"] = field
    else:
        args["failure_reason"] = AuthenticationEventFailureReason.UNKNOWN_FAILURE_REASON

    field = data.get("country_code", None)
    if field is not None:
        args["country_code"] = field
    else:
        args["country_code"] = StdCountryCode.UNKNOWN_COUNTRY_CODE

    field = data.get("mfa_type", None)
    if field is not None:
        args["mfa_type"] = field
    else:
        args["mfa_type"] = AuthenticationEventMFAType.UNKNOWN_MFA_TYPE

    return AuthenticationEvent(**args)


def unmarshal_ListAuthenticationEventsResponse(
    data: Any,
) -> ListAuthenticationEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAuthenticationEventsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("events", None)
    if field is not None:
        args["events"] = (
            [unmarshal_AuthenticationEvent(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["events"] = None

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListAuthenticationEventsResponse(**args)


def unmarshal_EventPrincipal(data: Any) -> EventPrincipal:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EventPrincipal' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    return EventPrincipal(**args)


def unmarshal_Event(data: Any) -> Event:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Event' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("locality", None)
    if field is not None:
        args["locality"] = field
    else:
        args["locality"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("source_ip", None)
    if field is not None:
        args["source_ip"] = field
    else:
        args["source_ip"] = None

    field = data.get("product_name", None)
    if field is not None:
        args["product_name"] = field
    else:
        args["product_name"] = None

    field = data.get("recorded_at", None)
    if field is not None:
        args["recorded_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["recorded_at"] = None

    field = data.get("principal", None)
    if field is not None:
        args["principal"] = unmarshal_EventPrincipal(field)
    else:
        args["principal"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    field = data.get("user_agent", None)
    if field is not None:
        args["user_agent"] = field
    else:
        args["user_agent"] = None

    field = data.get("service_name", None)
    if field is not None:
        args["service_name"] = field
    else:
        args["service_name"] = None

    field = data.get("method_name", None)
    if field is not None:
        args["method_name"] = field
    else:
        args["method_name"] = None

    field = data.get("resources", None)
    if field is not None:
        args["resources"] = (
            [unmarshal_Resource(v) for v in field] if field is not None else None
        )
    else:
        args["resources"] = []

    field = data.get("request_id", None)
    if field is not None:
        args["request_id"] = field
    else:
        args["request_id"] = None

    field = data.get("status_code", None)
    if field is not None:
        args["status_code"] = field
    else:
        args["status_code"] = 0

    field = data.get("request_body", None)
    if field is not None:
        args["request_body"] = field
    else:
        args["request_body"] = {}

    return Event(**args)


def unmarshal_SystemEvent(data: Any) -> SystemEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SystemEvent' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("id", None)
    if field is not None:
        args["id"] = field
    else:
        args["id"] = None

    field = data.get("locality", None)
    if field is not None:
        args["locality"] = field
    else:
        args["locality"] = None

    field = data.get("organization_id", None)
    if field is not None:
        args["organization_id"] = field
    else:
        args["organization_id"] = None

    field = data.get("product_name", None)
    if field is not None:
        args["product_name"] = field
    else:
        args["product_name"] = None

    field = data.get("source", None)
    if field is not None:
        args["source"] = field
    else:
        args["source"] = None

    field = data.get("system_name", None)
    if field is not None:
        args["system_name"] = field
    else:
        args["system_name"] = None

    field = data.get("resources", None)
    if field is not None:
        args["resources"] = (
            [unmarshal_Resource(v) for v in field] if field is not None else None
        )
    else:
        args["resources"] = []

    field = data.get("kind", None)
    if field is not None:
        args["kind"] = field
    else:
        args["kind"] = SystemEventKind.UNKNOWN_KIND

    field = data.get("recorded_at", None)
    if field is not None:
        args["recorded_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["recorded_at"] = None

    field = data.get("project_id", None)
    if field is not None:
        args["project_id"] = field
    else:
        args["project_id"] = None

    return SystemEvent(**args)


def unmarshal_ListCombinedEventsResponseCombinedEvent(
    data: Any,
) -> ListCombinedEventsResponseCombinedEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCombinedEventsResponseCombinedEvent' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("api", None)
    if field is not None:
        args["api"] = unmarshal_Event(field)
    else:
        args["api"] = None

    field = data.get("auth", None)
    if field is not None:
        args["auth"] = unmarshal_AuthenticationEvent(field)
    else:
        args["auth"] = None

    field = data.get("system", None)
    if field is not None:
        args["system"] = unmarshal_SystemEvent(field)
    else:
        args["system"] = None

    return ListCombinedEventsResponseCombinedEvent(**args)


def unmarshal_ListCombinedEventsResponse(data: Any) -> ListCombinedEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCombinedEventsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("events", None)
    if field is not None:
        args["events"] = (
            [unmarshal_ListCombinedEventsResponseCombinedEvent(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["events"] = None

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListCombinedEventsResponse(**args)


def unmarshal_ListEventsResponse(data: Any) -> ListEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListEventsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("events", None)
    if field is not None:
        args["events"] = (
            [unmarshal_Event(v) for v in field] if field is not None else None
        )
    else:
        args["events"] = []

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListEventsResponse(**args)


def unmarshal_ListExportJobsResponse(data: Any) -> ListExportJobsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListExportJobsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("export_jobs", None)
    if field is not None:
        args["export_jobs"] = (
            [unmarshal_ExportJob(v) for v in field] if field is not None else None
        )
    else:
        args["export_jobs"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListExportJobsResponse(**args)


def unmarshal_ProductService(data: Any) -> ProductService:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ProductService' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("methods", None)
    if field is not None:
        args["methods"] = field
    else:
        args["methods"] = None

    return ProductService(**args)


def unmarshal_Product(data: Any) -> Product:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Product' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("title", None)
    if field is not None:
        args["title"] = field
    else:
        args["title"] = None

    field = data.get("name", None)
    if field is not None:
        args["name"] = field
    else:
        args["name"] = None

    field = data.get("services", None)
    if field is not None:
        args["services"] = (
            [unmarshal_ProductService(v) for v in field] if field is not None else None
        )
    else:
        args["services"] = []

    return Product(**args)


def unmarshal_ListProductsResponse(data: Any) -> ListProductsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListProductsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("products", None)
    if field is not None:
        args["products"] = (
            [unmarshal_Product(v) for v in field] if field is not None else None
        )
    else:
        args["products"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListProductsResponse(**args)


def unmarshal_ListSystemEventsResponse(data: Any) -> ListSystemEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSystemEventsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("events", None)
    if field is not None:
        args["events"] = (
            [unmarshal_SystemEvent(v) for v in field] if field is not None else None
        )
    else:
        args["events"] = []

    field = data.get("next_page_token", None)
    if field is not None:
        args["next_page_token"] = field
    else:
        args["next_page_token"] = None

    return ListSystemEventsResponse(**args)


def unmarshal_SetEnabledAlertRulesResponse(data: Any) -> SetEnabledAlertRulesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetEnabledAlertRulesResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("alert_rules", None)
    if field is not None:
        args["alert_rules"] = (
            [unmarshal_AlertRule(v) for v in field] if field is not None else None
        )
    else:
        args["alert_rules"] = []

    return SetEnabledAlertRulesResponse(**args)


def marshal_ExportJobS3(
    request: ExportJobS3,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.bucket is not None:
        output["bucket"] = request.bucket

    if request.region is not None:
        output["region"] = request.region
    else:
        output["region"] = defaults.default_region

    if request.prefix is not None:
        output["prefix"] = request.prefix

    if request.project_id is not None:
        output["project_id"] = request.project_id

    return output


def marshal_CreateExportJobRequest(
    request: CreateExportJobRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    output.update(
        resolve_one_of(
            [
                OneOfPossibility(
                    param="s3", value=request.s3, marshal_func=marshal_ExportJobS3
                ),
            ]
        ),
    )

    if request.name is not None:
        output["name"] = request.name

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_DisableAlertRulesRequest(
    request: DisableAlertRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.alert_rule_ids is not None:
        output["alert_rule_ids"] = request.alert_rule_ids

    return output


def marshal_EnableAlertRulesRequest(
    request: EnableAlertRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.alert_rule_ids is not None:
        output["alert_rule_ids"] = request.alert_rule_ids

    return output


def marshal_SetEnabledAlertRulesRequest(
    request: SetEnabledAlertRulesRequest,
    defaults: ProfileDefaults,
) -> dict[str, Any]:
    output: dict[str, Any] = {}

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id
    else:
        output["organization_id"] = defaults.default_organization_id

    if request.enabled_alert_rule_ids is not None:
        output["enabled_alert_rule_ids"] = request.enabled_alert_rule_ids

    return output
