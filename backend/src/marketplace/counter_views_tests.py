from unittest import TestCase

import fakeredis
from marketplace.counter_views import CounterViewsRedis


class CounterViewsTestCase(TestCase):
    fixtures = [
        'test/categories.yaml',
        'test/marketplaces.yaml',
        'test/products.yaml',
        'test/product_pages.yaml',
        'test/product_states.yaml',
    ]

    def setUp(self):
        self.redis_client = fakeredis.FakeStrictRedis()

    def test_get_product_views_none(self):
        number_of_views = CounterViewsRedis(self.redis_client).get_product_views(2)
        self.assertEqual(number_of_views, 0)

    def test_increment_product_views(self):
        counter_views_obj = CounterViewsRedis(self.redis_client)
        product_id = 2

        counter_views_obj.create_initial_product_views(product_id)
        counter_views_obj.increment_product_views(product_id)
        number_of_views = counter_views_obj.get_product_views(product_id)
        self.assertEqual(number_of_views, 1)
