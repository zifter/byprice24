import http.client
from collections import OrderedDict

from django.test import Client
from django.test import TestCase


class MarketplaceViewEmptyTestCase(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_api_empty_list(self):
        response = self.client.get('/api/internal/marketplaces/')
        self.assertEqual(response.data['count'], 0)


class MarketplaceViewTestCase(TestCase):
    fixtures = ['test/marketplaces.yaml', ]

    expected = OrderedDict([
        ('id', 1),
        ('domain', 'www.21vek.by'),
        ('description', ''),
        ('logo_url', 'https://www.21vek.by/img/up/logo_21vek.by.png'),
        ('price_currency', 'BYN')
    ])

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_marketplaces_list_ok(self):
        response = self.client.get('/api/internal/marketplaces/')
        self.assertEqual(response.data['count'], 2)

        self.assertEqual(response.data['results'][0], MarketplaceViewTestCase.expected)

    def test_get_marketplace_ok(self):
        response = self.client.get('/api/internal/marketplaces/www.21vek.by')
        self.assertEqual(response.data, MarketplaceViewTestCase.expected)

    def test_get_marketplace_not_found(self):
        response = self.client.get('/api/internal/marketplaces/wrong-marketplace')
        self.assertEqual(response.status_code, http.client.NOT_FOUND)
