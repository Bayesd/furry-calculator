def convert_to_string(input):
    if type(input) == str:
        return input
    else:
        return str(input)


def more_than_nine(string):
    if len(convert_to_string(string)) > 9:
        return True
    else:
        return False


def add(x, y):
    return x + y


def power_of_two(x):
    return x ** 2


def modulo(x, y):
    return x % y


def denominator_is_zero(denominator):
    if denominator == 0:
        return True
    else:
        return False


def divide(x, y):
    if denominator_is_zero(y):
        return "undefined"
    else:
        return x / y


def int_division(x, y):
    if denominator_is_zero(y):
        return "undefined"
    else:
        return x // y
