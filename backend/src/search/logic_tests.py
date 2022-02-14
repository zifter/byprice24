from django.core.management import call_command
from django.test import TestCase
from parameterized import parameterized
from search.logic import find_closest_product


class SearchLogicTestCase(TestCase):
    fixtures = [
        'prod/categories.yaml',
        'test/products.yaml',
    ]

    @classmethod
    def setUpClass(cls):
        call_command('search_index', '--rebuild', '-f')

        super().setUpClass()

    @parameterized.expand([
        ('apple iphone 13', ),
        ('product with undefined query', ),
        ('Xiaomi Poco X3 NFC',),
    ])
    def test_unique_search_not_found(self, title):
        p = find_closest_product(title)

        assert p is None

    @parameterized.expand([
        ('Acer Extensa 15 EX215-53G-7014 NX.EGCER.009',),
        ('Samsung QE50LS01TBUA',),
    ])
    def test_full_match_found1(self, title):
        p = find_closest_product(title)

        assert p.name == title

    @parameterized.expand([
        ('Vitek VT1505', 'Vitek VT-1505'),
        ('Смартфон POCO X3 Pro 8GB/256GB международная версия (бронзовый)', 'Смартфон POCO X3 Pro 6GB/128GB международная версия (черный)'),
        ('Смартфон POCO X3 Pro 6Gb / 128Gb Blue(Global Version)', 'Смартфон POCO X3 Pro 6GB/128GB международная версия (черный)'),
        ('Xiaomi Poco X3 Pro 128GB', 'Смартфон POCO X3 Pro 6GB/128GB международная версия (черный)'),
        ('Смартфон Xiaomi POCO X3 Pro 6GB / 128GB Metal Bronze EU', 'Смартфон POCO X3 Pro 6GB/128GB международная версия (черный)'),
    ])
    def test_partial_match_found(self, title, found):
        p = find_closest_product(title)

        assert p.name == found
