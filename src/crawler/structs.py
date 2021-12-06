from urllib.parse import urlparse


class ProductData:
    def __init__(self, item):
        self.item = item

    @property
    def domain(self) -> str:
        return urlparse(self.url).netloc

    @property
    def url(self) -> str:
        return self.item['url']

    @property
    def name(self) -> str:
        return self.item['name']

    @property
    def price(self) -> str:
        return self.item['price']

    @property
    def price_currency(self) -> str:
        return self.item['price_currency']

    @property
    def image_url(self) -> str:
        return self.item['image_url']

    @property
    def rating(self) -> str:
        return self.item['rating']

    @property
    def review_count(self) -> str:
        return self.item['review_count']

    @property
    def categories(self) -> str:
        return self.item['categories']
