from django.urls import path

from .views import MarketplaceViewSet

marketplace_list = MarketplaceViewSet.as_view({
    'get': 'list',
})
marketplace_detail = MarketplaceViewSet.as_view({
    'get': 'retrieve',
})


urlpatterns = [
    path('v1/marketplaces/', marketplace_list, name='marketplace-list'),
    path('v1/marketplaces/<str:Domain>', marketplace_detail, name='marketplace-detail'),
]
