import unittest
import uuid

from requests.models import Response

from scaleway_core.api import API, ScalewayException, ValidationError
from scaleway_core.client import Client


def _response(status_code: int, body: bytes) -> Response:
    response = Response()
    response.status_code = status_code
    response._content = body
    return response


def _api() -> API:
    client = Client(
        access_key="SCW" + "A" * 17,
        secret_key=str(uuid.uuid4()),
    )
    return API(client)


class TestThrowOnError(unittest.TestCase):
    def test_non_json_error_raises_scaleway_exception_with_raw_body(self):
        response = _response(502, b"<html>Bad Gateway</html>")

        with self.assertRaises(ScalewayException) as context:
            _api()._throw_on_error(response)

        self.assertEqual(context.exception.status_code, 502)
        self.assertIn("<html>Bad Gateway</html>", str(context.exception))

    def test_json_error_raises_scaleway_exception(self):
        response = _response(500, b'{"message": "boom"}')

        with self.assertRaises(ScalewayException):
            _api()._throw_on_error(response)

    def test_validation_error_raises_validation_error(self):
        response = _response(
            400,
            b'{"message": "Validation Error", "fields": {"name": "required"}}',
        )

        with self.assertRaises(ValidationError) as context:
            _api()._throw_on_error(response)

        self.assertEqual(context.exception.errors, {"name": "required"})
