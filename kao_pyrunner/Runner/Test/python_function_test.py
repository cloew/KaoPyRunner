from kao_pyrunner.Runner.invalid_function_exception import InvalidFunctionException
from kao_pyrunner.Runner.python_function import PythonFunction

import unittest

NO_ARGS = "def testMethod():"
SINGLE_ARG = "def testMethod(i):"
MULTI_ARGS = "def testMethod(i, j):"

class init(unittest.TestCase):
    """ Test cases of init """
        
    def validFunction(self):
        """ Test that a valid function is handled properly """
        self.function = PythonFunction([NO_ARGS, "\tpass"])
        self.assertEquals([], self.function.arguments, 'Arguments should be empty when there are no arguments')
        
    def onlyHeader(self):
        """ Test that only a header being passed to a function throws an Invalid Function Exception- """
        with self.assertRaises(InvalidFunctionException):
            self.function = PythonFunction(NO_ARGS)

    def gibberish(self):
        """ Test that only a header being passed to a function throws an Invalid Function Exception- """
        with self.assertRaises(InvalidFunctionException):
            self.function = PythonFunction(["", ""])
            
    def none(self):
        """ Test that only a header being passed to a function throws an Invalid Function Exception- """
        with self.assertRaises(InvalidFunctionException):
            self.function = PythonFunction(None)
            
# Collect all test cases in this class
testcasesInit = ["validFunction", "onlyHeader", "gibberish", "none"]
suiteInit = unittest.TestSuite(map(init, testcasesInit))

##########################################################

class parseHeader(unittest.TestCase):
    """ Test cases of parseHeader """
    
    def  setUp(self):
        """ Build the function for the test """
        self.function = PythonFunction([NO_ARGS, "\tpass"])
        
    def noArguments(self):
        """ Test that no Arguments are handled properly """
        self.function.parseHeader(NO_ARGS)
        self.assertEquals([], self.function.arguments, 'Arguments should be empty when there are no arguments')
        
    def singleArguments(self):
        """ Test that a Single Argument is handled properly """
        self.function.parseHeader(SINGLE_ARG)
        self.assertEquals(['i'], self.function.arguments, 'Arguments should be the argument provided')
        
    def multipleArguments(self):
        """ Test that Multiple Arguments are handled properly """
        self.function.parseHeader(MULTI_ARGS)
        self.assertEquals(['i', 'j'], self.function.arguments, 'Arguments should be the provided arguments')

# Collect all test cases in this class
testcasesParseHeader = ["noArguments", "singleArguments", "multipleArguments"]
suiteParseHeader = unittest.TestSuite(map(parseHeader, testcasesParseHeader))

##########################################################

class buildHeaderWithHousekeeping(unittest.TestCase):
    """ Test cases of buildHeaderWithHousekeeping """
    def makeProperFunctionFromHeader(self, header):
        """ Return runnable function lines for a given header """
        return [header, "\tpass"]
        
    def noArguments(self):
        """ Test that a function with no Arguments is built properly """
        self.function = PythonFunction(self.makeProperFunctionFromHeader(NO_ARGS))
        header = self.function.buildHeaderWithHousekeeping()
        self.assertEquals(NO_ARGS, header.replace('__runner__', ''), 'Header should be rebuilt properly')
        
    def singleArguments(self):
        """ Test that a function with no Arguments is built properly """
        self.function = PythonFunction(self.makeProperFunctionFromHeader(SINGLE_ARG))
        header = self.function.buildHeaderWithHousekeeping()
        self.assertEquals(SINGLE_ARG, header.replace(', __runner__', ''), 'Header should be rebuilt properly')
        
    def multipleArguments(self):
        """ Test that a function with no Arguments is built properly """
        self.function = PythonFunction(self.makeProperFunctionFromHeader(MULTI_ARGS))
        header = self.function.buildHeaderWithHousekeeping()
        self.assertEquals(MULTI_ARGS, header.replace(', __runner__', ''), 'Header should be rebuilt properly')

# Collect all test cases in this class
testcasesBuildHeaderWithHousekeeping = ["noArguments", "singleArguments", "multipleArguments"]
suiteBuildHeaderWithHousekeeping = unittest.TestSuite(map(buildHeaderWithHousekeeping, testcasesBuildHeaderWithHousekeeping))

##########################################################

# Collect all test cases in this file
suites = [suiteParseHeader,
          suiteBuildHeaderWithHousekeeping,
          suiteInit]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)