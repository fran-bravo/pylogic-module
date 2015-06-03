global _
_ = None

# Clase Hecho/Caso #

class Case:

    def __init__(self, tupla):
        self.tupla = tupla
        self.resultados = []

    def tally(self, tup):
        if tup in self.tupla:
            return self.tupla
        else:
            return False


