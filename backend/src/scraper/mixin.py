import logging
from typing import Dict
from typing import Optional

import extruct
from common.item_types import Availability
from scraper.items import ProductScrapingResult
from scrapy.http import Response
from scraper.data_extractors import MicrodataExtractor, JsonLdExtractor


class StructuredDataMixin:
    """
    Это Mixin (примись для наследования), которая расширяет класс Spider для извлечения structured data

    https://developers.google.com/search/docs/advanced/structured-data/intro-structured-data
    """

    def extract_structured_data(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        logging.info('parse_structured_data %s', response.url)

        data = extruct.extract(response.text, base_url=response.url)

        if 'json-ld' in data:
            extractor = JsonLdExtractor()
        else:
            return None

        return extractor.extract_data(data, category, response.url)
