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
            image_url = item['properties']['image']
            product = ProductItem(
                url=response.url,
                name=item['properties']['name'],
                price=float(item['properties']['offers']['properties']['price']),
                price_currency=item['properties']['offers']['properties']['priceCurrency'],
                image_url=image_url if isinstance(image_url, str) else image_url[0],
                category=item['properties'].get('category') if item['properties'].get('category')
                else self.get_category_by_json_ld(data)
            )
            yield product

    @classmethod
    def get_category_by_json_ld(cls, data):
        return data['json-ld'][0]['itemListElement'][-2]['item']['name']
