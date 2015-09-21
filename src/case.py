from src.functions import compare_cases, _

# Clase Hecho/Caso #

class Case:

    def __init__(self, tupla):
        self.tupla = tupla
        self.resultados = []

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

