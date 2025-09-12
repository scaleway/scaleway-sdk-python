# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any
from dateutil import parser

from scaleway_core.bridge import (
    unmarshal_Money,
)
from .types import (
    PublicCatalogProductPropertiesHardwareCPUArch,
    PublicCatalogProductStatus,
    PublicCatalogProductPropertiesHardwareCPUPhysical,
    PublicCatalogProductPropertiesHardwareCPUVirtual,
    PublicCatalogProductPropertiesHardwareCPU,
    PublicCatalogProductPropertiesHardwareGPU,
    PublicCatalogProductPropertiesHardwareNetwork,
    PublicCatalogProductPropertiesHardwareRAM,
    PublicCatalogProductPropertiesHardwareStorage,
    PublicCatalogProductPropertiesAppleSilicon,
    PublicCatalogProductPropertiesBlockStorage,
    PublicCatalogProductPropertiesDedibox,
    PublicCatalogProductPropertiesElasticMetal,
    PublicCatalogProductPropertiesHardware,
    PublicCatalogProductPropertiesInstance,
    PublicCatalogProductPropertiesObjectStorage,
    PublicCatalogProductEnvironmentalImpactEstimation,
    PublicCatalogProductLocality,
    PublicCatalogProductPrice,
    PublicCatalogProductProperties,
    PublicCatalogProductUnitOfMeasure,
    PublicCatalogProduct,
    ListPublicCatalogProductsResponse,
)


def unmarshal_PublicCatalogProductPropertiesHardwareCPUPhysical(
    data: Any,
) -> PublicCatalogProductPropertiesHardwareCPUPhysical:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareCPUPhysical' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sockets", None)
    if field is not None:
        args["sockets"] = field
    else:
        args["sockets"] = 0

    field = data.get("cores_per_socket", None)
    if field is not None:
        args["cores_per_socket"] = field
    else:
        args["cores_per_socket"] = 0

    field = data.get("threads_per_core", None)
    if field is not None:
        args["threads_per_core"] = field
    else:
        args["threads_per_core"] = 0

    field = data.get("frequency", None)
    if field is not None:
        args["frequency"] = field
    else:
        args["frequency"] = 0

    field = data.get("benchmark", None)
    if field is not None:
        args["benchmark"] = field
    else:
        args["benchmark"] = 0

    return PublicCatalogProductPropertiesHardwareCPUPhysical(**args)


def unmarshal_PublicCatalogProductPropertiesHardwareCPUVirtual(
    data: Any,
) -> PublicCatalogProductPropertiesHardwareCPUVirtual:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareCPUVirtual' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("count", None)
    if field is not None:
        args["count"] = field
    else:
        args["count"] = 0

    return PublicCatalogProductPropertiesHardwareCPUVirtual(**args)


def unmarshal_PublicCatalogProductPropertiesHardwareCPU(
    data: Any,
) -> PublicCatalogProductPropertiesHardwareCPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareCPU' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("arch", None)
    if field is not None:
        args["arch"] = field
    else:
        args["arch"] = PublicCatalogProductPropertiesHardwareCPUArch.UNKNOWN_ARCH

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    field = data.get("threads", None)
    if field is not None:
        args["threads"] = field
    else:
        args["threads"] = 0

    field = data.get("virtual", None)
    if field is not None:
        args["virtual"] = unmarshal_PublicCatalogProductPropertiesHardwareCPUVirtual(
            field
        )
    else:
        args["virtual"] = None

    field = data.get("physical", None)
    if field is not None:
        args["physical"] = unmarshal_PublicCatalogProductPropertiesHardwareCPUPhysical(
            field
        )
    else:
        args["physical"] = None

    return PublicCatalogProductPropertiesHardwareCPU(**args)


def unmarshal_PublicCatalogProductPropertiesHardwareGPU(
    data: Any,
) -> PublicCatalogProductPropertiesHardwareGPU:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareGPU' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("count", None)
    if field is not None:
        args["count"] = field
    else:
        args["count"] = 0

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return PublicCatalogProductPropertiesHardwareGPU(**args)


