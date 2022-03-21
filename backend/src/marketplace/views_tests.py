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

    def test_get_list_products(self):
        response = self.client.get('/api/v1/products?id=5&id=4&id=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_list_products_order(self):
        response = self.client.get('/api/v1/products?id=5&id=3&id=4')
        self.assertEqual(response.data[0]['id'], 5)
        self.assertEqual(response.data[1]['id'], 3)
        self.assertEqual(response.data[2]['id'], 4)
