# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Region as ScwRegion,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ObsDatasourceInfoDataType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DATA_TYPE = "unknown_data_type"
    METRICS = "metrics"
    LOGS = "logs"
    TRACES = "traces"

    def __str__(self) -> str:
        return str(self.value)


class ObsExporterInfoDestinationType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_DESTINATION_TYPE = "unknown_destination_type"
    DATADOG = "datadog"
    OTLP = "otlp"

    def __str__(self) -> str:
        return str(self.value)


class ResourceType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    INSTANCE_SERVER = "instance_server"
    INSTANCE_VOLUME = "instance_volume"
    INSTANCE_IMAGE = "instance_image"
    INSTANCE_SECURITY_GROUP = "instance_security_group"
    INSTANCE_PRIVATE_NIC = "instance_private_nic"
    INSTANCE_SNAPSHOT = "instance_snapshot"
    INSTANCE_PLACEMENT_GROUP = "instance_placement_group"
    K8S_CLUSTER = "k8s_cluster"
    K8S_POOL = "k8s_pool"
    K8S_NODE = "k8s_node"
    DOMAIN_DOMAIN = "domain_domain"
    DNS_ZONE = "dns_zone"
    VPC_PRIVATE_NETWORK = "vpc_private_network"
    VPC_VPC = "vpc_vpc"
    VPG_GATEWAY = "vpg_gateway"
    APPLE_SILICON_SERVER = "apple_silicon_server"
    RDB_INSTANCE = "rdb_instance"
    RDB_SNAPSHOT = "rdb_snapshot"
    RDB_BACKUP = "rdb_backup"
    BAREMETAL_SERVER = "baremetal_server"
    TEM_DOMAIN = "tem_domain"
    LB_SERVER = "lb_server"
    SERVERLESS_FUNCTIONS_FUNCTION = "serverless_functions_function"
    SERVERLESS_CONTAINERS_CONTAINER = "serverless_containers_container"
    WBH_HOSTING = "wbh_hosting"
    REDIS_CLUSTER = "redis_cluster"
    SM_SECRET = "sm_secret"
    KMS_KEY = "kms_key"
    EDG_PIPELINE = "edg_pipeline"
    MNQ_NATS_ACCOUNT = "mnq_nats_account"
    SBS_VOLUME = "sbs_volume"
    SBS_SNAPSHOT = "sbs_snapshot"
    SERVERLESS_JOB_DEFINITION = "serverless_job_definition"
    SERVERLESS_SQLDB_DATABASE = "serverless_sqldb_database"
    SERVERLESS_SQLDB_BACKUP = "serverless_sqldb_backup"
    DDL_DATALAB = "ddl_datalab"
    MGDB_INSTANCE = "mgdb_instance"
    MGDB_SNAPSHOT = "mgdb_snapshot"
    IFR_DEPLOYMENT = "ifr_deployment"
    IFR_MODEL = "ifr_model"
    GAPI_BATCH = "gapi_batch"
    DTWH_DEPLOYMENT = "dtwh_deployment"
    OBS_DATASOURCE = "obs_datasource"
    OBS_EXPORTER = "obs_exporter"
    SVPN_VPN_GATEWAY = "svpn_vpn_gateway"
    SVPN_CUSTOMER_GATEWAY = "svpn_customer_gateway"
    SVPN_CONNECTION = "svpn_connection"
    SVPN_ROUTING_POLICY = "svpn_routing_policy"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class BrmServerInfo:
    ip: str


@dataclass
class ObsDatasourceInfo:
    type_: ObsDatasourceInfoDataType


@dataclass
class ObsExporterInfo:
    destination_type: ObsExporterInfoDestinationType


@dataclass
class ServerlessContainersContainerInfo:
    namespace_id: str
    """
    ID of the Namespace the Serverless Container belongs to.
    """


@dataclass
class ServerlessFunctionsFunctionInfo:
    namespace_id: str
    """
    ID of the Namespace the Serverless Function belongs to.
    """


@dataclass
class ServerlessSqldbBackupInfo:
    database_id: str


@dataclass
class VpcPrivateNetworkInfo:
    vpc_id: str
    """
    ID of the VPC the Private Network belongs to.
    """


@dataclass
class Resource:
    id: str
    """
    ID of the resource.
    """

    organization_id: str
    """
    ID of the Organization the resource belongs to.
    """

    type_: ResourceType
    """
    Type of the resource.
    """

    name: Optional[str] = None
    """
    Name of the resource.
    """

    project_id: Optional[str] = None
    """
    ID of the Project the resource belongs to.
    """

    global_: Optional[bool] = False

    zone: Optional[ScwZone] = None

    region: Optional[ScwRegion] = None

    vpc_private_network_info: Optional[VpcPrivateNetworkInfo] = None

    serverless_functions_function_info: Optional[ServerlessFunctionsFunctionInfo] = None

    serverless_containers_container_info: Optional[
        ServerlessContainersContainerInfo
    ] = None

    baremetal_server_info: Optional[BrmServerInfo] = None

    serverless_sqldb_backup_info: Optional[ServerlessSqldbBackupInfo] = None

    obs_datasource_info: Optional[ObsDatasourceInfo] = None

    obs_exporter_info: Optional[ObsExporterInfo] = None


@dataclass
class SearchResourcesRequest:
    query: str
    """
    Search query.
    """

    organization_id: Optional[str] = None
    """
    ID of the Organization to search in.
    """


@dataclass
class SearchResourcesResponse:
    resources: list[Resource]
    """
    Top resources found.
    """
