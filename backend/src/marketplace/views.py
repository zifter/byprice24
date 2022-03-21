from marketplace.models import Product
from marketplace.raw_queries import SELECT_PRODUCT_WITH_MIN_PRICE
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
    API Products for getting list of products, by their ids
    """
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'
    ordering_fields = ('id',)
    ordering = ('id',)

    def list(self, request, *args, **kwargs):
        params = self.request.query_params.getlist('id')
        serializer = IdSerializer(data=[{'id': product_id} for product_id in params], many=True)
        serializer.is_valid(raise_exception=True)

        queryset = self.model.objects.raw(SELECT_PRODUCT_WITH_MIN_PRICE,
                                          [tuple(product_id['id'] for product_id in serializer.validated_data)])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
