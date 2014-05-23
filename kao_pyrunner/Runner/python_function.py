from kao_pyrunner.Language.Python.whitespace_helper import findStartingWhitespace
from kao_pyrunner.Runner.invalid_function_exception import InvalidFunctionException

class PythonFunction:
    """ Represents a Python function """
    
    def __init__(self, functionLines):
        """ Initialize the Python Function with the lines of the function """
        if self.isRunnableFunction(functionLines):
            self.header = functionLines[0]
            self.body = functionLines[1:]
            self.parseHeader(self.header)
        else:
            raise InvalidFunctionException("The function is not runnable: " + str(functionLines))
            
    def isRunnableFunction(self, functionLines):
        """ Return if the lines represent a runnable function """
        return functionLines is not None and len(functionLines) > 1 and '(' in functionLines[0]
        
    def parseHeader(self, header):
        """ Parse the header """
        leftHeader, rightHeader = header.split('(')
        self.name = leftHeader.replace('def', '').strip()
        self.arguments = [argument.strip() for argument in rightHeader.split(')')[0].split(',') if argument.strip() != '']
        
    def generateFunctionWithHouseKeeping(self, houseKeepingGenerator):
        """ Generate the function with housekeeping inserted for introspection """
        newLines = list([self.header]+self.body)
        for i in range(len(self.body)+1):
            leadingWhitespace = self.getLeadingWhitespaceForLine(i)
            housekeepingLines = houseKeepingGenerator(i+1)
            newIndex = i+1+len(housekeepingLines)*i
            newLines[newIndex:newIndex] = [leadingWhitespace+line for line in housekeepingLines]
            
        newLines[0] = self.buildHeaderWithHousekeeping()
        newLines = [line.replace('\t', '    ') for line in newLines]
        return newLines
        
    def getLeadingWhitespaceForLine(self, index):
        """ Return the leading whitespace for the given line index """
        if index < len(self.body):
            line = self.body[index]
            leadingWhitespace = findStartingWhitespace(line)
        else:
            leadingWhitespace = "    "
        return leadingWhitespace
        
    def buildHeaderWithHousekeeping(self):
        """ Return the function header with housekeeping built-in """
        argumentString = ", ".join(self.arguments+['__runner__'])
        return "def {0}({1}):".format(self.name, argumentString)
        
    def needsArguments(self):
        """ Return if the function needs arguments """
        return len(self.arguments) > 0