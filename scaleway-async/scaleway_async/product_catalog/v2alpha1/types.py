# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

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


class PublicCatalogProductStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    PUBLIC_BETA = "public_beta"
    PREVIEW = "preview"
    GENERAL_AVAILABILITY = "general_availability"
    END_OF_DEPLOYMENT = "end_of_deployment"
    END_OF_SUPPORT = "end_of_support"

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

    virtual: Optional[PublicCatalogProductPropertiesHardwareCPUVirtual]

    physical: Optional[PublicCatalogProductPropertiesHardwareCPUPhysical]


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
class PublicCatalogProductPropertiesAppleSilicon:
    range: str
    """
    The range of the Apple Silicon server.
    """


@dataclass
class PublicCatalogProductPropertiesDedibox:
    range: str
    """
    The range of the Dedibox server.
    """


@dataclass
class PublicCatalogProductPropertiesElasticMetal:
    range: str
    """
    The range of the Elastic Metal server.
    """


@dataclass
class PublicCatalogProductPropertiesHardware:
    cpu: Optional[PublicCatalogProductPropertiesHardwareCPU]
    """
    The CPU hardware properties.
    """

    ram: Optional[PublicCatalogProductPropertiesHardwareRAM]
    """
    The RAM hardware properties.
    """

    storage: Optional[PublicCatalogProductPropertiesHardwareStorage]
    """
    The storage hardware properties.
    """

    network: Optional[PublicCatalogProductPropertiesHardwareNetwork]
    """
    The network hardware properties.
    """

    gpu: Optional[PublicCatalogProductPropertiesHardwareGPU]
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

    recommended_replacement_offer_ids: List[str]
    """
    The recommended replacement offer IDs of the Instance server.
    """


@dataclass
class PublicCatalogProductEnvironmentalImpactEstimation:
    kg_co2_equivalent: Optional[float]

    m3_water_usage: Optional[float]


@dataclass
class PublicCatalogProductLocality:
    global_: Optional[bool]

    region: Optional[ScwRegion]

    zone: Optional[ScwZone]

    datacenter: Optional[str]


@dataclass
class PublicCatalogProductPrice:
    retail_price: Optional[Money]
    """
    The retail price of the product.
    """


@dataclass
class PublicCatalogProductProperties:
    hardware: Optional[PublicCatalogProductPropertiesHardware]
    """
    The hardware properties of the product (if supported).
    """

    dedibox: Optional[PublicCatalogProductPropertiesDedibox]

    elastic_metal: Optional[PublicCatalogProductPropertiesElasticMetal]

    apple_silicon: Optional[PublicCatalogProductPropertiesAppleSilicon]

    instance: Optional[PublicCatalogProductPropertiesInstance]


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

    locality: Optional[PublicCatalogProductLocality]
    """
    The locality of the product.
    """

    price: Optional[PublicCatalogProductPrice]
    """
    The price of the product.
    """

    properties: Optional[PublicCatalogProductProperties]
    """
    The properties of the product.
    """

    environmental_impact_estimation: Optional[
        PublicCatalogProductEnvironmentalImpactEstimation
    ]
    """
    The environmental impact estimation of the product.
    """

    unit_of_measure: Optional[PublicCatalogProductUnitOfMeasure]
    """
    The unit of measure of the product.
    """

    end_of_life_at: Optional[datetime]
    """
    The end of life date of the product.
    """


@dataclass
class ListPublicCatalogProductsResponse:
    products: List[PublicCatalogProduct]
    """
    The list of products.
    """

    total_count: int
    """
    The total number of products in the catalog.
    """


@dataclass
class PublicCatalogApiListPublicCatalogProductsRequest:
    page: Optional[int]
    """
    Number of the page. Value must be greater or equal to 1.
    """

    page_size: Optional[int]
    """
    The number of products per page. Value must be greater or equal to 1.
    """

    product_types: Optional[List[ListPublicCatalogProductsRequestProductType]]
    """
    The list of filtered product categories.
    """

    locality: Optional[PublicCatalogProductLocality]
    """
    The locality of the products to filter by. If not set, all localities are returned.
    """
