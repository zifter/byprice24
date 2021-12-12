import logging
from typing import Optional

import extruct
from scraper.items import ProductItem
from scrapy.http import Response


class StructuredDataMixin:
    def parse_structured_data(self, response: Response) -> Optional[ProductItem]:
        logging.info('parse_structured_data %s', response.url)

        data = extruct.extract(response.text, base_url=response.url)

        if 'microdata' not in data:
            return None

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
                categories=self.extract_categories(data)
            )
            return product

    @classmethod
    def extract_categories(cls, data) -> list:
        if data.get('json-ld'):
            return [item['item']['name'] for item in data['json-ld'][0]['itemListElement']][:-1]

        return [data['microdata'][0]['properties']['category']]
