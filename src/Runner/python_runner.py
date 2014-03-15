
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
            
        results = {}
        for varName in self.variables:
            results[1] = "{0} = {1}".format(varName, self.variables[varName])
        results[lineNumber] = "return {0}".format(returnValue)
        return results
        
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
            housekeepingCommands = ["{0}self.lineNumber = {1}".format(leadingWhitespace, i+1),
                                    leadingWhitespace+"self.variables = {}", leadingWhitespace+"for name in [name for name in dir() if name != 'self' and name != 'name']:",
                                    leadingWhitespace+"\tself.variables[name]=eval(name)"]
            newIndex = i+1+len(housekeepingCommands)*i
            newLines[newIndex:newIndex] = housekeepingCommands
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