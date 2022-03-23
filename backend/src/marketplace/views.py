from marketplace.models import Product, Marketplace
from marketplace.serializers import ProductDetailsSerializer, MarketplaceSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView


class ProductDetailsViewSet(RetrieveAPIView):
    """
    API Product availability on marketplaces
    """
    model = Product
    queryset = Product.objects
    serializer_class = ProductDetailsSerializer
    lookup_field = 'id'
    ordering_fields = ('id',)
    ordering = ('id',)

class MarketplacesViewSet(ListAPIView):
    """
    API all marketplaces
    """
    model = Marketplace
    queryset = Marketplace.objects.all()
    serializer_class = MarketplaceSerializer

class MarketplaceDetailsViewSet(RetrieveAPIView):
    """
    API marketplace details
    """
    model = Marketplace
    queryset = Marketplace.objects
    serializer_class = MarketplaceSerializer
