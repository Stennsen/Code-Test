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
    distinctNumbers = set()
    number = [start]
    for i in range(hops):
        if start == 5:
            distinctNumbers.add(str(number))
        else:
            for j in jumpDict[start]:
                number.append(j)
                if i == hops:
                    distinctNumbers.add(str(number))
                number.pop()
    print(distinctNumbers)
    return len(distinctNumbers)


def test():                         # first Test: checks wether n=1 for any given number works

    for i in range(10):
        if genNumber(i, 1) == 2 and i !=5 and i != 4 and i != 6:
            print("Test " + str(i) + " passed")
        else:
            print("Test " + str(i) + " failed")
    if genNumber(5, 1) == 1:
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    if genNumber(4, 1) == 3:
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    if genNumber(6, 1) == 3:
        print("Test 4 passed")
    else:
        print("Test 4 failed")

test()
