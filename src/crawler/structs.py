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
    def preview_url(self) -> str:
        return self.item['preview_url']

    @property
    def availability(self) -> str:
        # https://schema.org/ItemAvailability
        return self.item['availability']

    @property
    def rating(self) -> float:
        return self.item['rating']

    @property
    def review_count(self) -> int:
        return self.item['review_count']

    @property
    def categories(self) -> str:
        return self.item['categories']

    @property
    def main_category(self) -> str:
        return self.item['main_category']
