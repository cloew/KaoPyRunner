import unittest

from Language.Python.Test.suite import suite as python_suite

suites = [python_suite]
suite = unittest.TestSuite(suites)