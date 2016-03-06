from unittest import TestCase
from pylogic.knowledge_base import KnowledgeBase
from pylogic.functions import _
from pylogic.creationals import CaseBuilder

builder = CaseBuilder()
x = 1
base = KnowledgeBase(3)


def assert_case_test(value, selector, tupla):
    case = builder.build()

    assert case.selector == selector
    assert case.tally(value) == tupla


class TestCase(TestCase):
    def test_case_tally(self):
        builder.set_config("default", True, "Hola")
        assert_case_test(True, "default", (True, "Hola"))

    def test_case_tally_2(self):
        builder.set_config("case2", x, True, object)
        assert_case_test(x, "case2", (x, True, object))

    def test_case_tally_3(self):
        builder.set_config("1", base, False, str())
        assert_case_test((base, _, _), "1", (base, False, str()))

    def test_case_tally_4(self):
        builder.set_config("legajo", "Homero", 123456)
        assert_case_test(("Homero", _), "legajo", ("Homero", 123456))

    def test_case_failed_tally(self):
        builder.set_config("identidad", ("Homero", "Gomez"))
        assert_case_test(("Bart", _), "identidad", False)
