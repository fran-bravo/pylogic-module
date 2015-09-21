from unittest import TestCase
from src.case import Case
from src.knowledge_base import KnowledgeBase
from src.functions import _

class TestCase(TestCase):
    def test_case_tally(self):
        case = Case((True, "Hola"))
        assert case.tally(True) == (True, "Hola")

    def test_case_tally_2(self):
        x = 1
        case = Case((x, True, object))
        assert case.tally(x) == (x, True, object)

    def test_case_tally_3(self):
        base = KnowledgeBase(3)
        case = Case((base, False, str()))
        assert case.tally(False) == (base, False, str())

    def test_case_tally_4(self):
        case = Case(("Homero", 123456))
        assert case.tally(("Homero", _)) == ("Homero", 123456)