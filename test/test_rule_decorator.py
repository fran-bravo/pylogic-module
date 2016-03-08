from unittest import TestCase
from pylogic.case import Case
from pylogic.predicate import Predicate
from pylogic.knowledge_base import KnowledgeBase
from pylogic.decorators import rule
from pylogic.exceptions import ArityError, NoneBaseError
from pylogic.functions import _
import pytest


def set_base():
    base = KnowledgeBase(2)
    base + Case("default", "homer", "bart")
    base + Case("default", "marge", "lisa")
    base + Case("default", "marge", "bart")
    base + Case("default", "homer", "lisa")
    return base


def set_predicate():
    predicate = Predicate()
    base = set_base()
    predicate.add_base(base)
    return predicate


def pred_filter(predicate, str1="", str2=""):
    @rule(predicate)
    def filtro(tupla):
        if tupla[0].startswith(str1) and tupla[1].startswith(str2):
            return True
        else:
            return False
    return filtro


class TestDecoratorCase(TestCase):
    def test_add_rule(self):
        predicate = set_predicate()

        filtro = pred_filter(predicate, "h", "b")
        filtro("parentH-sonB")

        assert predicate.tally(_, "bart") == [("homer", "bart")]
        assert predicate.tally("homer", _) == [("homer", "bart")]

    def test_add_step_rule(self):
        predicate = set_predicate()

        filtro = pred_filter(predicate, "h")
        filtro("parentH")
        assert predicate.tally(_, _) == [("homer", "bart"), ("homer", "lisa")]
        filtro2 = pred_filter(predicate, str2="b")
        filtro2("sonB")
        assert predicate.tally(_, _) == [("homer", "bart")]

    def test_arity_error(self):
        with pytest.raises(ArityError):
            predicate = set_predicate()

            filtro = pred_filter(predicate, "h", "b")
            filtro("parentH-sonB")

            predicate.tally(_, "bart", "lisa")

    def test_none_base_error(self):
        with pytest.raises(NoneBaseError):
            predicate = Predicate()

            filtro = pred_filter(predicate, "h", "b")
            filtro("parentH-sonB")

