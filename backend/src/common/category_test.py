import pytest
from common.category import get_category


def test_mobile_category_ok():
    mobile = get_category('mobile')
    assert mobile.name == 'mobile'
    assert 'смартфоны' in mobile.keywords


def test_get_unknown_category_exception():
    with pytest.raises(ValueError):
        _ = get_category('unknown-category-will-raise')
