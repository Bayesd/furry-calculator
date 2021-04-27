class StringMethods:
    def more_than_nine(string):
        if type(string) == str:
            if len(string) > 9:
                return True
            else:
                return False
        else:
            return False
