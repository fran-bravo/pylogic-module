from unittest import TestCase
from src.knowledge_base import KnowledgeBase
from src.decorators import case
from src.exceptions import ArityError
from src.functions import _
import pytest


def add_parent_strain(base):
    @case(base)
    def parent(father, son):
        print(father + " has a son named " + son)
        return
    return parent


def add_brother_strain(base):
    @case(base)
    def brothers(firstBorn, secondBorn):
        pass
    return brothers


class TestCase(TestCase):
    def test_add_case(self):
        base = KnowledgeBase(2)
        parent = add_parent_strain(base)
        parent("bob", "tim")

        assert base.tally("parent","bob","tim") == True

    def test_arity_error(self):
        base = KnowledgeBase(2)
        with pytest.raises(ArityError):
            @case(base)
            def brothers(firstBorn, secondBorn, thirdBorn):
                pass
            brothers("Caleb", "George", "Paul")

    def test_add_case2(self):
        base = KnowledgeBase(2)
        brothers = add_brother_strain(base)
        brothers("Caleb", "George")

        assert base.tally("brothers", "Caleb", "George") == True

    def test_base_strains(self):
        base = KnowledgeBase(2)
        brothers = add_brother_strain(base)
        parent = add_parent_strain(base)

        brothers("Caleb", "George")
        brothers("Caleb", "Tim")
        brothers("George", "Tim")
        parent("Bob", "Caleb")
        parent("Bob", "George")
        parent("Bob", "Tim")

        assert base.amount_of_strains() == 2
        assert base.tally("brothers", "Caleb", _) == [("Caleb","George"), ("Caleb", "Tim")]
        assert base.tally("parent", "Bob", _) == [("Bob","Caleb"), ("Bob","George"), ("Bob", "Tim")]