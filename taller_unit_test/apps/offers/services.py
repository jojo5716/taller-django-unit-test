from taller_unit_test.apps.offers.models import Offer


def list():
    return Offer.objects.filter(is_active=True)
