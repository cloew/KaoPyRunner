import unittest

from Runner.Test.python_function_test import suite as python_function_suite
from Runner.Test.python_runner_test import suite as python_runner_suite

suites = [python_runner_suite,
          python_function_suite]
suite = unittest.TestSuite(suites)