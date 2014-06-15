import sys

runner = None

def RunMethod(runnableBody, currentRunner):
    global runner
    runner = currentRunner
    
    try: 
        exec runnableBody in sys.modules[__name__].__dict__
    except Exception as error:
        return runner.lineNumber, None, error
    return runner.lineNumber, returnValue, None