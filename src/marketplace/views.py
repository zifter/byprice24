from marketplace.filters import ProductSearchFilter
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.serializers import MarketplaceSerializer
from marketplace.serializers import ProductSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
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


class ProductsPagination(PageNumberPagination):
    page_size = 10


class ProductViewSet(generics.ListAPIView):
    """
    API Product
    """
    model = Product
    queryset = Product.objects
    serializer_class = ProductSerializer
    filter_backends = [ProductSearchFilter]
    search_fields = ['name']
    pagination_class = ProductsPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(data={'results': serializer.data})
