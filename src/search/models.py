from datetime import datetime

import pytz
from django.db import models


class QueryHistory(models.Model):
    """
    Queries information
    """
    query = models.CharField(max_length=50)
    number_found_products = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=datetime.fromtimestamp(0, tz=pytz.UTC))

    def __str__(self):
        return f'{self.query} [{self.number_found_products}] [{self.timestamp}]'
