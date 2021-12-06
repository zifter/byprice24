from marketplace.serializers import ProductSearchSerializer
from rest_framework import filters


class ProductSearchFilter(filters.SearchFilter):
    search_param = 'query'

    def get_search_terms(self, request):
        params = request.query_params.get(self.search_param, '')
        params = params.replace('\x00', '')
        params = params.replace(',', ' ')
        params = params.replace('\'', ' ')
        params = params.strip()

        ProductSearchSerializer(data=dict(query=params)).is_valid(raise_exception=True)
        return params.split()
