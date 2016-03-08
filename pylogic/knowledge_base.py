from pylogic.functions import compare_cases, _count_answers, flat
from pylogic.exceptions import ArityError, TallyError, SelectorError
from pylogic.case import Case
from collections import OrderedDict


# Clase Base de Conocimiento #


class KnowledgeBase:
    """
    Main object for logical queries in the logical environment, consists of:
    - An arity, that is used to specify the length of the cases which it supports
    - A list of cases, that represent the values stored
    """

#  Magical Methods #

    def __init__(self, arity):
        self.arity = arity
        self.cases = OrderedDict()

    def __str__(self):
        return "Arity: " + str(self.arity) + " Cases: " + str(self.cases)

    def __add__(self, case):
        """ Interface to associate + operator with add_case method
        :param case
        """

        self.add_case(case)

    def __sub__(self, caselector):
        """ Interface to associate - operator with either delete_strain or remove_case method
        :param caselector
        """

        if type(caselector) is str:
            self.delete_strain(caselector)
        elif type(caselector) is Case:
            self.remove_case(caselector)

    def __getitem__(self, selector):
        """ Interface to implement indexing
        :param selector
        """

        return self.cases[selector]

    def __contains__(self, caselector):
        """ Interface to implement in expressions
        :param caselector
        """

        if type(caselector) is str:
            return caselector in self.cases.keys()
        elif type(caselector) is Case:
            return caselector.tupla in self._selected_values(caselector.selector)

    def __iter__(self):
        """ Implementation of for expressions """

        for selector in self.cases.keys():
            for case in self._selected_values(selector):
                yield Case(selector, *case)

# Auxiliary Methods for Add #

    def _exists(self, selector):
        """ Method that validates the existence of a selector """

        return selector in self.cases.keys()

    def _add_to_strain(self, case):
        """ Method that adds a case to a selector strain
        :param case
        """

        lista = self.cases[case.selector]
        lista.append(case.tupla)
        self.cases.update({case.selector: lista})

    def _add_new_to_strain(self, case):
        """ Method that adds a new case to a new selector strain
        :param case
        """

        self.cases.update({case.selector: [case.tupla]})

# Auxiliary Methods for Tally #

    def _validate_arity(self, values):
        """ Validation for the arity of the values
        :param values
        """

        if len(values) != self.arity:
            raise ArityError

    def _validate_selector(self, selector):
        """ Validation for the existence of a selector
        :param selector
        """

        if not self._exists(selector):
            raise SelectorError

    def _search_values(self, values):
        """ Method that searches the values in all the strains
        :param values
        """

        for strain_values in self.cases.values():
            if values in strain_values:
                return True
        return False

    def _flat_values(self):
        """ Method that returns the values of all the strains in a single list """

        return flat(self.cases.values())

    def _selected_values(self, selector):
        """ Method that returns the values of a specific selector strain
        :param selector
        """
        return self.cases[selector]

    def _tally_no_var(self, selector, values):
        """ Method that searches if there's a tuple equal to the values.
        :param selector: str
        :param values: tuple
        """

        for case in self._selected_values(selector):
            if case == values:
                return True
        return False

    def _tally_multiple_vars(self, selector, values):
        """ Method that compares the tuples associated with the selector against the values received.
        Returns a list with the answers found.
        :param selector: str
        :param values: tuple
        """

        results = []
        for tupla in self._selected_values(selector):
            if compare_cases(tupla, values):
                results.append(tupla)
        return results

    def _tally_no_selector(self, values):
        """ Method that compares if any selector strain has the specified values
        :param values
        """

        results = []
        for tupla in self._flat_values():
            if compare_cases(tupla, values):
                results.append(tupla)
        return results

    def _amount_of_answers(self, tupla):
        """ Method that checks the tuple and returns the amount of values to be answered
        :param tupla: tuple
        """

        if self._search_values(tupla):
            return 0
        else:
            return _count_answers(tupla)

    def _analyse_values(self, selector, values):
        """ Method that checks how the values passed are composed and selects the adequate behaviour.
        :param selector: str
        :param values: tuple
        """

        if selector is None:
            return self._tally_no_selector(values)
        elif self._amount_of_answers(values) == 0:
            return self._tally_no_var(selector, values)
        elif self._amount_of_answers(values) > 0:
            return self._tally_multiple_vars(selector, values)
        else:
            raise TallyError

# Public Methods

    def add_case(self, case):
        """ Method for the addition of cases to the base
        :param case
        """

        self._validate_arity(case.tupla)
        if self._exists(case.selector):
            self._add_to_strain(case)
        else:
            self._add_new_to_strain(case)

    def delete_strain(self, selector):
        """ Method for the deletion of a selector strain
        :param selector
        """

        self.cases.pop(selector)

    def remove_case(self, case):
        """ Method for the deletion of a specified case
        :param case
        """

        cases = self._selected_values(case.selector)
        cases.remove(case.tupla)

    def tally(self, selector=None, *variables):
        """ Method for the logical assertion of values
        :param selector
        :param variables
        """

        values = tuple(variables)
        self._validate_arity(values)
        return self._analyse_values(selector, values)

    def strains(self):
        """ Method for the inspection of the strains of the base """

        return list(self.cases.keys())

    def strain(self, selector):
        """ Method for the inspection of the values of a strain
        :param selector:
        :return:  list
        """

        return list(self.cases[selector])

    def amount_of_strains(self):
        """ Method that returns the amount of strains of the base
        :return: int
        """

        return len(self.strains())



