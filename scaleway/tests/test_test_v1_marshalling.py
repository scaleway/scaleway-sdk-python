import random
import unittest
import uuid
from typing import Any, Dict

import utils

from scaleway.test.v1.marshalling import (
    marshal_CreateHumanRequest,
    unmarshal_Human,
    unmarshal_ListHumansResponse,
)
from scaleway.test.v1.types import (
    CreateHumanRequest,
    EyeColors,
    Human,
    HumanStatus,
    ListHumansResponse,
)

system_random = random.SystemRandom()

def _mock_human_raw() -> Dict[str, Any]:
    altitude_in_meter = system_random.randint(0, 100)
    created_at = utils.random_date_string(
        "1990-01-01T00:00:00Z", "2023-01-01T00:00:00Z"
    )

    return {
        "id": str(uuid.uuid4()),
        "organization_id": str(uuid.uuid4()),
        "created_at": created_at,
        "updated_at": utils.random_date_string(created_at, "2023-01-01T00:00:00Z"),
        "height": system_random.uniform(100, 200),
        "shoe_size": system_random.uniform(10, 50),
        "altitude_in_meter": altitude_in_meter,
        "altitude_in_millimeter": altitude_in_meter * 1000,
        "fingers_count": system_random.randint(0, 100),
        "hair_count": system_random.randint(0, 10000),
        "is_happy": system_random.choice([True, False]),
        "eyes_color": str(system_random.choice(list(EyeColors))),
        "status": str(system_random.choice(list(HumanStatus))),
        "name": utils.random_name(),
        "project_id": str(uuid.uuid4()),
    }


def _mock_human() -> Human:
    altitude_in_meter = system_random.randint(0, 100)
    created_at = utils.random_date("1990-01-01T00:00:00Z", "2023-01-01T00:00:00Z")

    return Human(
        id=str(uuid.uuid4()),
        organization_id=str(uuid.uuid4()),
        created_at=created_at,
        updated_at=utils.random_date(created_at, "2023-01-01T00:00:00Z"),
        height=system_random.uniform(100, 200),
        shoe_size=system_random.uniform(10, 50),
        altitude_in_meter=altitude_in_meter,
        altitude_in_millimeter=altitude_in_meter * 1000,
        fingers_count=system_random.randint(0, 100),
        hair_count=system_random.randint(0, 10000),
        is_happy=system_random.choice([True, False]),
        eyes_color=EyeColors(system_random.choice(list(EyeColors))),
        status=HumanStatus(system_random.choice(list(HumanStatus))),
        name=utils.random_name(),
        project_id=str(uuid.uuid4()),
    )
@unittest.skip("API test is not deploy")
class TestTestV1UnmarshallingHuman(unittest.TestCase):
    def _assert_raw_and_unmarshalled_human(
        self,
        raw: Dict[str, Any],
        unmarshalled: Human,
    ) -> None:
        self.assertTrue(isinstance(unmarshalled, Human))
        self.assertEqual(unmarshalled.altitude_in_meter, raw["altitude_in_meter"])
        self.assertEqual(
            unmarshalled.altitude_in_millimeter, raw["altitude_in_millimeter"]
        )
        self.assertEqual(
            utils.datetime_to_string(unmarshalled.created_at)
            if unmarshalled.created_at is not None
            else None,
            raw["created_at"],
        )
        self.assertEqual(unmarshalled.eyes_color, raw["eyes_color"])
        self.assertEqual(unmarshalled.fingers_count, raw["fingers_count"])
        self.assertEqual(unmarshalled.hair_count, raw["hair_count"])
        self.assertEqual(unmarshalled.height, raw["height"])
        self.assertEqual(unmarshalled.id, raw["id"])
        self.assertEqual(unmarshalled.is_happy, raw["is_happy"])
        self.assertEqual(unmarshalled.name, raw["name"])
        self.assertEqual(unmarshalled.organization_id, raw["organization_id"])
        self.assertEqual(unmarshalled.project_id, raw["project_id"])
        self.assertEqual(unmarshalled.shoe_size, raw["shoe_size"])
        self.assertEqual(unmarshalled.status, raw["status"])
        self.assertEqual(
            utils.datetime_to_string(unmarshalled.updated_at)
            if unmarshalled.updated_at is not None
            else None,
            raw["updated_at"],
        )

    def test_unmarshal_Human(self) -> None:
        data = _mock_human_raw()
        human = unmarshal_Human(data)
        self._assert_raw_and_unmarshalled_human(data, human)

    def test_unmarshal_ListHumansResponse(self) -> None:
        humans = [_mock_human_raw() for _ in range(10)]
        data = {
            "humans": humans,
            "total_count": 1,
        }

        list_humans_response = unmarshal_ListHumansResponse(data)

        self.assertTrue(isinstance(list_humans_response, ListHumansResponse))
        self.assertEqual(len(list_humans_response.humans), len(humans))

        for i in range(len(list_humans_response.humans)):
            self._assert_raw_and_unmarshalled_human(
                humans[i], list_humans_response.humans[i]
            )

def _mock_create_human_request() -> CreateHumanRequest:
    human = _mock_human()

    return CreateHumanRequest(
        height=human.height,
        shoe_size=human.shoe_size,
        altitude_in_meter=human.altitude_in_meter,
        altitude_in_millimeter=human.altitude_in_millimeter,
        fingers_count=human.fingers_count,
        hair_count=human.hair_count,
        is_happy=human.is_happy,
        eyes_color=human.eyes_color,
        name=human.name,
        project_id=human.project_id,
        organization_id=human.organization_id,
    )

@unittest.skip("API test is not deploy")
class TestTestV1MarshallingCreateHumanRequest(unittest.TestCase):
    def _assert_create_human_request_and_raw(
        self,
        request: CreateHumanRequest,
        raw: Dict[str, Any],
    ) -> None:
        self.assertTrue(isinstance(request, CreateHumanRequest))
        self.assertEqual(request.altitude_in_meter, raw["altitude_in_meter"])
        self.assertEqual(request.altitude_in_millimeter, raw["altitude_in_millimeter"])
        self.assertEqual(request.eyes_color, raw["eyes_color"])
        self.assertEqual(request.fingers_count, raw["fingers_count"])
        self.assertEqual(request.hair_count, raw["hair_count"])
        self.assertEqual(request.height, raw["height"])
        self.assertEqual(request.is_happy, raw["is_happy"])
        self.assertEqual(request.name, raw["name"])
        self.assertEqual(request.shoe_size, raw["shoe_size"])

    def test_marshal_CreateHumanRequest(self) -> None:
        request = _mock_create_human_request()
        raw = marshal_CreateHumanRequest(request, utils.random_profile_defaults())
        self._assert_create_human_request_and_raw(request, raw)
