from time import sleep

from common.cache import VisitedCacheInMemory
from django.test import TestCase


class CacheTestCase(TestCase):
    def test_check_in_memory(self):
        cache = VisitedCacheInMemory()

        self.assertFalse(cache.is_visited('meta.com/'))
        self.assertFalse(cache.is_visited('meta.com/'))

        cache.visit('meta.com/', 1)
        self.assertTrue(cache.is_visited('meta.com/'))

        sleep(1)
        self.assertFalse(cache.is_visited('meta.com/'))
