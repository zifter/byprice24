from typing import Optional

from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'texus.by'
    allowed_domains = [
        'texus.by',
    ]

    rules = (
        CategoryRule(allow='mobilnye_telefony', category='mobile'),
        CategoryRule(allow='noutbuki', category='notebook'),
        CategoryRule(allow='planshety', category='tabletpc'),
        CategoryRule(allow='monitory', category='display'),
        CategoryRule(allow='kompyutery', category='desktoppc'),
        CategoryRule(allow='televizory', category='tv'),
        CategoryRule(allow='naushniki,garnitury', category='headphones'),
    )

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
