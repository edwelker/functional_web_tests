import unittest2
from sst.actions import *


def test_A():
    unittest2.FunctionTestCase(lambda: None)
    assert 2 == 4


def test_B():
    unittest2.FunctionTestCase(lambda: None)
    assert 1 == 2

test_A()
test_B()
