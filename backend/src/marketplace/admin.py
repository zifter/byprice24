from django.contrib import admin
from marketplace.models import Category
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.models import ProductState
# Register your models here.

admin.site.register(Marketplace)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductPage)
admin.site.register(ProductState)
