import unittest

from kao_pyrunner.FunctionFinder.Test.python_function_finder_test import suite as python_function_finder_suite

suites = [python_function_finder_suite]
suite = unittest.TestSuite(suites)