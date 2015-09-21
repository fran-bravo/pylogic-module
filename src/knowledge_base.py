from src.functions import compare_cases, count_answers, _

# Clase Base de Conocimiento #

class KnowledgeBase:

    def __init__(self, arity):
        self.arity = arity
        self.cases = []

    def add_case(self, case):
        if len(case.tupla) == self.arity:
            self.cases.append(case)
        else:
            raise ArityError


# Auxiliar Methods for Tally #

    def validate_arity(self, variables):
        if len(variables) != self.arity:
            raise ArityError

    def amount_of_answers(self, tupla):
        if tupla in self.cases:
            return 0
        else:
            return count_answers(tupla)

    def tally_no_var(self, variables):
        for case in self.cases:
            if case.tupla == variables:
                return True
        return False

    def tally_multiple_vars(self, variables):
        results = []
        for case in self.cases:
            if compare_cases(case.tupla, variables):
                results.append(case.tupla)
        #print("resultados:", results)
        return results

    def tally(self, variables):
        self.validate_arity(variables)
        if self.amount_of_answers(variables) == 0:
            return self.tally_no_var(variables)
        elif self.amount_of_answers(variables) > 0:
            return self.tally_multiple_vars(variables)
        else:
            raise TallyError


# Clase Error de Aridad #

class ArityError(Exception):
    pass

class TallyError(Exception):
    pass

