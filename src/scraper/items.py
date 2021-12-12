# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class ProductItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    price_currency = scrapy.Field()
    availability = scrapy.Field()
    rating = scrapy.Field()
    review_count = scrapy.Field()
    preview_url = scrapy.Field()
    main_category = scrapy.Field()
    categories = scrapy.Field()
