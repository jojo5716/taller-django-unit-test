from django.test import TestCase

from taller_unit_test.apps.offers.tests.helpers.offers import create_multiple_offers


class AnimalTestCase(TestCase):
    def setUp(self):
        pass

    def testAssertTrue(self):
        self.assertTrue(True)

# class TestBasic(TestCase):
#     # def setUp(self):
#         # Load test data
#         # create_multiple_offers()

#     def testAssertTrue(self):
#         self.assertTrue(True)

    # def test_customer_count(self):
    #     self.assertEqual(len(self.app.customers), 100)

    # def test_existence_of_customer(self):
    #     customer = self.app.get_customer(id=10)
    #     self.assertEqual(customer.name, "Org XYZ")
    #     self.assertEqual(customer.address, "10 Red Road, Reading")