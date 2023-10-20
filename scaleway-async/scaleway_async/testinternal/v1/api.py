# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Any, Awaitable, Dict, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Money,
    Region,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    Zone,
    unmarshal_ScwFile,
    unmarshal_ServiceInfo,
)
from scaleway_core.utils import (
    WaitForOptions,
    random_name,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ListCharactersRequestOrderBy,
    MapEnum,
    PostAllOptionalMessageNestedEnum,
    PostAllTypesMessageNestedEnum,
    Type,
    ComplexValidateMsg,
    EchoMessage,
    GetEnumMessage,
    GetZoneResponse,
    ListCharactersResponse,
    MetadataResponse,
    PatchEnumMessage,
    PatchEnumRequest,
    PostAllMapTypesMessage,
    PostAllMapTypesRequest,
    PostAllOptionalMessage,
    PostAllOptionalMessageNestedMessage,
    PostAllOptionalMessageNestedMessageWithOptional,
    PostAllOptionalRequest,
    PostAllTypesMessage,
    PostAllTypesMessageNestedMessage,
    PostAllTypesRequest,
    PostBodyAndPathAndQueryMessage,
    PostBodyAndPathAndQueryRequest,
    PostBodyAndPathComplexMessage,
    PostBodyAndPathComplexRequest,
    PostBodyAndPathSimple2Message,
    PostBodyAndPathSimple2Request,
    PostBodyAndPathSimpleMessage,
    PostBodyAndPathSimpleRequest,
    PostComplexValidateMessage,
    PostComplexValidateRequest,
    PostDeprecatedOrganizationMessage,
    PostDeprecatedOrganizationRequest,
    PostDeprecatedProjectMessage,
    PostDeprecatedProjectRequest,
    PostEchoRequest,
    PostEchoTimeSeriesMessage,
    PostEchoTimeSeriesRequest,
    PostEnumMessage,
    PostEnumRequest,
    PostIPMessage,
    PostIPRequest,
    PostOneOfMessage,
    PostOneOfRequest,
    PostOrganizationIdMessage,
    PostOrganizationIdRequest,
    PostProjectIdMessage,
    PostProjectIdRequest,
    PostScalarTypesMessage,
    PostScalarTypesRequest,
    PostTagsMessage,
    PostTagsRequest,
    PostWaitRequest,
    RegionalApiPostEchoRequest,
    Transient,
    ZoneApiPostEchoRequest,
    _GetRegionResponse,
)
from .content import (
    TRANSIENT_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_PostAllTypesMessage,
    unmarshal_PostBodyAndPathSimpleMessage,
    unmarshal_EchoMessage,
    unmarshal_GetEnumMessage,
    unmarshal_GetZoneResponse,
    unmarshal_ListCharactersResponse,
    unmarshal_MetadataResponse,
    unmarshal_PatchEnumMessage,
    unmarshal_PostAllMapTypesMessage,
    unmarshal_PostAllOptionalMessage,
    unmarshal_PostBodyAndPathAndQueryMessage,
    unmarshal_PostBodyAndPathComplexMessage,
    unmarshal_PostBodyAndPathSimple2Message,
    unmarshal_PostComplexValidateMessage,
    unmarshal_PostDeprecatedOrganizationMessage,
    unmarshal_PostDeprecatedProjectMessage,
    unmarshal_PostEchoTimeSeriesMessage,
    unmarshal_PostEnumMessage,
    unmarshal_PostIPMessage,
    unmarshal_PostOneOfMessage,
    unmarshal_PostOrganizationIdMessage,
    unmarshal_PostProjectIdMessage,
    unmarshal_PostScalarTypesMessage,
    unmarshal_PostTagsMessage,
    unmarshal_Transient,
    unmarshal__GetRegionResponse,
    marshal_PatchEnumRequest,
    marshal_PostAllMapTypesRequest,
    marshal_PostAllOptionalRequest,
    marshal_PostAllTypesRequest,
    marshal_PostBodyAndPathAndQueryRequest,
    marshal_PostBodyAndPathComplexRequest,
    marshal_PostBodyAndPathSimple2Request,
    marshal_PostBodyAndPathSimpleRequest,
    marshal_PostComplexValidateRequest,
    marshal_PostDeprecatedOrganizationRequest,
    marshal_PostDeprecatedProjectRequest,
    marshal_PostEchoRequest,
    marshal_PostEchoTimeSeriesRequest,
    marshal_PostEnumRequest,
    marshal_PostIPRequest,
    marshal_PostOneOfRequest,
    marshal_PostOrganizationIdRequest,
    marshal_PostProjectIdRequest,
    marshal_PostScalarTypesRequest,
    marshal_PostTagsRequest,
    marshal_PostWaitRequest,
    marshal_RegionalApiPostEchoRequest,
    marshal_ZoneApiPostEchoRequest,
)


