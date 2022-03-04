import itertools
from typing import Generator
from typing import Optional

import requests
from scraper.base import SpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Request
from scrapy.http import Response


class Spider(SpiderBase, StructuredDataMixin):
    name: str = 'goldapple.by'

    ITEMS_COUNT_IN_RESPONSE = 20

    CATALOG_URL = 'catalog_url'
    SCRIPT_URL = 'script_url'
    CATEGORY = 'category'

    DEFAULT_CATEGORY = 'face_makeup'

    def start_requests(self) -> list[Request] | Generator[Request, None, None]:
        urls = [
            {
                self.CATALOG_URL: 'https://goldapple.by/azija',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=10&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/makijazh',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=3&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/uhod',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=4&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/volosy',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=6&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/parfjumerija',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=7&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/aptechnaja-kosmetika',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=3747&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/organika',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=12&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/dlja-muzhchin',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=3887&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/detjam',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=4357&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/podrostkam',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=6018&page={page}'),
                self.CATEGORY: 'face_makeup',
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/mini-formaty',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=5159&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            },
            {
                self.CATALOG_URL: 'https://goldapple.by/exclusives',
                self.SCRIPT_URL: ('https://goldapple.by/web_scripts/discover/'
                                  'category/products?cat=4349&page={page}'),
                self.CATEGORY: self.DEFAULT_CATEGORY,
            }
        ]

        headers = {'referer': 'https://goldapple.by'}

        if self.follow:
            for url in urls:
                for page in itertools.count(1):
                    response = requests.get(
                        url=url[self.SCRIPT_URL].format(page=page),
                        headers=headers
                    )

                    data = response.json()

                    if 'products' not in data:
                        break

                    for product in data['products']:
                        item_url = product['url']

                        yield Request(url=item_url,
                                      callback=self.parse_product,
                                      headers=headers,
                                      cb_kwargs={'category': url[self.CATEGORY]})
        else:
            category = self.DEFAULT_CATEGORY

            matched_categories = [url.get(self.CATEGORY) for url in urls
                                  if url.get(self.CATALOG_URL) in self.start_urls[0]]
            if len(matched_categories) > 0:
                category = matched_categories[0]

            yield Request(url=self.start_urls[0],
                          callback=self.parse_product,
                          headers=headers,
                          cb_kwargs={'category': category})

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
