from unittest import TestCase
from pylogic.case import Case
from pylogic.knowledge_base import KnowledgeBase
from pylogic.functions import _, count_answers


class TestKnowledgeBase2(TestCase):

    base2 = KnowledgeBase(3)

    case5 = Case("default", "Nombre", 4, True)
    case6 = Case("default", "Apellido", 4, False)
    case7 = Case("default", "Apellido", 5, True)
    case8 = Case("default", object, list, 4)

    base2.add_case(case5)
    base2.add_case(case6)
    base2.add_case(case7)
    base2.add_case(case8)

    def test_tally4(self):
        assert self.base2.tally("default", "Apellido", _, False) == [("Apellido", 4, False)]

    def test_tally5(self):
        assert self.base2.tally("default", "Nombre", 4, True) == True

    def test_tally6(self):
        assert self.base2.tally("default", "Carlos", 4, True) == False

    def test_tally7(self):
        assert self.base2.tally("default", _, 4, _) == [("Nombre", 4, True), ("Apellido", 4, False)]

    def test_tally_all(self):
        assert self.base2.tally("default", _, _, _) == [("Nombre", 4, True), ("Apellido", 4, False), ("Apellido", 5, True), (object, list, 4)]

    def test_tally_no_selector(self):
        self.base2.add_case(Case("otros", True, "premio", 3))
        assert self.base2.tally(_,  _, _, _) == [("Nombre", 4, True), ("Apellido", 4, False), ("Apellido", 5, True), (object, list, 4), (True, "premio", 3)]

    def test_amount_of_answers_empty(self):
        assert count_answers(_, _, _) == 3

    def test_amount_of_answers_full(self):
        assert count_answers("Nombre", 4, True) == 0

    def test_amount_of_answers_wrong(self):
        assert count_answers("ASDSA", 2, str()) == 0
