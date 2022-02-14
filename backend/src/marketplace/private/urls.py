from django.urls import path
from marketplace.private.views import MarketplaceViewSet
from marketplace.private.views import ProductPageViewSet
from marketplace.private.views import ProductStateViewSet
from marketplace.private.views import ProductViewSet


urlpatterns = [
    path('marketplaces/',
         MarketplaceViewSet.as_view({'get': 'list', })),
    path('marketplaces/<str:domain>',
         MarketplaceViewSet.as_view({'get': 'retrieve', })),
    path('products/',
         ProductViewSet.as_view({'get': 'list', })),
    path('products/<str:id>',
         ProductViewSet.as_view({'get': 'retrieve', })),

    path('product_pages/',
         ProductPageViewSet.as_view({'get': 'list', })),
    path('product_pages/<str:id>',
         ProductPageViewSet.as_view({'get': 'retrieve', })),

    path('product_states/',
         ProductStateViewSet.as_view({'get': 'list', })),
    path('product_states/<str:id>',
         ProductStateViewSet.as_view({'get': 'retrieve', })),
]
