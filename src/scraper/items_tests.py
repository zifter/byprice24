import pytest
from scraper.items import ProductScrapingResult


def test_product_scraping_result_validate():
    with pytest.raises(TypeError):
        ProductScrapingResult(
            url=123,
        )
