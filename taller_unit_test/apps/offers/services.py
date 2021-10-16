from taller_unit_test.apps.offers.models import Offer


def list():
    return Offer.objects.filter(is_active=True)

def create(validated_data):
    return Offer.objects.create(
        name=validated_data["name"],
        description=validated_data["description"],
        price=validated_data["price"] * 2,
    )