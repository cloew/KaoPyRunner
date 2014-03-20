from Runner.python_function import PythonFunction

import unittest

class parseHeader(unittest.TestCase):
    """ Test cases of parseHeader """
    
    def  setUp(self):
        """ Build the function for the test """
        self.function = PythonFunction(None)
        
    def noArguments(self):
        """ Test that no Arguments are handled properly """
        self.function.parseHeader("def testMethod():")
        self.assertEquals([], self.function.arguments, 'Arguments should be empty when there are no arguments')

# Collect all test cases in this class
testcasesParseHeader = ["noArguments"]
suiteParseHeader = unittest.TestSuite(map(parseHeader, testcasesParseHeader))

##########################################################

# Collect all test cases in this file
suites = [suiteParseHeader]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)