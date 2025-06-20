import unittest
from contextlib import ExitStack
from typing import Optional

import utils

from scaleway import Client, WaitForOptions
from scaleway.test.v1 import EyeColors, Human, HumanStatus, TestV1API

@unittest.skip("API test is not deploy")
class TestTestV1(unittest.TestCase):
    def setUp(self) -> None:
        client = Client.from_config_file_and_env()
        self.api = TestV1API(client, bypass_validation=True)

        res = self.api.register(username="scaleway-sdk-python")
        client.access_key = res.access_key
        client.secret_key = res.secret_key
        client.default_project_id = "00000000-0000-0000-0000-000000000000"

    def test_create_human(self) -> None:
        name = utils.random_name()

        with ExitStack() as stack:
            human = self.api.create_human(
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
            stack.callback(self.api.delete_human, human_id=human.id)

            self.assertEqual(human.name, name)

    def test_list_humans(self) -> None:
        humans = self.api.list_humans()
        self.assertTrue(isinstance(humans.humans, list))

    def test_list_humans_all(self) -> None:
        humans = self.api.list_humans_all()
        self.assertTrue(isinstance(humans, list))

    def test_get_human(self) -> None:
        name = utils.random_name()

        with ExitStack() as stack:
            human = self.api.create_human(
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
            stack.callback(self.api.delete_human, human_id=human.id)

            human2 = self.api.get_human(human_id=human.id)
            self.assertEqual(human.id, human2.id)

    def test_update_human(self) -> None:
        name = utils.random_name()

        with ExitStack() as stack:
            human = self.api.create_human(
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
            stack.callback(self.api.delete_human, human_id=human.id)

            human2 = self.api.update_human(
                human_id=human.id,
                height=2.0,
                eyes_color=EyeColors.BLUE,
            )

            self.assertEqual(human.id, human2.id)
            self.assertEqual(human2.height, 2.0)
            self.assertEqual(human2.eyes_color, EyeColors.BLUE)

    def test_delete_human(self) -> None:
        name = utils.random_name()

        human: Optional[Human] = None

        with ExitStack() as stack:
            human = self.api.create_human(
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
            stack.callback(self.api.delete_human, human_id=human.id)

        if human is None:
            raise Exception("human is None")

        try:
            self.api.wait_for_human(human_id=human.id)
        except Exception as e:
            self.assertNotIsInstance(e, TimeoutError)
            pass

    def test_run_human(self) -> None:
        name = utils.random_name()

        with ExitStack() as stack:
            human = self.api.create_human(
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
            stack.callback(self.api.delete_human, human_id=human.id)

            self.api.run_human(human_id=human.id)
            human = self.api.wait_for_human(
                human_id=human.id,
                options=WaitForOptions(
                    stop=lambda human: human.status == HumanStatus.RUNNING
                ),
            )

            self.assertEqual(human.status, HumanStatus.RUNNING)
