import logging
from typing import Optional

import extruct
from common.item_types import Availability
from common.item_types import Category
from scraper.items import ProductScrapingResult
from scrapy.http import Response


class StructuredDataMixin:
    """
    Это Mixin (примись для наследования), которая расширяет класс Spider для извлечения structured data

    https://developers.google.com/search/docs/advanced/structured-data/intro-structured-data
    """

    def extract_structured_data(self, response: Response, category: Category) -> Optional[ProductScrapingResult]:
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

            availability = properties['offers']['properties']['availability'].replace('http://schema.org/', '') if \
                properties['offers']['properties'].get('availability') else Availability.InStock.value

            properties = item['properties']
            product = ProductScrapingResult(
                url=response.url,
                title=self.extract_title(properties),
                main_category=category,
                description=self.extract_description(data, item),
                price=round(float(properties['offers']['properties']['price']), 2),
                price_currency=self.extract_price_currency(properties),
                rating=float(
                    properties['aggregateRating']['properties']['ratingValue']
                    if 'aggregateRating' in properties
                    else '0'),
                review_count=int(
                    properties['aggregateRating']['properties']['reviewCount']
                    if 'aggregateRating' in properties
                    else '0'),
                availability=Availability(availability),
                preview_url=preview_url,
                categories=self.extract_categories(data)
            )
            return product

    @classmethod
    def extract_title(cls, properties) -> str:
        if isinstance(properties['name'], list):
            return properties['name'][0]
        return properties['name']

    @classmethod
    def extract_categories(cls, data) -> list:
        if data.get('json-ld'):
            return [item['item']['name'] for item in data['json-ld'][0]['itemListElement']][:-1]

        category = data['microdata'][0]['properties'].get('category')
        if category:
            return [category]

        return []

    @classmethod
    def extract_description(cls, data, item) -> str:
        properties = item['properties']
        if 'description' in properties:
            if len(properties['description']) > 512:
                return cls.shorten_description(properties['description'])
            return properties['description']

        dublincore = data['dublincore']
        if dublincore:
            return dublincore[0]['elements'][0]['content']

        return ''

    @classmethod
    def shorten_description(cls, description) -> str:
        short_description = []
        for description_paragraph in description.split('\n'):
            short_description.append(description_paragraph)
            if len('\n'.join(short_description)) > 512:
                short_description.pop()
                return '\n'.join(short_description)

    @classmethod
    def extract_price_currency(cls, properties) -> str:
        return properties['offers']['properties']['priceCurrency'] if not \
            properties['offers']['properties']['priceCurrency'] == 'BYR' else 'BYN'
