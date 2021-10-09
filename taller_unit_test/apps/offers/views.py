from rest_framework import viewsets, permissions

from taller_unit_test.apps.offers.models import Offer
from taller_unit_test.apps.offers.serializers import OfferSerilizer


class OfferView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerilizer