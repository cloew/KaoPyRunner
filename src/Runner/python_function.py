
class PythonFunction:
    """ Represents a Python function """
    
    def __init__(self, functionLines):
        """ Initialize the Python Function with the lines of the function """
        self.header = functionLines[0]
        self.name = self.header.replace('def', '').strip().split('(')[0]
        self.body = functionLines[1:]
        
    def generateFunctionWithHouseKeeping(self, houseKeepingGenerator):
        """ Generate the function with housekeeping inserted for introspection """
        newLines = list([self.header]+self.body)
        for i in range(len(self.body)+1):
            leadingWhitespace = self.getLeadingWhitespaceForLine(i+1)
            housekeepingLines = houseKeepingGenerator(i+1)
            newIndex = i+1+len(housekeepingLines)*i
            newLines[newIndex:newIndex] = [leadingWhitespace+line for line in housekeepingLines]
        newLines[0] = "def {0}(__runner__):".format(self.name)
        return newLines
        
    def getLeadingWhitespaceForLine(self, index):
        """ Return the leading whitespace for the given line index """
        index = index-1
        if index < len(self.body):
            line = self.body[index]
            leadingWhitespace = line[:len(line)-len(line.lstrip())]
        else:
            leadingWhitespace = "\t"
        return leadingWhitespace