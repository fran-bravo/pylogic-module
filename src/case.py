from src.functions import compare_cases


# Clase Hecho/Caso #


class Case:
    """Basic type of object for the logical programming, consists of:
    - A selector, used to identify the family of cases
    - A tuple, containing the values associated to the case
    """

    def __init__(self, selector, *args):
        self.selector = str(selector)
        self.tupla = tuple(args)

    def __str__(self):
        return self.selector + str(self.tupla)

    def tally_single_value(self, value):
        if value in self.tupla:
            return self.tupla
        else:
            return False

    def tally_tuple(self,tupla):
        if compare_cases(tupla, self.tupla):
            return self.tupla
        else:
            return False

    def tally(self, value):
        if type(value) != tuple:
            return self.tally_single_value(value)
        else:
            return self.tally_tuple(value)

