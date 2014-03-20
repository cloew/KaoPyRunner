
class PythonRunner:
    """ Represents a runner of a Python class """
    
    def __init__(self, functionLines):
        """ Initialize the Python Runner """
        self.functionHeader = functionLines[0]
        self.functionName = self.functionHeader.replace('def', '').strip().split('(')[0]
        self.functionLines = functionLines
        self.previousState = None
        self.functionStates = {}
        self.lineNumber = 0
        
    def processFunction(self):
        """ Processes the given function """
        lastLineNumber, returnValue = self.runFunction()
            
        results = {}
        for lineNumber in self.functionStates:
            functionState = self.functionStates[lineNumber]
            for varName in functionState:
                variableStatement = ["{0} = {1}".format(varName, self.getValue(functionState[varName]))]
                if lineNumber in results:
                    results[lineNumber] += variableStatement
                else:
                    results[lineNumber] = variableStatement
        results[lastLineNumber] = ["return {0}".format(self.getValue(returnValue))]
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
            housekeepingCommands = ["__variables__ = {}", 
                                    "for __var_name__ in [__var_name__ for __var_name__ in dir() if __var_name__ not in ['__runner__', '__var_name__', '__variables__']]:",
                                    "\t__variables__[__var_name__]=eval(__var_name__)",
                                    "__runner__.storeState({0}, __variables__)".format(i+1)]
            newIndex = i+1+len(housekeepingCommands)*i
            newLines[newIndex:newIndex] = [leadingWhitespace+command for command in housekeepingCommands]
        newLines[0] = "def {0}(__runner__):".format(self.functionName)
        return newLines
        
    def getLeadingWhitespaceForLine(self, index):
        """ Return the leading whitespace for the given line index """
        if index < len(self.functionLines):
            nextLine = self.functionLines[index]
            leadingWhitespace = nextLine[:len(nextLine)-len(nextLine.lstrip())]
        else:
            leadingWhitespace = "\t"
        return leadingWhitespace
        
    def storeState(self, lineNumber, variables):
        """ Store the current state of the function """
        self.functionStates[self.lineNumber] = {}
        for varName in variables:
            if self.previousState is None or varName not in self.previousState or self.previousState[varName] != variables[varName]:
                self.functionStates[self.lineNumber][varName] = variables[varName]
                
        self.lineNumber = lineNumber
        self.previousState = variables
        
    def getValue(self, value):
        """ Return a proper form of the value """
        if type(value) == str:
            value = "'{0}'".format(value)
        return value