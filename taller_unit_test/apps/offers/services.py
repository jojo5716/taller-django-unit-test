from taller_unit_test.apps.offers.models import Offer


def list():
    return Offer.objects.filter(is_active=True)

def create(validated_data):
    return Offer.objects.create(
        name=validated_data["name"],
        description=validated_data["description"],
        price=validated_data["price"] * 2,
    )

def update(instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.price = validated_data.get('price', instance.price)

    return instance

