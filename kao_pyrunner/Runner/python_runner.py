from Runner.python_function import PythonFunction

class PythonRunner:
    """ Represents a runner of a Python class """
    
    def __init__(self, functionLines, parameters=[]):
        """ Initialize the Python Runner """
        self.function = PythonFunction(functionLines)
        
        self.previousState = None
        self.functionStates = {}
        self.lineNumber = 0
        self.parameters = parameters
        
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
        newLines = self.function.generateFunctionWithHouseKeeping(self.generateHousekeepingLines)
        wholeFunction = "\n".join(newLines)
        callFunctionString = self.getFunctionCallString()
        
        exec(wholeFunction)
        exec(callFunctionString)
        return self.lineNumber, returnValue
        
    def getFunctionCallString(self):
        """ Return the Function Call String """
        if self.function.needsArguments():
            return "returnValue = {0}({1}, self)".format(self.function.name, self.getFunctionParameterString())
        else:
            return "returnValue = {0}(self)".format(self.function.name)
        
    def getFunctionParameterString(self):
        """ Return the Function Parameter String """
        return ", ".join([str(self.getValue(parameter)) for parameter in self.parameters])
        
    def generateHousekeepingLines(self, lineNumber):
        """ Generate the housekeeping lines for the current line """
        return ["__variables__ = {}", 
                "for __var_name__ in [__var_name__ for __var_name__ in dir() if __var_name__ not in ['__runner__', '__var_name__', '__variables__']]:",
                "\t__variables__[__var_name__]=eval(__var_name__)",
                "__runner__.storeState({0}, __variables__)".format(lineNumber)]
        
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