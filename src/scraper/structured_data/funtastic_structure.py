from common.item_types import Availability
from scraper.items import ProductScrapingResult
from scraper.structured_data.mixin import StructuredDataMixin


class FuntasticStructuredData(StructuredDataMixin):

    @classmethod
    def get_product_scraper_result(cls, url, data, item, category, availability, preview_url):
        properties = item['properties']

        product = ProductScrapingResult(
            url=url,
            title=properties['name'] if not isinstance(properties['name'], list) else
            properties['name'][0].split(' Посмотреть')[0],
            main_category=category,
            description=cls.extract_description(data, item),
            price=round(float(properties['offers']['properties']['price']), 2),
            price_currency=properties['offers']['properties']['priceCurrency'] if not
            properties['offers']['properties']['priceCurrency'] == 'BYR' else 'BYN',
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
            categories=cls.extract_categories(data)
        )
        return product
