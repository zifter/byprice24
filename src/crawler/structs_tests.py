from crawler.structs import ProductData
from scraper.items import ProductItem


def test_product_data():
    item = ProductItem(
        url='https://21vek.by/mobile/x3pro8gb256gb_poco_01.html',
        name='Смартфон POCO X3 Pro 8GB/256GB (синий)',
        price=1049.0,
        price_currency='BYN',
    )

    data = ProductData(item)

    assert data.domain == '21vek.by'
