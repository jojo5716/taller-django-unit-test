from taller_unit_test.apps.offers.models import Offer

def create_multiple_offers(number_offers_to_create):
    def _create_offer(index):
        return {
            "name": "Offer {index}",
            "description": "Offer description",
            "price": index * 100
        }

    for number in range(number_offers_to_create):
        offer = Offer.objects.create(**_create_offer(number))
        offer.save()