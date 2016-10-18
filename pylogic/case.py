from pylogic.functions import compare_cases

# Clase Hecho/Caso #


class Case:
    """
    Basic type of object for the logical programming, consists of:
    - A selector, used to identify the family of cases
    - A tuple, containing the values associated to the case
    """

# Magic Methods #

    def __init__(self, selector, *args):
        self.selector = str(selector)
        self.tupla = tuple(args)

    def __str__(self):
        return self.selector + str(self.tupla)

    def __add__(self, base):
        """ Implementation of + operand for the sake of conmutativity
        :param base:
        """

        base.add_case(self)

    def __eq__(self, case):
        """ Implementation of equality between cases
        :param case:
        """

        return self.selector == case.selector and self.tupla == case.tupla

# Public Interface #

    def tally(self, value):
        """
        Public interface of the class that allows the tally behaviour.
        Validates if either the value is in the Case Tuple or, if value is a tuple,
        tallies it to the Case Tuple.
        :param value: object, tuple
        """

         if value in self.tupla:
            return self.tupla
        elif type(value) == Case and compare_cases(value, self.tupla):
            return True
        else:
            return False