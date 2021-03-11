from testcase.test_mathfunc import *
import unittest


test_dir = '../testcase'

if __name__ == '__main__':
#way1:通过discover形式
    # suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
    # runner = unittest.TextTestRunner()
    # runner(suite)
#way2 通过testloader
    suite1 = unittest.TestLoader().loadTestsFromNames('TestMathFunc')
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)