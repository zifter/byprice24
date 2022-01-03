from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.models import ProductState
from marketplace.private.serializers import MarketplaceSerializer
from marketplace.private.serializers import ProductPageSerializer
from marketplace.private.serializers import ProductSerializer
from marketplace.private.serializers import ProductStateSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class ModelPagination(PageNumberPagination):
    page_size = 10


class MarketplaceViewSet(viewsets.ModelViewSet):
    """
    API Marketplaces
    """
    model = Marketplace
    queryset = Marketplace.objects.order_by('id')
    pagination_class = ModelPagination
    serializer_class = MarketplaceSerializer
    lookup_field = 'domain'
    ordering_fields = ('id',)
    ordering = ('id',)


class ProductViewSet(viewsets.ModelViewSet):
    """
    API Products
    """
    model = Product
    queryset = Product.objects.order_by('id')
    pagination_class = ModelPagination
    serializer_class = ProductSerializer
    lookup_field = 'name'
    ordering_fields = ('id',)
    ordering = ('id',)


class ProductPageViewSet(viewsets.ModelViewSet):
    """
    API Products
    """
    model = ProductPage
    queryset = ProductPage.objects.order_by('id')
    pagination_class = ModelPagination
    serializer_class = ProductPageSerializer
    lookup_field = 'id'
    ordering_fields = ('id',)
    ordering = ('id',)


class ProductStateViewSet(viewsets.ModelViewSet):
    """
    API Products
    """
    model = ProductState
    queryset = ProductState.objects.order_by('id')
    pagination_class = ModelPagination
    serializer_class = ProductStateSerializer
    lookup_field = 'id'
    ordering_fields = ('id',)
    ordering = ('id',)
