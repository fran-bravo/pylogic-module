from unittest import TestCase
from pylogic.knowledge_base import KnowledgeBase
from pylogic.case import Case


def initialize():
    base = KnowledgeBase(2)
    case = Case("parent", "homer", "bart")
    return base, case


class TestBaseOperand(TestCase):
    def test_add_case(self):
        base, case = initialize()

        base + case

        assert base.tally("parent", "homer", "bart") == True

    def test_remove_strain(self):
        base, case = initialize()

        base + case
        base - "parent"

        assert base.strains() == []

    def test_remove_case(self):
        base, case = initialize()

        base + case
        base - case

        assert base.strain("parent") == []

    def test_indexing(self):
        base, case = initialize()

        base + case

        assert base["parent"] == [("homer", "bart")]

    def test_in(self):
        base, case = initialize()

        base + case

        assert case in base
        assert "parent" in base
