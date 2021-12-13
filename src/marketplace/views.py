from marketplace.filters import ProductSearchFilter
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.serializers import MarketplaceSerializer
from marketplace.serializers import ProductAvailabilitySerializer
from marketplace.serializers import ProductSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response


class MarketplaceViewSet(viewsets.ModelViewSet):
    """
    API Marketplaces
    """
    model = Marketplace
    queryset = Marketplace.objects
    serializer_class = MarketplaceSerializer
    lookup_field = 'domain'
    ordering_fields = ('domain',)
    ordering = ('domain',)


class ProductViewSet(generics.ListAPIView):
    """
    API Product
    """
    model = Product
    queryset = Product.objects
    serializer_class = ProductSerializer
    filter_backends = [ProductSearchFilter]
    search_fields = ['name']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(data={'results': serializer.data})


class ProductAvailabilityViewSet(viewsets.ModelViewSet):
    """
    API Product availability on marketplaces
    """
    model = Product
    queryset = Product.objects
    serializer_class = ProductAvailabilitySerializer
    lookup_field = 'id'
    ordering_fields = ('id',)
    ordering = ('id',)
