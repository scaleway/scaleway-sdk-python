import unittest
from decimal import Decimal

from scaleway_core.bridge import unmarshal_Decimal, marshal_Decimal


class TestBridgeMarshal(unittest.TestCase):
    def test_decimal_marshal(self):
        decimal = Decimal("1.2")
        self.assertEqual(marshal_Decimal(decimal, None), {"value": "1.2"})

    def test_decimal_unmarshal(self):
        decimal = Decimal("1.2")
        self.assertEqual(unmarshal_Decimal({"value": "1.2"}), decimal)
