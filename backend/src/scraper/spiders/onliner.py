from typing import Optional

from scraper.base import CategoryRule, SiteMapSpiderBase
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response


class Spider(SiteMapSpiderBase, StructuredDataMixin):
    name: str = 'catalog.onliner.by'

    allowed_domains = [
        'catalog.onliner.by',
    ]

    sitemap_urls = (
        'https://catalog.onliner.by/sitemap.xml',
    )

    sitemap_rules = [
        ('', 'parse_product'),
    ]

    def sitemap_filter(self, entries):
        for entry in entries:
            url = entry['loc']
            matches = ['/review/create', '/reviews', '/prices', '/used', '?']
            if 'sitemap' not in url:
                if any(x in url for x in matches):
                    continue
                yield entry
            else:
                if 'https://catalog.onliner.by/sitemap/products' in url:
                    number = int(url.replace('https://catalog.onliner.by/sitemap/products-', '').replace('.xml.gz', ''))
                    if 1 < number <= 5:
                        yield entry

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
