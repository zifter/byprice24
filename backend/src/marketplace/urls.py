from django.urls import include
from django.urls import path
from marketplace.views import CategoriesGroupListViewSet
from marketplace.views import CategoriesGroupViewSet
from marketplace.views import MarketplaceDetailsViewSet
from marketplace.views import MarketplacesViewSet
from marketplace.views import PopularProductsViewSet
from marketplace.views import ProductDetailsViewSet
from marketplace.views import ProductsViewSet

urlpatterns = [
    path('internal/', include('marketplace.private.urls')),

    path('v1/products/<str:id>', ProductDetailsViewSet.as_view(), name='product-detail'),
    path('v1/products', ProductsViewSet.as_view(), name='product-list'),
    path('v1/popular-products', PopularProductsViewSet.as_view(), name='products-popular'),
    path('v1/marketplaces', MarketplacesViewSet.as_view()),
    path('v1/marketplaces/<str:pk>', MarketplaceDetailsViewSet.as_view()),
    path('v1/categories', CategoriesGroupListViewSet.as_view()),
    path('v1/categories/<str:category>', CategoriesGroupViewSet.as_view()),
]
