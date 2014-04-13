
def findStartingWhitespace(pythonLine):
    """ Returns the starting whitespace for the python line string given """
    return pythonLine[:len(pythonLine)-len(pythonLine.lstrip())]