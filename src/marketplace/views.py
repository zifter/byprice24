from marketplace.models import Product
from marketplace.serializers import ProductDetailsSerializer
from rest_framework.generics import RetrieveAPIView


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
