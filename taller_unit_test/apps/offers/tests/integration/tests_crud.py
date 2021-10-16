import requests
from django.test import TransactionTestCase

from taller_unit_test.apps.offers.tests.helpers.offers import create_multiple_offers
from taller_unit_test.apps.offers import services as offerService 

NUMBER_OFFERS_TO_CREATE = 3
ENDPOINT_BASE_URL = "http://localhost:8000"
ENDPOINT_OFFER_LIST = f"{ENDPOINT_BASE_URL}/offers/"

class OfferCRUDTestCase(TransactionTestCase):
    # def setUp(self):
    #     create_multiple_offers(NUMBER_OFFERS_TO_CREATE)

    def test_list_endpoint_returns_all_active_offers(self):
        create_multiple_offers(NUMBER_OFFERS_TO_CREATE)

        offer_list = requests.get(ENDPOINT_OFFER_LIST)
        offer_list = offerService.list()
        # self.assertEqual(offer_list.count(), NUMBER_OFFERS_TO_CREATE)
