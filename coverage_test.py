from function_coverage_test import *

import unittest

def my_suite():
    theSuite = unittest.TestSuite()
    theSuite.addTest(unittest.makeSuite(FunctionCoverageTests))

    return theSuite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = my_suite()
    runner.run(test_suite)