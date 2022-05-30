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
                if i == hops-1:
                    distinctNumbers.add(str(number))
                number.pop()
    return len(distinctNumbers)


def test():                             # second Test: checks wether n=2 for start=1 works - it should be 4 distinct numbers
    if genNumber(1, 2) == 4:
        print("Test passed")
    else:
        print("Test failed")

test()
