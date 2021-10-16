from taller_unit_test.apps.offers.models import Offer

NUMBER_OFFERS_TO_CREATE = 3

def create_multiple_offers():
    def _create_offer(index):
        return {
            "name": "Offer {index}",
            "description": "Offer description",
            "price": index * 100
        }

    for number in range(NUMBER_OFFERS_TO_CREATE):
        print (number)