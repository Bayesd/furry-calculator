from Calculator import Calc
from StringMethods import more_than_nine, convert_to_string


def test_add():
    assert 5 == Calc.add(3, 2)
    assert 19 == Calc.add(8, 11)


def test_power_of_two():
    assert 0 == Calc.power_of_two(0)
    assert 9 == Calc.power_of_two(3)
    assert 25 == Calc.power_of_two(5)


def test_modulo():
    assert 2 == Calc.modulo(6, 4)
    assert 3 == Calc.modulo(8, 5)


def test_convert_To_String():
    assert type(convert_to_string(1234618)) == str
    assert type(convert_to_string(True)) == str
    assert type(convert_to_string(1234618)) != int
    assert type(convert_to_string(True)) != bool

def test_more_than_nine():
    assert more_than_nine("Flaggstångsknopp") is True
    assert more_than_nine("Ord") is False
    assert more_than_nine(244) is False
    assert more_than_nine(467382467823) is True
