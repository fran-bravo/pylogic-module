from src.case import *
from src.knowledge_base import *
from src.predicate import *

class CaseBuilder:

    def __init__(self, selector="default", tupla=()):
        self.selector = selector
        self.tupla = tupla

    def set_selector(self, selector):
        self.selector = selector

    def set_tupla(self, tupla):
        self.tupla = tupla

    def set_config(self, selector, tupla):
        self.set_selector(selector)
        self.set_tupla(tupla)

    def build(self):
        return Case(self.tupla, self.selector)
