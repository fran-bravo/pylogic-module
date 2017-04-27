import pytest, sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
from unittest import TestCase
from pylogic.functions import flat, eval_elems, compare_tuple, check_tuple_elem, filter_tuple_repeats


class TestFunctions(TestCase):

    def test_flat(self):
        lista = [1, 2, ["string"]]
        assert flat(lista) == [1, 2, "string"]

    def test_eval_elems_false(self):
        lista = [False, True, True]
        assert eval_elems(lista) is False

    def test_eval_elems_true(self):
        lista = ["string", 1, 2]
        assert eval_elems(lista) == lista

    def test_compare_tuple_false(self):
        tup1 = ('homer', 'bart')
        tup2 = ('homer', 'lisa')
        assert compare_tuple(tup1, tup2) is False

    def test_compare_tuple_true(self):
        tup1 = ('homer', 'bart')
        assert compare_tuple(tup1, tup1) is True

    def test_check_tuple_elem(self):
        tup1 = ('homer', 'bart')
        tup2 = ('homer', 'lisa')
        lista = [tup1, tup2]
        assert check_tuple_elem(tup1, lista) is True

    def test_filter_tuple_repeats(self):
        tup1 = ('homer', 'bart')
        tup2 = ('homer', 'lisa')
        lista = [tup1, tup2, tup1]
        assert filter_tuple_repeats(lista) == [tup1, tup2]