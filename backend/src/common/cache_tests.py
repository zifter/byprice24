from time import sleep

from common.cache import VisitedCacheInMemory


def test_check_in_memory():
    cache = VisitedCacheInMemory()

    assert cache.is_visited('meta.com/') is False
    assert cache.is_visited('meta.com/') is False

    cache.visit('meta.com/', 1)
    assert cache.is_visited('meta.com/') is True

    sleep(1)
    assert cache.is_visited('meta.com/') is False
