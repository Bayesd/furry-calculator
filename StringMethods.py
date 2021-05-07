def convertToString(input):
    if type(input) == str:
        return input
    else:
        return str(input)


def more_than_nine(string):
    if len(convertToString(string)) > 9:
        return True
    else:
        return False
