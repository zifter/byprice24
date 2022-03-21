import abc
from datetime import datetime
from datetime import timedelta

import pytz


class VisitedCacheBase:
    @abc.abstractmethod
    def visit(self, url, ttl):
        pass

    @abc.abstractmethod
    def is_visited(self, url) -> bool:
        pass


class VisitedCacheInMemory(VisitedCacheBase):
    def __init__(self):
        super().__init__()

        self._cache = {}

    def visit(self, url, ttl):
        self._cache[url] = datetime.now(tz=pytz.UTC) + timedelta(seconds=ttl)

    def is_visited(self, url) -> bool:
        v: datetime = self._cache.get(url, None)
        if v:
            return v > datetime.now(tz=pytz.UTC)

        return False
