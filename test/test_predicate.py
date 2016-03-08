from unittest import TestCase
from pylogic.case import Case
from pylogic.knowledge_base import KnowledgeBase
from pylogic.predicate import Predicate
from pylogic.functions import _


class TestPredicate(TestCase):
    base = KnowledgeBase(3)

    case = Case("default", "Pablo", 4, True)

    case5 = Case("default", "Nombre", 4, True)
    case6 = Case("default", "Apellido", 4, False)
    case7 = Case("default", "Apellido", 5, True)
    case8 = Case("default", str(), 4, object)

    base.add_case(case)
    base.add_case(case5)
    base.add_case(case6)
    base.add_case(case7)
    base.add_case(case8)

    def test_simple_predicate(self):
        predicate = Predicate()
        predicate.add_base(self.base)

        assert predicate.tally(_, 4, _) == [("Pablo", 4, True), ("Nombre", 4, True), ("Apellido", 4, False), (str(), 4, object)]

    def test_two_bases_predicate(self):
        predicate = Predicate()
        predicate.add_base(self.base)

        predicate.add_rule(lambda tup: tup[1] > 3)

        assert predicate.tally(_, 4, _) == [("Pablo", 4, True), ("Nombre", 4, True), ("Apellido", 4, False), (str(), 4, object)]

    def test_complex_predicate(self):
        predicate = Predicate()
        predicate.add_base(self.base)

        predicate.add_rule(lambda tup: tup[1] > 4)

        assert predicate.tally(_, _, True) == [("Apellido", 5, True)]

    def test_another_predicate(self):
        predicate = Predicate()
        predicate.add_base(self.base)

        predicate.add_rule(lambda tup: tup[0].startswith("A"))

        assert predicate.tally(_, _, True) == [("Apellido", 5, True)]

    def test_def_predicate(self):
        predicate = Predicate()
        predicate.add_base(self.base)

        def filtro(tupla):
            if tupla[1] == 4 and (tupla[0] == "Nombre" or tupla[0] == "Pablo"):
                return True
            else:
                return False

        predicate.add_rule(filtro)

        assert predicate.tally(_, _, True) == [("Pablo", 4, True), ("Nombre", 4, True)]

