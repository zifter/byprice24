from django.urls import include
from django.urls import path
from marketplace.views import ProductDetailsViewSet
from marketplace.views import ProductsViewSet

urlpatterns = [
    path('internal/', include('marketplace.private.urls')),

    path('v1/products/<str:id>', ProductDetailsViewSet.as_view(), name='product-detail'),
    path('v1/products', ProductsViewSet.as_view())
]
