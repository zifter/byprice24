from typing import Optional

from common.item_types import Category
from scraper.base import CategoryRule
from scraper.base import SpiderBase
from scraper.items import ProductScrapingResult
from scraper.structured_data.funtastic_structure import FuntasticStructuredData
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor


class Spider(SpiderBase, FuntasticStructuredData):
    name: str = 'www.funtastik.by'
    allowed_domains = [
        'www.funtastik.by',
    ]

    rules = (

        CategoryRule(LinkExtractor(allow=('igrushki/konstruktory',)), category=Category.LEGO),
    )

    def parse_product_impl(self, response: Response, category: Category) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
