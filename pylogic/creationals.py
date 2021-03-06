from pylogic.case import Case
from pylogic.knowledge_base import KnowledgeBase


class CaseBuilder:

    def __init__(self, selector="default"):
        self.selector = selector
        self.tupla = []

    def set_selector(self, selector):
        self.selector = selector

    def set_tupla(self, *tupla):
        self.tupla = tupla

    def set_config(self, selector, *tupla):
        self.set_selector(selector)
        self.set_tupla(*tupla)

    def build(self):
        return Case(self.selector, *self.tupla)

    @staticmethod
    def build_from(tupla, selector="default"):
        return Case(selector, *tupla)


class BaseBuilder:

    def __init__(self, aridad=0, cases={}):
        self.aridad = aridad
        self.cases = cases

    def set_aridad(self, aridad):
        self.aridad = aridad

    def set_cases(self, cases):
        self.cases = cases

    def set_config(self, aridad, cases):
        self.set_aridad(aridad)
        self.set_cases(cases)

    def build(self):
        base = KnowledgeBase(self.aridad)
        for k in self.cases.keys():
            for case in self.cases[k]:
                base + case
        return base
