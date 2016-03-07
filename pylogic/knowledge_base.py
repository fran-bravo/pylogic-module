from pylogic.functions import compare_cases, _count_answers, flat
from pylogic.exceptions import ArityError, TallyError, SelectorError
from pylogic.case import Case
from collections import OrderedDict
import typing

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
        :param case:
        """

        self.add_case(case)

    def __sub__(self, caselector):
        """ Interface to associate - operator with either delete_strain or remove_case method
        :param caselector:
        """

        if type(caselector) is str:
            self.delete_strain(caselector)
        elif type(caselector) is Case:
            self.remove_case(caselector)

    def __getitem__(self, selector):
        """ Interface to implement indexing
        :param selector:
        """

        return self.cases[selector]

    def __contains__(self, caselector):
        """ Interface to implement in expresions
        :param caselector:
        """

        if type(caselector) is str:
            return caselector in self.cases.keys()
        elif type(caselector) is Case:
            return caselector.tupla in self._selected_values(caselector.selector)

# Auxiliary Methods for Add #

    def _exists(self, selector):
        return selector in self.cases.keys()

    def _add_to_list(self, case):
        lista = self.cases[case.selector]
        lista.append(case.tupla)
        self.cases.update({case.selector: lista})

    def _add_new_to_list(self, case):
        self.cases.update({case.selector: [case.tupla]})

# Auxiliary Methods for Tally #

    def _validate_arity(self, variables):
        if len(variables) != self.arity:
            raise ArityError

    def _validate_selector(self, selector):
        if not self._exists(selector):
            raise SelectorError

    def _search_values(self, tupla):
        for l in self.cases.values():
            if tupla in l:
                return True
        return False

    def _flat_values(self):
        return flat(self.cases.values())

    def _selected_values(self, selector):
        return self.cases[selector]

    def _tally_no_var(self, selector, values):
        """ Searches if there's a tuple equal to the values.

        :param selector: str
        :param values: tuple"""
        for case in self._selected_values(selector):
            if case == values:
                return True
        return False

    def _tally_multiple_vars(self, selector, values):
        """ Compares the tuples associated with the selector against the values received.
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
        print("No selector")
        results = []
        for tupla in self._flat_values():
            if compare_cases(tupla, values):
                results.append(tupla)
        return results

    def _amount_of_answers(self, tupla):
        """ Checks the tuple and returns the amount of values to be answered

        :param tupla: tuple
        """

        if self._search_values(tupla):
            return 0
        else:
            return _count_answers(tupla)

    def _analyse_values(self, selector, values):
        """ Checks how the values passed are composed and selects the adecuate behaviour.

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
        self._validate_arity(case.tupla)
        if self._exists(case.selector):
            self._add_to_list(case)
        else:
            self._add_new_to_list(case)

    def delete_strain(self, selector):
        self.cases.pop(selector)

    def remove_case(self, case):
        cases = self._selected_values(case.selector)
        cases.remove(case.tupla)

    def tally(self, selector=None, *variables):
        values = tuple(variables)
        self._validate_arity(values)
        return self._analyse_values(selector, values)

    def strains(self):
        return list(self.cases.keys())

    def strain(self, selector):
        return list(self.cases[selector])

    def amount_of_strains(self):
        return len(self.strains())



