import abc
from datetime import datetime
from datetime import timedelta


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
        self._cache[url] = datetime.now() + timedelta(seconds=ttl)

    def is_visited(self, url) -> bool:
        v: datetime = self._cache.get(url, None)
        if v:
            return v > datetime.now()

        return False
