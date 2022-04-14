# import pytest
# from marketplace.category_group import CategoryGroup
# from marketplace.category_group import group_path
#
#
# def test_get_group_path_leaf():
#     assert group_path('mobile') == [
#         CategoryGroup('elektronika', 'Электроника'),
#         CategoryGroup('mobilnye-telefony-i-aksessuary', 'Мобильные телефоны и аксессуары'),
#         CategoryGroup('mobile', 'Смартфоны'),
#     ]
#
#
# def test_get_group_path_main():
#     assert group_path('elektronika') == [
#         CategoryGroup('elektronika', 'Электроника'),
#     ]
#
#
# def test_unknown_raise_exception():
#     with pytest.raises(KeyError):
#         group_path('unknown')
