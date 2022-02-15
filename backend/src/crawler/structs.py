from urllib.parse import urlparse

from common.utils import cleanup_url
from scraper.items import ProductScrapingResult


class ProductData:
    def __init__(self, item):
        self._result: ProductScrapingResult = item

    @property
    def domain(self) -> str:
        v = urlparse(self._result.url)
        return v.hostname

    @property
    def url(self) -> str:
        return cleanup_url(self._result.url)
