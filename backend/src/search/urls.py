from django.urls import path
from search.views import SearchProductQueryAutocompleteView
from search.views import SearchProductViewSet

urlpatterns = [
    path('v1/search/products', SearchProductViewSet.as_view(), name='search-product-list'),
    path('v1/search-autocomplete/products', SearchProductQueryAutocompleteView.as_view(), name='search-autocomplete-product-list'),
]
