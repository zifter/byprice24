from unittest.mock import Mock
from unittest.mock import patch

from django.test import Client
from django.test import TestCase
from marketplace.constants import LAST_CHECK_DATE_FORMATE
from marketplace.models import Product
from marketplace.models import ProductState


class ProductsViewTestCase(TestCase):
    fixtures = [
        'test/categories.yaml',
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

    def test_list_products_serializer_fields(self):
        product_id = 5

        response = self.client.get(f'/api/v1/products?id={product_id}')

        product = Product.objects.get(id=product_id)
        product_state = ProductState.objects.get(product_page__product_id=product_id)

        assert len(response.json()) == 1
        response_data = response.json()[0]

        assert response_data['id'] == product.id
        assert response_data['name'] == product.name
        assert response_data['category'] == product.category.name
        assert response_data['preview_url'] == product.preview_url
        assert response_data['last_check'] == product_state.last_check.strftime(LAST_CHECK_DATE_FORMATE)
        assert response_data['min_offer'] == {
            'price': str(product_state.price),
            'price_currency': product_state.price_currency,
        }

    def test_list_products_fail(self):
        response = self.client.get('/api/v1/products')
        self.assertEqual(response.status_code, 400)

    def test_get_all_marketplaces(self):
        response = self.client.get('/api/v1/marketplaces')
        marketplaces = [{'domain': 'www.21vek.by', 'logo_url': 'https://www.21vek.by/img/up/logo_21vek.by.png', 'description': '', 'delivery': True},
                        {'domain': 'www.ilp.by', 'logo_url': 'https://userimages.shopmanager.by/3100630/ilp-logo.png', 'description': '', 'delivery': True}]
        self.assertEqual(response.data, marketplaces)

    def test_get_marketplace(self):
        response = self.client.get('/api/v1/marketplaces/1')
        marketplace = {'domain': 'www.21vek.by', 'logo_url': 'https://www.21vek.by/img/up/logo_21vek.by.png', 'description': '', 'delivery': True}
        self.assertEqual(response.data, marketplace)

    @patch('marketplace.counter_views.CounterViewsRedis.get_most_popular_products_id',
           (lambda: Mock(return_value=[]))())
    def test_get_no_popular_products(self):
        response = self.client.get('/api/v1/popular-products')
        self.assertEqual(response.status_code, 404)

    @patch('marketplace.counter_views.CounterViewsRedis.get_most_popular_products_id',
           (lambda: Mock(return_value=[2, 3, 4]))())
    def test_get_popular_products(self):
        response = self.client.get('/api/v1/popular-products')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], 2)
