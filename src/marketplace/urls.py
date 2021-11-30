from django.urls import path

from .views import MarketplaceViewSet
from .views import ProductViewSet

marketplace_list = MarketplaceViewSet.as_view({
    'get': 'list',
})
marketplace_detail = MarketplaceViewSet.as_view({
    'get': 'retrieve',
})

product_search_list = ProductViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('v1/marketplaces/', marketplace_list, name='marketplace-list'),
    path('v1/marketplaces/<str:domain>', marketplace_detail, name='marketplace-detail'),
    path('v1/search/products', product_search_list, name='product-search-list'),
]
