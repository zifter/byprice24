import http.client
from collections import OrderedDict

from django.test import Client
from django.test import TestCase


class MarketplaceViewEmptyTestCase(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_api_empty_list(self):
        response = self.client.get('/api/v1/marketplaces/')
        self.assertEqual(len(response.data), 0)


class MarketplaceViewTestCase(TestCase):
    fixtures = ['marketplaces_test.yaml', ]

    expected = OrderedDict([
        ('id', 1),
        ('domain', 'localhost'),
        ('description', ''),
        ('rating', 0),
        ('image_logo_url', 'https://www.test.by/')
    ])

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_marketplaces_list_ok(self):
        response = self.client.get('/api/v1/marketplaces/')
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0], MarketplaceViewTestCase.expected)

    def test_get_marketplace_ok(self):
        response = self.client.get('/api/v1/marketplaces/localhost')
        self.assertEqual(response.data, MarketplaceViewTestCase.expected)

    def test_get_marketplace_not_found(self):
        response = self.client.get('/api/v1/marketplaces/wrong-markeplace')
        self.assertEqual(response.status_code, http.client.NOT_FOUND)


class ProductViewTestCase(TestCase):
    fixtures = ['marketplaces_test.yaml', 'products_test.yaml', 'product_pages_test.yaml', 'product_states_test.yaml', ]

    expected = {'count': 2,
                'next': None,
                'previous': None,
                'results':
                    [
                        {'marketplaces_count_instock': 2,
                         'min_offer': {'price': 340.3, 'price_currency': 'BYN'},
                         'id': 2,
                         'name': 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009',
                         'category': 'notebook',
                         'description': '',
                         'preview_url': None},

                        {'marketplaces_count_instock': 1,
                         'min_offer': {'price': 580.3, 'price_currency': 'BYN'},
                         'id': 3,
                         'name': 'Acer Extensa 15 EX215-54-348Z NX.EGJER.00M',
                         'category': 'notebook',
                         'description': '',
                         'preview_url': None}
                    ]
                }

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_products_startswith_search_list_ok(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'Acer'})
        self.assertEqual(len(response.data['results']), 2)

        self.assertEqual(response.data, self.expected)

    def test_get_product_full_search_ok(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009'})
        self.assertEqual(response.data['results'], [self.expected['results'][0]])

    def test_pagination_full_page(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'Samsung',
                                         'page': 1})
        self.assertEqual(response.data['count'], 12)
        self.assertEqual(len(response.data['results']), 10)

    def test_pagination_not_full_page(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'Samsung',
                                         'page': 2})
        self.assertEqual(len(response.data['results']), 2)

    def test_get_products_empty_list(self):
        response = self.client.get('/api/v1/search/products', data={'query': 'Apple'})
        self.assertEqual(response.data, {'count': 0,
                                         'next': None,
                                         'previous': None, 'results': []}
                         )

    def test_query_whitespaces_removal(self):
        response = self.client.get('/api/v1/search/products', data={'query': '  Acer  '})
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data, self.expected)

    def test_fail_search_too_short_query(self):
        response = self.client.get('/api/v1/search/products', data={'query': 'A'})
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)

    def test_fail_search_no_query(self):
        response = self.client.get('/api/v1/search/products')
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)
