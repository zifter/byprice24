from urllib.parse import urlparse

from scraper.items import ProductScrapingResult


class ProductData:
    def __init__(self, item):
        self.result: ProductScrapingResult = item

    @property
    def domain(self) -> str:
        return urlparse(self.result.url).netloc
