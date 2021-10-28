from taller_unit_test.apps.offers.models import Offer
from taller_unit_test.apps.offers import price as priceService

def list():
    return Offer.objects.filter(is_active=True)

def create(validated_data):

    return Offer.objects.create(
        name=validated_data["name"],
        description=validated_data["description"],
        price=priceService.calculate_price(validated_data["price"])
    )

def update(instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)

    if validated_data.get('price', None):
        price = priceService.calculate_price(validated_data["price"])
        instance.price = price
    
    return instance

