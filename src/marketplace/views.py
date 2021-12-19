from common import shared_queue
from common.elastic.elastic import ElasticManager
from marketplace.elastic_loader import ELASTICSEARCH_PRODUCT_INDEX
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.serializers import MarketplaceSerializer
from marketplace.serializers import ProductAvailabilitySerializer
from marketplace.serializers import ProductQuerySerializer
from marketplace.serializers import ProductSearchSerializer
from rest_framework import viewsets
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


class ProductViewSet(APIView):
    """
    API Product
    """
    page_size = 20

    def get(self, request, *args, **kwargs):
        query_param = self.request.query_params.get('query')
        page = self.request.query_params.get('page', '1')
        ProductQuerySerializer(data={'query': query_param,
                                     'page': page}).is_valid(raise_exception=True)

        data = ElasticManager(ELASTICSEARCH_PRODUCT_INDEX).search_data(query_param, self.page_size, page)
        serializer = ProductSearchSerializer(data['objects'], many=True)

        shared_queue.get_flow_queue().push_query(query=request.query_params['query'],
                                                 number_found_products=int(data['count']))
        return Response(data={'count': data['count'],
                              'next_page': data['next_page'],
                              'previous_page': data['previous_page'],
                              'results': serializer.data})


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
