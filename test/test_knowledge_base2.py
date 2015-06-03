from unittest import TestCase
from src.case import Case
from src.knowledge_base import KnowledgeBase

global _
_ = None

class TestKnowledgeBase2(TestCase):

    base2 = KnowledgeBase(3)

    case5 = Case(("Nombre", 4, True))
    case6 = Case(("Apellido", 4, False))
    case7 = Case(("Apellido", 5, True))

    base2.add_case(case5)
    base2.add_case(case6)
    base2.add_case(case7)

    def test_tally4(self):
        assert self.base2.tally(("Apellido", _, False)) == [("Apellido", 4, False)]

    def test_tally5(self):
        assert self.base2.tally(("Nombre", 4, True)) == True

    def test_tally6(self):
        assert self.base2.tally(("Carlos", 4, True)) == False

    def test_tally7(self):
        assert self.base2.tally((_, 4, _)) == [("Nombre", 4, True), ("Apellido", 4, False)]

    def test_amount_of_answers_empty(self):
        assert self.base2.amount_of_answers((_, _, _)) == 3

    def test_amount_of_answers_full(self):
        assert self.base2.amount_of_answers(("Nombre", 4, True)) == 0

    def test_amount_of_answers_wrong(self):
        assert self.base2.amount_of_answers(("ASDSA", 2, str())) == 0
