from common.paths import TEST_DATA_DIR

from ..items import ProductItem
from ..utils import fake_response_from_file
from .schema_org import SchemaOrgSpider


PAGES_DIR = TEST_DATA_DIR.joinpath('parsing', 'marketplaces')


def test_check_parser_21vek_by():
    URL = 'https://www.21vek.by/mobile/x3pro8gb256gb_poco_01.html'
    filepath = PAGES_DIR.joinpath('21vek', 'poco-pro-x3.html')

    p = SchemaOrgSpider()
    fake_response = fake_response_from_file(filepath, url=URL)
    results = list(p.parse_item(fake_response))

    expected = ProductItem(
        url=URL,
        name='Смартфон POCO X3 Pro 8GB/256GB (синий)',
        price=1049.0,
        price_currency='BYN',
        image_url='https://static.21vek.by/img/galleries/6632/831/preview_b/x3pro8gb256gb_poco_01_60dd5ddb2379f.png',
        categories=['Смартфоны, ТВ и электроника', 'Смартфоны, аксессуары', 'Смартфоны']
    )

    assert results[0] == expected


# TODO make it works
# def test_check_parser_amd_by():
#     URL = 'https://www.amd.by/mobile/apple-iphone-13-pro-max-1tb-grafitovyi/'
#     filepath = PAGES_DIR.joinpath('amd', 'iphone-13.html')
#
#     p = SchemaOrgSpider()
#     fake_response = fake_response_from_file(filepath, url=URL)
#     results = list(p.parse_item(fake_response))
#
#     expected = ProductItem(
#         url=URL,
#         name='Смартфон POCO X3 Pro 8GB/256GB (синий)',
#         price=1049.0,
#         price_currency='BYN',
#     )
#
#     assert results[0] == expected


def test_check_parser_ilp_by():
    URL = 'https://www.ilp.by/notebook/apple/mxk32'
    filepath = PAGES_DIR.joinpath('ilp', 'macbook.html')

    p = SchemaOrgSpider()
    fake_response = fake_response_from_file(filepath, url=URL)
    results = list(p.parse_item(fake_response))

    expected = ProductItem(
        url=URL,
        name='Apple MacBook Pro 13" Touch Bar 2020 MXK32',
        price=3440.0,
        price_currency='BYN',
        image_url='https://cdn.dataimgstore.com/preview/64/3/2626323/y9uMMTST0z.jpeg',
        categories=['Ноутбуки']
    )

    assert results[0] == expected
