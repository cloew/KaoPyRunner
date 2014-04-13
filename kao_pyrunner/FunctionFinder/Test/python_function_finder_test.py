from kao_pyrunner.FunctionFinder.python_function_finder import PythonFunctionFinder

import unittest

TEST_METHOD = ["", "def testMethod():", "\tif True:", "\t\treturn 2", "\t", "\treturn None", "\t", ""]

class findFunction(unittest.TestCase):
    """ Test cases of findFunction """
    
    def  setUp(self):
        """ Build the Function Finder for the test """
        self.finder = PythonFunctionFinder()
        
    def beforeFunction(self):
        """ Test that it returns None when vbefore a function """
        function = self.finder.findFunction(TEST_METHOD, 0, 0)
        
        self.assertIs(None, function, 'The function should be None when not actually within a function body')
        
    def inFunction(self):
        """ Test that it returns the proper lines when not in a function """
        function = self.finder.findFunction(TEST_METHOD, 3, 0)
        
        self.assertIsNot(None, function, 'The function should not be None when within a function body')
        self.assertEquals(TEST_METHOD[1:7], function, 'The function should contain the proper lines')
        
    def afterFunction(self):
        """ Test that it returns None when after a function """
        function = self.finder.findFunction(TEST_METHOD, 7, 0)
        
        self.assertIs(None, function, 'The function should not be None when within a function body')

# Collect all test cases in this class
testcasesFindFunction = ["beforeFunction", "inFunction", "afterFunction"]
suiteFindFunction = unittest.TestSuite(map(findFunction, testcasesFindFunction))

##########################################################

# Collect all test cases in this file
suites = [suiteFindFunction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)