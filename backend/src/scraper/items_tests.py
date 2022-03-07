import pytest
from scraper.items import ProductScrapingResult


def test_result_required_title():
    with pytest.raises(TypeError):
        ProductScrapingResult()


def test_result_required_main_category():
    with pytest.raises(TypeError):
        ProductScrapingResult(
            title='test',
        )


def test_result_required_url():
    with pytest.raises(TypeError):
        ProductScrapingResult(
            title='test',
            main_category='mobile',
        )


def test_result_required_description():
    with pytest.raises(TypeError):
        ProductScrapingResult(
            title='test',
            main_category='mobile',
            url='https://url.by',
        )


def test_result_required_price():
    with pytest.raises(TypeError):
        ProductScrapingResult(
            title='test',
            main_category='mobile',
            url='https://url.by',
            description='test',
        )


def test_result_required_price_currency():
    with pytest.raises(TypeError):
        ProductScrapingResult(
            title='test',
            main_category=123,
            url='https://url.by',
            description='test',
            price=101.11,
        )


def test_result_ok():
    ProductScrapingResult(
        title='test',
        main_category='mobile',
        url='https://url.by',
        description='test',
        price=101.11,
        price_currency='BYN',
    )


def test_result_price_currency_is_not_empty():
    with pytest.raises(ValueError):
        ProductScrapingResult(
            title='test',
            main_category='mobile',
            url='https://url.by',
            description='test',
            price=101.11,
            price_currency='',
        )
