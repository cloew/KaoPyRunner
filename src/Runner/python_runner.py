
class PythonRunner:
    """ Represents a runner of a Python class """
    
    def __init__(self, functionLines):
        """ Initialize the Python Runner """
        self.functionLines = functionLines[1:]
        
    def processFunction(self):
        """ Processes the given function """
        returnValue = self.runFunction()
        return {1:"return {0}".format(returnValue)}
        
    def runFunction(self):
        """ Run the function """
        wholeFunction = "\n".join([line.lstrip() for line in self.functionLines])
        exec(wholeFunction)