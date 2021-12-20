from rest_framework.response import Response
from rest_framework.views import APIView
from search.logic import find_all_matches
from search.serializers import ProductSearchSerializer


class SearchProductViewSet(APIView):
    """
    API Product
    """
    page_size = 20

    def get(self, request, *args, **kwargs):
        query_param = self.request.query_params.get('query')
        # page = self.request.query_params.get('page', '1')
        qs = find_all_matches(query_param)
        serializer = ProductSearchSerializer(qs, many=True)

        # shared_queue.get_flow_queue().push_query(query=request.query_params['query'],
        #                                          number_found_products=int(data['count']))

        return Response(data={'results': serializer.data})
