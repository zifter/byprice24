from common import shared_queue
from common.elastic.elastic import ElasticManager
from rest_framework.response import Response
from rest_framework.views import APIView
from search.elastic_loader import ELASTICSEARCH_PRODUCT_INDEX
from search.serializers import ProductQuerySerializer
from search.serializers import ProductSearchSerializer


class SearchProductViewSet(APIView):
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
