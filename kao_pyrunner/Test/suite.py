import unittest

from kao_pyrunner.FunctionFinder.Test.suite import suite as functionfinder_suite
from kao_pyrunner.Language.Test.suite import suite as language_suite
from kao_pyrunner.Runner.Test.suite import suite as runner_suite

suites = [functionfinder_suite,
          language_suite,
          runner_suite]
suite = unittest.TestSuite(suites)