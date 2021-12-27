from typing import Optional

from common.item_types import Category
from scraper.base import CategoryRule
from scraper.base import SpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor


class Spider(SpiderBase, StructuredDataMixin):
    name: str = 'www.funtastik.by'
    allowed_domains = [
        'www.funtastik.by',
    ]

    rules = (

        CategoryRule(LinkExtractor(allow=('igrushki/konstruktory',)), category=Category.LEGO),
    )

    def parse_product_impl(self, response: Response, category: Category) -> Optional[ProductScrapingResult]:
        structured_data = self.extract_structured_data(response, category)
        structured_data.title = structured_data.title.split(' Посмотреть')[0]
        return structured_data
