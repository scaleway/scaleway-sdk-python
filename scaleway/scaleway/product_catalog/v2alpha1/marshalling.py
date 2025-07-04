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
    ListPublicCatalogProductsRequestProductType,
    PublicCatalogProductPropertiesHardwareCPUArch,
    PublicCatalogProductStatus,
    PublicCatalogProductUnitOfMeasureCountableUnit,
    PublicCatalogProductPropertiesHardwareCPUPhysical,
    PublicCatalogProductPropertiesHardwareCPUVirtual,
    PublicCatalogProductPropertiesHardwareCPU,
    PublicCatalogProductPropertiesHardwareGPU,
    PublicCatalogProductPropertiesHardwareNetwork,
    PublicCatalogProductPropertiesHardwareRAM,
    PublicCatalogProductPropertiesHardwareStorage,
    PublicCatalogProductPropertiesAppleSilicon,
    PublicCatalogProductPropertiesDedibox,
    PublicCatalogProductPropertiesElasticMetal,
    PublicCatalogProductPropertiesHardware,
    PublicCatalogProductPropertiesInstance,
    PublicCatalogProductEnvironmentalImpactEstimation,
    PublicCatalogProductLocality,
    PublicCatalogProductPrice,
    PublicCatalogProductProperties,
    PublicCatalogProductUnitOfMeasure,
    PublicCatalogProduct,
    ListPublicCatalogProductsResponse,
)

def unmarshal_PublicCatalogProductPropertiesHardwareCPUPhysical(data: Any) -> PublicCatalogProductPropertiesHardwareCPUPhysical:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareCPUPhysical' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sockets", 0)
    args["sockets"] = field

    field = data.get("cores_per_socket", 0)
    args["cores_per_socket"] = field

    field = data.get("threads_per_core", 0)
    args["threads_per_core"] = field

    field = data.get("frequency", 0)
    args["frequency"] = field

    field = data.get("benchmark", 0)
    args["benchmark"] = field

    return PublicCatalogProductPropertiesHardwareCPUPhysical(**args)

def unmarshal_PublicCatalogProductPropertiesHardwareCPUVirtual(data: Any) -> PublicCatalogProductPropertiesHardwareCPUVirtual:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareCPUVirtual' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("count", 0)
    args["count"] = field

    return PublicCatalogProductPropertiesHardwareCPUVirtual(**args)

