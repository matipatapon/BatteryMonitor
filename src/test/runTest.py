def runTest(testFunction):
    print(f" TEST {testFunction.__name__}", end="")
    testFunction()
    print(" - PASSED")
