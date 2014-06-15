from kao_pyrunner.Language.Python.whitespace_helper import findStartingWhitespace

class PythonFunctionFinder:
    """ Class that can find a function in a list of lines """
    
    def findFunction(self, lines, row, column):
        """ Return the function for the current row and column in the given lines """
        startOfFunction = self.findStartOfFunction(lines, row)
        if startOfFunction is None:
            return None
            
        endOfFunction = self.findEndOfFunction(lines, startOfFunction)
        return startOfFunction, endOfFunction
        
    def findStartOfFunction(self, lines, row):
        """ Return the line number of the start of the function """
        currentRow = row
        startingLine = lines[currentRow]
        currentLine = startingLine
        
        
        while currentRow > 0 and not currentLine.lstrip().startswith("def "):
            currentRow = currentRow-1
            currentLine = lines[currentRow]
            
        
        
        if self.withinFunction(currentLine, startingLine):
            return currentRow
        else:
            return None
            
    def findEndOfFunction(self, lines, startOfFunction):
        """ Return line number for the start of the function """
        startingLeadingWhitespace = findStartingWhitespace(lines[startOfFunction])
        endOfFunction = len(lines)
        
        for i in range(startOfFunction+1, len(lines)):
            line = lines[i]
            currentLeadingWhitespace = findStartingWhitespace(line)
            if len(currentLeadingWhitespace) <= len(startingLeadingWhitespace):
                endOfFunction = i
                break
        
        return endOfFunction
        
    def withinFunction(self, currentLine, startingLine):
        """ Return if within a function """
        startingLeadingWhitespace = findStartingWhitespace(startingLine)
        currentLeadingWhitespace = findStartingWhitespace(currentLine)
        
        return currentLine.lstrip().startswith("def ") and (len(currentLeadingWhitespace) < len(startingLeadingWhitespace) or currentLine == startingLine)