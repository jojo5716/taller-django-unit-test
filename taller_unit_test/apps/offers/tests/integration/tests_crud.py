import requests
from django.test import TransactionTestCase
from rest_framework.test import APIRequestFactory

from taller_unit_test.apps.offers.tests.helpers.offers import create_multiple_offers
from taller_unit_test.apps.offers import services as offerService

NUMBER_OFFERS_TO_CREATE = 3
ENDPOINT_BASE_URL = "http://localhost:8000"
ENDPOINT_OFFER_LIST = f"{ENDPOINT_BASE_URL}/offers/"


# class OfferCRUDTestCase(TransactionTestCase):
#     def setUp(self):
#         create_multiple_offers(NUMBER_OFFERS_TO_CREATE)

#     def test_list_endpoint_returns_all_active_offers(self):
#         offer_list = requests.get(ENDPOINT_OFFER_LIST).json()

#         expected_result = [
#             {
#                 'id': 1, 
#                 'name': 'Offer 1', 
#                 'description': 'Offer 1', 
#                 'price': 2.0
#             }
#         ]

#         self.assertEqual(offer_list["count"], 1)
#         self.assertEqual(offer_list["results"], expected_result)
