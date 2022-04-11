from datetime import datetime

import pytz
from common.item_types import Availability
from django.db import models

"""
Some requirements and thoughts for data model:
* Marketplace have a lot of product
* Marketplace have a lot of pages which describes ONE product
* Some marketplace is more preferred then others in query result (prioritization)
* Product on the marketplace might have price and that price can be changed by marketplace
* We need to store price history
* We need to know time when information was updated last time
"""


class Marketplace(models.Model):
    """
    Marketplace site information
    """
    domain = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=128, blank=True)
    logo_url = models.URLField()
    delivery = models.BooleanField(default=False)

    def __str__(self):
        return str(self.domain)


class Category(models.Model):
    """
    General information about product
    """
    name = models.CharField(max_length=128, unique=True, primary_key=True)
    keywords = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def semantic_id(self) -> str:
        return str(self.name)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    """
    General information about product
    """
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=512)
    preview_url = models.URLField(max_length=256, null=True)

    def semantic_id(self) -> str:
        return f'{self.category.semantic_id()}/{str(self.name).lower()}'

    def __str__(self):
        return str(self.name)


class ProductPage(models.Model):
    """
    Description of Product at Marketplace
    """
    product = models.ForeignKey(Product, related_name='product_pages', on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Marketplace, related_name='marketplace', on_delete=models.CASCADE)
    url = models.URLField()
    name = models.CharField(max_length=192)
    description = models.CharField(max_length=512)
    preview_url = models.CharField(max_length=256, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} [{self.marketplace}]'


class ProductState(models.Model):
    """
    Description of Product state on the Product page of Marketplace
    """
    product_page = models.ForeignKey(ProductPage, related_name='product_states', on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.fromtimestamp(0, tz=pytz.UTC))
    last_check = models.DateTimeField(default=datetime.fromtimestamp(0, tz=pytz.UTC))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_currency = models.CharField(max_length=8)
    rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    availability = models.CharField(max_length=24, default='', choices=Availability.choices())

    def __str__(self):
        return f'{self.product_page} [{self.price} {self.price_currency}]'
