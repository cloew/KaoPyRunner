import unittest

from kao_pyrunner.Language.Python.Test.suite import suite as python_suite

suites = [python_suite]
suite = unittest.TestSuite(suites)