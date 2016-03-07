from unittest import TestCase
from pylogic.knowledge_base import KnowledgeBase
from pylogic.decorators import case
from pylogic.exceptions import ArityError
from pylogic.functions import _
import pytest


def add_parent_strain(base):
    @case(base)
    def parent(father, son):
        pass
    return parent


def add_brother_strain(base):
    @case(base)
    def brothers(firstBorn, secondBorn):
        pass
    return brothers


def set_up_parents(base):
    parent = add_parent_strain(base)

    parent("Bob", "Caleb")
    parent("Bob", "George")
    parent("Bob", "Tim")

    return parent


def set_up_brothers(base):
    brothers = add_brother_strain(base)

    brothers("Caleb", "George")
    brothers("Caleb", "Tim")
    brothers("George", "Tim")
    brothers("George", "Caleb")
    brothers("Tim", "Caleb")
    brothers("Tim", "George")

    return brothers


def set_up_strain(base):
    return set_up_brothers(base), set_up_parents(base)


class TestDecoratorCase(TestCase):
    def test_add_case(self):
        base = KnowledgeBase(2)
        parent = add_parent_strain(base)
        parent("bob", "tim")

        assert base.tally("parent","bob","tim") == True

    def test_arity_error(self):
        with pytest.raises(ArityError):
            base = KnowledgeBase(2)
            @case(base)
            def brothers(firstBorn, secondBorn, thirdBorn):
                pass
            brothers("Caleb", "George", "Paul")

    def test_add_case2(self):
        base = KnowledgeBase(2)
        brothers = add_brother_strain(base)
        brothers("Caleb", "George")

        assert base.tally("brothers", "Caleb", "George") == True

    def test_base_strains_corrects(self):
        base = KnowledgeBase(2)
        set_up_strain(base)

        assert base.amount_of_strains() == 2
        assert base.tally("parent", "Bob", "Caleb") == True
        assert base.tally("brothers", "Caleb", "Tim") == True
        assert base.tally("brothers", "Tim", "Caleb") == True

    def test_base_strains_fails(self):
        base = KnowledgeBase(2)
        set_up_strain(base)

        assert base.tally("parent", "Tim", _) == []
        assert base.tally("parent", "George", "Tim") == False
        assert base.tally("brothers", "Gina", _) == []

    def test_base_strains_list_results(self):
        base = KnowledgeBase(2)
        brothers, parent = set_up_strain(base)

        assert base.tally("parent", "Bob", _) == [("Bob","Caleb"), ("Bob","George"), ("Bob", "Tim")]
        assert base.tally("brothers", "Caleb", _) == [("Caleb","George"), ("Caleb", "Tim")]
        assert base.tally("brothers", "Tim", _) == [("Tim", "Caleb"), ("Tim", "George")]