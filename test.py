import unittest

from kao_pyrunner.Test.suite import suite as kao_pyrunner_suite

# Collect all the test suites
suites = [kao_pyrunner_suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
