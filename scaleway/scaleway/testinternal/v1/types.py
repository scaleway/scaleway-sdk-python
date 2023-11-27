# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from scaleway_core.bridge import (
    Money,
    Region,
    TimeSeries,
    Zone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)


class ComplexTestEnum(str, Enum, metaclass=StrEnumMeta):
    COMPLEX_ZERO = "complex_zero"
    COMPLEX_ONE = "complex_one"
    COMPLEX_TWO = "complex_two"

    def __str__(self) -> str:
        return str(self.value)


class ListCharactersRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)


class MapEnum(str, Enum, metaclass=StrEnumMeta):
    MAP_ENUM_FOO = "map_enum_foo"
    MAP_ENUM_BAR = "map_enum_bar"
    MAP_ENUM_BAZ = "map_enum_baz"

    def __str__(self) -> str:
        return str(self.value)


class PostAllOptionalMessageNestedEnum(str, Enum, metaclass=StrEnumMeta):
    UNSPECIFIED = "unspecified"
    FOO = "foo"
    BAR = "bar"
    BAZ = "baz"
    NEG = "neg"

    def __str__(self) -> str:
        return str(self.value)


class PostAllTypesMessageNestedEnum(str, Enum, metaclass=StrEnumMeta):
    ZERO = "zero"
    FOO = "foo"
    BAR = "bar"
    BAZ = "baz"
    NEG = "neg"

    def __str__(self) -> str:
        return str(self.value)


class TransientStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    PENDING = "pending"
    ERROR = "error"
    DONE = "done"

    def __str__(self) -> str:
        return str(self.value)


