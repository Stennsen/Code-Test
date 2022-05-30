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
    if hops == 0 or number[len(number)-1]== 5:
        distinctNumbers.add(str(number))
    else:
        for j in jumpDict[number[len(number)-1]]:
            number.append(j)
            jump(number, hops-1)
            number.pop()

def getDisctinctNumbers(start, hops):
    global distinctNumbers
    distinctNumbers = set()
    number = [start]
    jump(number, hops)
    return len(distinctNumbers)

print("Enter starting number:")
start = int(input())
print("Enter amount of jumps:")
jumps = int(input())
print(str(getDisctinctNumbers(start, jumps)) + " differnt numbers are possible.")
