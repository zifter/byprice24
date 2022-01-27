from common.enums import ExtendedEnum


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
