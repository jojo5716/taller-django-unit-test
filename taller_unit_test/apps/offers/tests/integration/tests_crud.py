from django.test import TestCase
from taller_unit_test.apps import offers

from taller_unit_test.apps.offers.tests.helpers.offers import create_multiple_offers
from taller_unit_test.apps.offers import services as offerService 

NUMBER_OFFERS_TO_CREATE = 3

class OfferCRUDTestCase(TestCase):
    def setUp(self):
        create_multiple_offers(NUMBER_OFFERS_TO_CREATE)