class Type(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN = "unknown"
    START1_XS = "start1_xs"
    START1_S = "start1_s"
    START1_M = "start1_m"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class PostAllTypesMessageNestedMessage:
    bb: int


@dataclass
class PostAllTypesMessage:
    singular_int32: int

    singular_int64: int

    singular_uint32: int

    singular_uint64: int

    singular_sint32: int

    singular_sint64: int

    singular_fixed32: int

    singular_fixed64: int

    singular_sfixed32: int

    singular_sfixed64: int

    singular_float: float

    singular_double: float

    singular_bool: bool

    singular_string: str

    singular_bytes: str

    singular_nested_enum: PostAllTypesMessageNestedEnum

    repeated_int32: List[int]

    repeated_int64: List[int]

    repeated_uint32: List[int]

    repeated_uint64: List[int]

    singular_nested_message: Optional[PostAllTypesMessageNestedMessage]

    repeated_sint32: List[int]

    repeated_sint64: List[int]

    repeated_fixed32: List[int]

    repeated_fixed64: List[int]

    repeated_sfixed32: List[int]

    repeated_sfixed64: List[int]

    repeated_float: List[float]

    repeated_double: List[float]

    repeated_bool: List[bool]

    repeated_string: List[str]

    repeated_bytes: List[str]

    repeated_nested_message: List[PostAllTypesMessageNestedMessage]

    repeated_nested_enum: List[PostAllTypesMessageNestedEnum]

    singular_string_ip: str

    singular_string_ipv4: str

    singular_double_value: Optional[float]

    singular_float_value: Optional[float]

    singular_int64_value: Optional[int]

    singular_uint64_value: Optional[int]

    singular_int32_value: Optional[int]

    singular_uint32_value: Optional[int]

    singular_bool_value: Optional[bool]

    singular_string_value: Optional[str]

    singular_bytes_value: Optional[str]

    singular_timestamp: Optional[datetime]

    singular_any: Optional[Any]

    singular_struct: Optional[Dict[str, Any]]

    singular_money: Optional[Money]

    singular_strings_value: Optional[List[str]]

    singular_duration: Optional[str]

    singular_ip: Optional[str]

    singular_string_value_ip: Optional[str]

    singular_ipv4: Optional[str]

    singular_string_value_ipv4: Optional[str]

    singular_ipv6: Optional[str]

    singular_string_ipv6: str

    singular_uint64_size: int

    singular_string_ipnet: str

    repeated_double_value: List[float]

    singular_string_value_ipv6: Optional[str]

    singular_std_duration: Optional[str]

    singular_std_long_duration: Optional[str]

    singular_size: Optional[int]

    singular_uint64value_size: Optional[int]

    singular_string_value_ipnet: Optional[str]

    repeated_float_value: List[float]

    repeated_int64_value: List[int]

    repeated_uint64_value: List[int]

    repeated_int32_value: List[int]

    repeated_uint32_value: List[int]

    repeated_bool_value: List[bool]

    repeated_string_value: List[str]

    repeated_bytes_value: List[str]

    repeated_timestamp: List[datetime]

    repeated_any: List[Any]

    repeated_struct: List[Dict[str, Any]]

    repeated_money: List[Money]

    repeated_strings_value: List[List[str]]

    repeated_duration: List[str]

    repeated_ip: List[str]

    repeated_string_ip: List[str]

    repeated_string_value_ip: List[str]

    repeated_ipv4: List[str]

    repeated_string_ipv4: List[str]

    repeated_string_value_ipv4: List[str]

    repeated_ipv6: List[str]

    repeated_string_ipv6: List[str]

    repeated_string_value_ipv6: List[str]

    repeated_std_duration: List[str]

    repeated_std_long_duration: List[str]

    repeated_size: List[int]

    repeated_uint64_size: List[int]

    repeated_uint64value_size: List[int]

    repeated_string_ipnet: List[str]

    repeated_string_value_ipnet: List[str]

    oneof_uint32: Optional[int]

    oneof_nested_message: Optional[PostAllTypesMessageNestedMessage]

    oneof_string: Optional[str]

    oneof_bytes: Optional[str]


@dataclass
class PostAllOptionalMessageNestedMessage:
    s: str


@dataclass
class PostAllOptionalMessageNestedMessageWithOptional:
    bb: Optional[int]


@dataclass
class PostBodyAndPathSimpleMessage:
    path: str

    body: str


@dataclass
class ComplexValidateMsg:
    const: str

    int_const: int

    bool_const: bool

    float_const: float

    nested: Optional[ComplexValidateMsg]

    float_val: Optional[float]

    dur_val: Optional[str]

    ts_val: Optional[datetime]

    another: Optional[ComplexValidateMsg]

    double_in: float

    enum_const: ComplexTestEnum

    rep_ts_val: List[datetime]

    map_val: Dict[int, str]

    bytes_val: str

    any_val: Optional[Any]

    x: Optional[str]

    y: Optional[int]


@dataclass
class EchoMessage:
    str_: str

    strs: List[str]


@dataclass
class GetEchoRequest:
    str_: str
    """
    A string.
    """

    strs: Optional[List[str]]
    """
    A slice of strings.
    """


@dataclass
class GetEnumMessage:
    type_: Type


@dataclass
class GetEnumRequest:
    type_: Optional[Type]


@dataclass
class GetTransientRequest:
    transient_id: str


@dataclass
class GetZoneResponse:
    zone: Zone
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ListCharactersRequest:
    page: Optional[int]
    """
    A positive integer to choose the page to display.
    """

    page_size: Optional[int]
    """
    A positive integer lower or equal to 100 to select the number of items to display.
    """

    order_by: Optional[ListCharactersRequestOrderBy]
    """
    Order the listing.
    """

    name: Optional[str]
    """
    Filter characters by name, this is a "contains" matching.
    """

    tags: Optional[List[str]]
    """
    Dummy tags to check the comma_separated_list argument.
    """


@dataclass
class ListCharactersResponse:
    total_count: int

    characters: List[str]


@dataclass
class MetadataResponse:
    metadata: Dict[str, str]


@dataclass
class PatchEnumMessage:
    type_: Type


@dataclass
class PatchEnumRequest:
    type_: Optional[Type]


@dataclass
class PostAllMapTypesMessage:
    map_int32_int32: Dict[int, int]

    map_int64_int64: Dict[int, int]

    map_uint32_uint32: Dict[int, int]

    map_uint64_uint64: Dict[int, int]

    map_sint32_sint32: Dict[int, int]

    map_sint64_sint64: Dict[int, int]

    map_fixed32_fixed32: Dict[int, int]

    map_fixed64_fixed64: Dict[int, int]

    map_sfixed32_sfixed32: Dict[int, int]

    map_sfixed64_sfixed64: Dict[int, int]

    map_int32_float: Dict[int, float]

    map_int32_double: Dict[int, float]

    map_string_string: Dict[str, str]

    map_int32_bytes: Dict[int, str]

    map_int32_enum: Dict[int, MapEnum]

    map_int32_all_types: Dict[int, PostAllTypesMessage]

    map_int32_ip: Dict[int, str]

    map_int32_std_duration: Dict[int, str]

    map_int32_std_long_duration: Dict[int, str]

    map_int32_size: Dict[int, int]

    map_int32_uint64_size: Dict[int, int]

    map_int32_uint64value_size: Dict[int, int]

    map_int32_string_ip: Dict[int, str]

    map_int32_string_value_ip: Dict[int, str]

    map_int32_ipv4: Dict[int, str]

    map_int32_string_ipv4: Dict[int, str]

    map_int32_string_value_ipv4: Dict[int, str]

    map_int32_ipv6: Dict[int, str]

    map_int32_string_ipv6: Dict[int, str]

    map_int32_string_value_ipv6: Dict[int, str]

    map_int32_strings_value: Dict[int, List[str]]

    map_int32_duration: Dict[int, str]


@dataclass
class PostAllMapTypesRequest:
    map_int32_int32: Optional[Dict[int, int]]

    map_int64_int64: Optional[Dict[int, int]]

    map_uint32_uint32: Optional[Dict[int, int]]

    map_uint64_uint64: Optional[Dict[int, int]]

    map_sint32_sint32: Optional[Dict[int, int]]

    map_sint64_sint64: Optional[Dict[int, int]]

    map_fixed32_fixed32: Optional[Dict[int, int]]

    map_fixed64_fixed64: Optional[Dict[int, int]]

    map_sfixed32_sfixed32: Optional[Dict[int, int]]

    map_sfixed64_sfixed64: Optional[Dict[int, int]]

    map_int32_float: Optional[Dict[int, float]]

    map_int32_double: Optional[Dict[int, float]]

    map_string_string: Optional[Dict[str, str]]

    map_int32_bytes: Optional[Dict[int, str]]

    map_int32_enum: Optional[Dict[int, MapEnum]]

    map_int32_all_types: Optional[Dict[int, PostAllTypesMessage]]

    map_int32_ip: Optional[Dict[int, str]]

    map_int32_std_duration: Optional[Dict[int, str]]

    map_int32_std_long_duration: Optional[Dict[int, str]]

    map_int32_size: Optional[Dict[int, int]]

    map_int32_uint64_size: Optional[Dict[int, int]]

    map_int32_uint64value_size: Optional[Dict[int, int]]

    map_int32_string_ip: Optional[Dict[int, str]]

    map_int32_string_value_ip: Optional[Dict[int, str]]

    map_int32_ipv4: Optional[Dict[int, str]]

    map_int32_string_ipv4: Optional[Dict[int, str]]

    map_int32_string_value_ipv4: Optional[Dict[int, str]]

    map_int32_ipv6: Optional[Dict[int, str]]

    map_int32_string_ipv6: Optional[Dict[int, str]]

    map_int32_string_value_ipv6: Optional[Dict[int, str]]

    map_int32_strings_value: Optional[Dict[int, List[str]]]

    map_int32_duration: Optional[Dict[int, str]]


@dataclass
class PostAllOptionalMessage:
    optional_int32: Optional[int]

    optional_int64: Optional[int]

    optional_uint32: Optional[int]

    optional_uint64: Optional[int]

    optional_sint32: Optional[int]

    optional_sint64: Optional[int]

    optional_fixed32: Optional[int]

    optional_fixed64: Optional[int]

    optional_sfixed32: Optional[int]

    optional_sfixed64: Optional[int]

    optional_float: Optional[float]

    optional_double: Optional[float]

    optional_bool: Optional[bool]

    optional_string: Optional[str]

    optional_bytes: Optional[str]

    optional_cord: Optional[str]

    optional_nested_message_with_optional: Optional[
        PostAllOptionalMessageNestedMessageWithOptional
    ]

    lazy_nested_message_with_optional: Optional[
        PostAllOptionalMessageNestedMessageWithOptional
    ]

    optional_nested_enum: Optional[PostAllOptionalMessageNestedEnum]

    optional_nested_message: Optional[PostAllOptionalMessageNestedMessage]

    singular_int32: int

    singular_int64: int

    nested_message: Optional[PostAllOptionalMessageNestedMessage]

    singular_double_value: Optional[float]

    singular_float_value: Optional[float]

    singular_int64_value: Optional[int]

    singular_uint64_value: Optional[int]

    singular_int32_value: Optional[int]

    singular_uint32_value: Optional[int]

    singular_bool_value: Optional[bool]

    singular_string_value: Optional[str]

    singular_bytes_value: Optional[str]

    singular_timestamp: Optional[datetime]

    singular_any: Optional[Any]

    singular_struct: Optional[Dict[str, Any]]

    singular_money: Optional[Money]

    singular_strings_value: Optional[List[str]]

    singular_duration: Optional[str]

    map_string_string: Optional[Dict[str, str]]

    timeseries: Optional[TimeSeries]


@dataclass
class PostAllOptionalRequest:
    optional_int32: Optional[int]

    optional_int64: Optional[int]

    optional_uint32: Optional[int]

    optional_uint64: Optional[int]

    optional_sint32: Optional[int]

    optional_sint64: Optional[int]

    optional_fixed32: Optional[int]

    optional_fixed64: Optional[int]

    optional_sfixed32: Optional[int]

    optional_sfixed64: Optional[int]

    optional_float: Optional[float]

    optional_double: Optional[float]

    optional_bool: Optional[bool]

    optional_string: Optional[str]

    optional_bytes: Optional[str]

    optional_cord: Optional[str]

    optional_nested_message_with_optional: Optional[
        PostAllOptionalMessageNestedMessageWithOptional
    ]

    lazy_nested_message_with_optional: Optional[
        PostAllOptionalMessageNestedMessageWithOptional
    ]

    optional_nested_enum: Optional[PostAllOptionalMessageNestedEnum]

    optional_nested_message: Optional[PostAllOptionalMessageNestedMessage]

    singular_int32: int

    singular_int64: int

    nested_message: Optional[PostAllOptionalMessageNestedMessage]

    singular_double_value: Optional[float]

    singular_float_value: Optional[float]

    singular_int64_value: Optional[int]

    singular_uint64_value: Optional[int]

    singular_int32_value: Optional[int]

    singular_uint32_value: Optional[int]

    singular_bool_value: Optional[bool]

    singular_string_value: Optional[str]

    singular_bytes_value: Optional[str]

    singular_timestamp: Optional[datetime]

    singular_any: Optional[Any]

    singular_struct: Optional[Dict[str, Any]]

    singular_money: Optional[Money]

    singular_strings_value: Optional[List[str]]

    singular_duration: Optional[str]

    map_string_string: Optional[Dict[str, str]]

    timeseries: Optional[TimeSeries]


@dataclass
class PostAllTypesRequest:
    singular_int32: int

    singular_int64: int

    singular_uint32: int

    singular_uint64: int

    singular_sint32: int

    singular_sint64: int

    singular_fixed32: int

    singular_fixed64: int

    singular_sfixed32: int

    singular_sfixed64: int

    singular_float: float

    singular_double: float

    singular_bool: bool

    singular_string: str

    singular_bytes: str

    singular_nested_message: Optional[PostAllTypesMessageNestedMessage]

    singular_nested_enum: Optional[PostAllTypesMessageNestedEnum]

    repeated_int32: Optional[List[int]]

    repeated_int64: Optional[List[int]]

    singular_string_ip: str

    singular_string_ipv4: str

    singular_string_ipv6: str

    singular_uint64_size: int

    singular_string_ipnet: str

    repeated_uint32: Optional[List[int]]

    repeated_uint64: Optional[List[int]]

    repeated_sint32: Optional[List[int]]

    repeated_sint64: Optional[List[int]]

    repeated_fixed32: Optional[List[int]]

    repeated_fixed64: Optional[List[int]]

    repeated_sfixed32: Optional[List[int]]

    repeated_sfixed64: Optional[List[int]]

    repeated_float: Optional[List[float]]

    repeated_double: Optional[List[float]]

    repeated_bool: Optional[List[bool]]

    repeated_string: Optional[List[str]]

    repeated_bytes: Optional[List[str]]

    repeated_nested_message: Optional[List[PostAllTypesMessageNestedMessage]]

    repeated_nested_enum: Optional[List[PostAllTypesMessageNestedEnum]]

    singular_double_value: Optional[float]

    singular_float_value: Optional[float]

    singular_int64_value: Optional[int]

    singular_uint64_value: Optional[int]

    singular_int32_value: Optional[int]

    singular_uint32_value: Optional[int]

    singular_bool_value: Optional[bool]

    singular_string_value: Optional[str]

    singular_bytes_value: Optional[str]

    singular_timestamp: Optional[datetime]

    singular_any: Optional[Any]

    singular_struct: Optional[Dict[str, Any]]

    singular_money: Optional[Money]

    singular_strings_value: Optional[List[str]]

    singular_duration: Optional[str]

    singular_ip: Optional[str]

    singular_string_value_ip: Optional[str]

    singular_ipv4: Optional[str]

    singular_string_value_ipv4: Optional[str]

    singular_ipv6: Optional[str]

    singular_string_value_ipv6: Optional[str]

    singular_std_duration: Optional[str]

    singular_std_long_duration: Optional[str]

    singular_size: Optional[int]

    singular_uint64value_size: Optional[int]

    singular_string_value_ipnet: Optional[str]

    repeated_double_value: Optional[List[float]]

    repeated_float_value: Optional[List[float]]

    repeated_int64_value: Optional[List[int]]

    repeated_uint64_value: Optional[List[int]]

    repeated_int32_value: Optional[List[int]]

    repeated_uint32_value: Optional[List[int]]

    repeated_bool_value: Optional[List[bool]]

    repeated_string_value: Optional[List[str]]

    repeated_bytes_value: Optional[List[str]]

    repeated_timestamp: Optional[List[datetime]]

    repeated_any: Optional[List[Any]]

    repeated_struct: Optional[List[Dict[str, Any]]]

    repeated_money: Optional[List[Money]]

    repeated_strings_value: Optional[List[List[str]]]

    repeated_duration: Optional[List[str]]

    repeated_ip: Optional[List[str]]

    repeated_string_ip: Optional[List[str]]

    repeated_string_value_ip: Optional[List[str]]

    repeated_ipv4: Optional[List[str]]

    repeated_string_ipv4: Optional[List[str]]

    repeated_string_value_ipv4: Optional[List[str]]

    repeated_ipv6: Optional[List[str]]

    repeated_string_ipv6: Optional[List[str]]

    repeated_string_value_ipv6: Optional[List[str]]

    repeated_std_duration: Optional[List[str]]

    repeated_std_long_duration: Optional[List[str]]

    repeated_size: Optional[List[int]]

    repeated_uint64_size: Optional[List[int]]

    repeated_uint64value_size: Optional[List[int]]

    repeated_string_ipnet: Optional[List[str]]

    repeated_string_value_ipnet: Optional[List[str]]

    oneof_uint32: Optional[int]

    oneof_nested_message: Optional[PostAllTypesMessageNestedMessage]

    oneof_string: Optional[str]

    oneof_bytes: Optional[str]


@dataclass
class PostBodyAndPathAndQueryMessage:
    path: str

    query: str

    body: Optional[PostBodyAndPathSimpleMessage]


@dataclass
class PostBodyAndPathAndQueryRequest:
    path: str

    query: str

    body: Optional[PostBodyAndPathSimpleMessage]


@dataclass
class PostBodyAndPathComplexMessage:
    path: str

    body: Optional[PostBodyAndPathSimpleMessage]


@dataclass
class PostBodyAndPathComplexRequest:
    path: str

    body: Optional[PostBodyAndPathSimpleMessage]


@dataclass
class PostBodyAndPathSimple2Message:
    path: str

    body: str


@dataclass
class PostBodyAndPathSimple2Request:
    path: str

    body: str


@dataclass
class PostBodyAndPathSimpleRequest:
    path: str

    body: str


@dataclass
class PostComplexValidateMessage:
    val: Optional[ComplexValidateMsg]


@dataclass
class PostComplexValidateRequest:
    val: Optional[ComplexValidateMsg]


@dataclass
class PostDeprecatedOrganizationMessage:
    organization: Optional[str]


@dataclass
class PostDeprecatedOrganizationRequest:
    organization: Optional[str]


@dataclass
class PostDeprecatedProjectMessage:
    project: Optional[str]


@dataclass
class PostDeprecatedProjectRequest:
    project: Optional[str]


@dataclass
class PostEchoRequest:
    str_: Optional[str]

    strs: Optional[List[str]]


@dataclass
class PostEchoTimeSeriesMessage:
    metrics: Optional[TimeSeries]


@dataclass
class PostEchoTimeSeriesRequest:
    metrics: Optional[TimeSeries]


@dataclass
class PostEnumMessage:
    type_: Type

    type2: Optional[Type]

    type3: Type


@dataclass
class PostEnumRequest:
    type_: Optional[Type]

    type2: Optional[Type]

    type3: Type


@dataclass
class PostIPMessage:
    ip_v4: Optional[str]

    ip_v6: Optional[str]

    ip: Optional[str]


@dataclass
class PostIPRequest:
    ip_v4: Optional[str]

    ip_v6: Optional[str]

    ip: Optional[str]


@dataclass
class PostOneOfMessage:
    test: Optional[str]

    test2: Optional[int]

    test_nested: Optional[EchoMessage]

    test3: Optional[int]


@dataclass
class PostOneOfRequest:
    test: Optional[str]

    test2: Optional[int]

    test_nested: Optional[EchoMessage]

    test3: Optional[int]


@dataclass
class PostOrganizationIdMessage:
    organization_id: str


@dataclass
class PostOrganizationIdRequest:
    organization_id: Optional[str]


@dataclass
class PostProjectIdMessage:
    project_id: str


@dataclass
class PostProjectIdRequest:
    project_id: Optional[str]


@dataclass
class PostScalarTypesMessage:
    double_field: float

    float_field: float

    int32_field: int

    int64_field: int

    uint32_field: int

    uint64_field: int

    bool_field: bool

    string_field: str


@dataclass
class PostScalarTypesRequest:
    double_field: float

    float_field: float

    int32_field: int

    int64_field: int

    uint32_field: int

    uint64_field: int

    bool_field: bool

    string_field: str


@dataclass
class PostTagsMessage:
    tags: Optional[List[str]]


@dataclass
class PostTagsRequest:
    tags: Optional[List[str]]


@dataclass
class PostTransientRequest:
    pass


@dataclass
class PostWaitRequest:
    duration: Optional[str]
    """
    Waiting duration.
    """


@dataclass
class RegionalApiGetMetadataRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiGetRegionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiGetServiceInfoRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class RegionalApiPostEchoRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    str_: Optional[str]

    strs: Optional[List[str]]


@dataclass
class Transient:
    status: TransientStatus


@dataclass
class ZoneApiGetMetadataRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZoneApiGetZoneRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """


@dataclass
class ZoneApiPostEchoRequest:
    zone: Optional[Zone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """

    str_: Optional[str]

    strs: Optional[List[str]]


@dataclass
class _GetRegionResponse:
    region: Region
    """
    Region to target. If none is passed will use default region from the config.
    """
