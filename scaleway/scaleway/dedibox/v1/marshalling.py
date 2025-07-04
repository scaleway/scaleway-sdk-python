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
    AttachFailoverIPToMacAddressRequestMacType,
    BMCAccessStatus,
    BackupStatus,
    FailoverBlockVersion,
    FailoverIPInterfaceType,
    FailoverIPStatus,
    FailoverIPVersion,
    GetRpnStatusResponseStatus,
    IPSemantic,
    IPStatus,
    IPVersion,
    IPv6BlockDelegationStatus,
    InvoicePaymentMethod,
    InvoiceStatus,
    ListFailoverIPsRequestOrderBy,
    ListInvoicesRequestOrderBy,
    ListOSRequestOrderBy,
    ListOffersRequestOrderBy,
    ListRefundsRequestOrderBy,
    ListRpnCapableSanServersRequestOrderBy,
    ListRpnCapableServersRequestOrderBy,
    ListRpnGroupMembersRequestOrderBy,
    ListRpnGroupsRequestOrderBy,
    ListRpnInvitesRequestOrderBy,
    ListRpnSansRequestOrderBy,
    ListRpnServerCapabilitiesRequestOrderBy,
    ListRpnV2CapableResourcesRequestOrderBy,
    ListRpnV2GroupLogsRequestOrderBy,
    ListRpnV2GroupsRequestOrderBy,
    ListRpnV2MembersRequestOrderBy,
    ListRpnV2MembersRequestType,
    ListServerDisksRequestOrderBy,
    ListServerEventsRequestOrderBy,
    ListServersRequestOrderBy,
    ListServicesRequestOrderBy,
    LogAction,
    LogStatus,
    MemoryType,
    NetworkInterfaceInterfaceType,
    OSArch,
    OSType,
    OfferAntiDosInfoType,
    OfferCatalog,
    OfferPaymentFrequency,
    OfferSANInfoType,
    OfferServerInfoStock,
    PartitionFileSystem,
    PartitionType,
    RaidArrayRaidLevel,
    RefundMethod,
    RefundStatus,
    RescueProtocol,
    RpnGroupMemberStatus,
    RpnGroupType,
    RpnSanIpType,
    RpnSanStatus,
    RpnV2GroupStatus,
    RpnV2GroupType,
    RpnV2MemberStatus,
    ServerDiskType,
    ServerInstallStatus,
    ServerStatus,
    ServiceLevelLevel,
    ServiceProvisioningStatus,
    ServiceType,
    IP,
    CPU,
    Disk,
    Memory,
    PersistentMemory,
    RaidController,
    OfferAntiDosInfo,
    OfferBackupInfo,
    OfferBandwidthInfo,
    OfferFailoverBlockInfo,
    OfferFailoverIpInfo,
    OfferLicenseInfo,
    OfferRPNInfo,
    OfferSANInfo,
    OfferServerInfo,
    OfferServiceLevelInfo,
    OfferStorageInfo,
    Offer,
    OS,
    RpnSan,
    RpnGroup,
    NetworkInterface,
    ServerLocation,
    ServerOption,
    ServiceLevel,
    Server,
    RpnV2GroupSubnet,
    RpnV2Group,
    Service,
    FailoverBlock,
    FailoverIP,
    BMCAccess,
    Backup,
    CanOrderResponse,
    CreateFailoverIPsResponse,
    GetIPv6BlockQuotasResponseQuota,
    GetIPv6BlockQuotasResponse,
    GetRemainingQuotaResponse,
    GetRpnStatusResponse,
    IPv6Block,
    Invoice,
    ListFailoverIPsResponse,
    ListIPv6BlockSubnetsAvailableResponseSubnet,
    ListIPv6BlockSubnetsAvailableResponse,
    InvoiceSummary,
    ListInvoicesResponse,
    RpnSanIpRpnV2Group,
    RpnSanIpServer,
    RpnSanIp,
    ListIpsResponse,
    ListOSResponse,
    ListOffersResponse,
    RefundSummary,
    ListRefundsResponse,
    RpnSanServer,
    ListRpnCapableSanServersResponse,
    ListRpnCapableServersResponse,
    RpnGroupMember,
    ListRpnGroupMembersResponse,
    ListRpnGroupsResponse,
    ListRpnInvitesResponse,
    RpnSanSummary,
    ListRpnSansResponse,
    RpnServerCapability,
    ListRpnServerCapabilitiesResponse,
    ListRpnV2CapableResourcesResponse,
    RpnV2Member,
    Log,
    ListRpnV2GroupLogsResponse,
    ListRpnV2GroupsResponse,
    ListRpnV2MembersResponse,
    ServerDisk,
    ListServerDisksResponse,
    ServerEvent,
    ListServerEventsResponse,
    ServerSummary,
    ListServersResponse,
    ListServicesResponse,
    ListSubscribableServerOptionsResponse,
    RaidArray,
    Raid,
    Refund,
    Rescue,
    Partition,
    ServerDefaultPartitioning,
    ServerInstall,
    SubscribeStorageOptionsResponse,
    AttachFailoverIPToMacAddressRequest,
    AttachFailoverIPsRequest,
    CreateFailoverIPsRequest,
    CreateServerRequest,
    DetachFailoverIPsRequest,
    IPv6BlockApiCreateIPv6BlockRequest,
    IPv6BlockApiCreateIPv6BlockSubnetRequest,
    IPv6BlockApiUpdateIPv6BlockRequest,
    InstallPartition,
    InstallServerRequest,
    RpnSanApiAddIpRequest,
    RpnSanApiCreateRpnSanRequest,
    RpnSanApiRemoveIpRequest,
    RpnV1ApiAddRpnGroupMembersRequest,
    RpnV1ApiCreateRpnGroupRequest,
    RpnV1ApiDeleteRpnGroupMembersRequest,
    RpnV1ApiLeaveRpnGroupRequest,
    RpnV1ApiRpnGroupInviteRequest,
    RpnV1ApiUpdateRpnGroupNameRequest,
    RpnV2ApiAddRpnV2MembersRequest,
    RpnV2ApiCreateRpnV2GroupRequest,
    RpnV2ApiDeleteRpnV2MembersRequest,
    RpnV2ApiEnableRpnV2GroupCompatibilityRequest,
    RpnV2ApiUpdateRpnV2GroupNameRequest,
    RpnV2ApiUpdateRpnV2VlanForMembersRequest,
    StartBMCAccessRequest,
    StartRescueRequest,
    SubscribeServerOptionRequest,
    SubscribeStorageOptionsRequest,
    UpdatableRaidArray,
    UpdateRaidRequest,
    UpdateReverseRequest,
    UpdateServerBackupRequest,
    UpdateServerRequest,
    UpdateServerTagsRequest,
)

