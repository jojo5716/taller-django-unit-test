from rest_framework import serializers
from taller_unit_test.apps import offers

from taller_unit_test.apps.offers import models 
from taller_unit_test.apps.offers import services as offerService
class OfferSerilizer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        fields = ['id', 'name', 'description', 'price']

    def update(self, instance, validated_data):
        return offerService.update(instance, validated_data)
