
class PythonFunctionFinder:
    """ Class that can find a function in a list of lines """
    
    def findFunction(self, lines, row, column):
        """ Return the function for the current row and column in the given lines """
        startOfFunction = self.findStartOfFunction(lines, row)
        if startOfFunction is None:
            return None
            
        currentLine = lines[startOfFunction]
        return lines[startOfFunction:]
        
    def findStartOfFunction(self, lines, row):
        """ Return the line number of the start of the function """
        currentRow = row
        currentLine = lines[currentRow]
        while currentRow > 0 and not currentLine.lstrip().startswith("def "):
            currentRow = currentRow-1
            currentLine = lines[currentRow]
        
        if currentLine.lstrip().startswith("def "):
            return currentRow
        else:
            return None