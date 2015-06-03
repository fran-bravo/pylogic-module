global _
_ = None

# Funciones Anónimas independientes #

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
        lista = list(tupla)
        answers = 0
        if tupla in self.cases:
            return answers
        else:
            for l in lista:
                if l == _:
                    answers += 1
        return answers

    def tally_no_var(self, variables):
        for case in self.cases:
            if case.tupla == variables:
                return True
        return False

    def tally_one_var(self, variables):
        results = []
        for case in self.cases:
            if compare_cases(case.tupla, variables):
                results.append(case.tupla)
        #print("resultados:", results)
        return results

    def tally(self, variables):
        answers = self.amount_of_answers(variables)
        self.validate_arity(variables)
        if answers == 0:
            return self.tally_no_var(variables)
        elif answers > 0:
            return self.tally_one_var(variables)

# Clase Error de Aridad #

class ArityError(Exception):
    pass

