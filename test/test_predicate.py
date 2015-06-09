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

    base2 = KnowledgeBase(3)

    case8 = Case((str(),4,object))

    base2.add_case(case8)

    def test_simple_predicate(self):
        predicate = Predicate()
        predicate.add_base(self.base)

        assert predicate.tally((_, 4, _)) == [("Pablo", 4, True), ("Nombre", 4, True), ("Apellido", 4, False)]

    def test_two_rule_predicate(self):
        predicate = Predicate()
        predicate.add_base(self.base)
        predicate.add_base(self.base2)

        predicate.add_rule(lambda tup: tup[1]>3)

        assert predicate.tally((_, 4, _)) == [("Pablo", 4, True), ("Nombre", 4, True), ("Apellido", 4, False), (str(), 4, object)]

    def test_complex_predicate(self):
        predicate = Predicate()
        predicate.add_base(self.base)
        predicate.add_base(self.base2)

        predicate.add_rule(lambda tup: tup[1]>4)

        assert predicate.tally((_, _, True)) == [("Apellido", 5, True)]

    def test_another_predicate(self):
        predicate = Predicate()
        predicate.add_base(self.base)
        predicate.add_base(self.base2)

        predicate.add_rule(lambda tup: tup[0].startswith("A"))

        assert predicate.tally((_, _, True)) == [("Apellido", 5, True)]

