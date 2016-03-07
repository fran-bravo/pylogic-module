from pylogic.functions import compare_cases

# Clase Hecho/Caso #


class Case:
    """
    Basic type of object for the logical programming, consists of:
    - A selector, used to identify the family of cases
    - A tuple, containing the values associated to the case
    """

    def __init__(self, selector, *args):
        self.selector = str(selector)
        self.tupla = tuple(args)

    def __str__(self):
        return self.selector + str(self.tupla)

    def __add__(self, base) -> None:
        base.add_case(self)

    def tally(self, value):
        """
        Public interface of the class that allows the tally behaviour.
        Validates if either the value is in the Case Tuple or, if value is a tuple,
        tallies it to the Case Tuple.

        :param value: object, tuple
        """
        if value in self.tupla or compare_cases(value, self.tupla):
            return self.tupla
        else:
            return False
