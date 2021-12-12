from typing import Generator

from common.categories import Category
from scraper.base import CategoryRule
from scraper.base import SpiderBase
from scraper.items import ProductItem
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor


class Spider(SpiderBase, StructuredDataMixin):
    name: str = 'www.21vek.by'
    allowed_domains = [
        'www.21vek.by',
    ]

    rules = (
        CategoryRule(LinkExtractor(allow=('mobile',)), category=Category.MOBILE),
        CategoryRule(LinkExtractor(allow=('notebooks',)), category=Category.NOTEBOOK),
        CategoryRule(LinkExtractor(allow=('headphones',)), category=Category.HEADPHONE),
    )

    def parse_item(self, response: Response, category: str) -> Generator[ProductItem, None, None]:
        item = self.parse_structured_data(response)
        item['main_category'] = category
        if item:
            yield item
