# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ListPublicCatalogProductsRequestProductType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PRODUCT_TYPE = "unknown_product_type"
    INSTANCE = "instance"
    APPLE_SILICON = "apple_silicon"
    ELASTIC_METAL = "elastic_metal"
    DEDIBOX = "dedibox"
    BLOCK_STORAGE = "block_storage"
    OBJECT_STORAGE = "object_storage"
    MANAGED_INFERENCE = "managed_inference"
    GENERATIVE_APIS = "generative_apis"
    LOAD_BALANCER = "load_balancer"
    SECRET_MANAGER = "secret_manager"
    KEY_MANAGER = "key_manager"
    MANAGED_REDIS_DATABASE = "managed_redis_database"
    KUBERNETES = "kubernetes"
    MANAGED_RELATIONAL_DATABASE = "managed_relational_database"

    def __str__(self) -> str:
        return str(self.value)


class ListPublicCatalogProductsRequestStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    PUBLIC_BETA = "public_beta"
    PREVIEW = "preview"
    GENERAL_AVAILABILITY = "general_availability"
    END_OF_NEW_FEATURES = "end_of_new_features"
    END_OF_GROWTH = "end_of_growth"
    END_OF_DEPLOYMENT = "end_of_deployment"
    END_OF_SUPPORT = "end_of_support"
    END_OF_SALE = "end_of_sale"
    END_OF_LIFE = "end_of_life"
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)


class PublicCatalogProductProductBadge(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_PRODUCT_BADGE = "unknown_product_badge"
    NEW_PRODUCT = "new_product"
    BEST_SELLER = "best_seller"
    BEST_VALUE = "best_value"
    POPULAR = "popular"

    def __str__(self) -> str:
        return str(self.value)


class PublicCatalogProductPropertiesGenerativeApisConsumptionMode(
    str, Enum, metaclass=StrEnumMeta
):
    UNKNOWN_CONSUMPTION_MODE = "unknown_consumption_mode"
    REALTIME = "realtime"
    BATCH = "batch"

    def __str__(self) -> str:
        return str(self.value)


class PublicCatalogProductPropertiesHardwareCPUArch(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ARCH = "unknown_arch"
    X64 = "x64"
    ARM64 = "arm64"
    RISCV = "riscv"
    APPLE_SILICON = "apple_silicon"

    def __str__(self) -> str:
        return str(self.value)


class PublicCatalogProductPropertiesManagedRelationalDatabaseStorageTypeStorageClass(
    str, Enum, metaclass=StrEnumMeta
):
    UNKNOWN_STORAGE_CLASS = "unknown_storage_class"
    BLOCK_SSD = "block_ssd"
    BLOCK_SSD_SNAPSHOT = "block_ssd_snapshot"
    LOCAL_SSD = "local_ssd"
    SBS_5K = "sbs_5k"
    SBS_5K_SNAPSHOT = "sbs_5k_snapshot"
    SBS_15K = "sbs_15k"
    SBS_15K_SNAPSHOT = "sbs_15k_snapshot"
    BACKUP = "backup"

    def __str__(self) -> str:
        return str(self.value)


class PublicCatalogProductPropertiesObjectStorageClassTypeStorageClass(
    str, Enum, metaclass=StrEnumMeta
):
    UNKNOWN_STORAGE_CLASS = "unknown_storage_class"
    STANDARD = "standard"
    GLACIER = "glacier"
    ONEZONE_IA = "onezone_ia"

    def __str__(self) -> str:
        return str(self.value)


class PublicCatalogProductPropertiesObjectStorageInternetTrafficTypeTrafficType(
    str, Enum, metaclass=StrEnumMeta
):
    UNKNOWN_TRAFFIC_TYPE = "unknown_traffic_type"
    INGRESS = "ingress"
    EGRESS = "egress"

    def __str__(self) -> str:
        return str(self.value)


class PublicCatalogProductPropertiesObjectStorageRestoreTypeRestoreType(
    str, Enum, metaclass=StrEnumMeta
):
    UNKNOWN_RESTORE_TYPE = "unknown_restore_type"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)


class PublicCatalogProductStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    PUBLIC_BETA = "public_beta"
    PREVIEW = "preview"
    GENERAL_AVAILABILITY = "general_availability"
    END_OF_NEW_FEATURES = "end_of_new_features"
    END_OF_GROWTH = "end_of_growth"
    END_OF_DEPLOYMENT = "end_of_deployment"
    END_OF_SUPPORT = "end_of_support"
    END_OF_SALE = "end_of_sale"
    END_OF_LIFE = "end_of_life"
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)


