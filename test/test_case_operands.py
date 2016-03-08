from unittest import TestCase
from pylogic.case import Case


class TestBaseOperand(TestCase):
    def test_eq_case(self):
        case1 = Case("parent", "homer", "bart")
        case2 = Case("parent", "homer", "bart")

        assert case1 == case2

    def test_not_eq_case1(self):
        case1 = Case("parent", "homer", "bart")
        case2 = Case("parent", "homer", "lisa")

        assert case1 != case2

    def test_not_eq_case2(self):
        case1 = Case("parent", "homer", "bart")
        case2 = Case("brother", "homer", "lisa")

        assert case1 != case2
