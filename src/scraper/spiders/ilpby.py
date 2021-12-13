from typing import Optional

from common.item_types import Category
from scraper.base import CategoryRule
from scraper.base import SpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor


class Spider(SpiderBase, StructuredDataMixin):
    name: str = 'www.ilp.by'
    allowed_domains = [
        'www.ilp.by',
    ]

    rules = (
        CategoryRule(LinkExtractor(allow=('notebook', )), category=Category.NOTEBOOK),
    )

    def parse_product_impl(self, response: Response, category: Category) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
