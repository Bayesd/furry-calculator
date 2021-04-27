from Calculator import Calc
from StringMethods import StringMethods as sm


class Test:
    def test_add(self):
        assert 5 == Calc.add(3, 2)
        assert 19 == Calc.add(8, 11)

    def test_power_of_two(self):
        assert 0 == Calc.power_of_two(0)
        assert 9 == Calc.power_of_two(3)
        assert 25 == Calc.power_of_two(5)

    def test_modulo(self):
        assert 2 == Calc.modulo(6, 4)
        assert 3 == Calc.modulo(8, 5)

    def test_more_than_nine(self):
        assert sm.more_than_nine("Flaggstångsknopp") is True
        assert sm.more_than_nine("Ord") is False
        assert sm.more_than_nine(244) is False
        assert sm.more_than_nine(467382467823) is False
