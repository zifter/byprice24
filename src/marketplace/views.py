from django.db.models import Prefetch
from marketplace.filters import ProductSearchFilter
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.serializers import MarketplaceSerializer
from marketplace.serializers import ProductAvailabilitySerializer
from marketplace.serializers import ProductSearchSerializer
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
    serializer_class = ProductSearchSerializer
    pagination_class = ProductsPagination
    filter_backends = [ProductSearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return Product.objects.prefetch_related(Prefetch('productpage_set',
                                                         queryset=ProductPage.objects.all(),
                                                         to_attr='product_pages'),
                                                Prefetch('product_pages__productstate_set',
                                                         to_attr='product_state'))

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

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
