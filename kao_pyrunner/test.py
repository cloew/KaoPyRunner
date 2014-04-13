import unittest

from FunctionFinder.Test.suite import suite as functionfinder_suite
from Language.Test.suite import suite as language_suite
from Runner.Test.suite import suite as runner_suite

# Collect all the test suites
suites = [runner_suite,
          functionfinder_suite,
          language_suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