class PublicCatalogProductUnitOfMeasureCountableUnit(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_COUNTABLE_UNIT = "unknown_countable_unit"
    CHUNK = "chunk"
    CORE = "core"
    CURRENCY = "currency"
    DEVICE = "device"
    DOMAIN = "domain"
    EMAIL = "email"
    GB_S = "gb_s"
    GIGABYTE = "gigabyte"
    HOUR = "hour"
    IOPS_GIGABYTE = "iops_gigabyte"
    IP = "ip"
    MONTH = "month"
    NODE = "node"
    PLAN = "plan"
    QUERY = "query"
    REQUEST = "request"
    SESSION = "session"
    VCPU_S = "vcpu_s"
    VERSION = "version"
    YEAR = "year"
    KEY = "key"
    TOKEN = "token"
    MINUTE = "minute"
    SETUP = "setup"
    DAY = "day"
    SECOND = "second"
    SAMPLE_DAY = "sample_day"
    GIGABYTE_DAY = "gigabyte_day"
    MVCPU = "mvcpu"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class PublicCatalogProductPropertiesHardwareCPUPhysical:
    sockets: int
    """
    The number of sockets of the CPU.
    """

    cores_per_socket: int
    """
    The number of cores per socket.
    """

    threads_per_core: int
    """
    The number of threads per core.
    """

    frequency: int
    """
    The frequency of the CPU in Hertz.
    """

    benchmark: int
    """
    The benchmark score of the CPU.
    """


@dataclass
class PublicCatalogProductPropertiesHardwareCPUVirtual:
    count: int
    """
    The number of vCPUs.
    """


@dataclass
class PublicCatalogProductPropertiesHardwareCPU:
    description: str
    """
    A human readable description of the CPU.
    """

    arch: PublicCatalogProductPropertiesHardwareCPUArch
    """
    The architecture of the CPU.
    """

    type_: str
    """
    The type of the CPU.
    """

    threads: int
    """
    The total number of threads.
    """

    virtual: Optional[PublicCatalogProductPropertiesHardwareCPUVirtual] = None

    physical: Optional[PublicCatalogProductPropertiesHardwareCPUPhysical] = None


@dataclass
class PublicCatalogProductPropertiesHardwareGPU:
    description: str
    """
    A human-readable description of the GPU.
    """

    count: int
    """
    The number of GPUs.
    """

    type_: str
    """
    The type of the GPU.
    """


@dataclass
class PublicCatalogProductPropertiesHardwareNetwork:
    description: str
    """
    A human-readable description of the network.
    """

    internal_bandwidth: int
    """
    The internal bandwidth in bits per second.
    """

    public_bandwidth: int
    """
    The default public bandwidth in bits per second.
    """

    max_public_bandwidth: int
    """
    The maximum public bandwidth in bits per second (may require subscription to options).
    """


@dataclass
class PublicCatalogProductPropertiesHardwareRAM:
    description: str
    """
    A human-readable description of the RAM.
    """

    size: int
    """
    The size of the RAM in bytes.
    """

    type_: str
    """
    The type of the RAM.
    """


@dataclass
class PublicCatalogProductPropertiesHardwareStorage:
    description: str
    """
    A human-readable description of the storage.
    """

    total: int
    """
    The total size of the storage in bytes.
    """


@dataclass
class PublicCatalogProductPropertiesKubernetesKapsuleControlPlaneType:
    pass


@dataclass
class PublicCatalogProductPropertiesKubernetesKosmosControlPlaneType:
    pass


@dataclass
class PublicCatalogProductPropertiesKubernetesKosmosNodeType:
    pass


@dataclass
class PublicCatalogProductPropertiesManagedRelationalDatabaseManagementType:
    pass


@dataclass
class PublicCatalogProductPropertiesManagedRelationalDatabaseMultiAzType:
    pass


@dataclass
class PublicCatalogProductPropertiesManagedRelationalDatabaseNodeType:
    pass


@dataclass
class PublicCatalogProductPropertiesManagedRelationalDatabaseStorageType:
    storage_class: (
        PublicCatalogProductPropertiesManagedRelationalDatabaseStorageTypeStorageClass
    )
    """
    The type of Storage class.
    """


@dataclass
class PublicCatalogProductPropertiesObjectStorageClassType:
    storage_class: PublicCatalogProductPropertiesObjectStorageClassTypeStorageClass
    """
    The storage class.
    """


@dataclass
class PublicCatalogProductPropertiesObjectStorageInternetTrafficType:
    traffic_type: (
        PublicCatalogProductPropertiesObjectStorageInternetTrafficTypeTrafficType
    )
    """
    The type of internet traffic.
    """


@dataclass
class PublicCatalogProductPropertiesObjectStorageRegionTrafficType:
    region_destination: str
    """
    The destination region for the region traffic.
    """


@dataclass
class PublicCatalogProductPropertiesObjectStorageRestoreType:
    restore_type: PublicCatalogProductPropertiesObjectStorageRestoreTypeRestoreType
    """
    The type of restore.
    """


@dataclass
class PublicCatalogProductPropertiesAppleSilicon:
    range: str
    """
    The range of the Apple Silicon server.
    """

    server_type: str
    """
    The server type of the Apple Silicon server.
    """


@dataclass
class PublicCatalogProductPropertiesBlockStorage:
    min_volume_size: int
    """
    The minimum size of storage volume for this product in bytes. Deprecated.
    """

    max_volume_size: int
    """
    The maximum size of storage volume for this product in bytes. Deprecated.
    """


@dataclass
class PublicCatalogProductPropertiesDedibox:
    range: str
    """
    The range of the Dedibox server.
    """

    offer_id: int
    """
    The offer ID of the Dedibox server.
    """


@dataclass
class PublicCatalogProductPropertiesElasticMetal:
    range: str
    """
    The range of the Elastic Metal server.
    """

    offer_id: str
    """
    The offer ID of the Elastic Metal server.
    """


@dataclass
class PublicCatalogProductPropertiesGenerativeApis:
    reasoning: bool
    supported_apis: list[str]
    consumption_mode: PublicCatalogProductPropertiesGenerativeApisConsumptionMode


@dataclass
class PublicCatalogProductPropertiesHardware:
    cpu: Optional[PublicCatalogProductPropertiesHardwareCPU] = None
    """
    The CPU hardware properties.
    """

    ram: Optional[PublicCatalogProductPropertiesHardwareRAM] = None
    """
    The RAM hardware properties.
    """

    storage: Optional[PublicCatalogProductPropertiesHardwareStorage] = None
    """
    The storage hardware properties.
    """

    network: Optional[PublicCatalogProductPropertiesHardwareNetwork] = None
    """
    The network hardware properties.
    """

    gpu: Optional[PublicCatalogProductPropertiesHardwareGPU] = None
    """
    The GPU hardware properties.
    """


@dataclass
class PublicCatalogProductPropertiesInstance:
    range: str
    """
    The range of the Instance server.
    """

    offer_id: str
    """
    The offer ID of the Instance server.
    """

    recommended_replacement_offer_ids: list[str]
    """
    The recommended replacement offer IDs of the Instance server.
    """


@dataclass
class PublicCatalogProductPropertiesKeyManager:
    pass


@dataclass
class PublicCatalogProductPropertiesKubernetes:
    kapsule_control_plane: Optional[
        PublicCatalogProductPropertiesKubernetesKapsuleControlPlaneType
    ] = None

    kosmos_control_plane: Optional[
        PublicCatalogProductPropertiesKubernetesKosmosControlPlaneType
    ] = None

    kosmos_node: Optional[PublicCatalogProductPropertiesKubernetesKosmosNodeType] = None


@dataclass
class PublicCatalogProductPropertiesLoadBalancer:
    pass


@dataclass
class PublicCatalogProductPropertiesManagedInference:
    instance_gpu_name: str
    """
    The name of the associated instance GPU to this node type.
    """


@dataclass
class PublicCatalogProductPropertiesManagedRedisDatabase:
    pass


@dataclass
class PublicCatalogProductPropertiesManagedRelationalDatabase:
    management: Optional[
        PublicCatalogProductPropertiesManagedRelationalDatabaseManagementType
    ] = None

    node: Optional[PublicCatalogProductPropertiesManagedRelationalDatabaseNodeType] = (
        None
    )

    storage: Optional[
        PublicCatalogProductPropertiesManagedRelationalDatabaseStorageType
    ] = None

    multi_az: Optional[
        PublicCatalogProductPropertiesManagedRelationalDatabaseMultiAzType
    ] = None


@dataclass
class PublicCatalogProductPropertiesObjectStorage:
    class_: Optional[PublicCatalogProductPropertiesObjectStorageClassType] = None

    restore: Optional[PublicCatalogProductPropertiesObjectStorageRestoreType] = None

    internet_traffic: Optional[
        PublicCatalogProductPropertiesObjectStorageInternetTrafficType
    ] = None

    region_traffic: Optional[
        PublicCatalogProductPropertiesObjectStorageRegionTrafficType
    ] = None


@dataclass
class PublicCatalogProductPropertiesSecretManager:
    pass


@dataclass
class PublicCatalogProductEnvironmentalImpactEstimation:
    kg_co2_equivalent: Optional[float] = None
    m3_water_usage: Optional[float] = None


@dataclass
class PublicCatalogProductLocality:
    global_: Optional[bool] = False

    region: Optional[ScwRegion] = None

    zone: Optional[ScwZone] = None

    datacenter: Optional[str] = None


@dataclass
class PublicCatalogProductPrice:
    retail_price: Optional[Money] = None
    """
    The retail price of the product.
    """


@dataclass
class PublicCatalogProductProperties:
    hardware: Optional[PublicCatalogProductPropertiesHardware] = None
    """
    The hardware properties of the product (if supported).
    """

    dedibox: Optional[PublicCatalogProductPropertiesDedibox] = None

    elastic_metal: Optional[PublicCatalogProductPropertiesElasticMetal] = None

    apple_silicon: Optional[PublicCatalogProductPropertiesAppleSilicon] = None

    instance: Optional[PublicCatalogProductPropertiesInstance] = None

    block_storage: Optional[PublicCatalogProductPropertiesBlockStorage] = None

    object_storage: Optional[PublicCatalogProductPropertiesObjectStorage] = None

    managed_inference: Optional[PublicCatalogProductPropertiesManagedInference] = None

    generative_apis: Optional[PublicCatalogProductPropertiesGenerativeApis] = None

    load_balancer: Optional[PublicCatalogProductPropertiesLoadBalancer] = None

    secret_manager: Optional[PublicCatalogProductPropertiesSecretManager] = None

    managed_redis_database: Optional[
        PublicCatalogProductPropertiesManagedRedisDatabase
    ] = None

    key_manager: Optional[PublicCatalogProductPropertiesKeyManager] = None

    kubernetes: Optional[PublicCatalogProductPropertiesKubernetes] = None

    managed_relational_database: Optional[
        PublicCatalogProductPropertiesManagedRelationalDatabase
    ] = None


@dataclass
class PublicCatalogProductUnitOfMeasure:
    unit: PublicCatalogProductUnitOfMeasureCountableUnit
    size: int


@dataclass
class PublicCatalogProduct:
    sku: str
    """
    The unique identifier of the product.
    """

    service_category: str
    """
    The category of the product.
    """

    product_category: str
    """
    The product category of the product.
    """

    product: str
    """
    The product name.
    """

    variant: str
    """
    The product variant.
    """

    description: str
    """
    The product description.
    """

    status: PublicCatalogProductStatus
    """
    The status of the product.
    """

    badges: list[PublicCatalogProductProductBadge]
    """
    Different badges that can be associated with the product.
    """

    locality: Optional[PublicCatalogProductLocality] = None
    """
    The locality of the product.
    """

    price: Optional[PublicCatalogProductPrice] = None
    """
    The price of the product.
    """

    properties: Optional[PublicCatalogProductProperties] = None
    """
    The properties of the product.
    """

    environmental_impact_estimation: Optional[
        PublicCatalogProductEnvironmentalImpactEstimation
    ] = None
    """
    The environmental impact estimation of the product.
    """

    unit_of_measure: Optional[PublicCatalogProductUnitOfMeasure] = None
    """
    The unit of measure of the product.
    """

    end_of_life_at: Optional[datetime] = None
    """
    The end of life date of the product.
    """

    end_of_growth_at: Optional[datetime] = None
    """
    The end of growth date of the product.
    """

    end_of_sale_at: Optional[datetime] = None
    """
    The end of sale date of the product.
    """


@dataclass
class ListPublicCatalogProductsResponse:
    products: list[PublicCatalogProduct]
    """
    The list of products.
    """

    total_count: int
    """
    The total number of products in the catalog.
    """


@dataclass
class PublicCatalogApiListPublicCatalogProductsRequest:
    page: Optional[int] = 0
    """
    Number of the page. Value must be greater or equal to 1.
    """

    page_size: Optional[int] = 0
    """
    The number of products per page. Value must be greater or equal to 1.
    """

    product_types: Optional[list[ListPublicCatalogProductsRequestProductType]] = field(
        default_factory=list
    )
    """
    The list of filtered product categories.
    """

    status: Optional[list[ListPublicCatalogProductsRequestStatus]] = field(
        default_factory=list
    )
    """
    The lists of filtered product status, if empty only products with status public_beta, general_availability, preview, end_of_new_features, end_of_growth, end_of_deployment, end_of_support, end_of_sale, end_of_life or retired will be returned.
    """

    global_: Optional[bool] = False

    region: Optional[ScwRegion] = None

    zone: Optional[ScwZone] = None

    datacenter: Optional[str] = None
