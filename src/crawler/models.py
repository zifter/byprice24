from datetime import datetime

from django.db import models
from marketplace.models import Marketplace
from scraper.utils import get_spiders


class ScrapingState(models.Model):
    PARSERS = [(k, k) for k in get_spiders().keys()]
    """
    General information about site
    """
    marketplace = models.OneToOneField(Marketplace, on_delete=models.CASCADE)
    spider_name = models.CharField(max_length=32, choices=PARSERS)
    last_scraping = models.DateTimeField(default=datetime.fromtimestamp(0))

    def __str__(self):
        return f'{str(self.marketplace)} [{str(self.last_scraping)}]'
