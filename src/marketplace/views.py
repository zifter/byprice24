from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.serializers import MarketplaceSerializer
from marketplace.serializers import ProductAvailabilitySerializer
from rest_framework import viewsets


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
