from Runner.python_runner import PythonRunner

import unittest

EMPTY_METHOD = ["def testMethod():", "\tpass"]

class processFunction(unittest.TestCase):
    """ Test cases of processFunction """
    
    def  setUp(self):
        """ Build the Python Runner for the test """
        self.runner = PythonRunner(EMPTY_METHOD)
        
    def handlesReturnValue(self):
        """ Test that the return value is added properly """
        results = self.runner.processFunction()
        self.assertEquals("return None", results[1], "Should have the return statement at the proper line")
        self.assertEquals(1, len(results), "Should only have the return statement")

# Collect all test cases in this class
testcasesProcessFunction = ["handlesReturnValue"]
suiteProcessFunction = unittest.TestSuite(map(processFunction, testcasesProcessFunction))

##########################################################

# Collect all test cases in this file
suites = [suiteProcessFunction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)