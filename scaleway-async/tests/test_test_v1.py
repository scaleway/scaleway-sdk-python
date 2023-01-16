import unittest
from contextlib import AsyncExitStack
from typing import Optional

import utils

from scaleway_async import Client, WaitForOptions
from scaleway_async.test.v1 import EyeColors, Human, HumanStatus, TestV1API


class TestTestV1(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        client = Client.from_config_file_and_env()
        self.api = TestV1API(client, bypass_validation=True)

        res = await self.api.register(username="scaleway-sdk-python")
        client.access_key = res.access_key
        client.secret_key = res.secret_key

    async def test_create_human(self) -> None:
        name = utils.random_name()

        async with AsyncExitStack() as stack:
            human = await self.api.create_human(
                height=1.0,
                shoe_size=1.0,
                altitude_in_meter=1,
                altitude_in_millimeter=1,
                fingers_count=1,
                hair_count=1,
                is_happy=True,
                eyes_color=EyeColors.BROWN,
                name=name,
            )
            stack.push_async_callback(self.api.delete_human, human_id=human.id)

            self.assertEqual(human.name, name)

    async def test_list_humans(self) -> None:
        humans = await self.api.list_humans()
        self.assertTrue(type(humans.humans) is list)

    async def test_list_humans_all(self) -> None:
        humans = await self.api.list_humans_all()
        self.assertTrue(type(humans) is list)

    async def test_get_human(self) -> None:
        name = utils.random_name()

        async with AsyncExitStack() as stack:
            human = await self.api.create_human(
                height=1.0,
                shoe_size=1.0,
                altitude_in_meter=1,
                altitude_in_millimeter=1,
                fingers_count=1,
                hair_count=1,
                is_happy=True,
                eyes_color=EyeColors.BROWN,
                name=name,
            )
            stack.push_async_callback(self.api.delete_human, human_id=human.id)

            human2 = await self.api.get_human(human_id=human.id)
            self.assertEqual(human.id, human2.id)

    async def test_update_human(self) -> None:
        name = utils.random_name()

        async with AsyncExitStack() as stack:
            human = await self.api.create_human(
                height=1.0,
                shoe_size=1.0,
                altitude_in_meter=1,
                altitude_in_millimeter=1,
                fingers_count=1,
                hair_count=1,
                is_happy=True,
                eyes_color=EyeColors.BROWN,
                name=name,
            )
            stack.push_async_callback(self.api.delete_human, human_id=human.id)

            human2 = await self.api.update_human(
                human_id=human.id,
                height=2.0,
                eyes_color=EyeColors.BLUE,
            )

            self.assertEqual(human.id, human2.id)
            self.assertEqual(human2.height, 2.0)
            self.assertEqual(human2.eyes_color, EyeColors.BLUE)

    async def test_delete_human(self) -> None:
        name = utils.random_name()

        human: Optional[Human] = None

        async with AsyncExitStack() as stack:
            human = await self.api.create_human(
                height=1.0,
                shoe_size=1.0,
                altitude_in_meter=1,
                altitude_in_millimeter=1,
                fingers_count=1,
                hair_count=1,
                is_happy=True,
                eyes_color=EyeColors.BROWN,
                name=name,
            )
            stack.push_async_callback(self.api.delete_human, human_id=human.id)

        if human is None:
            raise Exception("human is None")

        try:
            await self.api.wait_for_human(human_id=human.id)
        except Exception as e:
            self.assertNotIsInstance(e, TimeoutError)
            pass

    async def test_run_human(self):
        name = utils.random_name()

        async with AsyncExitStack() as stack:
            human = await self.api.create_human(
                height=1.0,
                shoe_size=1.0,
                altitude_in_meter=1,
                altitude_in_millimeter=1,
                fingers_count=1,
                hair_count=1,
                is_happy=True,
                eyes_color=EyeColors.BROWN,
                name=name,
            )
            stack.push_async_callback(self.api.delete_human, human_id=human.id)

            await self.api.run_human(human_id=human.id)
            human = await self.api.wait_for_human(
                human_id=human.id,
                options=WaitForOptions(
                    stop=lambda human: human.status == HumanStatus.RUNNING
                ),
            )

            self.assertEqual(human.status, HumanStatus.RUNNING)