def unmarshal_IP(data: Any) -> IP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_id", 0)
    args["ip_id"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("reverse", str())
    args["reverse"] = field

    field = data.get("version", getattr(IPVersion, "IPV4"))
    args["version"] = field

    field = data.get("cidr", 0)
    args["cidr"] = field

    field = data.get("netmask", str())
    args["netmask"] = field

    field = data.get("semantic", getattr(IPSemantic, "UNKNOWN"))
    args["semantic"] = field

    field = data.get("gateway", str())
    args["gateway"] = field

    field = data.get("status", getattr(IPStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    return IP(**args)

def unmarshal_CPU(data: Any) -> CPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CPU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("core_count", 0)
    args["core_count"] = field

    field = data.get("thread_count", 0)
    args["thread_count"] = field

    field = data.get("frequency", 0)
    args["frequency"] = field

    return CPU(**args)

def unmarshal_Disk(data: Any) -> Disk:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Disk' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", 0)
    args["capacity"] = field

    field = data.get("type", getattr(ServerDiskType, "SATA"))
    args["type_"] = field

    return Disk(**args)

def unmarshal_Memory(data: Any) -> Memory:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Memory' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", 0)
    args["capacity"] = field

    field = data.get("type", getattr(MemoryType, "DDR2"))
    args["type_"] = field

    field = data.get("frequency", 0)
    args["frequency"] = field

    field = data.get("is_ecc", False)
    args["is_ecc"] = field

    return Memory(**args)

def unmarshal_PersistentMemory(data: Any) -> PersistentMemory:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PersistentMemory' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("capacity", 0)
    args["capacity"] = field

    field = data.get("frequency", 0)
    args["frequency"] = field

    field = data.get("model", str())
    args["model"] = field

    return PersistentMemory(**args)

def unmarshal_RaidController(data: Any) -> RaidController:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RaidController' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("model", str())
    args["model"] = field

    field = data.get("raid_level", [])
    args["raid_level"] = field

    return RaidController(**args)

def unmarshal_OfferAntiDosInfo(data: Any) -> OfferAntiDosInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferAntiDosInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", str())
    args["type_"] = field

    return OfferAntiDosInfo(**args)

def unmarshal_OfferBackupInfo(data: Any) -> OfferBackupInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferBackupInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("size", str())
    args["size"] = field

    return OfferBackupInfo(**args)

def unmarshal_OfferBandwidthInfo(data: Any) -> OfferBandwidthInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferBandwidthInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("speed", str())
    args["speed"] = field

    return OfferBandwidthInfo(**args)

def unmarshal_OfferFailoverBlockInfo(data: Any) -> OfferFailoverBlockInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferFailoverBlockInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("onetime_fees", None)
    args["onetime_fees"] = unmarshal_Offer(field) if field is not None else None

    return OfferFailoverBlockInfo(**args)

def unmarshal_OfferFailoverIpInfo(data: Any) -> OfferFailoverIpInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferFailoverIpInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("onetime_fees", None)
    args["onetime_fees"] = unmarshal_Offer(field) if field is not None else None

    return OfferFailoverIpInfo(**args)

def unmarshal_OfferLicenseInfo(data: Any) -> OfferLicenseInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferLicenseInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bound_to_ip", str())
    args["bound_to_ip"] = field

    return OfferLicenseInfo(**args)

def unmarshal_OfferRPNInfo(data: Any) -> OfferRPNInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferRPNInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("speed", str())
    args["speed"] = field

    return OfferRPNInfo(**args)

def unmarshal_OfferSANInfo(data: Any) -> OfferSANInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferSANInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("ha", False)
    args["ha"] = field

    field = data.get("device_type", getattr(OfferSANInfoType, "HDD"))
    args["device_type"] = field

    return OfferSANInfo(**args)

def unmarshal_OfferServerInfo(data: Any) -> OfferServerInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferServerInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bandwidth", str())
    args["bandwidth"] = field

    field = data.get("stock", str())
    args["stock"] = field

    field = data.get("commercial_range", str())
    args["commercial_range"] = field

    field = data.get("disks", str())
    args["disks"] = [unmarshal_Disk(v) for v in field] if field is not None else None

    field = data.get("cpus", str())
    args["cpus"] = [unmarshal_CPU(v) for v in field] if field is not None else None

    field = data.get("memories", str())
    args["memories"] = [unmarshal_Memory(v) for v in field] if field is not None else None

    field = data.get("persistent_memories", str())
    args["persistent_memories"] = [unmarshal_PersistentMemory(v) for v in field] if field is not None else None

    field = data.get("raid_controllers", str())
    args["raid_controllers"] = [unmarshal_RaidController(v) for v in field] if field is not None else None

    field = data.get("available_options", str())
    args["available_options"] = [unmarshal_Offer(v) for v in field] if field is not None else None

    field = data.get("connectivity", str())
    args["connectivity"] = field

    field = data.get("stock_by_datacenter", str())
    args["stock_by_datacenter"] = {key: OfferServerInfoStock(value)for key, value in field.items()
    } if field is not None else None

    field = data.get("rpn_version", None)
    args["rpn_version"] = field

    field = data.get("onetime_fees", None)
    args["onetime_fees"] = unmarshal_Offer(field) if field is not None else None

    return OfferServerInfo(**args)

def unmarshal_OfferServiceLevelInfo(data: Any) -> OfferServiceLevelInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferServiceLevelInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("support_ticket", str())
    args["support_ticket"] = field

    field = data.get("support_phone", str())
    args["support_phone"] = field

    field = data.get("sales_support", str())
    args["sales_support"] = field

    field = data.get("git", str())
    args["git"] = field

    field = data.get("sla", str())
    args["sla"] = field

    field = data.get("priority_support", str())
    args["priority_support"] = field

    field = data.get("high_rpn_bandwidth", str())
    args["high_rpn_bandwidth"] = field

    field = data.get("customization", str())
    args["customization"] = field

    field = data.get("antidos", str())
    args["antidos"] = field

    field = data.get("extra_failover_quota", str())
    args["extra_failover_quota"] = field

    field = data.get("available_options", str())
    args["available_options"] = [unmarshal_Offer(v) for v in field] if field is not None else None

    return OfferServiceLevelInfo(**args)

def unmarshal_OfferStorageInfo(data: Any) -> OfferStorageInfo:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OfferStorageInfo' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("max_quota", str())
    args["max_quota"] = field

    field = data.get("size", str())
    args["size"] = field

    return OfferStorageInfo(**args)

def unmarshal_Offer(data: Any) -> Offer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Offer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("catalog", getattr(OfferCatalog, "ALL"))
    args["catalog"] = field

    field = data.get("payment_frequency", getattr(OfferPaymentFrequency, "MONTHLY"))
    args["payment_frequency"] = field

    field = data.get("pricing", None)
    args["pricing"] = unmarshal_Money(field) if field is not None else None

    field = data.get("server_info", None)
    args["server_info"] = unmarshal_OfferServerInfo(field) if field is not None else None

    field = data.get("service_level_info", None)
    args["service_level_info"] = unmarshal_OfferServiceLevelInfo(field) if field is not None else None

    field = data.get("rpn_info", None)
    args["rpn_info"] = unmarshal_OfferRPNInfo(field) if field is not None else None

    field = data.get("san_info", None)
    args["san_info"] = unmarshal_OfferSANInfo(field) if field is not None else None

    field = data.get("antidos_info", None)
    args["antidos_info"] = unmarshal_OfferAntiDosInfo(field) if field is not None else None

    field = data.get("backup_info", None)
    args["backup_info"] = unmarshal_OfferBackupInfo(field) if field is not None else None

    field = data.get("usb_storage_info", None)
    args["usb_storage_info"] = unmarshal_OfferStorageInfo(field) if field is not None else None

    field = data.get("storage_info", None)
    args["storage_info"] = unmarshal_OfferStorageInfo(field) if field is not None else None

    field = data.get("license_info", None)
    args["license_info"] = unmarshal_OfferLicenseInfo(field) if field is not None else None

    field = data.get("failover_ip_info", None)
    args["failover_ip_info"] = unmarshal_OfferFailoverIpInfo(field) if field is not None else None

    field = data.get("failover_block_info", None)
    args["failover_block_info"] = unmarshal_OfferFailoverBlockInfo(field) if field is not None else None

    field = data.get("bandwidth_info", None)
    args["bandwidth_info"] = unmarshal_OfferBandwidthInfo(field) if field is not None else None

    return Offer(**args)

def unmarshal_OS(data: Any) -> OS:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'OS' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("type", getattr(OSType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("version", str())
    args["version"] = field

    field = data.get("arch", getattr(OSArch, "UNKNOWN_ARCH"))
    args["arch"] = field

    field = data.get("allow_custom_partitioning", False)
    args["allow_custom_partitioning"] = field

    field = data.get("allow_ssh_keys", False)
    args["allow_ssh_keys"] = field

    field = data.get("requires_user", False)
    args["requires_user"] = field

    field = data.get("requires_admin_password", False)
    args["requires_admin_password"] = field

    field = data.get("requires_panel_password", False)
    args["requires_panel_password"] = field

    field = data.get("allowed_filesystems", [])
    args["allowed_filesystems"] = [PartitionFileSystem(v) for v in field] if field is not None else None

    field = data.get("requires_license", False)
    args["requires_license"] = field

    field = data.get("license_offers", [])
    args["license_offers"] = [unmarshal_Offer(v) for v in field] if field is not None else None

    field = data.get("display_name", str())
    args["display_name"] = field

    field = data.get("password_regex", str())
    args["password_regex"] = field

    field = data.get("hostname_max_length", 0)
    args["hostname_max_length"] = field

    field = data.get("max_partitions", None)
    args["max_partitions"] = field

    field = data.get("panel_password_regex", None)
    args["panel_password_regex"] = field

    field = data.get("requires_valid_hostname", None)
    args["requires_valid_hostname"] = field

    field = data.get("hostname_regex", None)
    args["hostname_regex"] = field

    field = data.get("released_at", None)
    args["released_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return OS(**args)

def unmarshal_RpnSan(data: Any) -> RpnSan:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnSan' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("datacenter_name", str())
    args["datacenter_name"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("server_hostname", str())
    args["server_hostname"] = field

    field = data.get("iqn_suffix", str())
    args["iqn_suffix"] = field

    field = data.get("offer_id", 0)
    args["offer_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("offer_name", str())
    args["offer_name"] = field

    field = data.get("status", getattr(RpnSanStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("storage_size", 0)
    args["storage_size"] = field

    field = data.get("iqn", str())
    args["iqn"] = field

    field = data.get("rpnv1_compatible", False)
    args["rpnv1_compatible"] = field

    field = data.get("rpnv1_implicit", False)
    args["rpnv1_implicit"] = field

    field = data.get("offer", None)
    args["offer"] = unmarshal_Offer(field) if field is not None else None

    field = data.get("delivered_at", None)
    args["delivered_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("terminated_at", None)
    args["terminated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return RpnSan(**args)

def unmarshal_RpnGroup(data: Any) -> RpnGroup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnGroup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("type", getattr(RpnGroupType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("active", False)
    args["active"] = field

    field = data.get("owner", str())
    args["owner"] = field

    field = data.get("members_count", 0)
    args["members_count"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return RpnGroup(**args)

def unmarshal_NetworkInterface(data: Any) -> NetworkInterface:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'NetworkInterface' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("card_id", 0)
    args["card_id"] = field

    field = data.get("device_id", 0)
    args["device_id"] = field

    field = data.get("mac", str())
    args["mac"] = field

    field = data.get("type", getattr(NetworkInterfaceInterfaceType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("ips", [])
    args["ips"] = [unmarshal_IP(v) for v in field] if field is not None else None

    return NetworkInterface(**args)

def unmarshal_ServerLocation(data: Any) -> ServerLocation:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerLocation' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rack", str())
    args["rack"] = field

    field = data.get("room", str())
    args["room"] = field

    field = data.get("datacenter_name", str())
    args["datacenter_name"] = field

    return ServerLocation(**args)

def unmarshal_ServerOption(data: Any) -> ServerOption:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerOption' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("options", str())
    args["options"] = [unmarshal_ServerOption(v) for v in field] if field is not None else None

    field = data.get("offer", None)
    args["offer"] = unmarshal_Offer(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return ServerOption(**args)

def unmarshal_ServiceLevel(data: Any) -> ServiceLevel:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServiceLevel' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("offer_id", 0)
    args["offer_id"] = field

    field = data.get("level", getattr(ServiceLevelLevel, "UNKNOWN"))
    args["level"] = field

    return ServiceLevel(**args)

def unmarshal_Server(data: Any) -> Server:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Server' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("status", getattr(ServerStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("rebooted_at", None)
    args["rebooted_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("abuse_contact", str())
    args["abuse_contact"] = field

    field = data.get("interfaces", [])
    args["interfaces"] = [unmarshal_NetworkInterface(v) for v in field] if field is not None else None

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("options", [])
    args["options"] = [unmarshal_ServerOption(v) for v in field] if field is not None else None

    field = data.get("has_bmc", False)
    args["has_bmc"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("is_outsourced", False)
    args["is_outsourced"] = field

    field = data.get("ipv6_slaac", False)
    args["ipv6_slaac"] = field

    field = data.get("qinq", False)
    args["qinq"] = field

    field = data.get("is_rpnv2_member", False)
    args["is_rpnv2_member"] = field

    field = data.get("is_hds", False)
    args["is_hds"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("offer", None)
    args["offer"] = unmarshal_Offer(field) if field is not None else None

    field = data.get("location", None)
    args["location"] = unmarshal_ServerLocation(field) if field is not None else None

    field = data.get("os", None)
    args["os"] = unmarshal_OS(field) if field is not None else None

    field = data.get("level", None)
    args["level"] = unmarshal_ServiceLevel(field) if field is not None else None

    field = data.get("rescue_os", None)
    args["rescue_os"] = unmarshal_OS(field) if field is not None else None

    return Server(**args)

def unmarshal_RpnV2GroupSubnet(data: Any) -> RpnV2GroupSubnet:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnV2GroupSubnet' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address", str())
    args["address"] = field

    field = data.get("cidr", str())
    args["cidr"] = field

    return RpnV2GroupSubnet(**args)

def unmarshal_RpnV2Group(data: Any) -> RpnV2Group:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnV2Group' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("compatible_rpnv1", False)
    args["compatible_rpnv1"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("type", getattr(RpnV2GroupType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("status", getattr(RpnV2GroupStatus, "UNKNOWN_GROUP_STATUS"))
    args["status"] = field

    field = data.get("owner", str())
    args["owner"] = field

    field = data.get("members_count", 0)
    args["members_count"] = field

    field = data.get("gateway", str())
    args["gateway"] = field

    field = data.get("subnet", None)
    args["subnet"] = unmarshal_RpnV2GroupSubnet(field) if field is not None else None

    field = data.get("rpnv1_group", None)
    args["rpnv1_group"] = unmarshal_RpnGroup(field) if field is not None else None

    return RpnV2Group(**args)

def unmarshal_Service(data: Any) -> Service:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Service' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("provisioning_status", getattr(ServiceProvisioningStatus, "UNKNOWN"))
    args["provisioning_status"] = field

    field = data.get("type", getattr(ServiceType, "UNKNOWN_TYPE"))
    args["type_"] = field

    field = data.get("resource_id", None)
    args["resource_id"] = field

    field = data.get("offer", None)
    args["offer"] = unmarshal_Offer(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("delivered_at", None)
    args["delivered_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("terminated_at", None)
    args["terminated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Service(**args)

def unmarshal_FailoverBlock(data: Any) -> FailoverBlock:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'FailoverBlock' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("nameservers", [])
    args["nameservers"] = field

    field = data.get("ip_version", getattr(FailoverBlockVersion, "UNKNOWN_VERSION"))
    args["ip_version"] = field

    field = data.get("cidr", 0)
    args["cidr"] = field

    field = data.get("netmask", str())
    args["netmask"] = field

    field = data.get("gateway_ip", str())
    args["gateway_ip"] = field

    return FailoverBlock(**args)

def unmarshal_FailoverIP(data: Any) -> FailoverIP:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'FailoverIP' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("reverse", str())
    args["reverse"] = field

    field = data.get("ip_version", getattr(FailoverIPVersion, "UNKNOWN_VERSION"))
    args["ip_version"] = field

    field = data.get("cidr", 0)
    args["cidr"] = field

    field = data.get("netmask", str())
    args["netmask"] = field

    field = data.get("gateway_ip", str())
    args["gateway_ip"] = field

    field = data.get("status", getattr(FailoverIPStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("type", getattr(FailoverIPInterfaceType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("mac", None)
    args["mac"] = field

    field = data.get("server_id", None)
    args["server_id"] = field

    field = data.get("block", None)
    args["block"] = unmarshal_FailoverBlock(field) if field is not None else None

    field = data.get("server_zone", None)
    args["server_zone"] = field

    return FailoverIP(**args)

def unmarshal_BMCAccess(data: Any) -> BMCAccess:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BMCAccess' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("url", str())
    args["url"] = field

    field = data.get("login", str())
    args["login"] = field

    field = data.get("password", str())
    args["password"] = field

    field = data.get("status", getattr(BMCAccessStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return BMCAccess(**args)

def unmarshal_Backup(data: Any) -> Backup:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Backup' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("login", str())
    args["login"] = field

    field = data.get("server", str())
    args["server"] = field

    field = data.get("status", getattr(BackupStatus, "UNKNOWN_BACKUP_STATUS"))
    args["status"] = field

    field = data.get("acl_enabled", False)
    args["acl_enabled"] = field

    field = data.get("autologin", False)
    args["autologin"] = field

    field = data.get("quota_space", 0)
    args["quota_space"] = field

    field = data.get("quota_space_used", 0)
    args["quota_space_used"] = field

    field = data.get("quota_files", 0)
    args["quota_files"] = field

    field = data.get("quota_files_used", 0)
    args["quota_files_used"] = field

    return Backup(**args)

def unmarshal_CanOrderResponse(data: Any) -> CanOrderResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CanOrderResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("can_order", str())
    args["can_order"] = field

    field = data.get("quota_ok", str())
    args["quota_ok"] = field

    field = data.get("phone_confirmed", str())
    args["phone_confirmed"] = field

    field = data.get("email_confirmed", str())
    args["email_confirmed"] = field

    field = data.get("user_confirmed", str())
    args["user_confirmed"] = field

    field = data.get("payment_mode", str())
    args["payment_mode"] = field

    field = data.get("billing_ok", str())
    args["billing_ok"] = field

    field = data.get("message", None)
    args["message"] = field

    return CanOrderResponse(**args)

def unmarshal_CreateFailoverIPsResponse(data: Any) -> CreateFailoverIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateFailoverIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("services", str())
    args["services"] = [unmarshal_Service(v) for v in field] if field is not None else None

    return CreateFailoverIPsResponse(**args)

def unmarshal_GetIPv6BlockQuotasResponseQuota(data: Any) -> GetIPv6BlockQuotasResponseQuota:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetIPv6BlockQuotasResponseQuota' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("quota", str())
    args["quota"] = field

    field = data.get("cidr", str())
    args["cidr"] = field

    return GetIPv6BlockQuotasResponseQuota(**args)

def unmarshal_GetIPv6BlockQuotasResponse(data: Any) -> GetIPv6BlockQuotasResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetIPv6BlockQuotasResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("quotas", [])
    args["quotas"] = [unmarshal_GetIPv6BlockQuotasResponseQuota(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return GetIPv6BlockQuotasResponse(**args)

def unmarshal_GetRemainingQuotaResponse(data: Any) -> GetRemainingQuotaResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetRemainingQuotaResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("failover_ip_quota", 0)
    args["failover_ip_quota"] = field

    field = data.get("failover_ip_remaining_quota", 0)
    args["failover_ip_remaining_quota"] = field

    field = data.get("failover_block_quota", 0)
    args["failover_block_quota"] = field

    field = data.get("failover_block_remaining_quota", 0)
    args["failover_block_remaining_quota"] = field

    return GetRemainingQuotaResponse(**args)

def unmarshal_GetRpnStatusResponse(data: Any) -> GetRpnStatusResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetRpnStatusResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", getattr(GetRpnStatusResponseStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("operations_left", None)
    args["operations_left"] = field

    return GetRpnStatusResponse(**args)

def unmarshal_IPv6Block(data: Any) -> IPv6Block:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'IPv6Block' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("address", str())
    args["address"] = field

    field = data.get("duid", str())
    args["duid"] = field

    field = data.get("nameservers", [])
    args["nameservers"] = field

    field = data.get("cidr", 0)
    args["cidr"] = field

    field = data.get("subnets", [])
    args["subnets"] = [unmarshal_IPv6Block(v) for v in field] if field is not None else None

    field = data.get("delegation_status", getattr(IPv6BlockDelegationStatus, "UNKNOWN_STATUS"))
    args["delegation_status"] = field

    return IPv6Block(**args)

def unmarshal_Invoice(data: Any) -> Invoice:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Invoice' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("payment_method", str())
    args["payment_method"] = field

    field = data.get("content", str())
    args["content"] = field

    field = data.get("transaction_id", str())
    args["transaction_id"] = field

    field = data.get("total_with_taxes", None)
    args["total_with_taxes"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_without_taxes", None)
    args["total_without_taxes"] = unmarshal_Money(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("paid_at", None)
    args["paid_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Invoice(**args)

def unmarshal_ListFailoverIPsResponse(data: Any) -> ListFailoverIPsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFailoverIPsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("failover_ips", [])
    args["failover_ips"] = [unmarshal_FailoverIP(v) for v in field] if field is not None else None

    return ListFailoverIPsResponse(**args)

def unmarshal_ListIPv6BlockSubnetsAvailableResponseSubnet(data: Any) -> ListIPv6BlockSubnetsAvailableResponseSubnet:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIPv6BlockSubnetsAvailableResponseSubnet' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("address", str())
    args["address"] = field

    field = data.get("cidr", str())
    args["cidr"] = field

    return ListIPv6BlockSubnetsAvailableResponseSubnet(**args)

def unmarshal_ListIPv6BlockSubnetsAvailableResponse(data: Any) -> ListIPv6BlockSubnetsAvailableResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIPv6BlockSubnetsAvailableResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subnet_availables", [])
    args["subnet_availables"] = [unmarshal_ListIPv6BlockSubnetsAvailableResponseSubnet(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListIPv6BlockSubnetsAvailableResponse(**args)

def unmarshal_InvoiceSummary(data: Any) -> InvoiceSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'InvoiceSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("payment_method", str())
    args["payment_method"] = field

    field = data.get("transaction_id", str())
    args["transaction_id"] = field

    field = data.get("total_with_taxes", None)
    args["total_with_taxes"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_without_taxes", None)
    args["total_without_taxes"] = unmarshal_Money(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("paid_at", None)
    args["paid_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return InvoiceSummary(**args)

def unmarshal_ListInvoicesResponse(data: Any) -> ListInvoicesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListInvoicesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("invoices", str())
    args["invoices"] = [unmarshal_InvoiceSummary(v) for v in field] if field is not None else None

    return ListInvoicesResponse(**args)

def unmarshal_RpnSanIpRpnV2Group(data: Any) -> RpnSanIpRpnV2Group:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnSanIpRpnV2Group' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    return RpnSanIpRpnV2Group(**args)

def unmarshal_RpnSanIpServer(data: Any) -> RpnSanIpServer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnSanIpServer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("datacenter_name", str())
    args["datacenter_name"] = field

    return RpnSanIpServer(**args)

def unmarshal_RpnSanIp(data: Any) -> RpnSanIp:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnSanIp' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(RpnSanIpType, "UNKNOWN"))
    args["type_"] = field

    field = data.get("server", None)
    args["server"] = unmarshal_RpnSanIpServer(field) if field is not None else None

    field = data.get("rpnv2_group", None)
    args["rpnv2_group"] = unmarshal_RpnSanIpRpnV2Group(field) if field is not None else None

    field = data.get("ip", None)
    args["ip"] = unmarshal_IP(field) if field is not None else None

    return RpnSanIp(**args)

def unmarshal_ListIpsResponse(data: Any) -> ListIpsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIpsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("ips", [])
    args["ips"] = [unmarshal_RpnSanIp(v) for v in field] if field is not None else None

    return ListIpsResponse(**args)

def unmarshal_ListOSResponse(data: Any) -> ListOSResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOSResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("os", [])
    args["os"] = [unmarshal_OS(v) for v in field] if field is not None else None

    return ListOSResponse(**args)

def unmarshal_ListOffersResponse(data: Any) -> ListOffersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListOffersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("offers", [])
    args["offers"] = [unmarshal_Offer(v) for v in field] if field is not None else None

    return ListOffersResponse(**args)

def unmarshal_RefundSummary(data: Any) -> RefundSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RefundSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("method", str())
    args["method"] = field

    field = data.get("total_with_taxes", None)
    args["total_with_taxes"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_without_taxes", None)
    args["total_without_taxes"] = unmarshal_Money(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("refunded_at", None)
    args["refunded_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return RefundSummary(**args)

def unmarshal_ListRefundsResponse(data: Any) -> ListRefundsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRefundsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("refunds", str())
    args["refunds"] = [unmarshal_RefundSummary(v) for v in field] if field is not None else None

    return ListRefundsResponse(**args)

def unmarshal_RpnSanServer(data: Any) -> RpnSanServer:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnSanServer' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("datacenter_name", str())
    args["datacenter_name"] = field

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("sans", [])
    args["sans"] = [unmarshal_RpnSan(v) for v in field] if field is not None else None

    field = data.get("zone", )
    args["zone"] = field

    return RpnSanServer(**args)

def unmarshal_ListRpnCapableSanServersResponse(data: Any) -> ListRpnCapableSanServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnCapableSanServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("san_servers", [])
    args["san_servers"] = [unmarshal_RpnSanServer(v) for v in field] if field is not None else None

    return ListRpnCapableSanServersResponse(**args)

def unmarshal_ListRpnCapableServersResponse(data: Any) -> ListRpnCapableServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnCapableServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("servers", [])
    args["servers"] = [unmarshal_Server(v) for v in field] if field is not None else None

    return ListRpnCapableServersResponse(**args)

def unmarshal_RpnGroupMember(data: Any) -> RpnGroupMember:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnGroupMember' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("status", getattr(RpnGroupMemberStatus, "UNKNOWN_RPN_MEMBER_STATUS"))
    args["status"] = field

    field = data.get("group_id", 0)
    args["group_id"] = field

    field = data.get("group_name", str())
    args["group_name"] = field

    field = data.get("group_owner", str())
    args["group_owner"] = field

    field = data.get("owner", str())
    args["owner"] = field

    field = data.get("san_server", None)
    args["san_server"] = unmarshal_RpnSanServer(field) if field is not None else None

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    field = data.get("speed", None)
    args["speed"] = field

    return RpnGroupMember(**args)

def unmarshal_ListRpnGroupMembersResponse(data: Any) -> ListRpnGroupMembersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnGroupMembersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("members", [])
    args["members"] = [unmarshal_RpnGroupMember(v) for v in field] if field is not None else None

    return ListRpnGroupMembersResponse(**args)

def unmarshal_ListRpnGroupsResponse(data: Any) -> ListRpnGroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnGroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("rpn_groups", [])
    args["rpn_groups"] = [unmarshal_RpnGroup(v) for v in field] if field is not None else None

    return ListRpnGroupsResponse(**args)

def unmarshal_ListRpnInvitesResponse(data: Any) -> ListRpnInvitesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnInvitesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("members", [])
    args["members"] = [unmarshal_RpnGroupMember(v) for v in field] if field is not None else None

    return ListRpnInvitesResponse(**args)

def unmarshal_RpnSanSummary(data: Any) -> RpnSanSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnSanSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("datacenter_name", str())
    args["datacenter_name"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("server_hostname", str())
    args["server_hostname"] = field

    field = data.get("iqn_suffix", str())
    args["iqn_suffix"] = field

    field = data.get("offer_id", 0)
    args["offer_id"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("offer_name", str())
    args["offer_name"] = field

    field = data.get("status", getattr(RpnSanStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("storage_size", 0)
    args["storage_size"] = field

    field = data.get("rpnv1_compatible", False)
    args["rpnv1_compatible"] = field

    field = data.get("rpnv1_implicit", False)
    args["rpnv1_implicit"] = field

    field = data.get("delivered_at", None)
    args["delivered_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("terminated_at", None)
    args["terminated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return RpnSanSummary(**args)

def unmarshal_ListRpnSansResponse(data: Any) -> ListRpnSansResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnSansResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("rpn_sans", [])
    args["rpn_sans"] = [unmarshal_RpnSanSummary(v) for v in field] if field is not None else None

    return ListRpnSansResponse(**args)

def unmarshal_RpnServerCapability(data: Any) -> RpnServerCapability:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnServerCapability' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("datacenter_name", str())
    args["datacenter_name"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("compatible_qinq", False)
    args["compatible_qinq"] = field

    field = data.get("can_join_qinq_group", False)
    args["can_join_qinq_group"] = field

    field = data.get("rpnv1_group_count", 0)
    args["rpnv1_group_count"] = field

    field = data.get("rpnv2_group_count", 0)
    args["rpnv2_group_count"] = field

    field = data.get("can_join_rpnv2_group", False)
    args["can_join_rpnv2_group"] = field

    field = data.get("ip_address", None)
    args["ip_address"] = field

    field = data.get("rpn_version", None)
    args["rpn_version"] = field

    return RpnServerCapability(**args)

def unmarshal_ListRpnServerCapabilitiesResponse(data: Any) -> ListRpnServerCapabilitiesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnServerCapabilitiesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("servers", [])
    args["servers"] = [unmarshal_RpnServerCapability(v) for v in field] if field is not None else None

    return ListRpnServerCapabilitiesResponse(**args)

def unmarshal_ListRpnV2CapableResourcesResponse(data: Any) -> ListRpnV2CapableResourcesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnV2CapableResourcesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("servers", [])
    args["servers"] = [unmarshal_Server(v) for v in field] if field is not None else None

    return ListRpnV2CapableResourcesResponse(**args)

def unmarshal_RpnV2Member(data: Any) -> RpnV2Member:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RpnV2Member' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("status", getattr(RpnV2MemberStatus, "UNKNOWN_MEMBER_STATUS"))
    args["status"] = field

    field = data.get("vlan", str())
    args["vlan"] = field

    field = data.get("server", None)
    args["server"] = unmarshal_Server(field) if field is not None else None

    field = data.get("rpnv1_group", None)
    args["rpnv1_group"] = unmarshal_RpnGroup(field) if field is not None else None

    field = data.get("speed", None)
    args["speed"] = field

    return RpnV2Member(**args)

def unmarshal_Log(data: Any) -> Log:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Log' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("action", getattr(LogAction, "UNKNOWN_LOG_ACTION"))
    args["action"] = field

    field = data.get("status", getattr(LogStatus, "UNKNOWN_LOG_STATUS"))
    args["status"] = field

    field = data.get("group", None)
    args["group"] = unmarshal_RpnV2Group(field) if field is not None else None

    field = data.get("member", None)
    args["member"] = unmarshal_RpnV2Member(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("finished_at", None)
    args["finished_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Log(**args)

def unmarshal_ListRpnV2GroupLogsResponse(data: Any) -> ListRpnV2GroupLogsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnV2GroupLogsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("logs", [])
    args["logs"] = [unmarshal_Log(v) for v in field] if field is not None else None

    return ListRpnV2GroupLogsResponse(**args)

def unmarshal_ListRpnV2GroupsResponse(data: Any) -> ListRpnV2GroupsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnV2GroupsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("rpn_groups", [])
    args["rpn_groups"] = [unmarshal_RpnV2Group(v) for v in field] if field is not None else None

    return ListRpnV2GroupsResponse(**args)

def unmarshal_ListRpnV2MembersResponse(data: Any) -> ListRpnV2MembersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRpnV2MembersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("members", [])
    args["members"] = [unmarshal_RpnV2Member(v) for v in field] if field is not None else None

    return ListRpnV2MembersResponse(**args)

def unmarshal_ServerDisk(data: Any) -> ServerDisk:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerDisk' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("connector", str())
    args["connector"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("capacity", str())
    args["capacity"] = field

    field = data.get("is_addon", str())
    args["is_addon"] = field

    return ServerDisk(**args)

def unmarshal_ListServerDisksResponse(data: Any) -> ListServerDisksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerDisksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("disks", [])
    args["disks"] = [unmarshal_ServerDisk(v) for v in field] if field is not None else None

    return ListServerDisksResponse(**args)

def unmarshal_ServerEvent(data: Any) -> ServerEvent:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerEvent' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("event_id", 0)
    args["event_id"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("date", None)
    args["date"] = parser.isoparse(field) if isinstance(field, str) else field

    return ServerEvent(**args)

def unmarshal_ListServerEventsResponse(data: Any) -> ListServerEventsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServerEventsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("events", [])
    args["events"] = [unmarshal_ServerEvent(v) for v in field] if field is not None else None

    return ListServerEventsResponse(**args)

def unmarshal_ServerSummary(data: Any) -> ServerSummary:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerSummary' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", 0)
    args["id"] = field

    field = data.get("datacenter_name", str())
    args["datacenter_name"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("expired_at", None)
    args["expired_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("offer_id", 0)
    args["offer_id"] = field

    field = data.get("offer_name", str())
    args["offer_name"] = field

    field = data.get("status", getattr(ServerStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("interfaces", [])
    args["interfaces"] = [unmarshal_NetworkInterface(v) for v in field] if field is not None else None

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("is_outsourced", False)
    args["is_outsourced"] = field

    field = data.get("qinq", False)
    args["qinq"] = field

    field = data.get("is_hds", False)
    args["is_hds"] = field

    field = data.get("os_id", None)
    args["os_id"] = field

    field = data.get("level", None)
    args["level"] = unmarshal_ServiceLevel(field) if field is not None else None

    field = data.get("rpn_version", None)
    args["rpn_version"] = field

    return ServerSummary(**args)

def unmarshal_ListServersResponse(data: Any) -> ListServersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("servers", [])
    args["servers"] = [unmarshal_ServerSummary(v) for v in field] if field is not None else None

    return ListServersResponse(**args)

def unmarshal_ListServicesResponse(data: Any) -> ListServicesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListServicesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("services", [])
    args["services"] = [unmarshal_Service(v) for v in field] if field is not None else None

    return ListServicesResponse(**args)

def unmarshal_ListSubscribableServerOptionsResponse(data: Any) -> ListSubscribableServerOptionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSubscribableServerOptionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", 0)
    args["total_count"] = field

    field = data.get("server_options", [])
    args["server_options"] = [unmarshal_Offer(v) for v in field] if field is not None else None

    return ListSubscribableServerOptionsResponse(**args)

def unmarshal_RaidArray(data: Any) -> RaidArray:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RaidArray' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("raid_level", getattr(RaidArrayRaidLevel, "NO_RAID"))
    args["raid_level"] = field

    field = data.get("disks", [])
    args["disks"] = [unmarshal_ServerDisk(v) for v in field] if field is not None else None

    return RaidArray(**args)

def unmarshal_Raid(data: Any) -> Raid:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Raid' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("raid_arrays", [])
    args["raid_arrays"] = [unmarshal_RaidArray(v) for v in field] if field is not None else None

    return Raid(**args)

def unmarshal_Refund(data: Any) -> Refund:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Refund' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("method", str())
    args["method"] = field

    field = data.get("content", str())
    args["content"] = field

    field = data.get("total_with_taxes", None)
    args["total_with_taxes"] = unmarshal_Money(field) if field is not None else None

    field = data.get("total_without_taxes", None)
    args["total_without_taxes"] = unmarshal_Money(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("refunded_at", None)
    args["refunded_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Refund(**args)

def unmarshal_Rescue(data: Any) -> Rescue:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Rescue' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("os_id", 0)
    args["os_id"] = field

    field = data.get("login", str())
    args["login"] = field

    field = data.get("password", str())
    args["password"] = field

    field = data.get("protocol", getattr(RescueProtocol, "VNC"))
    args["protocol"] = field

    return Rescue(**args)

def unmarshal_Partition(data: Any) -> Partition:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Partition' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(PartitionType, "PRIMARY"))
    args["type_"] = field

    field = data.get("file_system", getattr(PartitionFileSystem, "UNKNOWN"))
    args["file_system"] = field

    field = data.get("raid_level", getattr(RaidArrayRaidLevel, "NO_RAID"))
    args["raid_level"] = field

    field = data.get("capacity", 0)
    args["capacity"] = field

    field = data.get("connectors", [])
    args["connectors"] = field

    field = data.get("mount_point", None)
    args["mount_point"] = field

    return Partition(**args)

def unmarshal_ServerDefaultPartitioning(data: Any) -> ServerDefaultPartitioning:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerDefaultPartitioning' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("partitions", [])
    args["partitions"] = [unmarshal_Partition(v) for v in field] if field is not None else None

    return ServerDefaultPartitioning(**args)

def unmarshal_ServerInstall(data: Any) -> ServerInstall:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ServerInstall' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("os_id", str())
    args["os_id"] = field

    field = data.get("hostname", str())
    args["hostname"] = field

    field = data.get("partitions", str())
    args["partitions"] = [unmarshal_Partition(v) for v in field] if field is not None else None

    field = data.get("ssh_key_ids", str())
    args["ssh_key_ids"] = field

    field = data.get("status", str())
    args["status"] = field

    field = data.get("user_login", None)
    args["user_login"] = field

    field = data.get("panel_url", None)
    args["panel_url"] = field

    return ServerInstall(**args)

def unmarshal_SubscribeStorageOptionsResponse(data: Any) -> SubscribeStorageOptionsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SubscribeStorageOptionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("services", [])
    args["services"] = [unmarshal_Service(v) for v in field] if field is not None else None

    return SubscribeStorageOptionsResponse(**args)

def marshal_AttachFailoverIPToMacAddressRequest(
    request: AttachFailoverIPToMacAddressRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = None

    if request.mac is not None:
        output["mac"] = request.mac
    else:
        output["mac"] = None


    return output

def marshal_AttachFailoverIPsRequest(
    request: AttachFailoverIPsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_id is not None:
        output["server_id"] = request.server_id
    else:
        output["server_id"] = 0

    if request.fips_ids is not None:
        output["fips_ids"] = request.fips_ids
    else:
        output["fips_ids"] = str()


    return output

def marshal_CreateFailoverIPsRequest(
    request: CreateFailoverIPsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id
    else:
        output["offer_id"] = 0

    if request.quantity is not None:
        output["quantity"] = request.quantity
    else:
        output["quantity"] = 0

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_CreateServerRequest(
    request: CreateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id
    else:
        output["offer_id"] = 0

    if request.server_option_ids is not None:
        output["server_option_ids"] = request.server_option_ids
    else:
        output["server_option_ids"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.datacenter_name is not None:
        output["datacenter_name"] = request.datacenter_name
    else:
        output["datacenter_name"] = None


    return output

def marshal_DetachFailoverIPsRequest(
    request: DetachFailoverIPsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.fips_ids is not None:
        output["fips_ids"] = request.fips_ids
    else:
        output["fips_ids"] = str()


    return output

def marshal_IPv6BlockApiCreateIPv6BlockRequest(
    request: IPv6BlockApiCreateIPv6BlockRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id
    else:
        output["project_id"] = None


    return output

def marshal_IPv6BlockApiCreateIPv6BlockSubnetRequest(
    request: IPv6BlockApiCreateIPv6BlockSubnetRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.address is not None:
        output["address"] = request.address
    else:
        output["address"] = str()

    if request.cidr is not None:
        output["cidr"] = request.cidr
    else:
        output["cidr"] = 0


    return output

def marshal_IPv6BlockApiUpdateIPv6BlockRequest(
    request: IPv6BlockApiUpdateIPv6BlockRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.nameservers is not None:
        output["nameservers"] = request.nameservers
    else:
        output["nameservers"] = None


    return output

def marshal_InstallPartition(
    request: InstallPartition,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.file_system is not None:
        output["file_system"] = str(request.file_system)
    else:
        output["file_system"] = getattr(PartitionFileSystem, "UNKNOWN")

    if request.raid_level is not None:
        output["raid_level"] = str(request.raid_level)
    else:
        output["raid_level"] = getattr(RaidArrayRaidLevel, "NO_RAID")

    if request.capacity is not None:
        output["capacity"] = request.capacity
    else:
        output["capacity"] = 0

    if request.connectors is not None:
        output["connectors"] = request.connectors
    else:
        output["connectors"] = []

    if request.mount_point is not None:
        output["mount_point"] = request.mount_point
    else:
        output["mount_point"] = None


    return output

def marshal_InstallServerRequest(
    request: InstallServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.os_id is not None:
        output["os_id"] = request.os_id
    else:
        output["os_id"] = 0

    if request.hostname is not None:
        output["hostname"] = request.hostname
    else:
        output["hostname"] = str()

    if request.user_login is not None:
        output["user_login"] = request.user_login
    else:
        output["user_login"] = None

    if request.user_password is not None:
        output["user_password"] = request.user_password
    else:
        output["user_password"] = None

    if request.panel_password is not None:
        output["panel_password"] = request.panel_password
    else:
        output["panel_password"] = None

    if request.root_password is not None:
        output["root_password"] = request.root_password
    else:
        output["root_password"] = None

    if request.partitions is not None:
        output["partitions"] = [marshal_InstallPartition(item, defaults) for item in request.partitions]
    else:
        output["partitions"] = None

    if request.ssh_key_ids is not None:
        output["ssh_key_ids"] = request.ssh_key_ids
    else:
        output["ssh_key_ids"] = None

    if request.license_offer_id is not None:
        output["license_offer_id"] = request.license_offer_id
    else:
        output["license_offer_id"] = None

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id
    else:
        output["ip_id"] = None


    return output

def marshal_RpnSanApiAddIpRequest(
    request: RpnSanApiAddIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids
    else:
        output["ip_ids"] = str()


    return output

def marshal_RpnSanApiCreateRpnSanRequest(
    request: RpnSanApiCreateRpnSanRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.offer_id is not None:
        output["offer_id"] = request.offer_id
    else:
        output["offer_id"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RpnSanApiRemoveIpRequest(
    request: RpnSanApiRemoveIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids
    else:
        output["ip_ids"] = str()


    return output

def marshal_RpnV1ApiAddRpnGroupMembersRequest(
    request: RpnV1ApiAddRpnGroupMembersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ids is not None:
        output["server_ids"] = request.server_ids
    else:
        output["server_ids"] = None

    if request.san_server_ids is not None:
        output["san_server_ids"] = request.san_server_ids
    else:
        output["san_server_ids"] = None


    return output

def marshal_RpnV1ApiCreateRpnGroupRequest(
    request: RpnV1ApiCreateRpnGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.server_ids is not None:
        output["server_ids"] = request.server_ids
    else:
        output["server_ids"] = None

    if request.san_server_ids is not None:
        output["san_server_ids"] = request.san_server_ids
    else:
        output["san_server_ids"] = None

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RpnV1ApiDeleteRpnGroupMembersRequest(
    request: RpnV1ApiDeleteRpnGroupMembersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.member_ids is not None:
        output["member_ids"] = request.member_ids
    else:
        output["member_ids"] = str()


    return output

def marshal_RpnV1ApiLeaveRpnGroupRequest(
    request: RpnV1ApiLeaveRpnGroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.member_ids is not None:
        output["member_ids"] = request.member_ids
    else:
        output["member_ids"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RpnV1ApiRpnGroupInviteRequest(
    request: RpnV1ApiRpnGroupInviteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ids is not None:
        output["server_ids"] = request.server_ids
    else:
        output["server_ids"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_RpnV1ApiUpdateRpnGroupNameRequest(
    request: RpnV1ApiUpdateRpnGroupNameRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_RpnV2ApiAddRpnV2MembersRequest(
    request: RpnV2ApiAddRpnV2MembersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.servers is not None:
        output["servers"] = request.servers
    else:
        output["servers"] = str()


    return output

def marshal_RpnV2ApiCreateRpnV2GroupRequest(
    request: RpnV2ApiCreateRpnV2GroupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.servers is not None:
        output["servers"] = request.servers
    else:
        output["servers"] = str()

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = None


    return output

def marshal_RpnV2ApiDeleteRpnV2MembersRequest(
    request: RpnV2ApiDeleteRpnV2MembersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.member_ids is not None:
        output["member_ids"] = request.member_ids
    else:
        output["member_ids"] = str()


    return output

def marshal_RpnV2ApiEnableRpnV2GroupCompatibilityRequest(
    request: RpnV2ApiEnableRpnV2GroupCompatibilityRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.rpnv1_group_id is not None:
        output["rpnv1_group_id"] = request.rpnv1_group_id
    else:
        output["rpnv1_group_id"] = 0


    return output

def marshal_RpnV2ApiUpdateRpnV2GroupNameRequest(
    request: RpnV2ApiUpdateRpnV2GroupNameRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_RpnV2ApiUpdateRpnV2VlanForMembersRequest(
    request: RpnV2ApiUpdateRpnV2VlanForMembersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.member_ids is not None:
        output["member_ids"] = request.member_ids
    else:
        output["member_ids"] = str()

    if request.vlan is not None:
        output["vlan"] = request.vlan
    else:
        output["vlan"] = None


    return output

def marshal_StartBMCAccessRequest(
    request: StartBMCAccessRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip is not None:
        output["ip"] = request.ip
    else:
        output["ip"] = str()


    return output

def marshal_StartRescueRequest(
    request: StartRescueRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.os_id is not None:
        output["os_id"] = request.os_id
    else:
        output["os_id"] = 0


    return output

def marshal_SubscribeServerOptionRequest(
    request: SubscribeServerOptionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.option_id is not None:
        output["option_id"] = request.option_id
    else:
        output["option_id"] = 0


    return output

def marshal_SubscribeStorageOptionsRequest(
    request: SubscribeStorageOptionsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.options_ids is not None:
        output["options_ids"] = request.options_ids
    else:
        output["options_ids"] = str()


    return output

def marshal_UpdatableRaidArray(
    request: UpdatableRaidArray,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.raid_level is not None:
        output["raid_level"] = str(request.raid_level)
    else:
        output["raid_level"] = getattr(RaidArrayRaidLevel, "NO_RAID")

    if request.disk_ids is not None:
        output["disk_ids"] = request.disk_ids
    else:
        output["disk_ids"] = str()


    return output

def marshal_UpdateRaidRequest(
    request: UpdateRaidRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.raid_arrays is not None:
        output["raid_arrays"] = [marshal_UpdatableRaidArray(item, defaults) for item in request.raid_arrays]
    else:
        output["raid_arrays"] = str()


    return output

def marshal_UpdateReverseRequest(
    request: UpdateReverseRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse
    else:
        output["reverse"] = str()


    return output

def marshal_UpdateServerBackupRequest(
    request: UpdateServerBackupRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.password is not None:
        output["password"] = request.password
    else:
        output["password"] = None

    if request.autologin is not None:
        output["autologin"] = request.autologin
    else:
        output["autologin"] = None

    if request.acl_enabled is not None:
        output["acl_enabled"] = request.acl_enabled
    else:
        output["acl_enabled"] = None


    return output

def marshal_UpdateServerRequest(
    request: UpdateServerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.hostname is not None:
        output["hostname"] = request.hostname
    else:
        output["hostname"] = None

    if request.enable_ipv6 is not None:
        output["enable_ipv6"] = request.enable_ipv6
    else:
        output["enable_ipv6"] = None


    return output

def marshal_UpdateServerTagsRequest(
    request: UpdateServerTagsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output
