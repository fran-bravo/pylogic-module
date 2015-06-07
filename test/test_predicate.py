from unittest import TestCase
from src.case import Case
from src.knowledge_base import KnowledgeBase
from src.predicate import Predicate

__author__ = 'francisco'

global _
_ = None

class TestPredicate(TestCase):
    base = KnowledgeBase(3)

    case = Case(("Pablo", 4, True))

    case5 = Case(("Nombre", 4, True))
    case6 = Case(("Apellido", 4, False))
    case7 = Case(("Apellido", 5, True))

    base.add_case(case)
    base.add_case(case5)
    base.add_case(case6)
    base.add_case(case7)

    def test_simple_predicate(self):
        predicate = Predicate()
        predicate.add_rule(self.base)
        #predicate.add_rule(self.case)
        print(self.base.tally((_, 4, _)))
        print(self.case.tally((_, 4, _)))
        for p in predicate.tally((_, 4, _)):
            print(p)
