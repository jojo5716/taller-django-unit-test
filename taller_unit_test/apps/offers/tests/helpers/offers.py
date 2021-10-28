from taller_unit_test.apps.offers.models import Offer
from taller_unit_test.apps.offers import services as offerServices

def create_multiple_offers(number_offers_to_create):
    def _create_offer(index) -> dict:
        return {
            "name": f"Offer {index}",
            "description": f"Offer description {index}",
            "price": 100
        }

    for number in range(number_offers_to_create):
        offerServices.create(_create_offer(number))
