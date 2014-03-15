
class PythonRunner:
    """ Represents a runner of a Python class """
    
    def __init__(self, functionLines):
        """ Initialize the Python Runner """
        self.functionHeader = functionLines[0]
        self.functionName = self.functionHeader.replace('def', '').strip().split('(')[0]
        self.functionLines = functionLines
        
    def processFunction(self):
        """ Processes the given function """
        returnValue = self.runFunction()
        if type(returnValue) == str:
            returnValue = "'{0}'".format(returnValue)
        return {1:"return {0}".format(returnValue)}
        
    def runFunction(self):
        """ Run the function """
        wholeFunction = "\n".join(self.functionLines)
        exec(wholeFunction)
        exec("returnValue = {0}()".format(self.functionName))
        return returnValue