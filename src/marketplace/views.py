from common.elastic.elastic import ElasticManager
from marketplace.elastic import ELASTICSEARCH_PRODUCT_INDEX_NAME
from marketplace.models import Marketplace
from marketplace.serializers import MarketplaceSerializer
from marketplace.serializers import ProductSearchSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView


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


class ProductViewSet(APIView):
    """
    API Product
    """

    def get(self):
        query_param = self.request.query_params['query']
        data = ElasticManager(ELASTICSEARCH_PRODUCT_INDEX_NAME).search_data(query_param)
        serializer = ProductSearchSerializer(data, many=True)
        return Response(serializer.data)
