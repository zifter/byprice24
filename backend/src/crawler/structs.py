from urllib.parse import urlparse

from common.utils import cleanup_url
from marketplace.models import Category
from marketplace.models import Product
from scraper.items import ProductScrapingResult
from search.logic import find_closest_product


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

    @property
    def category_name(self) -> str:
        # TODO Find closest category
        return self._result.main_category

    def closest_product(self) -> Product:
        return find_closest_product(self._result.title)

    def category(self) -> Category:
        return Category.objects.get(name=self.category_name)
