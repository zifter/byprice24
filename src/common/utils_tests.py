from common.utils import KeywordsEnum


class TestKeywordsEnum(KeywordsEnum):
    FIRST_NAME = 'first_name', ('first_name', 'name', 'имя')
    LAST_NAME = 'last_name', ('last_name', 'second_name', 'фамилия')
    AGE = 'age', ('age', 'возраст')


def test_get_by_value_enum():
    assert TestKeywordsEnum.get_by_value('first_name').value == 'first_name'
    assert TestKeywordsEnum.get_by_value('last_name').value == 'last_name'
    assert TestKeywordsEnum.get_by_value('age').value == 'age'


def test_get_by_keywords():
    assert TestKeywordsEnum.get_by_keywords('имя').value == 'first_name'
    assert TestKeywordsEnum.get_by_keywords('фамилия').value == 'last_name'
    assert TestKeywordsEnum.get_by_keywords('возраст').value == 'age'
