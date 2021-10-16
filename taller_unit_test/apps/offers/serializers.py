from rest_framework import serializers

from taller_unit_test.apps.offers.models import Offer

class OfferSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'name', 'description', 'price']
