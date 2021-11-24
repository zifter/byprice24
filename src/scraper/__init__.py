# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.utils.log import configure_logging

from . import middlewares  # noqa: F401
from . import settings  # noqa: F401

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
