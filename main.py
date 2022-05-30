jumpDict = {1: {6, 8},              # this variable stores which numbers are reachable from the current dial
            2: {7, 9},              # scheme: The key is the starting Dial - The value is a Set of reachable numbers
            3: {4, 8},
            4: {3, 9, 0},
            5: {},
            6: {1, 7, 0},
            7: {2, 6},
            8: {1, 3},
            9: {2, 4},
            0: {4, 6}}



def genNumber(start, hops):
    return -1

def test():                         # first Test: checks wether n=1 for any given number works
    for i in range(10):
        if genNumber(i, 1) == 1:
            print("Test " + str(i) + " passed")
        else:
            print("Test " + str(i) + " failed")


test()
