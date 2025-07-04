# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, List, Optional

from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)

from .types import (
    ComplexTestEnum,
    ListCharactersRequestOrderBy,
    MapEnum,
    PostAllOptionalMessageNestedEnum,
    PostAllTypesMessageNestedEnum,
    TransientStatus,
    Type,PostAllTypesMessageNestedMessage,PostAllTypesMessage,PostAllOptionalMessageNestedMessage,PostAllOptionalMessageNestedMessageWithOptional,PostBodyAndPathSimpleMessage,ComplexValidateMsg,EchoMessage,GetEchoRequest,GetEnumMessage,GetEnumRequest,GetTransientRequest,GetZoneResponse,ListCharactersRequest,ListCharactersResponse,MetadataResponse,PatchEnumMessage,PatchEnumRequest,PostAllMapTypesMessage,PostAllMapTypesRequest,PostAllOptionalMessage,PostAllOptionalRequest,PostAllTypesRequest,PostBodyAndPathAndQueryMessage,PostBodyAndPathAndQueryRequest,PostBodyAndPathComplexMessage,PostBodyAndPathComplexRequest,PostBodyAndPathSimple2Message,PostBodyAndPathSimple2Request,PostBodyAndPathSimpleRequest,PostComplexValidateMessage,PostComplexValidateRequest,PostDeprecatedOrganizationMessage,PostDeprecatedOrganizationRequest,PostDeprecatedProjectMessage,PostDeprecatedProjectRequest,PostEchoRequest,PostEchoTimeSeriesMessage,PostEchoTimeSeriesRequest,PostEnumMessage,PostEnumRequest,PostIPMessage,PostIPRequest,PostOneOfMessage,PostOneOfRequest,PostOrganizationIdMessage,PostOrganizationIdRequest,PostProjectIdMessage,PostProjectIdRequest,PostScalarTypesMessage,PostScalarTypesRequest,PostTagsMessage,PostTagsRequest,PostTransientRequest,PostWaitRequest,RegionalApiGetMetadataRequest,RegionalApiGetRegionRequest,RegionalApiGetServiceInfoRequest,RegionalApiPostEchoRequest,Transient,ZoneApiGetMetadataRequest,ZoneApiGetZoneRequest,ZoneApiPostEchoRequest,)

@dataclass
class _GetRegionResponse:
    region: ScwRegion
    """
    Region to target. If none is passed will use default region from the config.
    """
