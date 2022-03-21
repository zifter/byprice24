from django.urls import include
from django.urls import path

from marketplace.views import ProductDetailsViewSet, MarketplacesViewSet, MarketplaceDetailsViewSet
from search.views import SearchProductViewSet



urlpatterns = [
    path('internal/', include('marketplace.private.urls')),

    path('v1/search/products', SearchProductViewSet.as_view(), name='product-search-list'),
    path('v1/products/<str:id>', ProductDetailsViewSet.as_view(), name='product-detail'),
    path('v1/marketplaces', MarketplacesViewSet.as_view()),
    path('v1/marketplaces/<str:pk>', MarketplaceDetailsViewSet.as_view()),
]