def unmarshal_PublicCatalogProductPropertiesHardwareNetwork(
    data: Any,
) -> PublicCatalogProductPropertiesHardwareNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareNetwork' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("internal_bandwidth", None)
    if field is not None:
        args["internal_bandwidth"] = field
    else:
        args["internal_bandwidth"] = 0

    field = data.get("public_bandwidth", None)
    if field is not None:
        args["public_bandwidth"] = field
    else:
        args["public_bandwidth"] = 0

    field = data.get("max_public_bandwidth", None)
    if field is not None:
        args["max_public_bandwidth"] = field
    else:
        args["max_public_bandwidth"] = 0

    return PublicCatalogProductPropertiesHardwareNetwork(**args)


def unmarshal_PublicCatalogProductPropertiesHardwareRAM(
    data: Any,
) -> PublicCatalogProductPropertiesHardwareRAM:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareRAM' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = 0

    field = data.get("type", None)
    if field is not None:
        args["type_"] = field
    else:
        args["type_"] = None

    return PublicCatalogProductPropertiesHardwareRAM(**args)


def unmarshal_PublicCatalogProductPropertiesHardwareStorage(
    data: Any,
) -> PublicCatalogProductPropertiesHardwareStorage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardwareStorage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("total", None)
    if field is not None:
        args["total"] = field
    else:
        args["total"] = 0

    return PublicCatalogProductPropertiesHardwareStorage(**args)


def unmarshal_PublicCatalogProductPropertiesAppleSilicon(
    data: Any,
) -> PublicCatalogProductPropertiesAppleSilicon:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesAppleSilicon' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("range", None)
    if field is not None:
        args["range"] = field
    else:
        args["range"] = None

    field = data.get("server_type", None)
    if field is not None:
        args["server_type"] = field
    else:
        args["server_type"] = None

    return PublicCatalogProductPropertiesAppleSilicon(**args)


def unmarshal_PublicCatalogProductPropertiesBlockStorage(
    data: Any,
) -> PublicCatalogProductPropertiesBlockStorage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesBlockStorage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("min_volume_size", None)
    if field is not None:
        args["min_volume_size"] = field
    else:
        args["min_volume_size"] = 0

    field = data.get("max_volume_size", None)
    if field is not None:
        args["max_volume_size"] = field
    else:
        args["max_volume_size"] = 0

    return PublicCatalogProductPropertiesBlockStorage(**args)


def unmarshal_PublicCatalogProductPropertiesDedibox(
    data: Any,
) -> PublicCatalogProductPropertiesDedibox:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesDedibox' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("range", None)
    if field is not None:
        args["range"] = field
    else:
        args["range"] = None

    field = data.get("offer_id", None)
    if field is not None:
        args["offer_id"] = field
    else:
        args["offer_id"] = 0

    return PublicCatalogProductPropertiesDedibox(**args)


def unmarshal_PublicCatalogProductPropertiesElasticMetal(
    data: Any,
) -> PublicCatalogProductPropertiesElasticMetal:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesElasticMetal' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("range", None)
    if field is not None:
        args["range"] = field
    else:
        args["range"] = None

    field = data.get("offer_id", None)
    if field is not None:
        args["offer_id"] = field
    else:
        args["offer_id"] = None

    return PublicCatalogProductPropertiesElasticMetal(**args)


