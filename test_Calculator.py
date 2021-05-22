from App import more_than_nine, convert_to_string, add, power_of_two, \
                modulo, denominator_is_zero, divide, int_division


def test_add():
    assert 5 == add(3, 2)
    assert 19 == add(8, 11)


def test_power_of_two():
    assert 0 == power_of_two(0)
    assert 9 == power_of_two(3)
    assert 25 == power_of_two(5)


def test_modulo():
    assert 2 == modulo(6, 4)
    assert 3 == modulo(8, 5)


def test_convert_To_String():
    assert type(convert_to_string(1234618)) == str
    assert type(convert_to_string(True)) == str
    assert type(convert_to_string(1234618)) != int
    assert type(convert_to_string(True)) != bool


def test_more_than_nine_with_strings():
    assert more_than_nine("Flaggstångsknopp") is True
    assert more_than_nine("Ord") is False


def test_more_than_nine_with_ints():
    assert more_than_nine(244) is False
    assert more_than_nine(467382467823) is True


def test_denominator_is_zero():
    assert denominator_is_zero(0) is True
    assert denominator_is_zero(1) is False


def test_divide():
    assert 5.0 == divide(25, 5)


def test_int_division():
    assert 2 == int_division(5, 2)
    assert 6 == int_division(12, 2)
