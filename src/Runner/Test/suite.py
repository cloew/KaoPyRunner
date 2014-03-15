import unittest

from Runner.Test.python_runner_test import suite as python_runner_suite

suites = [python_runner_suite]
suite = unittest.TestSuite(suites)