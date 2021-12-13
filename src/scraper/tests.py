from common.item_types import Availability
from common.item_types import Category
from scraper.items import ProductScrapingResult
from scraper.testing_utils import assert_spider


def test_spider_ilpby():
    url = 'https://www.ilp.by/notebook/apple/mxk32'
    expected = ProductScrapingResult(
        url=url,
        title='Apple MacBook Pro 13" Touch Bar 2020 MXK32',
        main_category=Category.NOTEBOOK,
        price=3440.0,
        price_currency='BYN',
        availability=Availability.InStock,
        preview_url='https://cdn.dataimgstore.com/preview/64/3/2626323/y9uMMTST0z.jpeg',
        rating=0.0,
        review_count=0,
        categories=[
            'Ноутбуки'
        ],
    )

    assert_spider(url, 'macbook.html', expected)


def test_spider_21vek_by():
    url = 'https://www.21vek.by/mobile/x3pro8gb256gb_poco_01.html'
    expected = ProductScrapingResult(
        url=url,
        title='Смартфон POCO X3 Pro 8GB/256GB (синий)',
        price=1049.0,
        price_currency='BYN',
        availability=Availability.InStock,
        preview_url='https://static.21vek.by/img/galleries/6632/831/preview_b/x3pro8gb256gb_poco_01_60dd5ddb2379f.png',
        rating=5.0,
        review_count=4,
        main_category=Category.SMARTPHONE,
        categories=[
            'Смартфоны, ТВ и электроника',
            'Смартфоны, аксессуары',
            'Смартфоны',
        ],
    )

    assert_spider(url, 'poco-pro-x3.html', expected)
