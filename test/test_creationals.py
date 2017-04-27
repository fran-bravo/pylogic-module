import pytest, sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
from unittest import TestCase
from pylogic.creationals import CaseBuilder, BaseBuilder
from pylogic.functions import _


class TestCreationals(TestCase):

    def test_build_from(self):
        tup = ('homer', 'bart')
        case = CaseBuilder.build_from(tup, 'parent')
        assert case.tally('homer') == tup
        assert case.tally('bart') == tup

    def test_build_base(self):
        tup = ('homer', 'bart')
        case1 = CaseBuilder.build_from(tup, 'parent')
        tup = ('homer', 'lisa')
        case2 = CaseBuilder.build_from(tup, 'parent')
        builder = BaseBuilder(2, {'parent': [case1, case2]})
        base = builder.build()
        assert base.tally("parent", 'homer', _) == [('homer', 'bart'), ('homer', 'lisa')]

    def test_build_base_with_sets(self):
        tup = ('homer', 'bart')
        case1 = CaseBuilder.build_from(tup, 'parent')
        tup = ('homer', 'lisa')
        case2 = CaseBuilder.build_from(tup, 'parent')
        builder = BaseBuilder()
        builder.set_config(2, {'parent': [case1, case2]})
        base = builder.build()
        assert base.tally("parent", 'homer', _) == [('homer', 'bart'), ('homer', 'lisa')]
