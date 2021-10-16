from django.test import TestCase
from taller_unit_test.apps import offers

from taller_unit_test.apps.offers.tests.helpers.offers import create_multiple_offers
from taller_unit_test.apps.offers import services as offerService 

NUMBER_OFFERS_TO_CREATE = 3

class OfferTestCase(TestCase):
    def setUp(self):
        create_multiple_offers(NUMBER_OFFERS_TO_CREATE)
    
    def test_offer_list_returns_3_offers(self):
        offer_list = offerService.list()

        self.assertEqual(offer_list.count(), NUMBER_OFFERS_TO_CREATE)

    def test_offer_update_returns_intance_with_attrs_changed(self):
        first_offer = offerService.list().first()
        update_offer_kwargs = {
            "name": "New offer name",
            "description": "New offer description",
            "price": 333
        }
        new_offer_obj = offerService.update(first_offer, update_offer_kwargs)

        self.assertEqual(new_offer_obj.name, update_offer_kwargs["name"])
        self.assertEqual(new_offer_obj.description, update_offer_kwargs["description"])
        self.assertEqual(new_offer_obj.price, update_offer_kwargs["price"])


    def test_offer_update_returns_same_intance_when_validated_data_is_empty(self):
        first_offer = offerService.list().first()
        update_offer_kwargs = {}
        new_offer_obj = offerService.update(first_offer, update_offer_kwargs)

        self.assertEqual(new_offer_obj.name, "Offer 2")
        self.assertEqual(new_offer_obj.description, "Offer description 2")
        self.assertEqual(new_offer_obj.price, 200.0)
