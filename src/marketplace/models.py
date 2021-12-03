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
    rating = models.IntegerField(default=0)

    def __str__(self):
        return str(self.domain)


# Create your models here.
class Product(models.Model):
    """
    General information about product
    """
    name = models.CharField(max_length=62, unique=True)
    category = models.CharField(max_length=62)
    description = models.CharField(max_length=32)
    image_url = models.CharField(max_length=256, null=True)

    def __str__(self):
        return str(self.name)


class ProductPage(models.Model):
    """
    Description of Product at Marketplace
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    url = models.CharField(max_length=256)

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

    def __str__(self):
        return f'{self.product_page} [{self.price} {self.price_currency}]'
