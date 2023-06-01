# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages,
    random_name,
    validate_path_param,
    wait_for_resource,
)
from .types import (
    ImageVisibility,
    ListImagesRequestOrderBy,
    ListNamespacesRequestOrderBy,
    ListTagsRequestOrderBy,
    Image,
    ListImagesResponse,
    ListNamespacesResponse,
    ListTagsResponse,
    Namespace,
    Tag,
    CreateNamespaceRequest,
    UpdateNamespaceRequest,
    UpdateImageRequest,
)
from .content import (
    IMAGE_TRANSIENT_STATUSES,
    NAMESPACE_TRANSIENT_STATUSES,
    TAG_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_CreateNamespaceRequest,
    marshal_UpdateImageRequest,
    marshal_UpdateNamespaceRequest,
    unmarshal_Image,
    unmarshal_Namespace,
    unmarshal_Tag,
    unmarshal_ListImagesResponse,
    unmarshal_ListNamespacesResponse,
    unmarshal_ListTagsResponse,
)


class RegistryV1API(API):
    """
    Container Registry API.

    Container Registry API.
    """

    def list_namespaces(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListNamespacesRequestOrderBy = ListNamespacesRequestOrderBy.CREATED_AT_ASC,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListNamespacesResponse:
        """
        List namespaces.
        List all namespaces in a specified region. By default, the namespaces listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `instance_id` and `project_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering namespace listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param organization_id: Filter by Organization ID.
        :param project_id: Filter by Project ID.
        :param name: Filter by the namespace name (exact match).
        :return: :class:`ListNamespacesResponse <ListNamespacesResponse>`

        Usage:
        ::

            result = api.list_namespaces()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/namespaces",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNamespacesResponse(res.json())

    def list_namespaces_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNamespacesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[Namespace]:
        """
        List namespaces.
        List all namespaces in a specified region. By default, the namespaces listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `instance_id` and `project_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering namespace listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param organization_id: Filter by Organization ID.
        :param project_id: Filter by Project ID.
        :param name: Filter by the namespace name (exact match).
        :return: :class:`List[ListNamespacesResponse] <List[ListNamespacesResponse]>`

        Usage:
        ::

            result = api.list_namespaces_all()
        """

        return fetch_all_pages(
            type=ListNamespacesResponse,
            key="namespaces",
            fetcher=self.list_namespaces,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "organization_id": organization_id,
                "project_id": project_id,
                "name": name,
            },
        )

    def get_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
    ) -> Namespace:
        """
        Get a namespace.
        Retrieve information about a given namespace, specified by its `namespace_id` and region. Full details about the namespace, such as `description`, `project_id`, `status`, `endpoint`, `is_public`, `size`, and `image_count` are returned in the response.
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: UUID of the namespace.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.get_namespace(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def wait_for_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Namespace, bool]] = None,
    ) -> Namespace:
        """
        Waits for :class:`Namespace <Namespace>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: UUID of the namespace.
        :param options: The options for the waiter
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.wait_for_namespace(namespace_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in NAMESPACE_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_namespace,
            options=options,
            args={
                "namespace_id": namespace_id,
                "region": region,
            },
        )

    def create_namespace(
        self,
        *,
        description: str,
        is_public: bool,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Namespace:
        """
        Create a namespace.
        Create a new Container Registry namespace. You must specify the namespace name and region in which you want it to be created. Optionally, you can specify the `project_id` and `is_public` in the request payload.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the namespace.
        :param description: Description of the namespace.
        :param organization_id: Namespace owner (deprecated).

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID on which the namespace will be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param is_public: Defines whether or not namespace is public.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.create_namespace(
                description="example",
                is_public=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/registry/v1/regions/{param_region}/namespaces",
            body=marshal_CreateNamespaceRequest(
                CreateNamespaceRequest(
                    description=description,
                    is_public=is_public,
                    region=region,
                    name=name or random_name(prefix="ns"),
                    organization_id=organization_id,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def update_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        is_public: Optional[bool] = None,
    ) -> Namespace:
        """
        Update a namespace.
        Update the parameters of a given namespace, specified by its `namespace_id` and `region`. You can update the `description` and `is_public` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: ID of the namespace to update.
        :param description: Namespace description.
        :param is_public: Defines whether or not the namespace is public.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.update_namespace(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "PATCH",
            f"/registry/v1/regions/{param_region}/namespaces/{param_namespace_id}",
            body=marshal_UpdateNamespaceRequest(
                UpdateNamespaceRequest(
                    namespace_id=namespace_id,
                    region=region,
                    description=description,
                    is_public=is_public,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def delete_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[Region] = None,
    ) -> Namespace:
        """
        Delete a namespace.
        Delete a given namespace. You must specify, in the endpoint, the `region` and `namespace_id` parameters of the namespace you want to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :param namespace_id: UUID of the namespace.
        :return: :class:`Namespace <Namespace>`

        Usage:
        ::

            result = api.delete_namespace(namespace_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_namespace_id = validate_path_param("namespace_id", namespace_id)

        res = self._request(
            "DELETE",
            f"/registry/v1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())

    def list_images(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListImagesRequestOrderBy = ListImagesRequestOrderBy.CREATED_AT_ASC,
        namespace_id: Optional[str] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListImagesResponse:
        """
        List images.
        List all images in a specified region. By default, the images listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `namespace_id` and `project_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering image listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param namespace_id: Filter by the namespace ID.
        :param name: Filter by the image name (exact match).
        :param organization_id: Filter by Organization ID.
        :param project_id: Filter by Project ID.
        :return: :class:`ListImagesResponse <ListImagesResponse>`

        Usage:
        ::

            result = api.list_images()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/images",
            params={
                "name": name,
                "namespace_id": namespace_id,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListImagesResponse(res.json())

    def list_images_all(
        self,
        *,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListImagesRequestOrderBy] = None,
        namespace_id: Optional[str] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Image]:
        """
        List images.
        List all images in a specified region. By default, the images listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `namespace_id` and `project_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering image listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param namespace_id: Filter by the namespace ID.
        :param name: Filter by the image name (exact match).
        :param organization_id: Filter by Organization ID.
        :param project_id: Filter by Project ID.
        :return: :class:`List[ListImagesResponse] <List[ListImagesResponse]>`

        Usage:
        ::

            result = api.list_images_all()
        """

        return fetch_all_pages(
            type=ListImagesResponse,
            key="images",
            fetcher=self.list_images,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "namespace_id": namespace_id,
                "name": name,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    def get_image(
        self,
        *,
        image_id: str,
        region: Optional[Region] = None,
    ) -> Image:
        """
        Get an image.
        Retrieve information about a given container image, specified by its `image_id` and region. Full details about the image, such as `name`, `namespace_id`, `status`, `visibility`, and `size` are returned in the response.
        :param region: Region to target. If none is passed will use default region from the config.
        :param image_id: UUID of the image.
        :return: :class:`Image <Image>`

        Usage:
        ::

            result = api.get_image(image_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/images/{param_image_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Image(res.json())

    def wait_for_image(
        self,
        *,
        image_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Image, bool]] = None,
    ) -> Image:
        """
        Waits for :class:`Image <Image>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param image_id: UUID of the image.
        :param options: The options for the waiter
        :return: :class:`Image <Image>`

        Usage:
        ::

            result = api.wait_for_image(image_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in IMAGE_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_image,
            options=options,
            args={
                "image_id": image_id,
                "region": region,
            },
        )

    def update_image(
        self,
        *,
        image_id: str,
        visibility: ImageVisibility,
        region: Optional[Region] = None,
    ) -> Image:
        """
        Update an image.
        Update the parameters of a given image, specified by its `image_id` and `region`. You can update the `visibility` parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param image_id: ID of the image to update.
        :param visibility: Set to `public` to allow the image to be pulled without authentication. Else, set to  `private`. Set to `inherit` to keep the same visibility configuration as the namespace.
        :return: :class:`Image <Image>`

        Usage:
        ::

            result = api.update_image(
                image_id="example",
                visibility=visibility_unknown,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "PATCH",
            f"/registry/v1/regions/{param_region}/images/{param_image_id}",
            body=marshal_UpdateImageRequest(
                UpdateImageRequest(
                    image_id=image_id,
                    visibility=visibility,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Image(res.json())

    def delete_image(
        self,
        *,
        image_id: str,
        region: Optional[Region] = None,
    ) -> Image:
        """
        Delete an image.
        Delete a given image. You must specify, in the endpoint, the `region` and `image_id` parameters of the image you want to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :param image_id: UUID of the image.
        :return: :class:`Image <Image>`

        Usage:
        ::

            result = api.delete_image(image_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "DELETE",
            f"/registry/v1/regions/{param_region}/images/{param_image_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Image(res.json())

    def list_tags(
        self,
        *,
        image_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListTagsRequestOrderBy = ListTagsRequestOrderBy.CREATED_AT_ASC,
        name: Optional[str] = None,
    ) -> ListTagsResponse:
        """
        List tags.
        List all tags for a given image, specified by region. By default, the tags listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `name`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param image_id: UUID of the image.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering tag listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param name: Filter by the tag name (exact match).
        :return: :class:`ListTagsResponse <ListTagsResponse>`

        Usage:
        ::

            result = api.list_tags(image_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_image_id = validate_path_param("image_id", image_id)

        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/images/{param_image_id}/tags",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTagsResponse(res.json())

    def list_tags_all(
        self,
        *,
        image_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTagsRequestOrderBy] = None,
        name: Optional[str] = None,
    ) -> List[Tag]:
        """
        List tags.
        List all tags for a given image, specified by region. By default, the tags listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `name`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param image_id: UUID of the image.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering tag listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param name: Filter by the tag name (exact match).
        :return: :class:`List[ListTagsResponse] <List[ListTagsResponse]>`

        Usage:
        ::

            result = api.list_tags_all(image_id="example")
        """

        return fetch_all_pages(
            type=ListTagsResponse,
            key="tags",
            fetcher=self.list_tags,
            args={
                "image_id": image_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
            },
        )

    def get_tag(
        self,
        *,
        tag_id: str,
        region: Optional[Region] = None,
    ) -> Tag:
        """
        Get a tag.
        Retrieve information about a given image tag, specified by its `tag_id` and region. Full details about the tag, such as `name`, `image_id`, `status`, and `digest` are returned in the response.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tag_id: UUID of the tag.
        :return: :class:`Tag <Tag>`

        Usage:
        ::

            result = api.get_tag(tag_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_tag_id = validate_path_param("tag_id", tag_id)

        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/tags/{param_tag_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Tag(res.json())

    def wait_for_tag(
        self,
        *,
        tag_id: str,
        region: Optional[Region] = None,
        options: Optional[WaitForOptions[Tag, bool]] = None,
    ) -> Tag:
        """
        Waits for :class:`Tag <Tag>` to be in a final state.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tag_id: UUID of the tag.
        :param options: The options for the waiter
        :return: :class:`Tag <Tag>`

        Usage:
        ::

            result = api.wait_for_tag(tag_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in TAG_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_tag,
            options=options,
            args={
                "tag_id": tag_id,
                "region": region,
            },
        )

    def delete_tag(
        self,
        *,
        tag_id: str,
        region: Optional[Region] = None,
        force: Optional[bool] = None,
    ) -> Tag:
        """
        Delete a tag.
        Delete a given image tag. You must specify, in the endpoint, the `region` and `tag_id` parameters of the tag you want to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :param tag_id: UUID of the tag.
        :param force: If two tags share the same digest the deletion will fail unless this parameter is set to true (deprecated).
        :return: :class:`Tag <Tag>`

        Usage:
        ::

            result = api.delete_tag(tag_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_tag_id = validate_path_param("tag_id", tag_id)

        res = self._request(
            "DELETE",
            f"/registry/v1/regions/{param_region}/tags/{param_tag_id}",
            params={
                "force": force,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Tag(res.json())
