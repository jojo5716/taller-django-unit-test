from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication

from taller_unit_test.apps.offers.models import Offer
from taller_unit_test.apps.offers.serializers import OfferSerilizer
from taller_unit_test.apps.offers.permissions import UpdateOfferPermission

class OfferView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerilizer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOfferPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)