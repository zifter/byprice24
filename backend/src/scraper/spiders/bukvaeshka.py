from typing import Optional

from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'bukvaeshka.by'

    allowed_domains = [
        'www.funtastik.by',
    ]

    rules = (
        CategoryRule(allow='knigi', category='books'),
        CategoryRule(allow='nastolnye_igry_igrushki1', category='boardgames'),
        CategoryRule(allow='ruchki', category='pen'),
    )

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
