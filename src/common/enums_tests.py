from common.enums import ExtendedEnum
from common.enums import KeywordsEnum


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


def test_values_ok():
    class TestEnum(ExtendedEnum):
        VALUE1 = 'value1'
        VALUE2 = 'value2'
        VALUE3 = 'value3'

    assert TestEnum.values() == ['value1', 'value2', 'value3']
    assert TestEnum.names() == ['VALUE1', 'VALUE2', 'VALUE3']
    assert TestEnum.choices() == [
        ('VALUE1', 'value1'),
        ('VALUE2', 'value2'),
        ('VALUE3', 'value3'),
    ]