def unmarshal_PublicCatalogProductPropertiesHardware(
    data: Any,
) -> PublicCatalogProductPropertiesHardware:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesHardware' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("cpu", None)
    if field is not None:
        args["cpu"] = unmarshal_PublicCatalogProductPropertiesHardwareCPU(field)
    else:
        args["cpu"] = None

    field = data.get("ram", None)
    if field is not None:
        args["ram"] = unmarshal_PublicCatalogProductPropertiesHardwareRAM(field)
    else:
        args["ram"] = None

    field = data.get("storage", None)
    if field is not None:
        args["storage"] = unmarshal_PublicCatalogProductPropertiesHardwareStorage(field)
    else:
        args["storage"] = None

    field = data.get("network", None)
    if field is not None:
        args["network"] = unmarshal_PublicCatalogProductPropertiesHardwareNetwork(field)
    else:
        args["network"] = None

    field = data.get("gpu", None)
    if field is not None:
        args["gpu"] = unmarshal_PublicCatalogProductPropertiesHardwareGPU(field)
    else:
        args["gpu"] = None

    return PublicCatalogProductPropertiesHardware(**args)


def unmarshal_PublicCatalogProductPropertiesInstance(
    data: Any,
) -> PublicCatalogProductPropertiesInstance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesInstance' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("range", None)
    if field is not None:
        args["range"] = field
    else:
        args["range"] = None

    field = data.get("offer_id", None)
    if field is not None:
        args["offer_id"] = field
    else:
        args["offer_id"] = None

    field = data.get("recommended_replacement_offer_ids", None)
    if field is not None:
        args["recommended_replacement_offer_ids"] = field
    else:
        args["recommended_replacement_offer_ids"] = []

    return PublicCatalogProductPropertiesInstance(**args)


def unmarshal_PublicCatalogProductPropertiesObjectStorage(
    data: Any,
) -> PublicCatalogProductPropertiesObjectStorage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPropertiesObjectStorage' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    return PublicCatalogProductPropertiesObjectStorage(**args)


def unmarshal_PublicCatalogProductEnvironmentalImpactEstimation(
    data: Any,
) -> PublicCatalogProductEnvironmentalImpactEstimation:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductEnvironmentalImpactEstimation' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("kg_co2_equivalent", None)
    if field is not None:
        args["kg_co2_equivalent"] = field
    else:
        args["kg_co2_equivalent"] = None

    field = data.get("m3_water_usage", None)
    if field is not None:
        args["m3_water_usage"] = field
    else:
        args["m3_water_usage"] = None

    return PublicCatalogProductEnvironmentalImpactEstimation(**args)


def unmarshal_PublicCatalogProductLocality(data: Any) -> PublicCatalogProductLocality:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductLocality' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("global", None)
    if field is not None:
        args["global_"] = field
    else:
        args["global_"] = False

    field = data.get("region", None)
    if field is not None:
        args["region"] = field
    else:
        args["region"] = None

    field = data.get("zone", None)
    if field is not None:
        args["zone"] = field
    else:
        args["zone"] = None

    field = data.get("datacenter", None)
    if field is not None:
        args["datacenter"] = field
    else:
        args["datacenter"] = None

    return PublicCatalogProductLocality(**args)


def unmarshal_PublicCatalogProductPrice(data: Any) -> PublicCatalogProductPrice:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductPrice' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("retail_price", None)
    if field is not None:
        args["retail_price"] = unmarshal_Money(field)
    else:
        args["retail_price"] = None

    return PublicCatalogProductPrice(**args)


def unmarshal_PublicCatalogProductProperties(
    data: Any,
) -> PublicCatalogProductProperties:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductProperties' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("hardware", None)
    if field is not None:
        args["hardware"] = unmarshal_PublicCatalogProductPropertiesHardware(field)
    else:
        args["hardware"] = None

    field = data.get("dedibox", None)
    if field is not None:
        args["dedibox"] = unmarshal_PublicCatalogProductPropertiesDedibox(field)
    else:
        args["dedibox"] = None

    field = data.get("elastic_metal", None)
    if field is not None:
        args["elastic_metal"] = unmarshal_PublicCatalogProductPropertiesElasticMetal(
            field
        )
    else:
        args["elastic_metal"] = None

    field = data.get("apple_silicon", None)
    if field is not None:
        args["apple_silicon"] = unmarshal_PublicCatalogProductPropertiesAppleSilicon(
            field
        )
    else:
        args["apple_silicon"] = None

    field = data.get("instance", None)
    if field is not None:
        args["instance"] = unmarshal_PublicCatalogProductPropertiesInstance(field)
    else:
        args["instance"] = None

    field = data.get("block_storage", None)
    if field is not None:
        args["block_storage"] = unmarshal_PublicCatalogProductPropertiesBlockStorage(
            field
        )
    else:
        args["block_storage"] = None

    field = data.get("object_storage", None)
    if field is not None:
        args["object_storage"] = unmarshal_PublicCatalogProductPropertiesObjectStorage(
            field
        )
    else:
        args["object_storage"] = None

    return PublicCatalogProductProperties(**args)


