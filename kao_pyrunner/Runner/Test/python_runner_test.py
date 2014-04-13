from kao_pyrunner.Runner.python_runner import PythonRunner

import unittest

EMPTY_METHOD = ["def testMethod():", "\tpass"]
RETURN_1_METHOD = ["def testMethod():", "\treturn 1"]
RETURN_STRING_METHOD = ["def testMethod():", "\treturn 'Blah'"]
MULTI_LINE_RETURN_METHOD = ["def testMethod():", "\t", "\t", "\treturn 1"]
EARLY_RETURN_METHOD = ["def testMethod():", "\tif True:", "\t\treturn 2", "\t", "\treturn None"]
VAR_INIT_METHOD = ["def testMethod():", "\ti=0"]
MULTI_LINE_VAR_INIT_METHOD = ["def testMethod():", "\t", "\t", "\ti=0"]
MULT_VAR_INITS_METHOD = ["def testMethod():", "\ti=0", "\tj=2"]
STRING_VAR_INIT_METHOD = ["def testMethod():", "\ti='Blah'"]
VAR_MOD_METHOD = ["def testMethod():", "\ti=0", "\ti=2"]
MULTI_VARS_METHOD = ["def testMethod():", "\ti,j=(0,1)"]
SINGLE_ARG_METHOD = ["def testMethod(i):", "\ti+=2"]
MULTIPLE_ARGS_METHOD = ["def testMethod(i, j):", "\ti+=2"]
MIXED_WHITESPACE_METHOD = ["def testMethod():", "\tif True:", "\t    return 2", "\t", "    return None"]

class processFunction(unittest.TestCase):
    """ Test cases of processFunction """
    
    def handleArguments_NoArguments(self):
        """ Test that no argument values works properly. Smoke Test mostly """
        self.runner = PythonRunner(VAR_INIT_METHOD)
        results = self.runner.processFunction()
        
        self.assertEquals(["i = 0"], results[1], "Should have the proper variable statement")
        
    def handleArguments_SingleArgument(self):
        """ Test that single argument value works properly. """
        self.runner = PythonRunner(SINGLE_ARG_METHOD, parameters=[1])
        results = self.runner.processFunction()
        
        self.assertEquals(["i = 1"], results[0], "Should have the proper variable statement")
        
    def handleArguments_MultipleArguments(self):
        """ Test that mulitple argument values works properly. """
        self.runner = PythonRunner(MULTIPLE_ARGS_METHOD, parameters=[1, 2])
        results = self.runner.processFunction()
        
        self.assertEquals(["i = 1", "j = 2"], results[0], "Should have the proper variable statement")
        
    def handlesVariables_Initialization(self):
        """ Test that the variable initialization is added properly """
        self.runner = PythonRunner(VAR_INIT_METHOD)
        results = self.runner.processFunction()
        
        self.assertEquals(["i = 0"], results[1], "Should have the proper variable statement")
        
    def handlesVariables_MultiLineInitialization(self):
        """ Test that the variable initialization is added properly """
        self.runner = PythonRunner(MULTI_LINE_VAR_INIT_METHOD)
        results = self.runner.processFunction()
        
        expectedLine = len(MULTI_LINE_VAR_INIT_METHOD)-1
        self.assertEquals(["i = 0"], results[expectedLine], "Should have the proper variable statement")
        
    def handlesVariables_MultipleInitializations(self):
        """ Test that the variable initializations are added properly """
        self.runner = PythonRunner(MULT_VAR_INITS_METHOD)
        results = self.runner.processFunction()
        
        self.assertEquals(["i = 0"], results[1], "Should have the proper variable statement")
        self.assertEquals(["j = 2"], results[2], "Should have the proper variable statement")
        
    def handlesVariables_StringValue(self):
        """ Test that the variable string value are added properly """
        self.runner = PythonRunner(STRING_VAR_INIT_METHOD)
        results = self.runner.processFunction()
        
        self.assertEquals(["i = 'Blah'"], results[1], "Should have the proper variable statement")
        
    def handlesVariables_Modification(self):
        """ Test that the variable modification is added properly """
        self.runner = PythonRunner(VAR_MOD_METHOD)
        results = self.runner.processFunction()
        
        self.assertEquals(["i = 2"], results[2], "Should have the proper variable statement")
        
    def handlesVariables_Multiple(self):
        """ Test that the variable modification is added properly """
        self.runner = PythonRunner(MULTI_VARS_METHOD)
        results = self.runner.processFunction()
        
        self.assertEquals(["i = 0", "j = 1"], results[1], "Should have the proper variable statement")
        
    def handlesReturnValue_Default(self):
        """ Test that the default return value is added properly """
        self.runner = PythonRunner(EMPTY_METHOD)
        results = self.runner.processFunction()
        
        expectedLine = len(EMPTY_METHOD)
        self.assertEquals(["return None"], results[expectedLine], "Should have the proper return statement")
        
    def handlesReturnValue_Explicit(self):
        """ Test that an explicit return value is added properly """
        self.runner = PythonRunner(RETURN_1_METHOD)
        results = self.runner.processFunction()
        self.assertEquals(["return 1"], results[1], "Should have the proper return statement")
        self.assertEquals(1, len(results), "Should only have the return statement")
        
    def handlesReturnValue_String(self):
        """ Test that an explicit string return value is added properly """
        self.runner = PythonRunner(RETURN_STRING_METHOD)
        results = self.runner.processFunction()
        self.assertEquals(["return 'Blah'"], results[1], "Should have the proper return statement")
        self.assertEquals(1, len(results), "Should only have the return statement")
        
    def handlesReturnValue_MultiLine(self):
        """ Test that a multi line function's return value is added properly """
        self.runner = PythonRunner(MULTI_LINE_RETURN_METHOD)
        results = self.runner.processFunction()
        
        expectedLine = len(MULTI_LINE_RETURN_METHOD)-1
        self.assertEquals(["return 1"], results[expectedLine], "Should have the proper return statement")
        
    def handlesReturnValue_EarlyReturn(self):
        """ Test that an early return value is added properly """
        self.runner = PythonRunner(EARLY_RETURN_METHOD)
        results = self.runner.processFunction()
        
        expectedLine = 2
        self.assertEquals(["return 2"], results[expectedLine], "Should have the proper return statement")
        
    def handlesMixedWhitespace(self):
        """ Test that the function Prcessor can handle mixed whitespace """
        self.runner = PythonRunner(MIXED_WHITESPACE_METHOD)
        try:
            results = self.runner.processFunction()
        except IndentationError as error:
            self.fail('An Indentation Error should not have occured')

# Collect all test cases in this class
testcasesProcessFunction = ["handleArguments_NoArguments", "handleArguments_SingleArgument", "handleArguments_MultipleArguments",
                            "handlesVariables_Initialization", "handlesVariables_MultiLineInitialization", "handlesVariables_MultipleInitializations", "handlesVariables_StringValue",
                            "handlesVariables_Modification", "handlesVariables_Multiple",
                            "handlesReturnValue_Default", "handlesReturnValue_Explicit", "handlesReturnValue_String", "handlesReturnValue_MultiLine", "handlesReturnValue_EarlyReturn",
                            "handlesMixedWhitespace"]
suiteProcessFunction = unittest.TestSuite(map(processFunction, testcasesProcessFunction))

##########################################################

# Collect all test cases in this file
suites = [suiteProcessFunction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)