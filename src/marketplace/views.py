from marketplace.filters import CustomSearchFilter
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.serializers import MarketplaceSerializer
from marketplace.serializers import ProductSerializer
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


class ProductViewSet(viewsets.ModelViewSet):
    """
    API Product
    """
    model = Product
    queryset = Product.objects
    serializer_class = ProductSerializer
    filter_backends = [CustomSearchFilter]
    search_fields = ['name']
