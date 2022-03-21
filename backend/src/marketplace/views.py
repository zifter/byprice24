from marketplace.models import Product
from marketplace.raw_queries import SELECT_PRODUCT_WITH_MIN_PRICE_BY_IDS
from marketplace.serializers import IdSerializer
from marketplace.serializers import ProductDetailsSerializer
from marketplace.serializers import ProductListSerializer
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


class ProductsViewSet(ListAPIView):
    """
    API Products for getting list of products, by their ids with order as passed ids had
    """
    model = Product
    queryset = Product.objects
    serializer_class = ProductListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        params = self.request.query_params.getlist('id')
        serializer = IdSerializer(data=[{'id': product_id} for product_id in params] if params else [{'id': None}],
                                  many=True)
        serializer.is_valid(raise_exception=True)

        list_of_product_ids = [product_id['id'] for product_id in serializer.validated_data]
        return self.model.objects.raw(
            SELECT_PRODUCT_WITH_MIN_PRICE_BY_IDS,
            [
                list_of_product_ids,  # To order products as the order of passed ids was
                tuple(list_of_product_ids)  # To get products by ids
            ])
