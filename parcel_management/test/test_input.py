import unittest

from parcel_management.route import Route
from parcel_management.parcel import Parcel
from parcel_management.recipient import Recipient
from parcel_management.address import Address

recpnt = Recipient("busra", Address("Vestdijk","47", "5611CA", "Eindhoven"))

class InputTest(unittest.TestCase):

    def test_address_nullity(self):
        with self.assertRaises(TypeError):
            recipient = Recipient("busra", Address=None)

    def test_name_empty(self):
        with self.assertRaises(ValueError):
            recipient = Recipient("", Address("Vestdijk","47", "5611CA", "Eindhoven"))

    def test_city_nullity(self):
        with self.assertRaises(TypeError):
            address = Address("vestdijk", "47", "5611CA", None)

    def test_city_empty(self):
        with self.assertRaises(ValueError):
            recipient = Recipient("Busra", Address("Vestdijk","47", "5611CA", ""))

    def test_weight_zero(self):
        with self.assertRaises(ValueError):
            parcel = Parcel(weight=0, value=1, recipient=recpnt)

    def test_weight_zero(self):
        with self.assertRaises(ValueError):
            parcel = Parcel(weight=-14, value=1, recipient=recpnt)

if __name__ == '__main__':
    unittest.main()