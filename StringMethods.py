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