def unmarshal_PublicCatalogProductPropertiesHardwareCPU(data: Any) -> PublicCatalogProductPropertiesHardwareCPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareCPU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", str())
    args["description"] = field

    field = data.get("arch", getattr(PublicCatalogProductPropertiesHardwareCPUArch, "UNKNOWN_ARCH"))
    args["arch"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("threads", 0)
    args["threads"] = field

    field = data.get("virtual", None)
    args["virtual"] = unmarshal_PublicCatalogProductPropertiesHardwareCPUVirtual(field) if field is not None else None

    field = data.get("physical", None)
    args["physical"] = unmarshal_PublicCatalogProductPropertiesHardwareCPUPhysical(field) if field is not None else None

    return PublicCatalogProductPropertiesHardwareCPU(**args)

def unmarshal_PublicCatalogProductPropertiesHardwareGPU(data: Any) -> PublicCatalogProductPropertiesHardwareGPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareGPU' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", str())
    args["description"] = field

    field = data.get("count", 0)
    args["count"] = field

    field = data.get("type", str())
    args["type_"] = field

    return PublicCatalogProductPropertiesHardwareGPU(**args)

def unmarshal_PublicCatalogProductPropertiesHardwareNetwork(data: Any) -> PublicCatalogProductPropertiesHardwareNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", str())
    args["description"] = field

    field = data.get("internal_bandwidth", 0)
    args["internal_bandwidth"] = field

    field = data.get("public_bandwidth", 0)
    args["public_bandwidth"] = field

    field = data.get("max_public_bandwidth", 0)
    args["max_public_bandwidth"] = field

    return PublicCatalogProductPropertiesHardwareNetwork(**args)

def unmarshal_PublicCatalogProductPropertiesHardwareRAM(data: Any) -> PublicCatalogProductPropertiesHardwareRAM:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareRAM' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", str())
    args["description"] = field

    field = data.get("size", 0)
    args["size"] = field

    field = data.get("type", str())
    args["type_"] = field

    return PublicCatalogProductPropertiesHardwareRAM(**args)

def unmarshal_PublicCatalogProductPropertiesHardwareStorage(data: Any) -> PublicCatalogProductPropertiesHardwareStorage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareStorage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("description", str())
    args["description"] = field

    field = data.get("total", 0)
    args["total"] = field

    return PublicCatalogProductPropertiesHardwareStorage(**args)

def unmarshal_PublicCatalogProductPropertiesAppleSilicon(data: Any) -> PublicCatalogProductPropertiesAppleSilicon:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesAppleSilicon' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("range", str())
    args["range"] = field

    return PublicCatalogProductPropertiesAppleSilicon(**args)

def unmarshal_PublicCatalogProductPropertiesDedibox(data: Any) -> PublicCatalogProductPropertiesDedibox:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesDedibox' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("range", str())
    args["range"] = field

    return PublicCatalogProductPropertiesDedibox(**args)

def unmarshal_PublicCatalogProductPropertiesElasticMetal(data: Any) -> PublicCatalogProductPropertiesElasticMetal:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesElasticMetal' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("range", str())
    args["range"] = field

    return PublicCatalogProductPropertiesElasticMetal(**args)

def unmarshal_PublicCatalogProductPropertiesHardware(data: Any) -> PublicCatalogProductPropertiesHardware:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardware' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("cpu", None)
    args["cpu"] = unmarshal_PublicCatalogProductPropertiesHardwareCPU(field) if field is not None else None

    field = data.get("ram", None)
    args["ram"] = unmarshal_PublicCatalogProductPropertiesHardwareRAM(field) if field is not None else None

    field = data.get("storage", None)
    args["storage"] = unmarshal_PublicCatalogProductPropertiesHardwareStorage(field) if field is not None else None

    field = data.get("network", None)
    args["network"] = unmarshal_PublicCatalogProductPropertiesHardwareNetwork(field) if field is not None else None

    field = data.get("gpu", None)
    args["gpu"] = unmarshal_PublicCatalogProductPropertiesHardwareGPU(field) if field is not None else None

    return PublicCatalogProductPropertiesHardware(**args)

def unmarshal_PublicCatalogProductPropertiesInstance(data: Any) -> PublicCatalogProductPropertiesInstance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesInstance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("range", str())
    args["range"] = field

    field = data.get("offer_id", str())
    args["offer_id"] = field

    field = data.get("recommended_replacement_offer_ids", [])
    args["recommended_replacement_offer_ids"] = field

    return PublicCatalogProductPropertiesInstance(**args)

def unmarshal_PublicCatalogProductEnvironmentalImpactEstimation(data: Any) -> PublicCatalogProductEnvironmentalImpactEstimation:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductEnvironmentalImpactEstimation' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("kg_co2_equivalent", None)
    args["kg_co2_equivalent"] = field

    field = data.get("m3_water_usage", None)
    args["m3_water_usage"] = field

    return PublicCatalogProductEnvironmentalImpactEstimation(**args)

def unmarshal_PublicCatalogProductLocality(data: Any) -> PublicCatalogProductLocality:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductLocality' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("global", None)
    args["global_"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("zone", None)
    args["zone"] = field

    field = data.get("datacenter", None)
    args["datacenter"] = field

    return PublicCatalogProductLocality(**args)

def unmarshal_PublicCatalogProductPrice(data: Any) -> PublicCatalogProductPrice:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPrice' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("retail_price", None)
    args["retail_price"] = unmarshal_Money(field) if field is not None else None

    return PublicCatalogProductPrice(**args)

def unmarshal_PublicCatalogProductProperties(data: Any) -> PublicCatalogProductProperties:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductProperties' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("hardware", None)
    args["hardware"] = unmarshal_PublicCatalogProductPropertiesHardware(field) if field is not None else None

    field = data.get("dedibox", None)
    args["dedibox"] = unmarshal_PublicCatalogProductPropertiesDedibox(field) if field is not None else None

    field = data.get("elastic_metal", None)
    args["elastic_metal"] = unmarshal_PublicCatalogProductPropertiesElasticMetal(field) if field is not None else None

    field = data.get("apple_silicon", None)
    args["apple_silicon"] = unmarshal_PublicCatalogProductPropertiesAppleSilicon(field) if field is not None else None

    field = data.get("instance", None)
    args["instance"] = unmarshal_PublicCatalogProductPropertiesInstance(field) if field is not None else None

    return PublicCatalogProductProperties(**args)

def unmarshal_PublicCatalogProductUnitOfMeasure(data: Any) -> PublicCatalogProductUnitOfMeasure:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductUnitOfMeasure' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("unit", str())
    args["unit"] = field

    field = data.get("size", str())
    args["size"] = field

    return PublicCatalogProductUnitOfMeasure(**args)

def unmarshal_PublicCatalogProduct(data: Any) -> PublicCatalogProduct:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProduct' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("sku", str())
    args["sku"] = field

    field = data.get("service_category", str())
    args["service_category"] = field

    field = data.get("product", str())
    args["product"] = field

    field = data.get("variant", str())
    args["variant"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("status", getattr(PublicCatalogProductStatus, "UNKNOWN_STATUS"))
    args["status"] = field

    field = data.get("locality", None)
    args["locality"] = unmarshal_PublicCatalogProductLocality(field) if field is not None else None

    field = data.get("price", None)
    args["price"] = unmarshal_PublicCatalogProductPrice(field) if field is not None else None

    field = data.get("properties", None)
    args["properties"] = unmarshal_PublicCatalogProductProperties(field) if field is not None else None

    field = data.get("environmental_impact_estimation", None)
    args["environmental_impact_estimation"] = unmarshal_PublicCatalogProductEnvironmentalImpactEstimation(field) if field is not None else None

    field = data.get("unit_of_measure", None)
    args["unit_of_measure"] = unmarshal_PublicCatalogProductUnitOfMeasure(field) if field is not None else None

    field = data.get("end_of_life_at", None)
    args["end_of_life_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return PublicCatalogProduct(**args)

def unmarshal_ListPublicCatalogProductsResponse(data: Any) -> ListPublicCatalogProductsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPublicCatalogProductsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("products", [])
    args["products"] = [unmarshal_PublicCatalogProduct(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListPublicCatalogProductsResponse(**args)
