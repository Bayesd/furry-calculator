class Calc:
    def add(x, y):
        return x + y

    def power_of_two(x):
        return x ** 2

print(Calc.power_of_two(int(input("Enter number:"))))