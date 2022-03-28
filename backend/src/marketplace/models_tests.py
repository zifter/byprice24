import pytest
from django.core.management import call_command
from marketplace.models import Category
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.models import ProductState

marketplace = Marketplace(
    domain='www.test.by',
    description='too long',
    logo_url='https://test',
)

category = Category(
    name='electronic',
    keywords='electronic',
)

product = Product(
    name='iPone',
    category=category,
    description='??',
)

product_page = ProductPage(
    product=product,
    marketplace=marketplace,
    url='www.test.by/ipone',
)

product_state = ProductState(
    product_page=product_page,
    price=199,
    price_currency='BYN',
)


def test_marketplace_is_printable_ok():
    assert str(marketplace) == 'www.test.by'


def test_category_is_printable_ok():
    assert str(category) == 'electronic'


def test_product_is_printable_ok():
    assert str(product) == 'iPone'


def test_semantic_id_ok():
    assert product.semantic_id() == 'electronic/ipone'


def test_product_page_is_printable_ok():
    assert str(product_page) == 'iPone [www.test.by]'


def test_product_state_is_printable_ok():
    assert str(product_state) == 'iPone [www.test.by] [199 BYN]'


@pytest.mark.django_db
def test_load_dump_ok():
    call_command('loaddata', 'dump/marketplace.yaml')


@pytest.mark.django_db
def test_load_prod_ok():
    call_command('loaddata', 'prod/markets.yaml')
    call_command('loaddata', 'prod/categories.yaml')
