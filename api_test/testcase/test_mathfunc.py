import unittest
from bin.module.test_mathfunc import *
from fronandend import *


class TestMathFunc(setup_teardown):
    def test_add(self):
        self.assertEqual(3, add(1, 2))
        print("成功")

    def test_minus(self):
        self.assertEqual(2, minus(7,5))
#

