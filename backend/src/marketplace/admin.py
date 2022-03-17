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
            self.show_notification_to_user(request, msg)
            return HttpResponseRedirect('.')

        if 'detach-product' in request.POST:
            product = Product.objects.filter(name=obj.name).first()
            if product:
                self.attach_product_page_to_existing_product(request, obj, existing_product=product)

            else:
                self.create_new_product_and_attach_product_page(request, obj)

            return HttpResponseRedirect('.')

        return super().response_change(request, obj)

    def attach_product_page_to_existing_product(self, request, obj, existing_product):

        if obj.product.name == existing_product.name:
            self.show_error_to_user(request, 'This product page has correct product')

        else:
            obj.product = existing_product
            obj.save()
            self.show_notification_to_user(request, 'Correct product was successfully attached to product page')

        return obj

    def create_new_product_and_attach_product_page(self, request, obj):
        new_product = Product.objects.create(name=obj.name, description=obj.description,
                                             category=obj.category, preview_url=obj.preview_url)
        new_product.save()
        obj.product = new_product
        obj.save()
        self.show_notification_to_user(request, 'Product was created and attached to product page')

        return obj

    @staticmethod
    def show_error_to_user(request, msg):
        return messages.error(request, msg)

    def show_notification_to_user(self, request, msg):
        return self.message_user(request, mark_safe(msg))


admin.site.register(ProductState)
