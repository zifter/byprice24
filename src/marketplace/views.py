from marketplace.models import Marketplace
from marketplace.serializers import MarketplaceSerializer
from rest_framework import viewsets


class MarketplaceViewSet(viewsets.ModelViewSet):
    """
    API Marketplaces
    """
    model = Marketplace
    queryset = Marketplace.objects
    serializer_class = MarketplaceSerializer
    lookup_field = 'Domain'
    ordering_fields = ('Domain', )
    ordering = ('Domain',)
