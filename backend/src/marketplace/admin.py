from crawler.agent import get_agent
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from marketplace.models import Category
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.models import ProductState

# Register your models here.

admin.site.register(Marketplace)
admin.site.register(Category)
admin.site.register(Product)


@admin.register(ProductPage)
class ProductPageAdmin(admin.ModelAdmin):
    change_form_template = 'product_page.html'

    def response_change(self, request, obj):
        if 'force-scrape' in request.POST:
            job_ids = get_agent().schedule(force=True, follow=False, marketplace=obj.marketplace, url_page=obj.url)
            url = f'/admin/django-rq/queues/0/{job_ids[0]}/'

            msg = mark_safe(f"This product page is scheduled to scrape - <a href='{url}'>Look at Job</a>")
            self.message_user(request, msg)
            return HttpResponseRedirect('.')

        return super().response_change(request, obj)


admin.site.register(ProductState)