class TestinternalV1API(API):
    """
    This API allows us to test.
    """

    async def get_service_info(
        self,
    ) -> ServiceInfo:
        """

        :return: :class:`ServiceInfo <ServiceInfo>`

        Usage:
        ::

            result = await api.get_service_info()
        """

        res = self._request(
            "GET",
            "/test-internal/v1",
        )

        self._throw_on_error(res)
        return unmarshal_ServiceInfo(res.json())

    async def delete_nothing(
        self,
    ) -> None:
        """
        This method deletes nothing.
        This method deletes nothing.


        Usage:
        ::

            result = await api.delete_nothing()
        """

        res = self._request(
            "DELETE",
            "/test-internal/v1",
        )

        self._throw_on_error(res)

    async def get_echo(
        self,
        *,
        str_: str,
        strs: Optional[List[str]] = None,
    ) -> EchoMessage:
        """
        Echo the request message.
        ### This is a multiline test.
        :param str_: A string.
        :param strs: A slice of strings.
        :return: :class:`EchoMessage <EchoMessage>`

        Usage:
        ::

            result = await api.get_echo(
                str="example",
            )
        """

        res = self._request(
            "GET",
            "/test-internal/v1/echo",
            params={
                "str": str_,
                "strs": strs,
            },
        )

        self._throw_on_error(res)
        return unmarshal_EchoMessage(res.json())

    async def _post_echo(
        self,
        *,
        str_: Optional[str] = None,
        strs: Optional[List[str]] = None,
    ) -> EchoMessage:
        """
        Echo the request message.
        Echo the request message.
        :param str_:
        :param strs:
        :return: :class:`EchoMessage <EchoMessage>`

        Usage:
        ::

            result = await api._post_echo()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/echo",
            body=marshal_PostEchoRequest(
                PostEchoRequest(
                    str_=str_ or random_name(prefix="name"),
                    strs=strs,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_EchoMessage(res.json())

    async def get_enum(
        self,
        *,
        type_: Optional[Type] = None,
    ) -> GetEnumMessage:
        """
        Get enum.
        Get enum.
        :param type_:
        :return: :class:`GetEnumMessage <GetEnumMessage>`

        Usage:
        ::

            result = await api.get_enum()
        """

        res = self._request(
            "GET",
            "/test-internal/v1/enum",
            params={
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_GetEnumMessage(res.json())

    async def post_enum(
        self,
        *,
        type_: Optional[Type] = None,
        type2: Optional[Type] = None,
        type3: Type = Type.unknown,
    ) -> PostEnumMessage:
        """
        Post enum.
        Post enum.
        :param type_:
        :param type2:
        :param type3:
        :return: :class:`PostEnumMessage <PostEnumMessage>`

        Usage:
        ::

            result = await api.post_enum(
                type3=Type.unknown,
            )
        """

        res = self._request(
            "POST",
            "/test-internal/v1/enum",
            body=marshal_PostEnumRequest(
                PostEnumRequest(
                    type_=type_,
                    type2=type2,
                    type3=type3,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostEnumMessage(res.json())

    async def patch_enum(
        self,
        *,
        type_: Optional[Type] = None,
    ) -> PatchEnumMessage:
        """
        Patch enum.
        Patch enum.
        :param type_:
        :return: :class:`PatchEnumMessage <PatchEnumMessage>`

        Usage:
        ::

            result = await api.patch_enum()
        """

        res = self._request(
            "PATCH",
            "/test-internal/v1/enum",
            body=marshal_PatchEnumRequest(
                PatchEnumRequest(
                    type_=type_,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PatchEnumMessage(res.json())

    async def post_tags(
        self,
        *,
        tags: Optional[List[str]] = None,
    ) -> PostTagsMessage:
        """
        Post tags.
        Post tags.
        :param tags:
        :return: :class:`PostTagsMessage <PostTagsMessage>`

        Usage:
        ::

            result = await api.post_tags()
        """

        res = self._request(
            "PUT",
            "/test-internal/v1/tags",
            body=marshal_PostTagsRequest(
                PostTagsRequest(
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostTagsMessage(res.json())

    async def post_file(
        self,
    ) -> ScwFile:
        """
        Post file.
        Post file.

        :return: :class:`ScwFile <ScwFile>`

        Usage:
        ::

            result = await api.post_file()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/file",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_ScwFile(res.json())

    async def post_ip(
        self,
        *,
        ip_v4: Optional[str] = None,
        ip_v6: Optional[str] = None,
        ip: Optional[str] = None,
    ) -> PostIPMessage:
        """
        Post IP.
        Post IP.
        :param ip_v4:
        :param ip_v6:
        :param ip:
        :return: :class:`PostIPMessage <PostIPMessage>`

        Usage:
        ::

            result = await api.post_ip()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/ip",
            body=marshal_PostIPRequest(
                PostIPRequest(
                    ip_v4=ip_v4,
                    ip_v6=ip_v6,
                    ip=ip,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostIPMessage(res.json())

    async def post_scalar_types(
        self,
        *,
        double_field: float,
        float_field: float,
        int32_field: int,
        int64_field: int,
        uint32_field: int,
        uint64_field: int,
        bool_field: bool,
        string_field: str,
    ) -> PostScalarTypesMessage:
        """
        Post scalar types.
        Post scalar types.
        :param double_field:
        :param float_field:
        :param int32_field:
        :param int64_field:
        :param uint32_field:
        :param uint64_field:
        :param bool_field:
        :param string_field:
        :return: :class:`PostScalarTypesMessage <PostScalarTypesMessage>`

        Usage:
        ::

            result = await api.post_scalar_types(
                double_field=3.14,
                float_field=3.14,
                int32_field=1,
                int64_field=1,
                uint32_field=1,
                uint64_field=1,
                bool_field=False,
                string_field="example",
            )
        """

        res = self._request(
            "POST",
            "/test-internal/v1/scalar-types",
            body=marshal_PostScalarTypesRequest(
                PostScalarTypesRequest(
                    double_field=double_field,
                    float_field=float_field,
                    int32_field=int32_field,
                    int64_field=int64_field,
                    uint32_field=uint32_field,
                    uint64_field=uint64_field,
                    bool_field=bool_field,
                    string_field=string_field,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostScalarTypesMessage(res.json())

    async def get_metadata(
        self,
    ) -> MetadataResponse:
        """

        :return: :class:`MetadataResponse <MetadataResponse>`

        Usage:
        ::

            result = await api.get_metadata()
        """

        res = self._request(
            "GET",
            "/test-internal/v1/metadata",
        )

        self._throw_on_error(res)
        return unmarshal_MetadataResponse(res.json())

    async def post_wait(
        self,
        *,
        duration: Optional[str] = None,
    ) -> None:
        """
        Wait until a given time in second.
        Wait until a given time in second.
        :param duration: Waiting duration.

        Usage:
        ::

            result = await api.post_wait()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/wait",
            body=marshal_PostWaitRequest(
                PostWaitRequest(
                    duration=duration,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)

    async def get_region(
        self,
    ) -> _GetRegionResponse:
        """
        Get a region.
        Get a region.

        :return: :class:`_GetRegionResponse <_GetRegionResponse>`

        Usage:
        ::

            result = await api.get_region()
        """

        res = self._request(
            "GET",
            "/test-internal/v1/region",
        )

        self._throw_on_error(res)
        return unmarshal__GetRegionResponse(res.json())

    async def post_organization_id(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> PostOrganizationIdMessage:
        """
        Post an organization ID.
        Post an organization ID.
        :param organization_id:
        :return: :class:`PostOrganizationIdMessage <PostOrganizationIdMessage>`

        Usage:
        ::

            result = await api.post_organization_id()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/organization-id",
            body=marshal_PostOrganizationIdRequest(
                PostOrganizationIdRequest(
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostOrganizationIdMessage(res.json())

    async def post_deprecated_organization(
        self,
        *,
        organization: Optional[str] = None,
    ) -> PostDeprecatedOrganizationMessage:
        """
        Post a deprecated organization ID.
        Post a deprecated organization ID.
        :param organization:
        :return: :class:`PostDeprecatedOrganizationMessage <PostDeprecatedOrganizationMessage>`
        :deprecated

        Usage:
        ::

            result = await api.post_deprecated_organization()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/deprecated-organization",
            body=marshal_PostDeprecatedOrganizationRequest(
                PostDeprecatedOrganizationRequest(
                    organization=organization,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostDeprecatedOrganizationMessage(res.json())

    async def post_project_id(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> PostProjectIdMessage:
        """
        :param project_id:
        :return: :class:`PostProjectIdMessage <PostProjectIdMessage>`

        Usage:
        ::

            result = await api.post_project_id()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/project-id",
            body=marshal_PostProjectIdRequest(
                PostProjectIdRequest(
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostProjectIdMessage(res.json())

    async def post_deprecated_project(
        self,
        *,
        project: Optional[str] = None,
    ) -> PostDeprecatedProjectMessage:
        """
        :param project:
        :return: :class:`PostDeprecatedProjectMessage <PostDeprecatedProjectMessage>`
        :deprecated

        Usage:
        ::

            result = await api.post_deprecated_project()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/deprecated-project",
            body=marshal_PostDeprecatedProjectRequest(
                PostDeprecatedProjectRequest(
                    project=project,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostDeprecatedProjectMessage(res.json())

    async def post_one_of(
        self,
        *,
        test: Optional[str] = None,
        test2: Optional[int] = None,
        test_nested: Optional[EchoMessage] = None,
        test3: Optional[int] = None,
    ) -> PostOneOfMessage:
        """
        :param test:
        :param test2:
        :param test_nested:
        :param test3:
        :return: :class:`PostOneOfMessage <PostOneOfMessage>`

        Usage:
        ::

            result = await api.post_one_of()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/oneof",
            body=marshal_PostOneOfRequest(
                PostOneOfRequest(
                    test=test,
                    test2=test2,
                    test_nested=test_nested,
                    test3=test3,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostOneOfMessage(res.json())

    async def post_body_and_path_simple(
        self,
        *,
        path: str,
        body: str,
    ) -> PostBodyAndPathSimpleMessage:
        """
        :param path:
        :param body:
        :return: :class:`PostBodyAndPathSimpleMessage <PostBodyAndPathSimpleMessage>`

        Usage:
        ::

            result = await api.post_body_and_path_simple(
                path="example",
                body="example",
            )
        """

        param_path = validate_path_param("path", path)

        res = self._request(
            "POST",
            f"/test-internal/v1/paths/{param_path}/simple",
            body=marshal_PostBodyAndPathSimpleRequest(
                PostBodyAndPathSimpleRequest(
                    path=path,
                    body=body,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostBodyAndPathSimpleMessage(res.json())

    async def post_body_and_path_simple2(
        self,
        *,
        path: str,
        body: str,
    ) -> PostBodyAndPathSimple2Message:
        """
        :param path:
        :param body:
        :return: :class:`PostBodyAndPathSimple2Message <PostBodyAndPathSimple2Message>`

        Usage:
        ::

            result = await api.post_body_and_path_simple2(
                path="example",
                body="example",
            )
        """

        param_path = validate_path_param("path", path)

        res = self._request(
            "POST",
            f"/test-internal/v1/paths/{param_path}/simple2",
            body=marshal_PostBodyAndPathSimple2Request(
                PostBodyAndPathSimple2Request(
                    path=path,
                    body=body,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostBodyAndPathSimple2Message(res.json())

    async def post_body_and_path_complex(
        self,
        *,
        path: str,
        body: Optional[PostBodyAndPathSimpleMessage] = None,
    ) -> PostBodyAndPathComplexMessage:
        """
        :param path:
        :param body:
        :return: :class:`PostBodyAndPathComplexMessage <PostBodyAndPathComplexMessage>`

        Usage:
        ::

            result = await api.post_body_and_path_complex(
                path="example",
            )
        """

        param_path = validate_path_param("path", path)

        res = self._request(
            "POST",
            f"/test-internal/v1/paths/{param_path}/complex",
            body=marshal_PostBodyAndPathComplexRequest(
                PostBodyAndPathComplexRequest(
                    path=path,
                    body=body,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostBodyAndPathComplexMessage(res.json())

    async def post_body_and_path_and_query(
        self,
        *,
        path: str,
        query: str,
        body: Optional[PostBodyAndPathSimpleMessage] = None,
    ) -> PostBodyAndPathAndQueryMessage:
        """
        :param path:
        :param query:
        :param body:
        :return: :class:`PostBodyAndPathAndQueryMessage <PostBodyAndPathAndQueryMessage>`

        Usage:
        ::

            result = await api.post_body_and_path_and_query(
                path="example",
                query="example",
            )
        """

        param_path = validate_path_param("path", path)

        res = self._request(
            "POST",
            f"/test-internal/v1/paths/{param_path}/bodyquery",
            body=marshal_PostBodyAndPathAndQueryRequest(
                PostBodyAndPathAndQueryRequest(
                    path=path,
                    query=query,
                    body=body,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostBodyAndPathAndQueryMessage(res.json())

    async def post_all_map_types(
        self,
        *,
        map_int32_int32: Optional[Dict[int, int]] = None,
        map_int64_int64: Optional[Dict[int, int]] = None,
        map_uint32_uint32: Optional[Dict[int, int]] = None,
        map_uint64_uint64: Optional[Dict[int, int]] = None,
        map_sint32_sint32: Optional[Dict[int, int]] = None,
        map_sint64_sint64: Optional[Dict[int, int]] = None,
        map_fixed32_fixed32: Optional[Dict[int, int]] = None,
        map_fixed64_fixed64: Optional[Dict[int, int]] = None,
        map_sfixed32_sfixed32: Optional[Dict[int, int]] = None,
        map_sfixed64_sfixed64: Optional[Dict[int, int]] = None,
        map_int32_float: Optional[Dict[int, float]] = None,
        map_int32_double: Optional[Dict[int, float]] = None,
        map_string_string: Optional[Dict[str, str]] = None,
        map_int32_bytes: Optional[Dict[int, str]] = None,
        map_int32_enum: Optional[Dict[int, MapEnum]] = None,
        map_int32_all_types: Optional[Dict[int, PostAllTypesMessage]] = None,
        map_int32_ip: Optional[Dict[int, str]] = None,
        map_int32_std_duration: Optional[Dict[int, str]] = None,
        map_int32_std_long_duration: Optional[Dict[int, str]] = None,
        map_int32_size: Optional[Dict[int, int]] = None,
        map_int32_uint64_size: Optional[Dict[int, int]] = None,
        map_int32_uint64value_size: Optional[Dict[int, int]] = None,
        map_int32_string_ip: Optional[Dict[int, str]] = None,
        map_int32_string_value_ip: Optional[Dict[int, str]] = None,
        map_int32_ipv4: Optional[Dict[int, str]] = None,
        map_int32_string_ipv4: Optional[Dict[int, str]] = None,
        map_int32_string_value_ipv4: Optional[Dict[int, str]] = None,
        map_int32_ipv6: Optional[Dict[int, str]] = None,
        map_int32_string_ipv6: Optional[Dict[int, str]] = None,
        map_int32_string_value_ipv6: Optional[Dict[int, str]] = None,
        map_int32_strings_value: Optional[Dict[int, List[str]]] = None,
        map_int32_duration: Optional[Dict[int, str]] = None,
    ) -> PostAllMapTypesMessage:
        """
        :param map_int32_int32:
        :param map_int64_int64:
        :param map_uint32_uint32:
        :param map_uint64_uint64:
        :param map_sint32_sint32:
        :param map_sint64_sint64:
        :param map_fixed32_fixed32:
        :param map_fixed64_fixed64:
        :param map_sfixed32_sfixed32:
        :param map_sfixed64_sfixed64:
        :param map_int32_float:
        :param map_int32_double:
        :param map_string_string:
        :param map_int32_bytes:
        :param map_int32_enum:
        :param map_int32_all_types:
        :param map_int32_ip:
        :param map_int32_std_duration:
        :param map_int32_std_long_duration:
        :param map_int32_size:
        :param map_int32_uint64_size:
        :param map_int32_uint64value_size:
        :param map_int32_string_ip:
        :param map_int32_string_value_ip:
        :param map_int32_ipv4:
        :param map_int32_string_ipv4:
        :param map_int32_string_value_ipv4:
        :param map_int32_ipv6:
        :param map_int32_string_ipv6:
        :param map_int32_string_value_ipv6:
        :param map_int32_strings_value:
        :param map_int32_duration:
        :return: :class:`PostAllMapTypesMessage <PostAllMapTypesMessage>`

        Usage:
        ::

            result = await api.post_all_map_types()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/map",
            body=marshal_PostAllMapTypesRequest(
                PostAllMapTypesRequest(
                    map_int32_int32=map_int32_int32,
                    map_int64_int64=map_int64_int64,
                    map_uint32_uint32=map_uint32_uint32,
                    map_uint64_uint64=map_uint64_uint64,
                    map_sint32_sint32=map_sint32_sint32,
                    map_sint64_sint64=map_sint64_sint64,
                    map_fixed32_fixed32=map_fixed32_fixed32,
                    map_fixed64_fixed64=map_fixed64_fixed64,
                    map_sfixed32_sfixed32=map_sfixed32_sfixed32,
                    map_sfixed64_sfixed64=map_sfixed64_sfixed64,
                    map_int32_float=map_int32_float,
                    map_int32_double=map_int32_double,
                    map_string_string=map_string_string,
                    map_int32_bytes=map_int32_bytes,
                    map_int32_enum=map_int32_enum,
                    map_int32_all_types=map_int32_all_types,
                    map_int32_ip=map_int32_ip,
                    map_int32_std_duration=map_int32_std_duration,
                    map_int32_std_long_duration=map_int32_std_long_duration,
                    map_int32_size=map_int32_size,
                    map_int32_uint64_size=map_int32_uint64_size,
                    map_int32_uint64value_size=map_int32_uint64value_size,
                    map_int32_string_ip=map_int32_string_ip,
                    map_int32_string_value_ip=map_int32_string_value_ip,
                    map_int32_ipv4=map_int32_ipv4,
                    map_int32_string_ipv4=map_int32_string_ipv4,
                    map_int32_string_value_ipv4=map_int32_string_value_ipv4,
                    map_int32_ipv6=map_int32_ipv6,
                    map_int32_string_ipv6=map_int32_string_ipv6,
                    map_int32_string_value_ipv6=map_int32_string_value_ipv6,
                    map_int32_strings_value=map_int32_strings_value,
                    map_int32_duration=map_int32_duration,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostAllMapTypesMessage(res.json())

    async def post_all_types(
        self,
        *,
        singular_int32: int,
        singular_int64: int,
        singular_uint32: int,
        singular_uint64: int,
        singular_sint32: int,
        singular_sint64: int,
        singular_fixed32: int,
        singular_fixed64: int,
        singular_sfixed32: int,
        singular_sfixed64: int,
        singular_float: float,
        singular_double: float,
        singular_bool: bool,
        singular_string: str,
        singular_bytes: str,
        singular_nested_message: Optional[PostAllTypesMessageNestedMessage] = None,
        singular_nested_enum: Optional[PostAllTypesMessageNestedEnum] = None,
        repeated_int32: Optional[List[int]] = None,
        singular_string_ip: str,
        singular_string_ipv4: str,
        singular_string_ipv6: str,
        singular_uint64_size: int,
        singular_string_ipnet: str,
        repeated_int64: Optional[List[int]] = None,
        repeated_uint32: Optional[List[int]] = None,
        repeated_uint64: Optional[List[int]] = None,
        repeated_sint32: Optional[List[int]] = None,
        repeated_sint64: Optional[List[int]] = None,
        repeated_fixed32: Optional[List[int]] = None,
        repeated_fixed64: Optional[List[int]] = None,
        repeated_sfixed32: Optional[List[int]] = None,
        repeated_sfixed64: Optional[List[int]] = None,
        repeated_float: Optional[List[float]] = None,
        repeated_double: Optional[List[float]] = None,
        repeated_bool: Optional[List[bool]] = None,
        repeated_string: Optional[List[str]] = None,
        repeated_bytes: Optional[List[str]] = None,
        repeated_nested_message: Optional[
            List[PostAllTypesMessageNestedMessage]
        ] = None,
        repeated_nested_enum: Optional[List[PostAllTypesMessageNestedEnum]] = None,
        oneof_uint32: Optional[int] = None,
        oneof_nested_message: Optional[PostAllTypesMessageNestedMessage] = None,
        oneof_string: Optional[str] = None,
        oneof_bytes: Optional[str] = None,
        singular_double_value: Optional[float] = None,
        singular_float_value: Optional[float] = None,
        singular_int64_value: Optional[int] = None,
        singular_uint64_value: Optional[int] = None,
        singular_int32_value: Optional[int] = None,
        singular_uint32_value: Optional[int] = None,
        singular_bool_value: Optional[bool] = None,
        singular_string_value: Optional[str] = None,
        singular_bytes_value: Optional[str] = None,
        singular_timestamp: Optional[datetime] = None,
        singular_any: Optional[Any] = None,
        singular_struct: Optional[Dict[str, Any]] = None,
        singular_money: Optional[Money] = None,
        singular_strings_value: Optional[List[str]] = None,
        singular_duration: Optional[str] = None,
        singular_ip: Optional[str] = None,
        singular_string_value_ip: Optional[str] = None,
        singular_ipv4: Optional[str] = None,
        singular_string_value_ipv4: Optional[str] = None,
        singular_ipv6: Optional[str] = None,
        singular_string_value_ipv6: Optional[str] = None,
        singular_std_duration: Optional[str] = None,
        singular_std_long_duration: Optional[str] = None,
        singular_size: Optional[int] = None,
        singular_uint64value_size: Optional[int] = None,
        singular_string_value_ipnet: Optional[str] = None,
        repeated_double_value: Optional[List[float]] = None,
        repeated_float_value: Optional[List[float]] = None,
        repeated_int64_value: Optional[List[int]] = None,
        repeated_uint64_value: Optional[List[int]] = None,
        repeated_int32_value: Optional[List[int]] = None,
        repeated_uint32_value: Optional[List[int]] = None,
        repeated_bool_value: Optional[List[bool]] = None,
        repeated_string_value: Optional[List[str]] = None,
        repeated_bytes_value: Optional[List[str]] = None,
        repeated_timestamp: Optional[List[datetime]] = None,
        repeated_any: Optional[List[Any]] = None,
        repeated_struct: Optional[List[Dict[str, Any]]] = None,
        repeated_money: Optional[List[Money]] = None,
        repeated_strings_value: Optional[List[List[str]]] = None,
        repeated_duration: Optional[List[str]] = None,
        repeated_ip: Optional[List[str]] = None,
        repeated_string_ip: Optional[List[str]] = None,
        repeated_string_value_ip: Optional[List[str]] = None,
        repeated_ipv4: Optional[List[str]] = None,
        repeated_string_ipv4: Optional[List[str]] = None,
        repeated_string_value_ipv4: Optional[List[str]] = None,
        repeated_ipv6: Optional[List[str]] = None,
        repeated_string_ipv6: Optional[List[str]] = None,
        repeated_string_value_ipv6: Optional[List[str]] = None,
        repeated_std_duration: Optional[List[str]] = None,
        repeated_std_long_duration: Optional[List[str]] = None,
        repeated_size: Optional[List[int]] = None,
        repeated_uint64_size: Optional[List[int]] = None,
        repeated_uint64value_size: Optional[List[int]] = None,
        repeated_string_ipnet: Optional[List[str]] = None,
        repeated_string_value_ipnet: Optional[List[str]] = None,
    ) -> PostAllTypesMessage:
        """
        Post all types.
        Post all types.
        :param singular_int32:
        :param singular_int64:
        :param singular_uint32:
        :param singular_uint64:
        :param singular_sint32:
        :param singular_sint64:
        :param singular_fixed32:
        :param singular_fixed64:
        :param singular_sfixed32:
        :param singular_sfixed64:
        :param singular_float:
        :param singular_double:
        :param singular_bool:
        :param singular_string:
        :param singular_bytes:
        :param singular_nested_message:
        :param singular_nested_enum:
        :param repeated_int32:
        :param singular_string_ip:
        :param singular_string_ipv4:
        :param singular_string_ipv6:
        :param singular_uint64_size:
        :param singular_string_ipnet:
        :param repeated_int64:
        :param repeated_uint32:
        :param repeated_uint64:
        :param repeated_sint32:
        :param repeated_sint64:
        :param repeated_fixed32:
        :param repeated_fixed64:
        :param repeated_sfixed32:
        :param repeated_sfixed64:
        :param repeated_float:
        :param repeated_double:
        :param repeated_bool:
        :param repeated_string:
        :param repeated_bytes:
        :param repeated_nested_message:
        :param repeated_nested_enum:
        :param oneof_uint32:
        :param oneof_nested_message:
        :param oneof_string:
        :param oneof_bytes:
        :param singular_double_value:
        :param singular_float_value:
        :param singular_int64_value:
        :param singular_uint64_value:
        :param singular_int32_value:
        :param singular_uint32_value:
        :param singular_bool_value:
        :param singular_string_value:
        :param singular_bytes_value:
        :param singular_timestamp:
        :param singular_any:
        :param singular_struct:
        :param singular_money:
        :param singular_strings_value:
        :param singular_duration:
        :param singular_ip:
        :param singular_string_value_ip:
        :param singular_ipv4:
        :param singular_string_value_ipv4:
        :param singular_ipv6:
        :param singular_string_value_ipv6:
        :param singular_std_duration:
        :param singular_std_long_duration:
        :param singular_size:
        :param singular_uint64value_size:
        :param singular_string_value_ipnet:
        :param repeated_double_value:
        :param repeated_float_value:
        :param repeated_int64_value:
        :param repeated_uint64_value:
        :param repeated_int32_value:
        :param repeated_uint32_value:
        :param repeated_bool_value:
        :param repeated_string_value:
        :param repeated_bytes_value:
        :param repeated_timestamp:
        :param repeated_any:
        :param repeated_struct:
        :param repeated_money:
        :param repeated_strings_value:
        :param repeated_duration:
        :param repeated_ip:
        :param repeated_string_ip:
        :param repeated_string_value_ip:
        :param repeated_ipv4:
        :param repeated_string_ipv4:
        :param repeated_string_value_ipv4:
        :param repeated_ipv6:
        :param repeated_string_ipv6:
        :param repeated_string_value_ipv6:
        :param repeated_std_duration:
        :param repeated_std_long_duration:
        :param repeated_size:
        :param repeated_uint64_size:
        :param repeated_uint64value_size:
        :param repeated_string_ipnet:
        :param repeated_string_value_ipnet:
        :return: :class:`PostAllTypesMessage <PostAllTypesMessage>`

        Usage:
        ::

            result = await api.post_all_types(
                singular_int32=1,
                singular_int64=1,
                singular_uint32=1,
                singular_uint64=1,
                singular_sint32=1,
                singular_sint64=1,
                singular_fixed32=1,
                singular_fixed64=1,
                singular_sfixed32=1,
                singular_sfixed64=1,
                singular_float=3.14,
                singular_double=3.14,
                singular_bool=False,
                singular_string="example",
                singular_bytes="example",
                singular_string_ip="example",
                singular_string_ipv4="example",
                singular_string_ipv6="example",
                singular_uint64_size=1,
                singular_string_ipnet="example",
            )
        """

        res = self._request(
            "POST",
            "/test-internal/v1/alltypes",
            body=marshal_PostAllTypesRequest(
                PostAllTypesRequest(
                    singular_int32=singular_int32,
                    singular_int64=singular_int64,
                    singular_uint32=singular_uint32,
                    singular_uint64=singular_uint64,
                    singular_sint32=singular_sint32,
                    singular_sint64=singular_sint64,
                    singular_fixed32=singular_fixed32,
                    singular_fixed64=singular_fixed64,
                    singular_sfixed32=singular_sfixed32,
                    singular_sfixed64=singular_sfixed64,
                    singular_float=singular_float,
                    singular_double=singular_double,
                    singular_bool=singular_bool,
                    singular_string=singular_string,
                    singular_bytes=singular_bytes,
                    singular_nested_message=singular_nested_message,
                    singular_nested_enum=singular_nested_enum,
                    repeated_int32=repeated_int32,
                    repeated_int64=repeated_int64,
                    singular_string_ip=singular_string_ip,
                    singular_string_ipv4=singular_string_ipv4,
                    singular_string_ipv6=singular_string_ipv6,
                    singular_uint64_size=singular_uint64_size,
                    singular_string_ipnet=singular_string_ipnet,
                    repeated_uint32=repeated_uint32,
                    repeated_uint64=repeated_uint64,
                    repeated_sint32=repeated_sint32,
                    repeated_sint64=repeated_sint64,
                    repeated_fixed32=repeated_fixed32,
                    repeated_fixed64=repeated_fixed64,
                    repeated_sfixed32=repeated_sfixed32,
                    repeated_sfixed64=repeated_sfixed64,
                    repeated_float=repeated_float,
                    repeated_double=repeated_double,
                    repeated_bool=repeated_bool,
                    repeated_string=repeated_string,
                    repeated_bytes=repeated_bytes,
                    repeated_nested_message=repeated_nested_message,
                    repeated_nested_enum=repeated_nested_enum,
                    singular_double_value=singular_double_value,
                    singular_float_value=singular_float_value,
                    singular_int64_value=singular_int64_value,
                    singular_uint64_value=singular_uint64_value,
                    singular_int32_value=singular_int32_value,
                    singular_uint32_value=singular_uint32_value,
                    singular_bool_value=singular_bool_value,
                    singular_string_value=singular_string_value,
                    singular_bytes_value=singular_bytes_value,
                    singular_timestamp=singular_timestamp,
                    singular_any=singular_any,
                    singular_struct=singular_struct,
                    singular_money=singular_money,
                    singular_strings_value=singular_strings_value,
                    singular_duration=singular_duration,
                    singular_ip=singular_ip,
                    singular_string_value_ip=singular_string_value_ip,
                    singular_ipv4=singular_ipv4,
                    singular_string_value_ipv4=singular_string_value_ipv4,
                    singular_ipv6=singular_ipv6,
                    singular_string_value_ipv6=singular_string_value_ipv6,
                    singular_std_duration=singular_std_duration,
                    singular_std_long_duration=singular_std_long_duration,
                    singular_size=singular_size,
                    singular_uint64value_size=singular_uint64value_size,
                    singular_string_value_ipnet=singular_string_value_ipnet,
                    repeated_double_value=repeated_double_value,
                    repeated_float_value=repeated_float_value,
                    repeated_int64_value=repeated_int64_value,
                    repeated_uint64_value=repeated_uint64_value,
                    repeated_int32_value=repeated_int32_value,
                    repeated_uint32_value=repeated_uint32_value,
                    repeated_bool_value=repeated_bool_value,
                    repeated_string_value=repeated_string_value,
                    repeated_bytes_value=repeated_bytes_value,
                    repeated_timestamp=repeated_timestamp,
                    repeated_any=repeated_any,
                    repeated_struct=repeated_struct,
                    repeated_money=repeated_money,
                    repeated_strings_value=repeated_strings_value,
                    repeated_duration=repeated_duration,
                    repeated_ip=repeated_ip,
                    repeated_string_ip=repeated_string_ip,
                    repeated_string_value_ip=repeated_string_value_ip,
                    repeated_ipv4=repeated_ipv4,
                    repeated_string_ipv4=repeated_string_ipv4,
                    repeated_string_value_ipv4=repeated_string_value_ipv4,
                    repeated_ipv6=repeated_ipv6,
                    repeated_string_ipv6=repeated_string_ipv6,
                    repeated_string_value_ipv6=repeated_string_value_ipv6,
                    repeated_std_duration=repeated_std_duration,
                    repeated_std_long_duration=repeated_std_long_duration,
                    repeated_size=repeated_size,
                    repeated_uint64_size=repeated_uint64_size,
                    repeated_uint64value_size=repeated_uint64value_size,
                    repeated_string_ipnet=repeated_string_ipnet,
                    repeated_string_value_ipnet=repeated_string_value_ipnet,
                    oneof_uint32=oneof_uint32,
                    oneof_nested_message=oneof_nested_message,
                    oneof_string=oneof_string,
                    oneof_bytes=oneof_bytes,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostAllTypesMessage(res.json())

    async def post_all_optional(
        self,
        *,
        optional_int32: Optional[int] = None,
        optional_int64: Optional[int] = None,
        optional_uint32: Optional[int] = None,
        optional_uint64: Optional[int] = None,
        optional_sint32: Optional[int] = None,
        optional_sint64: Optional[int] = None,
        optional_fixed32: Optional[int] = None,
        optional_fixed64: Optional[int] = None,
        optional_sfixed32: Optional[int] = None,
        optional_sfixed64: Optional[int] = None,
        optional_float: Optional[float] = None,
        optional_double: Optional[float] = None,
        optional_bool: Optional[bool] = None,
        optional_string: Optional[str] = None,
        optional_bytes: Optional[str] = None,
        optional_cord: Optional[str] = None,
        optional_nested_message_with_optional: Optional[
            PostAllOptionalMessageNestedMessageWithOptional
        ] = None,
        lazy_nested_message_with_optional: Optional[
            PostAllOptionalMessageNestedMessageWithOptional
        ] = None,
        optional_nested_enum: Optional[PostAllOptionalMessageNestedEnum] = None,
        optional_nested_message: Optional[PostAllOptionalMessageNestedMessage] = None,
        singular_int32: int,
        singular_int64: int,
        nested_message: Optional[PostAllOptionalMessageNestedMessage] = None,
        singular_double_value: Optional[float] = None,
        singular_float_value: Optional[float] = None,
        singular_int64_value: Optional[int] = None,
        singular_uint64_value: Optional[int] = None,
        singular_int32_value: Optional[int] = None,
        singular_uint32_value: Optional[int] = None,
        singular_bool_value: Optional[bool] = None,
        singular_string_value: Optional[str] = None,
        singular_bytes_value: Optional[str] = None,
        singular_timestamp: Optional[datetime] = None,
        singular_any: Optional[Any] = None,
        singular_struct: Optional[Dict[str, Any]] = None,
        singular_money: Optional[Money] = None,
        singular_strings_value: Optional[List[str]] = None,
        singular_duration: Optional[str] = None,
        map_string_string: Optional[Dict[str, str]] = None,
        timeseries: Optional[TimeSeries] = None,
    ) -> PostAllOptionalMessage:
        """
        :param optional_int32:
        :param optional_int64:
        :param optional_uint32:
        :param optional_uint64:
        :param optional_sint32:
        :param optional_sint64:
        :param optional_fixed32:
        :param optional_fixed64:
        :param optional_sfixed32:
        :param optional_sfixed64:
        :param optional_float:
        :param optional_double:
        :param optional_bool:
        :param optional_string:
        :param optional_bytes:
        :param optional_cord:
        :param optional_nested_message_with_optional:
        :param lazy_nested_message_with_optional:
        :param optional_nested_enum:
        :param optional_nested_message:
        :param singular_int32:
        :param singular_int64:
        :param nested_message:
        :param singular_double_value:
        :param singular_float_value:
        :param singular_int64_value:
        :param singular_uint64_value:
        :param singular_int32_value:
        :param singular_uint32_value:
        :param singular_bool_value:
        :param singular_string_value:
        :param singular_bytes_value:
        :param singular_timestamp:
        :param singular_any:
        :param singular_struct:
        :param singular_money:
        :param singular_strings_value:
        :param singular_duration:
        :param map_string_string:
        :param timeseries:
        :return: :class:`PostAllOptionalMessage <PostAllOptionalMessage>`

        Usage:
        ::

            result = await api.post_all_optional(
                singular_int32=1,
                singular_int64=1,
            )
        """

        res = self._request(
            "POST",
            "/test-internal/v1/alloptional",
            body=marshal_PostAllOptionalRequest(
                PostAllOptionalRequest(
                    optional_int32=optional_int32,
                    optional_int64=optional_int64,
                    optional_uint32=optional_uint32,
                    optional_uint64=optional_uint64,
                    optional_sint32=optional_sint32,
                    optional_sint64=optional_sint64,
                    optional_fixed32=optional_fixed32,
                    optional_fixed64=optional_fixed64,
                    optional_sfixed32=optional_sfixed32,
                    optional_sfixed64=optional_sfixed64,
                    optional_float=optional_float,
                    optional_double=optional_double,
                    optional_bool=optional_bool,
                    optional_string=optional_string,
                    optional_bytes=optional_bytes,
                    optional_cord=optional_cord,
                    optional_nested_message_with_optional=optional_nested_message_with_optional,
                    lazy_nested_message_with_optional=lazy_nested_message_with_optional,
                    optional_nested_enum=optional_nested_enum,
                    optional_nested_message=optional_nested_message,
                    singular_int32=singular_int32,
                    singular_int64=singular_int64,
                    nested_message=nested_message,
                    singular_double_value=singular_double_value,
                    singular_float_value=singular_float_value,
                    singular_int64_value=singular_int64_value,
                    singular_uint64_value=singular_uint64_value,
                    singular_int32_value=singular_int32_value,
                    singular_uint32_value=singular_uint32_value,
                    singular_bool_value=singular_bool_value,
                    singular_string_value=singular_string_value,
                    singular_bytes_value=singular_bytes_value,
                    singular_timestamp=singular_timestamp,
                    singular_any=singular_any,
                    singular_struct=singular_struct,
                    singular_money=singular_money,
                    singular_strings_value=singular_strings_value,
                    singular_duration=singular_duration,
                    map_string_string=map_string_string,
                    timeseries=timeseries,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostAllOptionalMessage(res.json())

    async def post_complex_validate(
        self,
        *,
        val: Optional[ComplexValidateMsg] = None,
    ) -> PostComplexValidateMessage:
        """
        :param val:
        :return: :class:`PostComplexValidateMessage <PostComplexValidateMessage>`

        Usage:
        ::

            result = await api.post_complex_validate()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/complex-validate",
            body=marshal_PostComplexValidateRequest(
                PostComplexValidateRequest(
                    val=val,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostComplexValidateMessage(res.json())

    async def list_characters(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCharactersRequestOrderBy] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> ListCharactersResponse:
        """
        List The Lord of the Rings characters.
        List The Lord of the Rings characters.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Order the listing.
        :param name: Filter characters by name, this is a "contains" matching.
        :param tags: Dummy tags to check the comma_separated_list argument.
        :return: :class:`ListCharactersResponse <ListCharactersResponse>`

        Usage:
        ::

            result = await api.list_characters()
        """

        res = self._request(
            "GET",
            "/test-internal/v1/characters",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "tags": ",".join(tags) if tags and len(tags) > 0 else None,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListCharactersResponse(res.json())

    async def list_characters_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListCharactersRequestOrderBy] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> List[str]:
        """
        List The Lord of the Rings characters.
        List The Lord of the Rings characters.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Order the listing.
        :param name: Filter characters by name, this is a "contains" matching.
        :param tags: Dummy tags to check the comma_separated_list argument.
        :return: :class:`List[str] <List[str]>`

        Usage:
        ::

            result = await api.list_characters_all()
        """

        return await fetch_all_pages_async(
            type=ListCharactersResponse,
            key="characters",
            fetcher=self.list_characters,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
                "tags": tags,
            },
        )

    async def post_echo_time_series(
        self,
        *,
        metrics: Optional[TimeSeries] = None,
    ) -> PostEchoTimeSeriesMessage:
        """
        Echo metrics.
        Echo metrics.
        :param metrics:
        :return: :class:`PostEchoTimeSeriesMessage <PostEchoTimeSeriesMessage>`

        Usage:
        ::

            result = await api.post_echo_time_series()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/echo-timeseries",
            body=marshal_PostEchoTimeSeriesRequest(
                PostEchoTimeSeriesRequest(
                    metrics=metrics,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_PostEchoTimeSeriesMessage(res.json())

    async def post_transient(
        self,
    ) -> Transient:
        """

        :return: :class:`Transient <Transient>`

        Usage:
        ::

            result = await api.post_transient()
        """

        res = self._request(
            "POST",
            "/test-internal/v1/transients",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Transient(res.json())

    async def get_transient(
        self,
        *,
        transient_id: str,
    ) -> Transient:
        """
        :param transient_id:
        :return: :class:`Transient <Transient>`

        Usage:
        ::

            result = await api.get_transient(
                transient_id="example",
            )
        """

        param_transient_id = validate_path_param("transient_id", transient_id)

        res = self._request(
            "GET",
            f"/test-internal/v1/transients/{param_transient_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Transient(res.json())

    async def wait_for_transient(
        self,
        *,
        transient_id: str,
        options: Optional[
            WaitForOptions[Transient, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Transient:
        """
        :param transient_id:
        :return: :class:`Transient <Transient>`

        Usage:
        ::

            result = await api.get_transient(
                transient_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in TRANSIENT_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_transient,
            options=options,
            args={
                "transient_id": transient_id,
            },
        )


class TestinternalV1RegionalAPI(API):
    """ """

    async def get_service_info(
        self,
        *,
        region: Optional[Region] = None,
    ) -> ServiceInfo:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ServiceInfo <ServiceInfo>`

        Usage:
        ::

            result = await api.get_service_info()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/test-internal/v1/regions/{param_region}",
        )

        self._throw_on_error(res)
        return unmarshal_ServiceInfo(res.json())

    async def get_region(
        self,
        *,
        region: Optional[Region] = None,
    ) -> _GetRegionResponse:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`_GetRegionResponse <_GetRegionResponse>`

        Usage:
        ::

            result = await api.get_region()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/test-internal/v1/regions/{param_region}/region",
        )

        self._throw_on_error(res)
        return unmarshal__GetRegionResponse(res.json())

    async def get_metadata(
        self,
        *,
        region: Optional[Region] = None,
    ) -> MetadataResponse:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`MetadataResponse <MetadataResponse>`

        Usage:
        ::

            result = await api.get_metadata()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/test-internal/v1/regions/{param_region}/metadata",
        )

        self._throw_on_error(res)
        return unmarshal_MetadataResponse(res.json())

    async def post_echo(
        self,
        *,
        region: Optional[Region] = None,
        str_: Optional[str] = None,
        strs: Optional[List[str]] = None,
    ) -> EchoMessage:
        """
        :param region: Region to target. If none is passed will use default region from the config.
        :param str_:
        :param strs:
        :return: :class:`EchoMessage <EchoMessage>`

        Usage:
        ::

            result = await api.post_echo()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/test-internal/v1/regions/{param_region}/echo",
            body=marshal_RegionalApiPostEchoRequest(
                RegionalApiPostEchoRequest(
                    region=region,
                    str_=str_ or random_name(prefix="name"),
                    strs=strs,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_EchoMessage(res.json())


class TestinternalV1ZoneAPI(API):
    """ """

    async def get_zone(
        self,
        *,
        zone: Optional[Zone] = None,
    ) -> GetZoneResponse:
        """
        Get a zone.
        Get a zone.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`GetZoneResponse <GetZoneResponse>`

        Usage:
        ::

            result = await api.get_zone()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/test-internal/v1/zones/{param_zone}/zone",
        )

        self._throw_on_error(res)
        return unmarshal_GetZoneResponse(res.json())

    async def get_metadata(
        self,
        *,
        zone: Optional[Zone] = None,
    ) -> MetadataResponse:
        """
        Get metadata.
        Get metadata.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :return: :class:`MetadataResponse <MetadataResponse>`

        Usage:
        ::

            result = await api.get_metadata()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/test-internal/v1/zones/{param_zone}/metadata",
        )

        self._throw_on_error(res)
        return unmarshal_MetadataResponse(res.json())

    async def post_echo(
        self,
        *,
        zone: Optional[Zone] = None,
        str_: Optional[str] = None,
        strs: Optional[List[str]] = None,
    ) -> EchoMessage:
        """
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param str_:
        :param strs:
        :return: :class:`EchoMessage <EchoMessage>`

        Usage:
        ::

            result = await api.post_echo()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/test-internal/v1/zones/{param_zone}/echo",
            body=marshal_ZoneApiPostEchoRequest(
                ZoneApiPostEchoRequest(
                    zone=zone,
                    str_=str_ or random_name(prefix="name"),
                    strs=strs,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_EchoMessage(res.json())
