import logging
from typing import Generator

import extruct
from scraper.items import ProductItem
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule


class SchemaOrgSpider(CrawlSpider):
    name: str = 'schema.org'

    rules = (
        Rule(LinkExtractor(unique=True), callback='parse_item', follow=True),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'target_url' in kwargs:
            self.start_urls.append(kwargs['target_url'])

    def parse_item(self, response: Response) -> Generator[ProductItem, None, None]:
        logging.info('parse %s', response.url)

        data = extruct.extract(response.text, base_url=response.url)

        if 'microdata' not in data:
            return

        microdata = data['microdata']
        for item in microdata:
            if item['type'] not in ('https://schema.org/Product', 'http://schema.org/Product'):
                continue
            properties = item['properties']
            image = properties['image']
            preview_url = image if isinstance(image, str) else image[0]

            product = ProductItem(
                url=response.url,
                name=properties['name'],
                price=float(properties['offers']['properties']['price']),
                price_currency=properties['offers']['properties']['priceCurrency'],
                rating=float(
                    properties['aggregateRating']['properties']['ratingValue']
                    if 'aggregateRating' in properties
                    else '0'),
                review_count=int(
                    properties['aggregateRating']['properties']['reviewCount']
                    if 'aggregateRating' in properties
                    else '0'),
                availability=properties['offers']['properties']['availability'].replace('http://schema.org/', ''),
                preview_url=preview_url,
                categories=self.get_categories(data)
            )
            yield product

    @classmethod
    def get_categories(cls, data) -> list:
        if data.get('json-ld'):
            return [item['item']['name'] for item in data['json-ld'][0]['itemListElement']][:-1]

        return [data['microdata'][0]['properties']['category']]
