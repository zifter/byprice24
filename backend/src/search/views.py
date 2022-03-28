from datetime import datetime

import pytz
from common import shared_queue
from common.shared_queue.structs import QueryRequest
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiParameter
from rest_framework.response import Response
from rest_framework.views import APIView
from search.enum import OrderingEnum
from search.logic import ProductSearch
from search.logic import ProductSearchAutocomplete
from search.serializers import ProductSearchAutocompleteQuerySerializer
from search.serializers import ProductSearchAutocompleteSerializer
from search.serializers import ProductSearchQuerySerializer
from search.serializers import ProductSearchResponse
from search.serializers import ProductSearchSerializer


class SearchProductViewSet(APIView):
    """
    API Product with search functionality
    """
    page_size = 20

    @extend_schema(
        parameters=[OpenApiParameter(name='query', description='Query to search a product', required=True, type=str),
                    OpenApiParameter(name='page', description='Page', required=False,
                                     type=int),
                    OpenApiParameter(name='ordering', description='Order result by price', required=False,
                                     enum=OrderingEnum.values())
                    ],
        responses=ProductSearchResponse
    )
    def get(self, request, *args, **kwargs):
        params = ProductSearchQuerySerializer(data={'query': self.request.query_params.get('query'),
                                                    'page': self.request.query_params.get('page', '1'),
                                                    'ordering': self.request.query_params.get('ordering')})
        params.is_valid(raise_exception=True)

        qs, count = ProductSearch().get_queryset(page_size=self.page_size, **params.data)
        serializer = ProductSearchSerializer(qs, many=True)

        self.push_query_into_db(params.data['query'], count)

        return Response(data={'count': count,
                              'next_page': params.data['page'] + 1 if params.data['page'] > 0 else 1,
                              'previous_page': params.data['page'] - 1 if params.data['page'] > 0 else 0,
                              'results': serializer.data})

    @staticmethod
    def push_query_into_db(query, number_found_products):
        obj = QueryRequest(
            query=query,
            result_count=number_found_products,
            timestamp=datetime.now(tz=pytz.UTC)
        )
        shared_queue.get_flow_queue().push_query(obj)


class SearchProductQueryAutocompleteView(APIView):
    """
    API Product
    """
    page_size = 5

    def get(self, request, *args, **kwargs):
        params = ProductSearchAutocompleteQuerySerializer(data={'query': self.request.query_params.get('query')})
        params.is_valid(raise_exception=True)

        qs = ProductSearchAutocomplete().get_queryset(query=params.data['query'], page=0, page_size=self.page_size)
        serializer = ProductSearchAutocompleteSerializer(qs, many=True)
        return Response(data=serializer.data)
