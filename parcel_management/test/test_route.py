import unittest

from parcel_management.route import Route
from parcel_management.parcel import Parcel
from parcel_management.recipient import Recipient
from parcel_management.address import Address

recipient = Recipient("busra", Address("Vestdijk","47", "5611CA", "Eindhoven"))

class ParcelTest(unittest.TestCase):

    def test_weight_smaller_1_mail(self):
        parcel = Parcel(weight=0.5,value=1,recipient=recipient)
        dep_list = Route(parcel).departments
        self.assertEqual(dep_list[0].name, "Mail")

    def test_department_count(self):
        parcel = Parcel(weight=0.5,value=50,recipient=recipient)
        dep_list = Route(parcel).departments
        self.assertEqual(len(dep_list), 1)

    def test_weight_smaller_10_regular(self):
        parcel = Parcel(weight=7, value=100, recipient=recipient)
        dep_list = Route(parcel).departments
        self.assertEqual(dep_list[0].name, "Regular")

    def test_weight_bigger_10_heavy(self):
        parcel = Parcel(weight=17, value=1000, recipient=recipient)
        dep_list = Route(parcel).departments
        self.assertEqual(dep_list[0].name, "Heavy")

    def test_insurance_mail(self):
        parcel = Parcel(weight=0.45, value=1001, recipient=recipient)
        dep_list = Route(parcel).departments
        self.assertEqual(dep_list[0].name, "Insurance")
        self.assertNotEqual(len(dep_list), 1)
        self.assertEqual(dep_list[1].name, "Mail")

    def test_insurance_regular(self):
        parcel = Parcel(weight=9.99, value=1001, recipient=recipient)
        dep_list = Route(parcel).departments
        self.assertEqual(dep_list[0].name, "Insurance")
        self.assertNotEqual(len(dep_list), 1)
        self.assertEqual(dep_list[1].name, "Regular")

    def test_insurance_heavy(self):
        parcel = Parcel(weight=10.01, value=1001, recipient=recipient)
        dep_list = Route(parcel).departments
        self.assertEqual(dep_list[0].name, "Insurance")
        self.assertNotEqual(len(dep_list), 1)
        self.assertEqual(dep_list[1].name, "Heavy")

if __name__ == '__main__':
    unittest.main()