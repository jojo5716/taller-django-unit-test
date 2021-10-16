from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from taller_unit_test.apps.offers import serializers, services

from taller_unit_test.apps.offers.models import Offer
from taller_unit_test.apps.offers.serializers import OfferSerilizer
from taller_unit_test.apps.offers.permissions import UpdateOfferPermission
from taller_unit_test.apps.offers import (
    services as offerService,
)

class OfferView(viewsets.ModelViewSet):
    queryset = offerService.list()
    serializer_class = OfferSerilizer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOfferPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        response_status = status.HTTP_400_BAD_REQUEST
        response_body = { "success": False }

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            offer = services.create(serializer.validated_data)

            response_status = status.HTTP_201_CREATED
            response_body = OfferSerilizer(offer).data

        return Response(response_body, status=response_status)
