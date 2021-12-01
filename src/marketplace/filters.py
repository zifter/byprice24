from marketplace.serializers import ProductSearchSerializer
from rest_framework import filters


class ProductSearchFilter(filters.SearchFilter):
    search_param = 'query'

    def filter_queryset(self, request, queryset, view):
        ProductSearchSerializer(data=request.query_params).is_valid(raise_exception=True)
        return super().filter_queryset(request, queryset, view)
