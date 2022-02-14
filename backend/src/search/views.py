from common import shared_queue
from rest_framework.response import Response
from rest_framework.views import APIView
from search.logic import ProductSearch
from search.serializers import ProductQuerySerializer
from search.serializers import ProductSearchSerializer


class SearchProductViewSet(APIView):
    """
    API Product
    """
    page_size = 20

    def get(self, request, *args, **kwargs):
        params = ProductQuerySerializer(data={'query': self.request.query_params.get('query'),
                                              'page': self.request.query_params.get('page', '1'),
                                              'ordering': self.request.query_params.get('ordering')})
        params.is_valid(raise_exception=True)

        search_obj = ProductSearch(page_size=self.page_size, **params.data)
        qs = search_obj.get_queryset()
        serializer = ProductSearchSerializer(qs, many=True)

        self.push_query_into_db(params.data['query'], search_obj.count)

        return Response(data={'count': search_obj.count,
                              'next_page': params.data['page'] + 1 if params.data['page'] > 0 else 1,
                              'previous_page': params.data['page'] - 1 if params.data['page'] > 0 else 0,
                              'results': serializer.data})

    @staticmethod
    def push_query_into_db(query, number_found_products):
        shared_queue.get_flow_queue().push_query(query=query,
                                                 number_found_products=number_found_products)
