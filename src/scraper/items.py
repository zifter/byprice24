# Define here the models for your scraped items
#
# See documentation in:
# https://docs.org/en/latest/topics/items.html
from datetime import datetime
from typing import List

import attr
import pytz
from common.item_types import Availability
from common.item_types import Category


@attr.s(on_setattr=attr.setters.validate)
class ProductScrapingResult:
    """
    Результат парсинга продукта со страницы магазина.
    Не все поля обязательные
    """
    url: str = attr.ib(validator=attr.validators.instance_of(str))
    title: str = attr.ib(validator=attr.validators.instance_of(str))
    main_category: Category = attr.ib(validator=attr.validators.instance_of(Category))
    price: float = attr.ib(validator=attr.validators.instance_of(float))
    price_currency: str = attr.ib(validator=attr.validators.instance_of(str))
    timestamp: datetime = attr.ib(default=datetime.now(tz=pytz.UTC))
    availability: Availability = attr.ib(default=Availability.InStock, validator=attr.validators.instance_of(Availability))
    rating: float = attr.ib(default=0.0, validator=attr.validators.instance_of(float))
    review_count: int = attr.ib(default=0, validator=attr.validators.instance_of(int))
    preview_url: str = attr.ib(default='', validator=attr.validators.instance_of(str))
    categories: List[str] = attr.ib(default=attr.Factory(list), validator=attr.validators.instance_of(list))
