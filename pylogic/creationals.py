from pylogic.case import Case
from pylogic.knowledge_base import KnowledgeBase
from pylogic.predicate import Predicate

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

    def build_from(self, tupla, selector="default"):
        return Case(selector, tupla)

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
        return KnowledgeBase(self.aridad, self.cases)
