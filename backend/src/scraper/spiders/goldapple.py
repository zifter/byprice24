from typing import Generator

import extruct
import requests
from common.item_types import Availability
from common.item_types import Category
from scraper.base import SpiderBase
from scraper.items import ProductScrapingResult
from scrapy.http import Request
from scrapy.http import TextResponse


class Spider(SpiderBase):
    name: str = 'goldapple.by'

    ITEMS_COUNT_IN_RESPONSE = 20

    CATALOG_URL = 'catalog_url'
    SCRIPT_URL = 'script_url'
    CATEGORY = 'category'

    def start_requests(self) -> list[Request] | Generator[Request, None, None]:
        urls = [
            {
                self.CATALOG_URL: 'https://goldapple.by/azija',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=10&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/makijazh',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=3&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/uhod',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=4&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/volosy',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=6&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/parfjumerija',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=7&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/aptechnaja-kosmetika',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=3747&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/organika',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=12&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/dlja-muzhchin',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=3887&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/detjam',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=4357&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/podrostkam',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=6018&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/mini-formaty',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=5159&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/exclusives',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=4349&page={page}'),
                self.CATEGORY: Category.COSMETIC,
            }
        ]

        for url in urls:
            catalog_url = url[self.CATALOG_URL]

            # Calculating requests count
            # Get information from catalog pages
            main_page = requests.get(catalog_url)

            data = extruct.extract(main_page.text, base_url=catalog_url)
            for microdata in data['microdata']:
                if microdata['type'] not in ('https://schema.org/Product',
                                             'http://schema.org/Product'):
                    continue

                # Taking info about а count of products items
                count = int(microdata['properties']['offers']
                            ['properties']['offerCount'])
                break

            # Calculate counts of requests
            # (ITEMS_COUNT_IN_RESPONSE - count of items in one request)
            pages_count = count // self.ITEMS_COUNT_IN_RESPONSE + (
                1 if count % self.ITEMS_COUNT_IN_RESPONSE else 0)

            # Generate urls for requests
            for page in range(1, pages_count + 1):
                yield Request(url=url[self.SCRIPT_URL].format(page=page),
                              callback=self.parse,
                              headers={'referer': 'https://goldapple.by'},
                              cb_kwargs=dict(category=url[self.CATEGORY]))

    def extract_categories(self, product: dict) -> list[str]:
        result = []
        for key in list(product.keys()):
            if key.startswith('dimension1'):
                result.append(product[key])

        return result

    def parse(self, response: TextResponse, category: Category
              ) -> list[ProductScrapingResult]:
        data = response.json()

        result = []
        for product in data['products']:
            title = '{} {}'.format(product['brand'], product['name'])
            price = round(float(product['price_object']['amount']), 2)
            categories = self.extract_categories(product)

            price_currency = 'BYN'
            if product['price_object']['currency'] != 'BYR':
                price_currency = product['price_object']['currency']

            availability = Availability.SoldOut
            if product['is_saleable']:
                availability = Availability.InStock

            product = ProductScrapingResult(
                url=product['url'],
                title=title,
                main_category=category,
                description='',
                price=price,
                price_currency=price_currency,
                # timestamp,
                availability=availability,
                # rating=rating,
                # review_count=review_count,
                # preview_url=preview_url,
                categories=categories,
            )

            result.append(product)

        return result
