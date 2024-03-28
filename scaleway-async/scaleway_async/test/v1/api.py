# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    EyeColors,
    ListHumansRequestOrderBy,
    CreateHumanRequest,
    Human,
    ListHumansResponse,
    RegisterRequest,
    RegisterResponse,
    UpdateHumanRequest,
)
from .content import (
    HUMAN_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Human,
    unmarshal_ListHumansResponse,
    unmarshal_RegisterResponse,
    marshal_CreateHumanRequest,
    marshal_RegisterRequest,
    marshal_UpdateHumanRequest,
)


class TestV1API(API):
    """
    No Auth Service for end-to-end testing.
    """

    async def register(
        self,
        *,
        username: str,
    ) -> RegisterResponse:
        """
        Register a user.
        Register a human and return a access-key and a secret-key that must be used in all other commands.

        Hint: you can use other test commands by setting the SCW_SECRET_KEY env variable.
        :param username:
        :return: :class:`RegisterResponse <RegisterResponse>`

        Usage:
        ::

            result = await api.register(
                username="example",
            )
        """

        res = self._request(
            "POST",
            "/test/v1/register",
            body=marshal_RegisterRequest(
                RegisterRequest(
                    username=username,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RegisterResponse(res.json())

    async def list_humans(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListHumansRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListHumansResponse:
        """
        List all your humans.
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :return: :class:`ListHumansResponse <ListHumansResponse>`

        Usage:
        ::

            result = await api.list_humans()
        """

        res = self._request(
            "GET",
            "/test/v1/humans",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListHumansResponse(res.json())

    async def list_humans_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListHumansRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Human]:
        """
        List all your humans.
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :return: :class:`List[Human] <List[Human]>`

        Usage:
        ::

            result = await api.list_humans_all()
        """

        return await fetch_all_pages_async(
            type=ListHumansResponse,
            key="humans",
            fetcher=self.list_humans,
            args={
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def get_human(
        self,
        *,
        human_id: str,
    ) -> Human:
        """
        Get human details.
        Get the human details associated with the given id.
        :param human_id: UUID of the human you want to get.
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = await api.get_human(
                human_id="example",
            )
        """

        param_human_id = validate_path_param("human_id", human_id)

        res = self._request(
            "GET",
            f"/test/v1/humans/{param_human_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Human(res.json())

    async def wait_for_human(
        self,
        *,
        human_id: str,
        options: Optional[WaitForOptions[Human, Union[bool, Awaitable[bool]]]] = None,
    ) -> Human:
        """
        Get human details.
        Get the human details associated with the given id.
        :param human_id: UUID of the human you want to get.
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = await api.get_human(
                human_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in HUMAN_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_human,
            options=options,
            args={
                "human_id": human_id,
            },
        )

    async def create_human(
        self,
        *,
        height: float,
        shoe_size: float,
        altitude_in_meter: int,
        altitude_in_millimeter: int,
        fingers_count: int,
        hair_count: int,
        is_happy: bool,
        name: str,
        eyes_color: Optional[EyeColors] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Human:
        """
        Create a new human.
        :param height:
        :param shoe_size:
        :param altitude_in_meter:
        :param altitude_in_millimeter:
        :param fingers_count:
        :param hair_count:
        :param is_happy:
        :param name:
        :param eyes_color:
        :param organization_id:
        One-Of ('project_identifier'): at most one of 'project_id', 'organization_id' could be set.
        :param project_id:
        One-Of ('project_identifier'): at most one of 'project_id', 'organization_id' could be set.
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = await api.create_human(
                height=3.14,
                shoe_size=3.14,
                altitude_in_meter=1,
                altitude_in_millimeter=1,
                fingers_count=1,
                hair_count=1,
                is_happy=False,
                name="example",
            )
        """

        res = self._request(
            "POST",
            "/test/v1/humans",
            body=marshal_CreateHumanRequest(
                CreateHumanRequest(
                    height=height,
                    shoe_size=shoe_size,
                    altitude_in_meter=altitude_in_meter,
                    altitude_in_millimeter=altitude_in_millimeter,
                    fingers_count=fingers_count,
                    hair_count=hair_count,
                    is_happy=is_happy,
                    name=name,
                    eyes_color=eyes_color,
                    project_id=project_id,
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Human(res.json())

    async def update_human(
        self,
        *,
        human_id: str,
        height: Optional[float] = None,
        shoe_size: Optional[float] = None,
        altitude_in_meter: Optional[int] = None,
        altitude_in_millimeter: Optional[int] = None,
        fingers_count: Optional[int] = None,
        hair_count: Optional[int] = None,
        is_happy: Optional[bool] = None,
        eyes_color: Optional[EyeColors] = None,
        name: Optional[str] = None,
    ) -> Human:
        """
        Update an existing human.
        Update the human associated with the given id.
        :param human_id: UUID of the human you want to update.
        :param height: Height of the human in meters.
        :param shoe_size:
        :param altitude_in_meter:
        :param altitude_in_millimeter:
        :param fingers_count:
        :param hair_count:
        :param is_happy:
        :param eyes_color:
        :param name:
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = await api.update_human(
                human_id="example",
            )
        """

        param_human_id = validate_path_param("human_id", human_id)

        res = self._request(
            "PATCH",
            f"/test/v1/humans/{param_human_id}",
            body=marshal_UpdateHumanRequest(
                UpdateHumanRequest(
                    human_id=human_id,
                    height=height,
                    shoe_size=shoe_size,
                    altitude_in_meter=altitude_in_meter,
                    altitude_in_millimeter=altitude_in_millimeter,
                    fingers_count=fingers_count,
                    hair_count=hair_count,
                    is_happy=is_happy,
                    eyes_color=eyes_color,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Human(res.json())

    async def delete_human(
        self,
        *,
        human_id: str,
    ) -> Human:
        """
        Delete an existing human.
        Delete the human associated with the given id.
        :param human_id: UUID of the human you want to delete.
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = await api.delete_human(
                human_id="example",
            )
        """

        param_human_id = validate_path_param("human_id", human_id)

        res = self._request(
            "DELETE",
            f"/test/v1/humans/{param_human_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Human(res.json())

    async def run_human(
        self,
        *,
        human_id: str,
    ) -> Human:
        """
        Start a 1h running for the given human.
        Start a one hour running for the given human.
        :param human_id: UUID of the human you want to make run.
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = await api.run_human(
                human_id="example",
            )
        """

        param_human_id = validate_path_param("human_id", human_id)

        res = self._request(
            "POST",
            f"/test/v1/humans/{param_human_id}/run",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Human(res.json())

    async def smoke_human(
        self,
        *,
        human_id: str,
    ) -> Human:
        """
        Make a human smoke.
        :param human_id: UUID of the human you want to make smoking.
        :return: :class:`Human <Human>`
        :deprecated

        Usage:
        ::

            result = await api.smoke_human(
                human_id="example",
            )
        """

        param_human_id = validate_path_param("human_id", human_id)

        res = self._request(
            "POST",
            f"/test/v1/humans/{param_human_id}/smoke",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Human(res.json())
