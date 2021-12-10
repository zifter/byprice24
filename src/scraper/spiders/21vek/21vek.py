# scrapy crawl 21vek.by -o 21vek-$(date '+%Y-%m-%d').csv -t csv
import extruct
from scraper.items import ProductItem
from scrapy import Request
from scrapy import Spider


class VekSpider(Spider):
    name = '21vek.by'
    urls = {
        'https://www.21vek.by/mobile/': 'mobile',
        'https://www.21vek.by/notebooks/': 'notebooks',
        'https://www.21vek.by/headphones/': 'headphones',
    }

    def start_requests(self):
        for start_url in self.urls:
            yield Request(url=start_url, meta={'category': self.urls[start_url]})

    def parse(self, response, **kwargs):
        product_urls = response.xpath("//a[@class='result__link j-ga_track']/@href").extract()
        for product_url in product_urls:
            yield Request(url=product_url, callback=self.parse_product, meta=response.meta)
        next_page = response.xpath("//a[@rel='next']/@href").extract_first()
        if next_page:
            yield Request(url=next_page, callback=self.parse, meta=response.meta)

    def parse_product(self, response, **kwargs):
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
                categories=response.meta['category']

            )
            yield product
