import logging
from typing import Dict
from typing import Optional

import extruct
from common.item_types import Availability
from scraper.items import ProductScrapingResult
from scrapy.http import Response


class StructuredDataMixin:
    """
    Это Mixin (примись для наследования), которая расширяет класс Spider для извлечения structured data

    https://developers.google.com/search/docs/advanced/structured-data/intro-structured-data
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def extract_structured_data(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
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

            title = self.extract_title(properties)
            description = self.extract_description(data, item)
            categories = self.extract_categories(data)
            rating = self.extract_rating(properties)

            offer = StructuredDataMixin.extract_offer(properties)
            price = self.extract_price(offer)
            price_currency = self.extract_price_currency(offer)
            availability = StructuredDataMixin.extract_availability(offer, price)

            review_count = 0
            if 'aggregateRating' in properties:
                review_count = int(properties['aggregateRating']['properties']['reviewCount'])

            product = ProductScrapingResult(
                url=response.url,
                title=title,
                main_category=category,
                description=description,
                price=price,
                price_currency=price_currency,
                rating=rating,
                review_count=review_count,
                availability=availability,
                preview_url=preview_url,
                categories=categories
            )

            return product

    @classmethod
    def extract_title(cls, properties) -> str:
        if isinstance(properties['name'], list):
            return properties['name'][0]
        return properties['name']

    @classmethod
    def extract_categories(cls, data) -> list:
        category = data['microdata'][0]['properties'].get('category')
        if category:
            return [category]

        if data.get('json-ld'):
            item_list_elements = data['json-ld'][0].get('itemListElement')
            if item_list_elements:
                return [item['item']['name'] for item in item_list_elements][:-1]

        return []

    @classmethod
    def extract_description(cls, data, item) -> str:
        description = ''
        properties = item['properties']
        if 'description' in properties:
            description = properties['description']

            if isinstance(description, list):
                description = description[0]
        else:
            dublincore = data['dublincore']
            if dublincore:
                description = dublincore[0]['elements'][0]['content']

        if len(description) > 512:
            description = cls.shorten_description(description)

        return description

    @classmethod
    def shorten_description(cls, description) -> str:
        short_description = []
        for description_paragraph in description.split('\n'):
            short_description.append(description_paragraph)
            if len('\n'.join(short_description)) > 512:
                short_description.pop()
                return '\n'.join(short_description)

    @classmethod
    def extract_rating(cls, properties) -> float:
        return float(properties['aggregateRating']['properties']['ratingValue'][0] if
                     'aggregateRating' in properties else '0')

    @classmethod
    def extract_price_currency(cls, offer) -> str:
        price_currency = ''
        if 'properties' in offer:
            value = offer['properties']['priceCurrency']
            price_currency = value if not value == 'BYR' else 'BYN'

        return price_currency

    @classmethod
    def extract_offer(cls, properties) -> Dict:
        offer = {}
        if 'offers' in properties:
            offers = properties['offers']
            offer = offers[0] if isinstance(offers, list) else offers

        return offer

    @classmethod
    def extract_availability(cls, offer: Dict, price: float) -> Availability:
        if price > 0:
            availability = Availability.InStock
        else:
            availability = Availability.OutOfStock

        if 'properties' in offer:
            if 'availability' in offer['properties']:
                value = offer['properties']['availability'].replace('http://schema.org/', '').replace('https://schema.org', '')
                availability = Availability(value)

        return availability

    @classmethod
    def extract_price(cls, offer) -> float:
        price = 0.0
        if 'properties' in offer:
            price = round(float(offer['properties']['price'].replace(' ', '')), 2)

        return price
