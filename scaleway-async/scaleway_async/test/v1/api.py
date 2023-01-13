# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages_async,
    validate_path_param,
    wait_for_resource_async,
)
from .types import (
    EyeColors,
    ListHumansRequestOrderBy,
    Human,
    ListHumansResponse,
    RegisterResponse,
    RegisterRequest,
    CreateHumanRequest,
    UpdateHumanRequest,
)
from .content import (
    HUMAN_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_CreateHumanRequest,
    marshal_RegisterRequest,
    marshal_UpdateHumanRequest,
    unmarshal_Human,
    unmarshal_ListHumansResponse,
    unmarshal_RegisterResponse,
)


class TestV1API(API):
    """
    Fake API.

    Test is a fake service that aim to manage fake humans. It is used for internal and public end-to-end tests.

    This service don't use the Scaleway authentication service but a fake one.
    It allows to use this test service publicly without requiring a Scaleway account.

    First, you need to register a user with `scw test human register` to get an access-key.
    Then, you can use other test commands by setting the SCW_SECRET_KEY env variable.
    """

    async def register(
        self,
        *,
        username: str,
    ) -> RegisterResponse:
        """
        Register a human and return a access-key and a secret-key that must be used in all other commands.

        Hint: you can use other test commands by setting the SCW_SECRET_KEY env variable.

        :param username:
        :return: :class:`RegisterResponse <RegisterResponse>`

        Usage:
        ::

            result = await api.register(username="example")
        """

        res = self._request(
            "POST",
            f"/test/v1/register",
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
        order_by: ListHumansRequestOrderBy = ListHumansRequestOrderBy.CREATED_AT_ASC,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListHumansResponse:
        """
        List all your humans
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
            f"/test/v1/humans",
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
        List all your humans
        :param page:
        :param page_size:
        :param order_by:
        :param organization_id:
        :param project_id:
        :return: :class:`List[ListHumansResponse] <List[ListHumansResponse]>`

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
        Get the human details associated with the given id.
        :param human_id: UUID of the human you want to get
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = await api.get_human(human_id="example")
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
        Waits for :class:`Human <Human>` to be in a final state.
        :param human_id: UUID of the human you want to get
        :param options: The options for the waiter
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = api.wait_for_human(human_id="example")
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
        eyes_color: EyeColors,
        name: str,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Human:
        """
        Create a new human
        :param height:
        :param shoe_size:
        :param altitude_in_meter:
        :param altitude_in_millimeter:
        :param fingers_count:
        :param hair_count:
        :param is_happy:
        :param eyes_color:
        :param organization_id: One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param name:
        :param project_id: One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = await api.create_human(
                height=1.0,
                shoe_size=1.0,
                altitude_in_meter=1,
                altitude_in_millimeter=1,
                fingers_count=1,
                hair_count=1,
                is_happy=True,
                eyes_color=unknown,
                name="example",
            )
        """

        res = self._request(
            "POST",
            f"/test/v1/humans",
            body=marshal_CreateHumanRequest(
                CreateHumanRequest(
                    height=height,
                    shoe_size=shoe_size,
                    altitude_in_meter=altitude_in_meter,
                    altitude_in_millimeter=altitude_in_millimeter,
                    fingers_count=fingers_count,
                    hair_count=hair_count,
                    is_happy=is_happy,
                    eyes_color=eyes_color,
                    name=name,
                    organization_id=organization_id,
                    project_id=project_id,
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
        eyes_color: EyeColors,
        height: Optional[float] = None,
        shoe_size: Optional[float] = None,
        altitude_in_meter: Optional[int] = None,
        altitude_in_millimeter: Optional[int] = None,
        fingers_count: Optional[int] = None,
        hair_count: Optional[int] = None,
        is_happy: Optional[bool] = None,
        name: Optional[str] = None,
    ) -> Human:
        """
        Update the human associated with the given id.
        :param human_id: UUID of the human you want to update
        :param height:
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
                eyes_color=unknown,
            )
        """

        param_human_id = validate_path_param("human_id", human_id)

        res = self._request(
            "PATCH",
            f"/test/v1/humans/{param_human_id}",
            body=marshal_UpdateHumanRequest(
                UpdateHumanRequest(
                    human_id=human_id,
                    eyes_color=eyes_color,
                    height=height,
                    shoe_size=shoe_size,
                    altitude_in_meter=altitude_in_meter,
                    altitude_in_millimeter=altitude_in_millimeter,
                    fingers_count=fingers_count,
                    hair_count=hair_count,
                    is_happy=is_happy,
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
        Delete the human associated with the given id.
        :param human_id: UUID of the human you want to delete
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = await api.delete_human(human_id="example")
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
        Start a one hour running for the given human.
        :param human_id: UUID of the human you want to make run
        :return: :class:`Human <Human>`

        Usage:
        ::

            result = await api.run_human(human_id="example")
        """

        param_human_id = validate_path_param("human_id", human_id)

        res = self._request(
            "POST",
            f"/test/v1/humans/{param_human_id}/run",
        )

        self._throw_on_error(res)
        return unmarshal_Human(res.json())

    async def smoke_human(
        self,
        *,
        human_id: Optional[str] = None,
    ) -> Human:
        """
        Make a human smoke.
        :param human_id: UUID of the human you want to make smoking
        :return: :class:`Human <Human>`
        :deprecated

        Usage:
        ::

            result = await api.smoke_human()
        """

        param_human_id = validate_path_param("human_id", human_id)

        res = self._request(
            "POST",
            f"/test/v1/humans/{param_human_id}/smoke",
        )

        self._throw_on_error(res)
        return unmarshal_Human(res.json())
