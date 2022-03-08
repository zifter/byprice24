from crawler.agent import get_agent
from django.contrib import admin
from django.contrib import messages
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

        if 'detach-product' in request.POST:
            if Product.objects.filter(name=obj.name).exists():
                self.attach_existed_product_to_product_page(obj, request)

            else:
                self.create_new_product_and_attach_to_product_page(obj, request)

            return HttpResponseRedirect('.')

        return super().response_change(request, obj)

    def attach_existed_product_to_product_page(self, obj, request):
        existed_product = Product.objects.get(name=obj.name)

        if obj.product.name == existed_product.name:
            self.alert_msg(request, 'This product page has correct product', True)

        else:
            obj.product = existed_product
            obj.save()
            self.alert_msg(request, 'Correct product was successfully attached to product page', False)

    def create_new_product_and_attach_to_product_page(self, obj, request):
        new_product = Product.objects.create(name=obj.name, description=obj.description,
                                             category=obj.category, preview_url=obj.preview_url)
        new_product.save()

        obj.product = new_product
        obj.save()
        self.alert_msg(request, 'Product was created and attached to product page', False)

    def alert_msg(self, request, msg, error: bool = False):
        if error:
            return messages.error(request, msg)
        else:
            return self.message_user(request, mark_safe(msg))


admin.site.register(ProductState)
