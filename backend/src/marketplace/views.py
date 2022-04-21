from django_redis import get_redis_connection
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiParameter
from marketplace.counter_views import CounterViewsRedis
from marketplace.models import CategoryGroup
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.raw_queries import SELECT_PRODUCT_WITH_MIN_PRICE_BY_IDS
from marketplace.serializers import CategoryGroupSerializer
from marketplace.serializers import MarketplaceSerializer
from marketplace.serializers import ProductDetailsSerializer
from marketplace.serializers import ProductListSerializer
from marketplace.serializers import ProductsQuerySerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response


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

    def retrieve(self, request, *args, **kwargs):
        resp = super().retrieve(request, *args, **kwargs)
        CounterViewsRedis(get_redis_connection()).increment_product_views(kwargs['id'])
        return resp


class ProductsViewSet(ListAPIView):
    """
    API Products for getting list of products, by their ids with order as passed ids had

    Example of request: api/v1/products?id=2&id=3
    """
    model = Product
    queryset = Product.objects
    serializer_class = ProductListSerializer
    pagination_class = None

    @extend_schema(
        parameters=[OpenApiParameter(name='id', required=True, type=int)],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        params = self.request.query_params.getlist('id')
        serializer = ProductsQuerySerializer(data=[{'id': product_id} for product_id in params] if params else [{'id': None}],
                                             many=True)
        serializer.is_valid(raise_exception=True)

        list_of_product_ids = [product_id['id'] for product_id in serializer.validated_data]
        return self.model.objects.raw(
            SELECT_PRODUCT_WITH_MIN_PRICE_BY_IDS,
            [
                list_of_product_ids,  # To order products as the order of passed ids was
                tuple(list_of_product_ids)  # To get products by ids
            ])


class PopularProductsViewSet(ListAPIView):
    """
    API Products for getting the most popular products
    """
    model = Product
    queryset = Product.objects
    serializer_class = ProductListSerializer
    number_of_products = 5
    pagination_class = None

    def list(self, request, *args, **kwargs):
        if not self.get_queryset():
            return Response(status=404)
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        counter_views_obj = CounterViewsRedis(get_redis_connection())
        product_ids = counter_views_obj.get_most_popular_products_id(self.number_of_products)

        if not product_ids:
            return []

        return self.model.objects.raw(
            SELECT_PRODUCT_WITH_MIN_PRICE_BY_IDS,
            [
                product_ids,
                tuple(product_ids)
            ])


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


class CategoriesGroupListViewSet(ListAPIView):
    """
    API categories group
    """
    model = CategoryGroup
    queryset = CategoryGroup.objects.filter(parent__isnull=True)
    serializer_class = CategoryGroupSerializer


class CategoriesGroupViewSet(RetrieveAPIView):
    """
    API categories group
    """
    model = CategoryGroup
    lookup_field = 'category'
    queryset = CategoryGroup.objects
    serializer_class = CategoryGroupSerializer
