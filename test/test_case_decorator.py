from unittest import TestCase
from src.knowledge_base import KnowledgeBase
from src.decorators import case

base = KnowledgeBase(2)


class TestCase(TestCase):
    def test_add_case(self):
        @case(base)
        def parent(father, son):
            print(father + " has a son named " + son)
            return
        parent("bob", "tim")

        assert base.tally("parent","bob","tim") == True
