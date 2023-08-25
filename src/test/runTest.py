def runTest(testFunction):
    print(f"\nTEST {testFunction.__name__}")
    testFunction()
    print("PASSED")
