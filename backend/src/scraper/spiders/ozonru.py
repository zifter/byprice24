import json
from typing import Optional

from common.item_types import Availability
from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'www.ozon.ru'
    allowed_domains = [
        'www.ozon.ru',
    ]

    rules = (
        CategoryRule(LinkExtractor(allow=(r'smartfon-\w+',)), category='mobile'),
        CategoryRule(LinkExtractor(allow=(r'noutbuk-\w+',)), category='notebook'),
        CategoryRule(LinkExtractor(allow=(r'naushniki-\w+',)), category='headphones'),
    )

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:

        data = json.loads(response.xpath("//script[@type='application/ld+json']//text()").extract_first())

        availability = data['offers']['availability'].replace('http://schema.org/', '')
        product = ProductScrapingResult(
            url=response.url,
            title=data['name'],
            main_category=category,
            description=data['description'],
            price=float(data['offers']['price']),
            price_currency=data['offers']['priceCurrency'],
            rating=float(data['aggregateRating']['ratingValue']),
            review_count=int(data['aggregateRating']['reviewCount']),
            availability=Availability(availability),
            preview_url=data['image'],
            categories=response.xpath("//span[@class='a3p5 be1']//text()").extract()
        )
        return product
