import uuid
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
        self.assertTrue('Detach Product' in str(resp.content))

    @patch('django.contrib.admin.ModelAdmin.message_user', (lambda: Mock())())
    @patch('crawler.agent.Agent.schedule', (lambda: Mock(return_value=[uuid.uuid4()]))())
    def test_click_on_force_scrape(self):
        request = RequestFactory().post('/')
        request.POST = {'force-scrape': True}

        admin_scraping_state = ProductPageAdmin(ProductPage, AdminSite())
        resp = admin_scraping_state.response_change(request, ProductPage.objects.first())
        self.assertEqual(302, resp.status_code)

    @patch('django.contrib.admin.ModelAdmin.message_user', (lambda: Mock())())
    def test_click_on_detach_product(self):
        request = RequestFactory().post('/')
        request.POST = {'detach-product': True}

        admin_scraping_state = ProductPageAdmin(ProductPage, AdminSite())
        resp = admin_scraping_state.response_change(request, ProductPage.objects.get(id=15))
        self.assertEqual(302, resp.status_code)

    @patch('django.contrib.admin.ModelAdmin.message_user', (lambda: Mock())())
    def test_attach_existed_product_to_product_page(self):
        request = RequestFactory().post('/')
        admin_scraping_state = ProductPageAdmin(ProductPage, AdminSite())

        product_page = ProductPage.objects.get(id=15)
        self.assertNotEqual(product_page.name, product_page.product.name)

        resp = admin_scraping_state.attach_existed_product_to_product_page(request, product_page)
        self.assertEqual(resp.name, resp.product.name)

    @patch('django.contrib.messages.api.add_message', (lambda: Mock())())
    def test_attach_error_message(self):
        request = RequestFactory().post('/')
        admin_scraping_state = ProductPageAdmin(ProductPage, AdminSite())

        resp = admin_scraping_state.attach_existed_product_to_product_page(request, ProductPage.objects.get(id=2))
        self.assertEqual(resp.name, resp.product.name)

    @patch('django.contrib.admin.ModelAdmin.message_user', (lambda: Mock())())
    def test_create_new_product_and_attach_to_product_page(self):
        request = RequestFactory().post('/')
        admin_scraping_state = ProductPageAdmin(ProductPage, AdminSite())

        resp = admin_scraping_state.create_new_product_and_attach_to_product_page(request, ProductPage.objects.first())
        self.assertEqual(resp.product.name, resp.name)
