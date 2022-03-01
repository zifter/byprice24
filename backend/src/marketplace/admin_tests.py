from unittest.mock import Mock
from unittest.mock import patch

from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from marketplace.admin import ProductPageAdmin
from marketplace.models import ProductPage


class ProductPageAdminTestCase(TestCase):
    fixtures = [
        'prod/markets.yaml',
        'prod/categories.yaml',
        'test/product_pages.yaml',
        'test/products.yaml'
    ]

    def setUp(self) -> None:
        User.objects.create_superuser(
            username='admin', password='admin', email='admin@example.com'
        )
        self.client = Client()
        self.client.login(username='admin', password='admin')

    def test_productpage_loads_correctly(self):
        resp = self.client.get(reverse(
            'admin:marketplace_productpage_change',
            args=(1,)
        ))
        self.assertTrue('Force Scrape' in str(resp.content))

    @patch('django.contrib.admin.ModelAdmin.message_user', (lambda: Mock())())
    def test_click_on_force_scrape(self):
        request = RequestFactory().post('/')
        request.POST = {'force-scrape': True}

        admin_scraping_state = ProductPageAdmin(ProductPage, AdminSite())
        resp = admin_scraping_state.response_change(request, ProductPage.objects.first())
        self.assertEqual(302, resp.status_code)
