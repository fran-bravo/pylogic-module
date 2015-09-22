from unittest import TestCase
from src.case import Case
from src.knowledge_base import KnowledgeBase
from src.knowledge_base import ArityError
from src.functions import _
import pytest

class TestKnowledgeBase(TestCase):

    base = KnowledgeBase(2)

    case1 = Case(("W", False))
    case2 = Case(("X", False))
    case3 = Case(("Y", False))
    case4 = Case(("Z", True))
    case5 = Case(selector="otros", tupla=(True, "Z"))

    base.add_case(case1)
    base.add_case(case2)
    base.add_case(case3)
    base.add_case(case4)
    base.add_case(case5)

    def test_add_case(self):
        base = KnowledgeBase(2)
        case = Case(("X", True))
        case2 = Case(("Y", True))
        base.add_case(case)
        base.add_case(case2)
        assert len(base.cases["default"]) == 2

    def test_fail_add_case(self):
        base = KnowledgeBase(3)
        case = Case(("X", True))
        with pytest.raises(ArityError):
            base.add_case(case)

    def test_tally(self):
        assert self.base.tally(("Z", _)) == [("Z", True)]

    def test_tally2(self):
        assert self.base.tally((_, False)) == [("W", False), ("X", False), ("Y", False)]

    def test_arity_error(self):
        with pytest.raises(ArityError):
            self.base.tally(("Z", _, True))

    def test_arity_error2(self):
        with pytest.raises(ArityError):
            self.base.tally("Z")





