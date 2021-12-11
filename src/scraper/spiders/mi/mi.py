# scrapy crawl mi.by -o mi-$(date '+%Y-%m-%d').csv -t csv
import json

from scraper.items import ProductItem
from scrapy import Request
from scrapy import Spider


class VekSpider(Spider):
    name = 'mi.by'
    urls = {
        'https://mi.by/catalog/telefony_1/': 'mobile',
        'https://mi.by/catalog/besprovodnye_naushniki/': 'headphones',
    }

    def start_requests(self):
        for start_url in self.urls:
            yield Request(url=start_url, meta={'category': self.urls[start_url]})

    def parse(self, response, **kwargs):
        product_urls = response.xpath("//a[@class='area-link']/@href").extract()
        for product_url in product_urls:
            yield Request(url=f'https://mi.by{product_url}', callback=self.parse_product, meta=response.meta)
        next_page = response.xpath("//a[@class='pagination-btn-next']/@href").extract_first()
        if next_page:
            yield Request(url=f'https://mi.by{next_page}', callback=self.parse, meta=response.meta)

    def parse_product(self, response, **kwargs):
        data = json.loads(response.xpath("//script[@type='application/json']//text()").extract_first())
        offers = data['offers']
        for offer in offers:
            product_data = offers[offer]
            product = ProductItem(
                url=response.url,
                name=product_data['NAME'],
                price=float(product_data['PRICE']),
                price_currency='BYN',
                rating=0.00,
                review_count=0,
                availability='OutOfStock' if product_data['OUT_OF_STOCK'] else 'InStock',
                preview_url=f"https://mi.by{list(product_data['IMAGES_SRCS'].values())[0]}",
                categories=response.meta['category']

            )
            yield product
