global _
_ = None

# Funciones Independientes #

def equal_or_empty(val1, val2):
    if val1 == val2:
        return True
    elif val1 == _:
        return True
    elif val2 == _:
        return True
    else:
        return False

def compare_cases(case1, case2):
    lista_bools = [(equal_or_empty(case1, case2)) for case1, case2 in zip(case1, case2)]
    return all(lista_bools)

def count_answers(tupla):
    lista, count = list(tupla), 0
    for l in lista:
            if l == _:
                count += 1
    return count

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

