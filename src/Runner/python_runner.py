
class PythonRunner:
    """ Represents a runner of a Python class """
    
    def __init__(self, functionLines):
        """ Initialize the Python Runner """
        self.functionHeader = functionLines[0]
        self.functionName = self.functionHeader.replace('def', '').strip().split('(')[0]
        self.functionLines = functionLines
        
    def processFunction(self):
        """ Processes the given function """
        lineNumber, returnValue = self.runFunction()
        if type(returnValue) == str:
            returnValue = "'{0}'".format(returnValue)
        return {lineNumber:"return {0}".format(returnValue)}
        
    def runFunction(self):
        """ Run the function """
        newLines = self.getNewFunctionLines()
        
        wholeFunction = "\n".join(newLines)
        exec(wholeFunction)
        exec("returnValue = {0}(self)".format(self.functionName))
        return self.lineNumber, returnValue
        
    def getNewFunctionLines(self):
        """ Return the new function lines """
        newLines = list(self.functionLines)
        for i in range(len(self.functionLines)):
            leadingWhitespace = self.getLeadingWhitespaceForLine(i+1)
            newLines[i+i+1:i+i+1] = ["{0}self.lineNumber = {1}".format(leadingWhitespace, i+1)]
        newLines[0] = "def {0}(self):".format(self.functionName)
        return newLines
        
    def getLeadingWhitespaceForLine(self, index):
        """ Return the leading whitespace for the given line index """
        if index < len(self.functionLines):
            nextLine = self.functionLines[index]
            leadingWhitespace = nextLine[:len(nextLine)-len(nextLine.lstrip())]
        else:
            leadingWhitespace = "\t"
        return leadingWhitespace