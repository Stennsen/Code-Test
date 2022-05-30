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

def jump(number, hops):
    print("Hops left " + str(hops) + ": " + str(number))
    if hops == 0 or number[len(number)-1]== 5:
        distinctNumbers.add(str(number))
        print("Numberpool: " + str(distinctNumbers))
    else:
        for j in jumpDict[number[len(number)-1]]:
            print("jump to " + str(j))
            number.append(j)
            jump(number, hops-1)
            number.pop()
            print(number)

def getDisctinctNumbers(start, hops):
    global distinctNumbers
    distinctNumbers = set()
    number = [start]
    jump(number, hops)
    print(distinctNumbers)
    return len(distinctNumbers)


def test():                             # second Test: checks wether n=2 for start=1 works - it should be 5 distinct numbers
    if getDisctinctNumbers(1, 2) == 5:
        print("Test passed")
    else:
        print("Test failed")

test()
