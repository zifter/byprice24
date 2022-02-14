from datetime import datetime

import pytz
from django.db import models
from marketplace.models import Marketplace


class ScrapingState(models.Model):
    """
    General information about site
    """
    marketplace = models.OneToOneField(Marketplace, on_delete=models.CASCADE)
    last_scraping = models.DateTimeField(default=datetime.fromtimestamp(0, tz=pytz.UTC))
    use_proxy = models.BooleanField(default=False)
    scraping_schedule = models.CharField(max_length=30, default='0 0 * * *')

    def __str__(self):
        return f'{str(self.marketplace)} [{str(self.last_scraping)}]'
