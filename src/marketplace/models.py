from common.item_types import Availability
from common.item_types import Category
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
    description = models.CharField(max_length=32, blank=True)
    logo_url = models.URLField()

    def __str__(self):
        return str(self.domain)


class Product(models.Model):
    """
    General information about product
    """
    name = models.CharField(max_length=62, unique=True)
    category = models.CharField(max_length=62, choices=Category.choices())
    description = models.CharField(max_length=512)
    preview_url = models.URLField(max_length=256, null=True)

    def __str__(self):
        return str(self.name)


class ProductPage(models.Model):
    """
    Description of Product at Marketplace
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    url = models.URLField()
    name = models.CharField(max_length=62, unique=True)
    description = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.product} [{self.marketplace}]'


class ProductState(models.Model):
    """
    Description of Product state on the Product page of Marketplace
    """
    product_page = models.ForeignKey(ProductPage, on_delete=models.CASCADE)
    created = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_currency = models.CharField(max_length=8)
    rating = models.FloatField()
    review_count = models.IntegerField()
    availability = models.CharField(max_length=24, default='', choices=Availability.choices())

    def __str__(self):
        return f'{self.product_page} [{self.price} {self.price_currency}]'
