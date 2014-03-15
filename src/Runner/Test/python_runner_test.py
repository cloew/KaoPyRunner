from Runner.python_runner import PythonRunner

import unittest

EMPTY_METHOD = ["def testMethod():", "\tpass"]
RETURN_1_METHOD = ["def testMethod():", "\treturn 1"]
RETURN_STRING_METHOD = ["def testMethod():", "\treturn 'Blah'"]
MULTI_LINE_RETURN_METHOD = ["def testMethod():", "\t", "\t", "\treturn 1"]

class processFunction(unittest.TestCase):
    """ Test cases of processFunction """
        
    def handlesReturnValue_Default(self):
        """ Test that the default return value is added properly """
        self.runner = PythonRunner(EMPTY_METHOD)
        results = self.runner.processFunction()
        self.assertEquals("return None", results[1], "Should have the proper return statement")
        self.assertEquals(1, len(results), "Should only have the return statement")
        
    def handlesReturnValue_Explicit(self):
        """ Test that an explicit return value is added properly """
        self.runner = PythonRunner(RETURN_1_METHOD)
        results = self.runner.processFunction()
        self.assertEquals("return 1", results[1], "Should have the proper return statement")
        self.assertEquals(1, len(results), "Should only have the return statement")
        
    def handlesReturnValue_String(self):
        """ Test that an explicit return value is added properly """
        self.runner = PythonRunner(RETURN_STRING_METHOD)
        results = self.runner.processFunction()
        self.assertEquals("return 'Blah'", results[1], "Should have the proper return statement")
        self.assertEquals(1, len(results), "Should only have the return statement")
        
    def handlesReturnValue_MultiLine(self):
        """ Test that an explicit return value is added properly """
        self.runner = PythonRunner(MULTI_LINE_RETURN_METHOD)
        results = self.runner.processFunction()
        
        expectedLine = len(MULTI_LINE_RETURN_METHOD)-1
        self.assertEquals("return 1", results[expectedLine], "Should have the proper return statement")

# Collect all test cases in this class
testcasesProcessFunction = ["handlesReturnValue_Default", "handlesReturnValue_Explicit", "handlesReturnValue_String", "handlesReturnValue_MultiLine"]
suiteProcessFunction = unittest.TestSuite(map(processFunction, testcasesProcessFunction))

##########################################################

# Collect all test cases in this file
suites = [suiteProcessFunction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)