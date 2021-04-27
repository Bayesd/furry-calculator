from Calculator import Calc


class Test:
    def test_add(self):
        assert 5 == Calc.add(3, 2)
        assert 19 == Calc.add(8, 11)

    def test_power_of_two(self):
        assert 0 == Calc.power_of_two(0)
        assert 9 == Calc.power_of_two(3)
        assert 25 == Calc.power_of_two(5)
