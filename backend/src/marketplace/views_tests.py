from django.test import Client
from django.test import TestCase


class ProductsViewTestCase(TestCase):
    fixtures = [
        'prod/categories.yaml',
        'test/marketplaces.yaml',
        'test/products.yaml',
        'test/product_pages.yaml',
        'test/product_states.yaml',
    ]

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_get_first_product_ok(self):
        response = self.client.get('/api/v1/products/2')
        self.assertEqual(response.data['name'], 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009')
