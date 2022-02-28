from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.urls import reverse


class ProductPageAdmin(TestCase):
    fixtures = [
        'prod/categories.yaml',
        'test/marketplaces.yaml',
        'test/products.yaml',
        'test/product_pages.yaml',
    ]

    def test_productpage_loads_correctly(self):
        # prepare client
        User.objects.create_superuser(
            username='admin', password='admin', email='admin@example.com'
        )
        c = Client()
        c.login(username='admin', password='admin')

        resp = c.get(reverse(
            'admin:marketplace_productpage_change',
            args=(1,)
        ))
        self.assertTrue('Force Scrape' in str(resp.content))
