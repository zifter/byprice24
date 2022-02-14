from typing import Optional

from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'www.funtastik.by'
    allowed_domains = [
        'www.funtastik.by',
    ]

    rules = (

        CategoryRule(LinkExtractor(allow=('igrushki/konstruktory',)), category='buildingkit'),
    )

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        structured_data = self.extract_structured_data(response, category)
        if structured_data:
            structured_data.title = structured_data.title.split(' Посмотреть')[0]
        return structured_data
