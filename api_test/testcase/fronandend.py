import unittest
class setup_teardown(unittest.TestCase):
    def setUp(self):
        print("执行用例开始")
    def tearDown(self):
        print("执行用例结束")