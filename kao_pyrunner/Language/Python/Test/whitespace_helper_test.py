from kao_pyrunner.Language.Python.whitespace_helper import findStartingWhitespace

import unittest

class findStartingWhitespaceTest(unittest.TestCase):
    """ Test cases of findStartingWhitespace """
        
    def spaces(self):
        """ Test that leading spaces are returned """
        EXPECTED_WHITESPACE = "    "
        line = EXPECTED_WHITESPACE + 'random stuff    '
        
        whitespace = findStartingWhitespace(line)
        self.assertEquals(EXPECTED_WHITESPACE, whitespace, 'The returned whitespace should match the Expected whitespace')
        
    def tabs(self):
        """ Test that leading tabs are returned """
        EXPECTED_WHITESPACE = "\t"
        line = EXPECTED_WHITESPACE + 'random stuff\t'
        
        whitespace = findStartingWhitespace(line)
        self.assertEquals(EXPECTED_WHITESPACE, whitespace, 'The returned whitespace should match the Expected whitespace')
        
    def noLeadingWhitespace(self):
        """ Test that no leading whitespace returns the empty string """
        EXPECTED_WHITESPACE = ""
        line = EXPECTED_WHITESPACE + 'random stuff'
        
        whitespace = findStartingWhitespace(line)
        self.assertEquals(EXPECTED_WHITESPACE, whitespace, 'The returned whitespace should match the Expected whitespace')

# Collect all test cases in this class
testcasesFindStartingWhitespace = ["spaces", "tabs", "noLeadingWhitespace"]
suiteFindStartingWhitespace = unittest.TestSuite(map(findStartingWhitespaceTest, testcasesFindStartingWhitespace))

##########################################################

# Collect all test cases in this file
suites = [suiteFindStartingWhitespace]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)