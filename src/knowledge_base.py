from src.functions import compare_cases, count_answers, flat, _
from src.exceptions import ArityError, TallyError, SelectorError
# Clase Base de Conocimiento #

class KnowledgeBase:
    """Main object for logical queries in the logical environment, consists of:
    - An arity, that is used to specify the length of the cases which it supports
    - A list of cases, that represent the values stored
    """

    def __init__(self, arity):
        self.arity = arity
        self.cases = {}

    def add_case(self, case):
        self._validate_arity(case.tupla)
        if self._exists(case.selector):
            self._add_to_list(case)
        else:
            self._add_new_to_list(case)

    def delete_strain(self, selector):
        self.cases.pop(selector)

# Auxiliar Methods for Add #

    def _exists(self, selector):
        return selector in self.cases.keys()

    def _add_to_list(self, case):
        lista = self.cases[case.selector]
        lista.append(case.tupla)
        self.cases.update({case.selector: lista})

    def _add_new_to_list(self, case):
        self.cases.update({case.selector: [case.tupla]})

# Auxiliar Methods for Tally #

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

    def _flat_values(self, selector):
        return self.cases[selector]

    def _tally_no_var(self, selector, variables):
        for case in self._flat_values(selector):
            if case == variables:
                return True
        return False

    def _tally_multiple_vars(self, selector, variables):
        results = []
        for tupla in self._flat_values(selector):
            if compare_cases(tupla, variables):
                results.append(tupla)
        return results

    def _amount_of_answers(self, tupla):
        if self._search_values(tupla):
            return 0
        else:
            return count_answers(tupla)

# Public Methods

    def tally(self, selector, *variables):
        vars = tuple(variables)
        self._validate_arity(vars)
        if self._amount_of_answers(vars) == 0:
            return self._tally_no_var(selector, vars)
        elif self._amount_of_answers(vars) > 0:
            return self._tally_multiple_vars(selector, vars)
        else:
            raise TallyError

    def amount_of_answers(self, *variables):
        tupla = tuple(variables)
        if self._search_values(tupla):
            return 0
        else:
            return count_answers(tupla)

    def strains(self):
        return list(self.cases.keys())

    def amount_of_strains(self):
        return len(self.strains())



