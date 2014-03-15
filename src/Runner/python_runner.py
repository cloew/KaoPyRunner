
lineNumber = 0

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
        newLines = list(self.functionLines)
        for i in range(len(self.functionLines)):
            if i+1 < len(self.functionLines):
                nextLine = self.functionLines[i+1]
                leadingWhitespace = nextLine[:len(nextLine)-len(nextLine.lstrip())]
            else:
                leadingWhitespace = "\t"
            newLines[i+i+1:i+i+1] = ["{0}lineNumber = {1}".format(leadingWhitespace, i+1)]
        newLines[1:1] = ["\tglobal lineNumber"]
        
        wholeFunction = "\n".join(newLines)
        exec(wholeFunction)
        exec("returnValue = {0}()".format(self.functionName))
        return lineNumber, returnValue