def unmarshal_PublicCatalogProductUnitOfMeasure(
    data: Any,
) -> PublicCatalogProductUnitOfMeasure:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProductUnitOfMeasure' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("unit", None)
    if field is not None:
        args["unit"] = field
    else:
        args["unit"] = None

    field = data.get("size", None)
    if field is not None:
        args["size"] = field
    else:
        args["size"] = None

    return PublicCatalogProductUnitOfMeasure(**args)


def unmarshal_PublicCatalogProduct(data: Any) -> PublicCatalogProduct:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PublicCatalogProduct' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("sku", None)
    if field is not None:
        args["sku"] = field
    else:
        args["sku"] = None

    field = data.get("service_category", None)
    if field is not None:
        args["service_category"] = field
    else:
        args["service_category"] = None

    field = data.get("product_category", None)
    if field is not None:
        args["product_category"] = field
    else:
        args["product_category"] = None

    field = data.get("product", None)
    if field is not None:
        args["product"] = field
    else:
        args["product"] = None

    field = data.get("variant", None)
    if field is not None:
        args["variant"] = field
    else:
        args["variant"] = None

    field = data.get("description", None)
    if field is not None:
        args["description"] = field
    else:
        args["description"] = None

    field = data.get("status", None)
    if field is not None:
        args["status"] = field
    else:
        args["status"] = PublicCatalogProductStatus.UNKNOWN_STATUS

    field = data.get("locality", None)
    if field is not None:
        args["locality"] = unmarshal_PublicCatalogProductLocality(field)
    else:
        args["locality"] = None

    field = data.get("price", None)
    if field is not None:
        args["price"] = unmarshal_PublicCatalogProductPrice(field)
    else:
        args["price"] = None

    field = data.get("properties", None)
    if field is not None:
        args["properties"] = unmarshal_PublicCatalogProductProperties(field)
    else:
        args["properties"] = None

    field = data.get("environmental_impact_estimation", None)
    if field is not None:
        args["environmental_impact_estimation"] = (
            unmarshal_PublicCatalogProductEnvironmentalImpactEstimation(field)
        )
    else:
        args["environmental_impact_estimation"] = None

    field = data.get("unit_of_measure", None)
    if field is not None:
        args["unit_of_measure"] = unmarshal_PublicCatalogProductUnitOfMeasure(field)
    else:
        args["unit_of_measure"] = None

    field = data.get("end_of_life_at", None)
    if field is not None:
        args["end_of_life_at"] = (
            parser.isoparse(field) if isinstance(field, str) else field
        )
    else:
        args["end_of_life_at"] = None

    return PublicCatalogProduct(**args)


def unmarshal_ListPublicCatalogProductsResponse(
    data: Any,
) -> ListPublicCatalogProductsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListPublicCatalogProductsResponse' failed as data isn't a dictionary."
        )

    args: dict[str, Any] = {}

    field = data.get("products", None)
    if field is not None:
        args["products"] = (
            [unmarshal_PublicCatalogProduct(v) for v in field]
            if field is not None
            else None
        )
    else:
        args["products"] = []

    field = data.get("total_count", None)
    if field is not None:
        args["total_count"] = field
    else:
        args["total_count"] = 0

    return ListPublicCatalogProductsResponse(**args)
